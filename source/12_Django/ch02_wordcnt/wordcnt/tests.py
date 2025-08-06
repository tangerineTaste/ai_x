from django.test import TestCase

# Create your tests here.
fulltxt = '홍길동 홍길동 아자'
strlength = len(fulltxt) # 글자수
words = fulltxt.split() # 단어들
wordcnt = len(words) # 단어 수
word_dic = dict() # 빈 딕셔너리 => {'홍길동':2, '아자':1}

for word in words:
    if word in word_dic.keys():
        word_dic[word] += 1
    else:
        word_dic[word] = 1

print(fulltxt)
print('글자수 -',strlength)
print('단어들 -',words)
print('단어수 -', wordcnt)
print(word_dic.items())