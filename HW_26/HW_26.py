def first_word(text):
    res = ''
    flag = False
    for ch in text:
        if ch.isalpha() or ch == "'":
            flag = True
            res += ch
        if not ch.isalpha() and flag and not ch == "'":
            break
    return res


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')

