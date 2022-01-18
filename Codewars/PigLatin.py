def pig_it(text):
    new_text = []
    split_string = text.split(" ")
    for word in split_string:
        if word.isalpha():
            split_word = list(word)
            split_word.append(split_word[0] + 'ay')
            split_word.remove(list(word)[0])
            new_text.append(''.join(split_word))
        else:
            new_text.append(word)
    return ' '.join(new_text)


if __name__ == "__main__":
    print(pig_it('Pig latin is cool !'))
