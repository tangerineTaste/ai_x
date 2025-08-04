from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def index(request):
    context = {
        'msg':'WordCount Welcome Page',
        'greeting': 'Hello, Django(장고)',
    }
    return render(request=request,
                  template_name='home/index.html',
                  context=context)

def test(request):

    return HttpResponse('''<h1>테스트 페이지</h1>
                        <button onclick="location='/'"> 처음으로</button>
                       ''')

def showIntId(request:HttpRequest, id:int):
    msg = f'숫자 ID는 {id}'
    id_type = "int 입니다"
    return render(request, 'home/showId.html', {'msg':msg, 'type':id_type})

def showStrId(request:HttpRequest, id:str):
    msg = f'문자 ID는 {id}'
    id_type = "str 입니다"
    return render(request, 'home/showId.html', {'msg':msg, 'type':id_type})