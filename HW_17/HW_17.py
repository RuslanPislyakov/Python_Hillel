def correct_sentence(text):
    temp_lst = list(text)
    if temp_lst[0].islower():
        temp_lst[0] = temp_lst[0].capitalize()
    if text[-1] != '.':
        temp_lst.append('.')
    return "".join(temp_lst)


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
