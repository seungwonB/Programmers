def solution(s):
    word = ''
    word_dict = {0:'zero', 1:'one', 2:'two',
                 3:'three', 4:'four', 5:'five',
                 6:'six', 7:'seven', 8:'eight', 9:'nine'}

    for i in range(10):
        s = s.replace(word_dict[i], str(i))

    return int(s)