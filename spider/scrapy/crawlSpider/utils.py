import config
import jieba
import pandas as pd


# 去掉回车换行
def delete_r_n(line):
    return line.replace("\r", "").replace("\n", "").strip()


# 读取停用词
def get_stop_words(stop_words_dir):
    stop_words = []

    with open(stop_words_dir, "r", encoding=config.encoding) as f_reader:
        for line in f_reader:
            line = delete_r_n(line)
            stop_words.append(line)

    stop_words = set(stop_words)
    return stop_words


# jieba精确分词
def jieba_cut_for_train(content, stop_words):
    word_list = [[]]
    new_seg = []
    if content != "" and content is not None:
        seg_list = jieba.cut(content)
        for word in seg_list:
            if word not in stop_words:
                new_seg.append(word)

    seg_len = len(new_seg)
    for i in range(6):
        step = i+1
        if(seg_len < step):
            break
        else:
            bb = [new_seg[i:i + step] for i in range(0, len(new_seg), step)]
            for b in bb:
                if b not in word_list:
                    word_list.append(b)
    del word_list[0]
    return word_list

# jieba精确分词
def jieba_cut(content, stop_words):
    word_list = []
    if content != "" and content is not None:
        seg_list = jieba.cut(content)
        for word in seg_list:
            if word not in stop_words:
                word_list.append(word)
    return word_list

# jieba搜索引擎分词
def jieba_cut_for_search(content, stop_words):
    word_list = []
    if content != "" and content is not None:
        seg_list = jieba.cut_for_search(content)
        for word in seg_list:
            if word not in stop_words:
                word_list.append(word)

    return word_list


# 清除不存在词汇表中的词语
def clear_word_from_vocab(word_list, vocab):
    new_word_list = []

    for word in word_list:
        if word in vocab:
            new_word_list.append(word)

    return new_word_list


# 文本预处理
def preprocessing_text_pd(text_dir, after_process_text_dir, stop_words_dir):
    stop_words = get_stop_words(stop_words_dir)
    sentences = []
    df = pd.read_csv(text_dir)

    for index, row in df.iterrows():
        # print(index)
        title = delete_r_n(row['title'])
        word_list = jieba_cut(title, stop_words)
        df.loc[index, 'title'] = " ".join(word_list)
        sentences.append(word_list)
    df.to_csv(after_process_text_dir, encoding=config.encoding, index=False)

    return sentences


# 文本预处理第二种方式
def preprocessing_text(text_dir, after_process_text_dir, stop_words_dir):
    # count = 0
    stop_words = get_stop_words(stop_words_dir)
    sentences = []
    f_writer = open(after_process_text_dir, "w")

    with open(text_dir, "r") as f_reader:
        for line in f_reader:
            line_list = line.strip().split(",")
            if(len(line_list)>1):
                aaa = delete_r_n(line_list[1])
                aa = jieba_cut_for_train(aaa, stop_words)
                for a in aa:
                    #print(a)
                    if a not in sentences:
                        sentences.append(a)
                        f_writer.write(" ".join(a) + "\n")
                        f_writer.flush()
            if len(line_list)==3 and line_list[2]!='':
                hh = delete_r_n(line_list[2])
                word_list = jieba_cut_for_train(hh, stop_words)

                for qq in word_list:
                    # print(qq)
                    if qq not in sentences:
                        sentences.append(qq)
                        f_writer.write(" ".join(qq) + "\n")
                        f_writer.flush()
    f_writer.close()
    return sentences

def preproce_text():
    data=[]
    with open('data/train_data.csv','r')as f:
        for line in f:
            d_list = line.split(',')
            d_new = []
            for d in d_list:
                if d == '\n':
                    pass
                else:
                    d1 = d.strip()
                    d2 = d1.strip('?')
                    d_new.append(d2)
            # d_str = ','.join(d_new)
            print(d_new)
            data.append(d_new[0])

    with open('data/train_data01.csv','w')as f:
        for i in range(len(data)):
            f.write(data[i]+'\n')
def get_sectenses():
    candates = []
    with open('data/cut_train_data.csv','r')as f:
        for line in f:
            candate = []
            line = line.split(' ')
            for it in line:
                candate.append(it.strip())
            candates.append(candate)
    return candates

def add_new_sectenses():
    # count = 0
    stop_words = get_stop_words('data/stop_words.txt')
    sentences = get_sectenses()
    f_writer = open('data/cut_train_data.csv', "a+")

    with open('data/add_train_data.csv', "r") as f_reader:
        for line in f_reader:
            hh = delete_r_n(line)
            word_list = jieba_cut_for_train(hh, stop_words)
            for qq in word_list:
                # print(qq)
                if qq not in sentences:
                    sentences.append(qq)
                    f_writer.write(" ".join(qq) + "\n")
                    f_writer.flush()
    f_writer.close()
    return sentences

if __name__ == "__main__":  # 如果只是运行本脚本
    # stop_words = get_stop_words(config.stop_word_dir)
    # content = "农、林、牧、渔业产品为原料进行的谷物磨制、饲料、植物油和制糖、屠宰及肉类、水产品，以及蔬菜、水果和坚果等食品的加工"
    # word_list = jieba_cut_for_train(content, stop_words)
    # word_list = jieba_cut(content, stop_words)
    # print(len(word_list),word_list)
    # word_list = jieba_cut_for_search(content, stop_words)
    # print(word_list)
    # preproce_text()
    # sentences = preprocessing_text('data/train_data.csv', 'data/cut_train_data.csv', 'data/stop_words.txt')
    # print(sentences)
    add_new_sectenses()
    # preproce_text()
