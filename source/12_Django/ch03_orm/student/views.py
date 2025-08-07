from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from django.contrib import messages

def list(request):
    students = Student.objects.all()
    return render(request, 'student/list.html', {'students':students})

def get(request, id):
    
    try:
        student = Student.objects.get(id=id)
        return render(request, 'student/get.html', {'student':student}, )
    except Student.DoesNotExist:
        messages.error(request, f'{id}번 학생을 찾을 수 없습니다.')
        return redirect("student:list")
    
def delete(request, id:int):
    studnet = Student.objects.get(id=id) # 없는 id일 경우 빈 list
    if studnet:
        studnet.delete()
        messages.success(request, f'{id}번 학생 삭제 완료!')
        return redirect('student:list')
    else:
        messages.error(request, f'{id}번 학생은 존재하지 않습니다')
        return redirect('student:list')