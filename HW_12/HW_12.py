
prohibited_chars = "_!#$%&'()*+,-./:;<=>?@[\\]^`{|}~ \""

text = input('Type text to convert to hashtag ')

text = text.title()

for ch in prohibited_chars:
    if ch in text:
        text = text.replace(ch, '')

text = '#' + text[:139]

print(text)
