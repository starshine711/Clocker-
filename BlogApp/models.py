from django.db import models
from django import forms

# Create your models here.
class Comment(models.Model):
    user = models.CharField(u"发布者", max_length=50,default='none')
    at_article = models.IntegerField(default=0)
    words = models.CharField(u"文本", max_length=50,default='none')
    pub_time =  models.DateTimeField(u'发布时间', auto_now=True, null=True)
    email = models.CharField(u"文本", max_length=50,default='none')
    def __str__(self):
        return self.user

    class Meta:  # 按时间下降排序
        ordering = ['-pub_time']
        verbose_name = "评论"
        verbose_name_plural = "评论"

class Article(models.Model):
    title = models.CharField(u"博客标题", max_length=100)  # 博客标题
    category = models.CharField(u"博客标签", max_length=50, blank=True)# 博客标签
    author = models.CharField(u"作者", max_length=50)
    pub_date = models.DateTimeField(u"发布日期", auto_now_add=True, editable=True)  # 博客发布日期
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)
    content = models.TextField(blank=True, null=True)  # 博客文章正文
    photo = models.TextField(default='none',blank=True, null=True)
    photo_list= models.TextField(default='none',blank=True, null=True)
    like_user = models.TextField(default=' ',blank=True, null=True)
    number = models.IntegerField(default=0)
    look_number =  models.IntegerField(default=0)
    comment_number = models.IntegerField(default=0)
    author_email = models.CharField(u"作者邮箱", max_length=50, blank=True)
    def __str__(self):
        return self.title

    class Meta:  # 按时间下降排序
        ordering = ['-pub_date']
        verbose_name = "文章"
        verbose_name_plural = "文章"


class User(models.Model):
    '''用户表'''

    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    name = models.CharField('名字',max_length=128, unique=True)
    password = models.CharField('密码',max_length=256)
    email = models.EmailField('邮箱',unique=True)
    sex = models.CharField('性别',max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField('注册时间',auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'

class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
