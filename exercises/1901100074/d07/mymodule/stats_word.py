def stats_text_en(text):
    elements = text.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        if len(element) and element.isascii():
            words.append(element)
    counter = {}
    word_set = set(words)
    for word in word_set:
        counter[word] = words.count(word)
    return sorted(counter.items(),key=lambda x: x[1],reverse=True)


def stats_text_cn(text):
    cn_characters = []
    for character in text:
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    counter = {}
    cn_character_set = set(cn_characters)
    for character in cn_character_set:
        counter[character] = cn_characters.count(character)
    return sorted(counter.items(),key=lambda x: x[1],reverse=True)

def stats_text(text):
    #合并 英文词频 和 中文字频 的结果
    return stats_text_en(text) + stats_text_cn(text)
if __name__ == '__main__':
    en_result = stats_text_en(en_text)
    cn_result = stats_text_cn(cn_text)
    print('统计参数中每个英文单词出现的次数 ==>\n',en_result)
    print('统计参数中每个中文单词出现的次数 ==>\n',cn_result)