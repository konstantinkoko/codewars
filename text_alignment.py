def justify(text, width):
    words_list = text.split()
    string = ''
    len_of_words = 0
    words_counter = 0
    last_string = False
    for i in range(len(words_list)):
        if i == len(words_list) - 1:
            last_string = True
            end_of_string = True
        elif ((len_of_words + len(words_list[i]) + words_counter) < width) and\
            ((len_of_words + len(words_list[i]) + len(words_list[i + 1]) + words_counter + 1) <= width):
            end_of_string = False
        else:
            end_of_string = True
        words_counter += 1
        len_of_words += len(words_list[i])
        if end_of_string:
            if words_counter > 1:
                backspaces_extra = (width - len_of_words)//(words_counter - 1)
                backspaces_remainder = (width - len_of_words) % (words_counter - 1)
                for j in range(words_counter - 1):
                    if last_string:
                        backspaces = 1
                    elif j <= backspaces_remainder - 1:
                        backspaces = backspaces_extra + 1
                    else:
                        backspaces = backspaces_extra
                    string += words_list[i - words_counter + j + 1] + backspaces * ' '
            if last_string:
                string += words_list[i]
            else:
                string += words_list[i] + '\n'
            len_of_words = 0
            words_counter = 0
    return string


print(justify('qw w wq qw w qw q ww   e we q eq   qe we q eqe eqw ewq ewq e qwe q  q we qw e wq wq eq e wqe wq  ee qweqw  qw ee wq ewq e wqe qw e', 9))
