def Change_text(text):
    '''
    function change all words in text
    function work only for russian language
    :param text: text in which we change all words
    :return: text with changed words
    '''
    def Max_change_word(word):
        '''
        function change max quantity letters in word
        function work only for russian words
        :param word: word in which we change letters
        :param set_of_vowels: vowels letters
        :param set_of_used_index: letters indexes hat we change
        :return : changed word
        '''
        result_word = ''
        set_of_vowels = 'йуеыаоэяиью'
        # add index of the first and the last letters
        set_of_used_index = {0, len(word) - 1}
        word_mas = [letter for letter in word]
        if len(word_mas) > 4:
            j = 0
            # go through each letter
            for i in range(1, len(word_mas)):
                if not (i in set_of_used_index):
                    j = 1
                    # if letter is vowel swap it with the nearest vowels in range 3
                    if word_mas[i] in set_of_vowels:
                        while (j < 4) and (j + i < len(word_mas) - 1):
                            if (word_mas[i + j] in set_of_vowels) and not (i + j in set_of_used_index)\
                                    and (word[i] != word[i+j]):
                                word_mas[i], word_mas[i + j] = word_mas[i + j], word_mas[i]
                                set_of_used_index = set_of_used_index.union({i + j})
                                break
                            j += 1
                    # if letter is consonant swap it with the nearest consonant in range 3
                    else:
                        while (j < 4) and (j + i < len(word_mas) - 1):
                            if (not (word_mas[i + j] in set_of_vowels)) and not (i + j in set_of_used_index) \
                                    and (word[i] != word[i + j]):
                                word_mas[i], word_mas[i + j] = word_mas[i + j], word_mas[i]
                                set_of_used_index = set_of_used_index.union({i + j})
                                break
                            j += 1
            # if last but one letter didn't swap with anything swap it with the previous
            if not (len(word_mas) - 2 in set_of_used_index):
                word_mas[-3], word_mas[- 2] = word_mas[- 2], word_mas[- 3]
        # if length of word is 3 or 4 swap second and third letters
        elif len(word_mas) > 2:
            word_mas[1], word_mas[2] = word_mas[2], word_mas[1]
        for i in word_mas:
            result_word += i
        return result_word

    word = ''
    result_text = ''
    # go through each letters
    for i in range(len(text)):
        # if i symbol is a letter add it to variable 'word'
        if 1040 <= ord(text[i]) <= 1103:
            word += text[i]
            # if i letter is the last one, change word and add it to the result_text
            if i + 1 == len(text):
                result_text += Max_change_word(word)
        # if i symbol is not a letter and previous symbol is a letter,
        # change word and add it with i symbol to result_text
        elif (not (1040 <= ord(text[i]) <= 1103)
              and ((1040 <= ord(text[i - 1]) <= 1103) and i != 0)):
            result_text += Max_change_word(word) + text[i]
            word = ''
        else:
            result_text += text[i]
    return result_text

def compare_text(text,changed_text):
    changed_letters = 0
    for i in range(len(text)):
        if text[i] == changed_text[i]:
            changed_letters +=1
    return changed_letters
text = input('введите текст на русском')
changed_text = Change_text(text)
print(text, '\n', changed_text, '\n', compare_text(text, changed_text), '\n', len(text))