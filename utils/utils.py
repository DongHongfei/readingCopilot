import time
from datetime import datetime

from dateutil import parser

from utils.log import logging


def parse_date(date_str, detailed_context=""):
    """尝试解析不同格式的日期字符串，转换为ISO 8601格式"""
    if date_str is None:
        logging.warning(f"日期字段为空，将使用当前日期. Context: {detailed_context}")
        return datetime.now().isoformat()

    formats = [
        '%a, %d %b %Y %H:%M:%S %Z',  # RFC 2822
        '%Y-%m-%dT%H:%M:%S.%fZ',     # RFC 3339
        '%Y-%m-%dT%H:%M:%S%z',       # RFC 3339 with timezone
    ]
    for fmt in formats:
        try:
            # 尝试使用strptime根据指定格式解析日期
            return datetime.strptime(date_str, fmt).isoformat()
        except ValueError:
            continue
    try:
        # 作为最后的手段，尝试dateutil的解析器
        return parser.parse(date_str).isoformat()
    except ValueError as e:
        logging.error(f"日期格式转换错误，输入值 '{date_str}': {e}")
        return None
    
def safe_api_call(callable, *args, **kwargs):
    max_retries = 3
    retry_count = 0
    while retry_count < max_retries:
        try:
            return callable(*args, **kwargs)
        except Exception as e:  # 修改为适应实际的异常类型
            retry_count += 1
            wait_time = (2 ** retry_count)  # Exponential backoff
            logging.info(f"达到请求上限，等待{wait_time}秒后重试")
            time.sleep(wait_time)
    logging.error("多次重试失败，放弃请求")
    return None    