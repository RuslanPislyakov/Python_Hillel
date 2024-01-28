import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    add_dict = False
    temp = ''
    tags = set()
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        for ch in html:
            if ch == '<':
                add_dict = True
            if add_dict:
                temp += ch
            if ch == '>':
                add_dict = False
                tags.add(temp)
                temp = ''

        for tag in tags:
            html = html.replace(tag, '')

    with codecs.open(result_file, 'w', 'utf-8') as result:
        result.write(html)


delete_html_tags('draft.html')
