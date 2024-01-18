def popular_words(text, words):

    text_lst = text.lower().split()

    res_dict = dict.fromkeys(words, 0)
    for word in text_lst:
        if word in res_dict:
            res_dict[word] += 1
    print(res_dict)
    return res_dict


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
