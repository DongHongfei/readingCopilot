
from markdown_it import MarkdownIt
from mdit_py_plugins.footnote import footnote_plugin
from mdit_py_plugins.front_matter import front_matter_plugin

from utils.config import NOTION_KEY
from utils.log import logging
from utils.rss_parser import convert_to_notion_blocks, html_to_markdown

content = """<p>“年龄不是问题，比我大七八岁都行，主要是不想努力了。”</p><p>“还没有毕业，可以给我找一个可以依靠的富婆吧哥？你把我信息挂上，到时候我有钱了，绝对忘不了咱公司。”</p><p>“老师，快同意我一下，我太渴望爱情了！”</p><p>李继延开金点子婚介公司25年，这两年遇到这样的男性客户尤其多。这些人并非想当赘婿，而是一心娶富婆，所以无一例外，全都被李继延打发走了。</p><p><strong>在李继延的微信联系人中，有上百名大学生等待入赘，</strong>他将这些人的微信备注成数字。譬如江苏男04182在校生211：“04”即2004年，指出生年份；“182”是身高；再后面是学校。</p><p>记者采访时，恰逢一个家里有四套房的男青年向李继延发送好友申请，李继延问对方是否有工作，对方回答，“暂时没有”。李继延拒绝了他的好友申请，让他先去找一份工作。</p><p>李继延桌子上摆着1部座机、6台手机，电脑点开着自家网站<strong>“杭州金点子婚姻介绍服务有限公司”</strong>，网页上有两个小飘窗，分别是：“青春不常在，抓紧谈恋爱！找到爱人，幸福一生！”“万名各阶层男女会员，有公务员、银行、事业单位、教师、医疗、白领、工程师、经商办企业、普通员工等。”</p><p class="image-wrapper"><img data-img-size-val="1080,810" src="https://img.36krcdn.com/hsossms/20240422/v2_11c82a20a6354342b01e57282e2a115c@1743780481_oswg121568oswg1080oswg810_img_000?x-oss-process=image/format,jpg/interlace,1/format,jpg/interlace,1/format,jpg/interlace,1" referrerpolicy="no-referrer"></p><p class="image-wrapper"><img data-img-size-val="1080,810" src="https://img.36krcdn.com/hsossms/20240422/v2_b1ae52dca24e4b449dc5b63b699f1c16@1743780481_oswg100645oswg1080oswg810_img_000?x-oss-process=image/format,jpg/interlace,1/format,jpg/interlace,1/format,jpg/interlace,1" referrerpolicy="no-referrer"></p><p class="img-desc">（摄/傅淼淼）</p><p>老婆孙纪梅坐在李继延对面，她五官清秀，皮肤很白，典型的江浙一带女人的相貌，讲话有很浓的萧山口音。每次当登门男客户提出想要入赘时，孙纪梅会和李继延一同面试对方。</p><p>金点子婚介公司门口印有身高刻度，对应160、170、180厘米身高。对方一走进来，李继延便大概知道对方身高多少，根本造不了假。</p><p class="image-wrapper"><img data-img-size-val="1080,1440" src="https://img.36krcdn.com/hsossms/20240422/v2_00b8b39b51604cc0ae7a7036730fdc42@1743780481_oswg130268oswg1080oswg1440_img_000?x-oss-process=image/format,jpg/interlace,1/format,jpg/interlace,1/format,jpg/interlace,1" referrerpolicy="no-referrer"></p><p class="img-desc">（摄/傅淼淼）</p><p>李继延常用“芝麻信用是多少？”做开场白。采访期间，一名外省的应届毕业的大学生前来申请赘婿，按要求点开支付宝。见对方芝麻信用高达745分，李继延满意地点点头。<strong>他要求男方芝麻信用至少在550分以上。</strong></p><p>男生来杭州一个月了，还没找到正式工作。李继延鼓励小伙子晚两年再来，“你相貌嘛还是很好的，人长得也高，晚两年再来吧，目前登记的女客户最小都要26岁”。孙纪梅在一旁叮嘱，“孩子你还年轻，去读个研究生吧，或是考个公务员。等自己条件好了，匹配到另一半条件也会更好。”</p><p>来金点子登记招婿的女客户，确实有一两个家产上亿的，最差家里也有几套房。此外，女方一般都还有稳定工作。之所以来这里登记，无非是想扩大交际圈，寻觅更好的结婚对象。李继延说：“这几年生意不好做，有些家里开工厂的生意不像之前好做了，但饿死的骆驼比马大，家里条件终归是好的。”</p><p>几年前，一名外省男客户慕名前来。他开着一家广告公司，身高183cm左右，中专文化。对方此行专为娃哈哈继承人宗馥莉而来，他以为李继延深耕杭州婚恋市场20多年，手中想必会有宗馥莉的联系方式。李继延听完一怔，告诉他，“从未接触过”。</p><p>对方不信，让李继延想想办法。李继延说：“娃哈哈不是有官网吗？你有没有给官网打过电话？”男人回说：“你以为我没打过吗？已经打过很多遍了。”</p><h2>当个赘婿，名正言顺“躺平”？</h2><p>即便对相亲市场的开门见山有所预期，但当真正身处沟通现场，内心还是不免为之一震。刚毕业的年轻大学生走后，一名开网约车的萧山本地人前来登记赘婿。男人戴一顶鸭舌帽，打门口经过时，大约168cm身高。</p><p>因为都是本地人，李继延和男人自此便开启了“加密”通话，因为即便在南京上过学，我也只能艰难听懂几句语气词，“噶嘛”“噶嘛好啦”。好在最后他们又开始用普通话沟通。李继延让对方摘掉帽子，看脱发严不严重。男人摘掉帽子，后脑勺有些稀疏。</p><p>“看来你压力蛮大的”，李继延笑着说。男人坦诚回答：“压力嘛，确实有一些。”“那你赌不赌？”李继延追问。男人回答，“不赌的。”“香烟吃不吃？酒呢？”男人挠了挠头，“每天嘛大概一包烟，酒嘛很少吃的。”</p><p>李继延有些犹豫，连着“噶嘛”了五六遍。男人见他颇为为难，跟他讲“报个名了嘛不要紧”，说完，起身走了。也许李继延一开始便觉得对方不符合要求，<strong>竟在刚才的对话中忘记询问芝麻信用的分数。</strong></p><p class="image-wrapper"><img data-img-size-val="1080,810" src="https://img.36krcdn.com/hsossms/20240422/v2_93689a459ae346eeb05d3b14c56a70a8@1743780481_oswg111067oswg1080oswg810_img_000?x-oss-process=image/format,jpg/interlace,1/format,jpg/interlace,1/format,jpg/interlace,1" referrerpolicy="no-referrer"></p><p class="img-desc">（摄/傅淼淼）</p><p>桌上打印了很多塑封文件，有李继延的采访，还有他写的爱情语录，其中还有一页是李继延写的拒绝对象——<strong>“有十种情形者婚介谢绝！”</strong></p><p>1.有犯罪记录；</p><p>2.心术不正，找情人二奶者；</p><p>3.素质低、粗劣、打骂人者；</p><p>4.身体上文身者（艺术文身者除外，不在明显地方，3厘米以内）；</p><p>5.偷盗等恶习不改者；</p><p>6.小鸡肚肠、心胸狭隘者；无不良嗜好，如喝酒、抽烟等等。</p><p>7.无理取闹，其它违法者；</p><p>8.心理变态者；</p><p>9.赌博、吸毒品、嫖娼、卖淫者；</p><p>10.有严重传染病者。</p><p>一经发现有以上劣迹者，婚介将拒绝服务，所收款项一律不退，有违法者，扭送司法机关，追究法律责任。</p><p>记者问李继延，“心理变态的人也不会直接告诉你啊？”李继延笑着说，“嗳，吓吓他嘛，先起到一个威慑作用。”每次遇到各方面符合条件的男客户，李继延都会把这张纸推至对方面前，让对方自查一下是否符合标准。</p><p>之前曾有一个清华毕业的男客户，因为胳膊上的文身，被李继延拒之门外，“女方不喜欢这样的。”</p><p><strong>前来应聘上门女婿的人很多，但符合标准的人很少。</strong>李继延和孙纪梅的把关十分严格，所以当符合条件的男女双方接触见面后，成功率亦十分高。</p><p>在李继延看来，过去的赘婿模式更容易出问题，因为男人上门后只想着好吃懒做，很多甚至沾染了赌博恶习。但近几年不会了，<strong>如今的赘婿赛道，早已挤满了优质人才。</strong>很多拿到户口的“新杭州人”，不仅在体制内有一份稳定工作，甚至还已经买好一套房。</p><p class="image-wrapper"><img data-img-size-val="1080,810" src="https://img.36krcdn.com/hsossms/20240422/v2_c33939818fe54eb287e370eb099b9051@1743780481_oswg153918oswg1080oswg810_img_000?x-oss-process=image/format,jpg/interlace,1/format,jpg/interlace,1/format,jpg/interlace,1" referrerpolicy="no-referrer"></p><p class="img-desc">（摄/傅淼淼）</p><p>李继延分析，如今的赘婿早已演变成四种形态：一是经济实惠型，男方各方面条件确实不好，倒插门入赘女方，以期改善生活；二是优势互补型，女方家里条件好，男方工作稳定、学历高，结婚后男方能帮忙辅导孩子功课，让下一代赢在起跑线上；三是强强联合型，男方已经有房有车，入赘是为了过上更舒适的生活，女方父母帮忙照顾下一代，自己的父母清闲一点；四是锦上添花型，男方自己有公司，年收入本就十分丰厚，入赘或许为了阶级跃升。一言以蔽之，入赘女婿正在逐步实现“新四化”：<strong>平常化、年轻化、高知化、优质化。</strong></p><p>无论是近期风靡的探讨女强男弱婚姻的《泪之女王》，抑或是出圈的男频爽剧“歪嘴龙王”系列——伴随着那句经典逆袭台词“三年之期已到，属于林家的，我要全部拿回来！”，加上嘴上的半永久的邪魅微笑，很多人对于赘婿的想象，更多聚焦在女强男弱婚姻的进退维谷，还有不少担心赘婿进门后会“软饭硬吃”，又要图女方家的财富和资源走捷径，又要当一家之主大男子主义，骨子里的旧观念还是没有变。</p><p>但在孙纪梅看来，这些预备上门当赘婿的男人，似乎并不会太过于纠结，很多抓马的场景无非是外界强加给他们的滤镜。担任红娘这么多年，李继延和孙纪梅似乎早已达成一种共识，<strong>所谓赘婿，无非是一种婚姻选择，一种既能帮助父母减轻压力，又能为下一代创造良好生活的婚姻模式，每个人都有权利选择自己想要的生活。</strong></p><p class="image-wrapper"><img data-img-size-val="1080,810" src="https://img.36krcdn.com/hsossms/20240422/v2_88dd9fba535c4870ae9698ed4ebc3e86@1743780481_oswg92621oswg1080oswg810_img_000?x-oss-process=image/format,jpg/interlace,1/format,jpg/interlace,1/format,jpg/interlace,1" referrerpolicy="no-referrer"></p><p class="img-desc">（摄/傅淼淼）</p><p>“我们筛选蛮严格的，通过前期沟通，人品就能试出个大概，太拧巴的我们这关都过不了。而且能招赘婿的，一般都是家里不舍得女儿受委屈，所以只要你对他们的女儿好，女方家里一定会加倍对你好。你去那些旅行社看看，很多节假日出国玩的都是女婿和丈母娘一家子出去。家里条件好的话，总会有很多时间一起玩。压力小一点，生活轻松一点。不然还个房贷几十年，哪有时间享受生活？大家都想过小康生活嘛。很简单的。”孙纪梅说。</p><h2>时代不同了，女人一样可以娶老公</h2><p><strong>杭州萧山的赘婿文化由来已久，上门女婿随处可见。</strong>这一点似乎天然为赘婿营造了宽松的文化环境，减轻了几千年文化积习难改的心理负担。</p><p>萧山在划区并市之前，是全国经济百强县；划区并市之后，又是全国经济百强区。在这片丰饶的土地上，曾经诞生过22家A股上市公司，一度家家设厂，户户开店。随着20世纪80年代计划生育的推进，萧山产生大量招婿需求，很多萧山企业家更是公开招领上门女婿。</p><p>此外，萧山还是把入赘写进拆迁条例的地方。2017年的<strong>《蜀山街道城中村改造房屋征收安置实施细则》</strong>中就提到了“符合入赘条件的女婿”，这里的入赘条件指家庭中有一个女儿或者两个女儿，家庭中必须没有男孩，但两个女儿只有一个可以入赘，另一个不能入赘。</p><p>这条规定更多针对萧山当地拆迁户，多一个上门女婿就能多拿70平米的安置房，实打实的真金白银，也是萧山当地喜欢找上门女婿的原因。李继延感慨：“70平方米啊，按现在的房价也要好几百万。现在赚钱多难，感情也是要讲现实的。”</p><p>不过，早期因为拆迁而选择入赘的男性，很多学历并不高，更不懂得经营婚姻，大多只知道好吃懒做，甚至沾染了赌博恶习。这或许也是李继延反复询问对方是否赌博的原因，查芝麻信用也是为了核实对方征信。</p><p>近几年，选择入赘的男性学历与个人条件均有明显提升，很多人调侃去萧山入赘难度不亚于考公上岸，还有人调侃，<strong>“改变人生的两个路口，一个是参加高考，一个是去萧山入赘”</strong>。这或许不过是一句笑谈，但“经济基础决定上层建筑”却是大多数人的共识。</p><p class="image-wrapper"><img data-img-size-val="1080,810" src="https://img.36krcdn.com/hsossms/20240422/v2_12f5a10b61f84e97877bfe57a1e2ef67@1743780481_oswg114209oswg1080oswg810_img_000?x-oss-process=image/format,jpg/interlace,1/format,jpg/interlace,1/format,jpg/interlace,1" referrerpolicy="no-referrer"></p><p class="img-desc">（摄/傅淼淼）</p><p>费孝通在《生育制度》一书中写道：“夫妇一方面是共同享受生活的乐趣，一方面又是共同经营一件极重要又极基本的社会事业。若不能两全其美，就得牺牲一项。在中国传统社会里是牺牲前者。”</p><p>夫妻之间要经营全面合作的生活：一是把事务上的合作减少，使夫妇间偏重感情调谐，趣味和兴趣的相投；一是把感情方面的要求撇开，偏重于经济上的、事业上的合作。在费孝通看来，“这种偏重的方向，初无高下之别；重要的是要看生活的环境如何。”毋庸置疑，通过相亲途径步入婚姻的两个人，大都选择了后者。</p><p>对很多人来讲，爱情似乎是一道语文题，需要做很多阅读理解，方能领悟彼此的心意，<strong>但婚姻却更像一道数学题，人们各自拿出筹码做资源置换，很多入赘女方家族企业的男性，就像是从女方家中拿到A轮、B轮、天使轮的投资。</strong></p><p>此外，杭州有着天然的地方文化优越感。人们常说“上有天堂，下有苏杭”，位于长三角核心地带的杭州萧山，经济的确要更发达一些，能够享受到很多城市化阶段性的成果，因此很多家庭会舍不得女儿外嫁，没有人会轻易离开“天堂”。</p><p>赘婿放在其他城市，或许尚且需要时间来接受，但在萧山当地，甚至会形成一种不招赘婿，反而不被理解的处境。孙纪梅就曾听邻里讨论某某家，因为没有招赘婿，被众人评价为“不要好”。</p><p>经营金点子婚介公司的25年来，赘婿的生意越来越好，报名费也从二三百元涨到了一万五千元。但李继延孙纪梅夫妇并没有因此发财，他们目前只有一套房产，一间100多平米的旧房子。</p><p class="image-wrapper"><img data-img-size-val="1080,810" src="https://img.36krcdn.com/hsossms/20240422/v2_1404f4b603f84968b6a9d746d2b39fcf@1743780481_oswg125212oswg1080oswg810_img_000?x-oss-process=image/format,jpg/interlace,1/format,jpg/interlace,1/format,jpg/interlace,1" referrerpolicy="no-referrer"></p><p class="img-desc">（摄/傅淼淼）</p><p>夫妇二人育有一个女儿，也曾考虑过招上门女婿，但家里只有一套房产，并不满足当地招赘的准入门槛。春节期间，女儿带两位老人去厦门旅游。李继延只在第一天出门拍了几张照片，剩下的时间一直待在宾馆忙着接打电话。孙纪梅感慨：“他忙都忙死了，根本没时间休息，出来了也在酒店办公。”</p><p>婚介所里除了李继延和孙纪梅，还有三名“爱情猎头”，由三名已经退休的阿姨组成。她们平日里不用坐班，利用自身人脉为会员找到匹配对象，“资源多了，成功率自然会高。”</p><p>李继延还经常写文章在杭州各大城市报刊投稿、登广告，“很多人以为我们夫妻开了这么多年婚介公司，一定有很多存款。其实我们手里根本没有钱。我们需要一直花钱搞推广，只有这样才能吸引更多优质男青年上门。”</p><p class="image-wrapper"><img data-img-size-val="1080,810" src="https://img.36krcdn.com/hsossms/20240422/v2_4977169e35934116a580c2d55ec8af23@1743780481_oswg113589oswg1080oswg810_img_000?x-oss-process=image/format,jpg/interlace,1/format,jpg/interlace,1/format,jpg/interlace,1" referrerpolicy="no-referrer"></p><p class="img-desc">（摄/傅淼淼）</p><p>李继延曾是杭州萧山五金交电公司的员工，还在夜校做过日语老师。他第一次帮别人促成姻缘，正是把外地同事介绍给当地人做上门女婿。1999年，李继延从国企下岗，便开了金点子嫁娶赘婿公司，如今的婚介所仍开在他曾经任职的前国企大楼里。</p><p>“我们以青年、中年、老年婚姻嫁娶为主，这些要占业务量的3/4，上门女婿不过占总业务量的1/4。很多人认为我们是专做上门女婿的，肯定是误会了。赘婿不过是我们萧山当地的特色。”李继延说。</p><p>金点子婚介公司的墙上挂着<strong>“天下第一红娘”</strong>的招牌，另一面墙上，则挂满了李继延接受媒体采访的合影。婚介所里，处处可见李继延总结的“爱情箴言”，他给每一个都取了名字：《爱情兵法》《择偶忠告》《恋爱三部曲》……</p><p>一则箴言上写着——呼吁全国各大、中、小城市，农村家庭，有多套房，比较富裕的大龄女、适龄女，移风易俗，把暂时无房的大龄男、适龄男娶了吧！<strong>时代不同了，女人一样可以娶老公！</strong></p><p class="image-wrapper"><img data-img-size-val="1080,810" src="https://img.36krcdn.com/hsossms/20240422/v2_6b717fe2d73c46cbba83530dc59df8a2@1743780481_oswg128412oswg1080oswg810_img_000?x-oss-process=image/format,jpg/interlace,1/format,jpg/interlace,1/format,jpg/interlace,1" referrerpolicy="no-referrer"></p><p class="img-desc">（摄/傅淼淼）</p><p class="editor-note">本文来自微信公众号<a target="_blank" rel="noopener noreferrer nofollow" href="https://mp.weixin.qq.com/s/XqOV39A47q7DNmCA_-i5uQ">“惊蛰青年”（ID:wakinglism）</a>，作者：傅淼淼，校对：遇见，编辑：尤蕾，36氪经授权发布。</p>"""

# 初始化 Markdown 解析器
md = MarkdownIt().use(front_matter_plugin).use(footnote_plugin)

def main():
    
    markdown_content = html_to_markdown(content)
    logging.info(f"markdown_content: {markdown_content}")
    env = {}
    tokens = md.parse(markdown_content, env)
    logging.info(f"tokens: {tokens}")
    notion_blocks = convert_to_notion_blocks(tokens)
    # for block in notion_blocks:
        # print(block)
    logging.info(f"notion_blocks: {notion_blocks}")
                

if __name__ == "__main__":
    main()
