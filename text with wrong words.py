def Change_text(text):
    '''
    function change all words in text
    function work only for russian language
    :param text: text in which we change all words
    :return: text with changed words
    '''
    def Change_word(word):
        '''
        function swap second and third letters
        :param word: word in which we change letters
        :return : changed word
        '''
        result_word = ''
        i = 3
        if len (word) > 2:
            result_word += word[0] + word [2] + word [1]
            while i < len(word):
                result_word += word[i]
                i += 1
        return result_word

    i = 0
    word = ''
    result_text = ''
    # go through each letters
    for i in range(len(text)):
        # if i symbol is a letter add it to variable 'word'
        if 1040 <= ord(text[i]) <= 1103:
            word += text[i]
            # if i letter is the last one, change word and add it to the result_text
            if i + 1 == len(text):
                result_text += Change_word(word)
        # if i symbol is not a letter and previous symbol is a letter,
        # change word and add it with i symbol to result_text
        elif (not (1040 <= ord(text[i]) <= 1103)
              and ((1040 <= ord(text[i - 1]) <= 1103) and i != 0)):
            result_text += Change_word(word) + text[i]
            word = ''
        else:
            result_text += text[i]

    return result_text

text = input('введите текст на русском')

print(text)
print(Change_text(text))