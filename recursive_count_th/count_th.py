'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    n = "th"
    if len(word) < len(n):
        return 0
    elif word[0:len(n)] == n:
        return 1+count_th(word[1:])
    else:
        return count_th(word[1:])


# def count_th(word, n):
#     if len(word) == 0:
#         return 0
#     # print(word[0: len(n)])
#     elif word[0: len(n)] == n:  # if the first x chars in the word matches n
#         return 1 + count_th(word[len(n)-1:], n)
#     else:
#         return count_th(word[len(n)-1:], n)  # count from the remaining index
if __name__ == '__main__':
    wordy = "ththththhhthth"
    n = "gabby"
    # wordy = "geeksforgeeks"
    # n = "geeks"
    print(count_th(wordy))
    # print(count_th(wordy, n))

# def count_th(word, n):
#     if not word:
#         return 0
#     elif word[0] == n:
#         print("first char", word[0], n)
#         return 1+count_th(word[1:], n)
#     else:
#         print("slice", word[1:], n)
#         return count_th(word[1:], n)


# word = "thhtthht"
# n = "th"

# print(count_th(word))
