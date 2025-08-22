from django.db import models
from django.contrib.auth.models import User
from decouple import config
# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User,
          on_delete=models.CASCADE) # User가 삭제될 때, profile은 어떻게 할지?
  phone_number = models.CharField(verbose_name="전화", max_length=20)
  address      = models.CharField(verbose_name="주소", max_length=100)
  def __str__(self):
    return "{}({}-{})".format(self.user.username,
                              self.phone_number,
                              self.address)
  
# 이벤트처리 == (post_save) : profile.save() 성공시 가입인사를 매일로 전송
from django.db.models.signals import post_save
from django.core.mail import send_mail
GMAIL_HOST_USER = config("GMAIL_HOST_USER")
def on_send_mail(sender, **kwargs):
  print("이벤트 처리 시작", kwargs)
  if kwargs['created']: # True: 회원가입, False: 이미 존재하는 회원정보 수정 등
    user = kwargs['instance'].user
    if not user.email:
      print("이메일 주소가 없어")
      return
    subject = f"{user.username}님 가입을 환영합니다!"
    body = f"안녕하세요 {user.username}님\n\n가입인사를 받으시길 바랍니다.\n\n감사합니다."
    bodyhtml = f"<p>안녕하세요 {user.username}님</p><p>가입인사를 받으시길 바랍니다.</p><p>감사합니다.</p>"
    send_mail(subject, body, GMAIL_HOST_USER, [user.email], html_message=bodyhtml) # type: ignore
# on_send_mail 함수와 post_save 연결
post_save.connect(on_send_mail, sender=Profile)