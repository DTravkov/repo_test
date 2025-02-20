import re


pattern1 = "ab*"
test_case1 = 'abbbba'
print(bool(re.match(pattern1,test_case1)))
pattern2 = "ab{2,3}"
test_case2 = 'abbbb'
print(bool(re.match(pattern2,test_case2)))

pattern3 = r"\b[a-z]+_[a-z]+\b"
test_case3 = 'lower_case not_upper_case' # second *not_upper_case consists of 3 words.thats why it is not included
print(re.findall(pattern3,test_case3))

pattern4 = r"\b[A-Z]{1}[a-z]+\b"
test_case4 = "Username azbdfb Usernameovich"
print(re.findall(pattern4,test_case4))

pattern5 = r"(.*a.*b\b)"
test_case5 = 'BVVC999aVCZXCZXCZXKVOFO_)_()(||b'
print(bool(re.match(pattern5,test_case5)))

pattern6= r"[\s,.]"
test_case6 = 'I\'ve been to many, many places'
print(re.sub(pattern6, ":",test_case6))

test_case7 = "case_sentence"
test_case7 = ''.join(word.capitalize() for word in test_case7.split('_'))
print(test_case7)


test_case8 = "CaseSentence"
pattern8 = '[A-Z][a-z]+|[a-z]+'
re.findall(pattern8,test_case8)
print(re.findall(pattern8,test_case8))

test_case9 = "CaseSentence"
pattern9 = '[A-Z][a-z]+|[a-z]+'
re.findall(pattern9,test_case9)
print(' '.join(re.findall(pattern9,test_case9)))


test_case10 = 'CamelToSnake'
test_case10 = '_'.join(x.lower() for x in re.findall('[A-Z][a-z]+',test_case10))
print(test_case10)
