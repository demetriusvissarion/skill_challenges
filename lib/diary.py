def make_snippet(text):
    count = 0
    for i in range(0, len(text)):
        if text[i] == " ":
            count += 1
    if count in range(0, 5):
        return text
    else:
        words = text.split()
        result = ' '.join(words[0:5]) + '...'
        return result
    
print(make_snippet('one two three four five six'))