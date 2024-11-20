# 导入pandas，用于数据提取
import pandas as pd
# 导入jieba分词，可用于文章分词
import jieba
# 导入collection模块的Counter方法，对分完词后的词进行频数统计
from collections import Counter
# 导入wordCloud及配置模块,利用pyecharts绘制词云WordCloud，当然你也也可以安装WordCloud库进行词云绘制
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType


# 可根据你的数据集来判断是否使用pandas进行文本数据获取，如要获取爬取出来的csv文件等，下面例子展示了获取评论文件中关于某种商品（goods)的评论(str)text
# def get_text(goods):
#     path ='comments.csv'
#     with open(path,encoding='utf-8') as f:
#         data =pd.read_csv(f)
#     #商品种类
#     types = data['cat'].unique()
#     #获取该商品种类的评论文本
#     text = data[(data['cat']==goods)]['review'].values.tolist()
#     text = str(text)[1:-1]
#     print(types)
#     return text

# 读取停用词
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
    # readlines()读取所有行并返回列表
    return stopwords


if __name__ == '__main__':
    # 读取样例文本（你需要在此文件中修改你自己的数据，可采用多种停用词的分割符、
    # 空格、空行进行关键词分割）
    with open('004.txt', 'r', encoding='utf-8') as f:
        sentence = f.read()
    # 如果使用pandas
    # sentence = get_text(goods)

    # 读取停用词
    stopwords = stopwordslist(r"stopwords.txt")  # 读取停用词，原文件无转译符

    # # -------------------1.大段文字，需利用jieba分词----------------------------
    # # 如果你是一大段文字，可以采用结巴分词进行分词
    sentence = jieba.lcut(sentence)  # 调用结巴分词，获得generator类型数据
    # 给停用词添加换行符号
    stopwords.append('\n')
    # 将分词结果消除空格形成列表
    dict = []
    for word in sentence:
        if word not in stopwords:
            dict.append(word.replace(' ', ''))
    sentence = "".join(dict)
    #
    # # ------------------------------------------------------------------------

    # --------------2.段内有明显分割符号，仅利用停用词文件进行分割--------------------
    # 将可能出现在停用词中的符号全部转换为空格
    # dict = []
    # for word in sentence:
    #     if word in stopwords:
    #         dict.append(" ")
    #     else:
    #         dict.append(word)
    #     # else: dict = sentence.split()
    # sentence = "".join(dict)
    # # 以空格分割字符串并形成列表
    # dict = sentence.split()

    # --------------------------------------------------------------------------

    # 分词结果
    print("分词结果为：")
    print(dict)

    # 词频统计,使用Count计数方法
    words_counter = Counter(dict)
    # 将Counter类型转换为列表
    words_list = words_counter.most_common(2000)
    # 统计词频出现次数
    print("统计结果为：")
    print(words_list)

    # WordCloud模块，链式调用配置，最終生成htmL文件
    c = (
        WordCloud()
        .add("", words_list, word_size_range=[15, 100], word_gap=3, is_draw_out_of_bound=False, shape="pentagon")
        .set_global_opts(title_opts=opts.TitleOpts(title="词云"), tooltip_opts=opts.TooltipOpts(is_show=True), )
        .render("词云.html")
    )
    # 进入html，在浏览器打开即可看到效果
    print("\n词云已生成！请到评论词云.html文件中查看!")
