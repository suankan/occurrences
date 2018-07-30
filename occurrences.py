'''
Preface:
Do not use any extended functionality of the framework to solve this problem. \
(For example, don't use the string methods that have functionality such as \
IndexOf, substring, regular expression classes, LINQ etc). The test should \
take no longer than an hour for you to complete, please submit the working \
source code to solve the problem along with any supporting code that you \
might have used in testing.

Problem:
We need a way of finding all the occurrences of a particular set of \
characters in a string. It should

Accept two strings as input. One called 'textToSearch' and one called 'subtext'
The solution should match the subtext against the textToSearch, outputting \
the positions of the beginning of each match for the subtext within the \
textToSearch.

Multiple matches are possible
Matching is case insensitive
If no matches have been found, no output is generated

Sample Acceptance Criteria
Text:
textToSearch = "Peter told me that peter the pickle piper piped a pitted \
pickle before he petered out. Phew!"
Subtext: Expected Result
Peter "1, 20, 75"
peter "1, 20, 75"
pick "30, 58"
pi "30, 37, 43, 51, 58"
z "<No Output>"
Peterz :<No Output>"
'''


def find_all_occurrences(text_to_search, sub_text):
    '''
    Method:

    For each character in a given textToSearch we will be checking if the \
    next sequence of chars from 0 to the length of given search pattern \
    equals to a corresponding character in subText pattern. If every next \
    char coinside we increment ok_counter by one. In the end of the length \
    of subText pattern if ok_counter equals to the length of subText \
    pattern - it means the whole subText pattern was found.

    Bounds: the most outer range will be from 0 to the length of \
    textToSearch minus length of subText in order to never go out \
    of list indexes.

    Note! expected result counts occurrences from 1, not from 0.
    '''

    sub_test_len = len(sub_text)

    result = []
    for i in range(len(text_to_search) - sub_test_len):
        ok_counter = 0
        for j in range(sub_test_len):
            if sub_text[j].lower() == text_to_search[i+j].lower():
                ok_counter += 1

        if ok_counter == sub_test_len:
            result.append(str(i+1))
        else:
            continue

    if not result:
        return '<No Output>'

    return ', '.join(result)
