def count_words(string):
    if string:
        count = 1
        for i in range(0, len(string)):
            if string[i] == " ":
                count += 1
        return count
    else:
        return 0