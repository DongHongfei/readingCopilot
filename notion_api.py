import logging

from notion_client import Client

from rss_parser import convert_to_notion_blocks, markdown_to_notion_blocks
from utils import log_error


class NotionAPI:
    def __init__(self, token):
        self.notion = Client(auth=token)
        logging.info("Notion API客户端已初始化。")

    def query_open_rss(self, database_id):
        """
        查询启用的RSS源，返回一个列表包含每个RSS源的详细信息。
        不再使用状态作为筛选条件，而是检查'Enabled'字段确保RSS源处于启用状态。
        """
        try:
            # 使用Notion API查询启用的RSS源，过滤条件为Disabled字段为False
            query = {"filter": {"property": "Disabled", "checkbox": {"equals": False}}}
            response = self.notion.databases.query(database_id=database_id, **query)
            
            # 解析响应数据，提取RSS源信息
            rss_feeds = [
                {
                    "id": item["id"],
                    "Title": item["properties"]["Name"]["title"][0]["plain_text"],
                    "Link": item["properties"]["Url"]["url"],
                    "AiSummaryEnabled": item["properties"]["AiSummaryEnabled"]["checkbox"],
                    "Tags": [tag["name"] for tag in item["properties"]["Tags"]["multi_select"]],
                    "Updated": item["properties"]["Updated"]["date"]["start"] if item["properties"]["Updated"]["date"] else None
                }
                for item in response["results"]
            ]
            
            logging.info(f"查询到{len(rss_feeds)}个启用的RSS源。")
            return rss_feeds
        except Exception as e:
            # logging.error(f"查询RSS源错误: {e}")
            log_error("Query Open RSS", "查询RSS源错误", exception=str(e))
            return []


    def is_page_exist(self, page_link, database_id):
        """检查指定链接的页面是否已存在于Notion数据库中"""
        query = {
            "filter": {
                "property": "Link",
                "url": {
                    "equals": page_link
                }
            }
        }
        response = self.notion.databases.query(database_id=database_id, **query)
        return len(response.get("results", [])) > 0

    def create_article_page(self, rss, entry, database_id, md):
        """在Notion数据库中创建文章页面，并在必要时分批添加内容块"""
        logging.info(f"开始创建文章页面：{entry['content']}")
        tokens = md.parse(entry['content'], {})
        blocks = convert_to_notion_blocks(tokens)

        properties = {
            "Title": {"title": [{"text": {"content": entry["title"]}}]},
            "Link": {"url": entry["link"]},
            "State": {"select": {"name": "Unread"}},
            "Published": {"date": {"start": entry["date"]}},
            "Source": {"relation": [{"id": entry["rss_info"]["id"]}]},
            "Tags": {"multi_select": [{"name": tag} for tag in entry["tags"]]}
        }

        try:
            # 创建页面
            response = self.notion.pages.create(parent={"database_id": database_id}, properties=properties, children=blocks[:100])
            page_id = response.get('id')
            if page_id:
                logging.info(f"文章 '{entry['title']}' 的首批100个块已成功保存到Notion。")
                # 如果还有更多块需要添加，继续添加剩余块
                remaining_blocks = blocks[100:]
                while remaining_blocks:
                    self.notion.blocks.children.append(block_id=page_id, children=remaining_blocks[:100])
                    remaining_blocks = remaining_blocks[100:]
                    logging.info(f"成功添加了更多块到Notion页面。")
                return page_id
            else:
                logging.error(f"未能创建文章('{entry['title']}')页面，未获得page_id")
        except Exception as e:
            log_error("Create Article Page", "创建文章页面时出错", rss_name=rss['Title'], article_title=entry['title'], exception=str(e))

        return None

        
    def update_rss_status(self, rss_id, status):
        """更新RSS源状态"""
        try:
            update_data = {
                "properties": {
                    "Status": {
                        "select": {
                            "name": status
                        }
                    }
                }
            }
            self.notion.pages.update(page_id=rss_id, **update_data)
            logging.info(f"RSS源 {rss_id} 状态更新为 {status}.")
        except Exception as e:
            logging.error(f"更新RSS状态时出错: {e}")

    def update_article_summary(self, page_id, summary):
        update_data = {
            "properties": {
                "AI summary": {
                    "rich_text": [{
                        "text": {
                            "content": summary
                        }
                    }]
                }
            }
        }
        self.notion.pages.update(page_id=page_id, **update_data)
