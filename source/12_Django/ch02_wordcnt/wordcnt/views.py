from django.shortcuts import render

def wordinput(request):
    return render(request, 'wordcnt/wordinput.html')

def about(request):
    return render(request, 'wordcnt/about.html')

def result(request):
    fulltxt = request.POST['fulltxt']
    strlength = len(fulltxt) # 글자수
    words = fulltxt.split() # 단어들
    wordcnt = len(words) # 단어 수
    word_dic = dict() # 빈 딕셔너리 => {'홍길동':2, '아자':1}

    for word in words:
        if word in word_dic.keys():
            word_dic[word] += 1
        else:
            word_dic[word] = 1

    context={'fulltxt':fulltxt,
             'wordcnt':wordcnt, 
             'strlength':strlength, 
             'dict':word_dic.items()}

    return render(request, 'wordcnt/result.html', context=context)
