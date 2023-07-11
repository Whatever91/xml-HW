import xml.etree.ElementTree as ET


def read_xml(file_path, word_max_len=6, top_words_amt=10):
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse('newsafr.xml', parser)
    root = tree.getroot()
    all_words = []
    news_list = root.findall('channel/item/description')
    for news in news_list:
        raw = [word for word in news.text.split() if len(word) > word_max_len]
        all_words.extend(raw)
    unique_words = list(set(all_words))
    words_counted = [[word, all_words.count(word)] for word in unique_words]
    words_counted.sort(key=lambda x: x[1], reverse=True)
    result = [w[0] for w in words_counted[:top_words_amt]]
    return result

if __name__ == '__main__':
    print(read_xml('newsafr.xml'))