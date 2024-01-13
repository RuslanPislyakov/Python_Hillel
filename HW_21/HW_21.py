def is_palindrome(init_str):
    punctuation_chars = "!,-.:;? "

    init_str = init_str.lower()

    for ch in punctuation_chars:
        if ch in punctuation_chars:
            init_str = init_str.replace(ch, '')

    revers_lst = list(init_str)
    revers_lst.reverse()
    revers_str = ''.join(revers_lst)

    if init_str == revers_str:
        return True
    else:
        return False


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
