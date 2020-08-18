from django.shortcuts import render,redirect,HttpResponse
from .models import User,RegisterForm,Article,Comment
from . import c3
basic = c3.basic
import json
# Create your views here.
def main(request):
    #return redirect("/index/")
    return render(request,'main.html')

def index(request):    
    article = Article.objects.all()
    user_head = [User.objects.get(name=i.author).email.replace('@qq.com','') for i in article ]
    return render(request,'new\index.html',{'article':article,'latest_article':article[0:3]})
def choose_comment(id):
    comment_all = Comment.objects.all()
    comment = []
    for c in comment_all:
        if c.at_article == int(id):
            comment.append(c)
    return comment
       #对应文章的评论
def showArticle(request):
    if request.GET and 'id' in request.GET:
        id = request.GET.get('id')
        article = Article.objects.get(id=id) 
        article.look_number += 1  
        comment = choose_comment(id)
        article.comment_number = len(comment)
        article.save()
        if request.POST:
            if request.session.get('is_login', None) and request.POST.get('words'):# 是否登录
                article = Article.objects.get(id=id)
                article.comment_number += 1
                article.save()
                new_comment = Comment.objects.create()
                new_comment.user = request.session.get('user_name')
                new_comment.email = User.objects.get(name=new_comment.user).email.replace('@qq.com', '')
                new_comment.words = request.POST.get('words')
                new_comment.at_article = int(id)
                new_comment.save()
                comment = choose_comment(id)
                return render(request, '{}.html'.format(id), {"message": "评论成功", 'i': article, "comment": comment})
            if request.POST.get('name') and request.POST.get('email') and request.POST.get('words'):
                comment_txt = request.POST.get('words')
                article = Article.objects.get(id=id)
                article.comment_number+=1
                article.save()
                new_comment = Comment.objects.create()
                new_comment.user = request.POST.get('name') 
                new_comment.email = request.POST.get('email').replace('@qq.com','')
                new_comment.words = request.POST.get('words') 
                new_comment.at_article = int(id)
                new_comment.save()
                comment = choose_comment(id)
                return render(request,'{}.html'.format(id),{"message":"评论成功",'i':article,"comment":comment})
            else:
                return render(request, '{}.html'.format(id), {"message":'请将表单内容填写完整','i':article,"comment":comment})
        return render(request,'{}.html'.format(id),{'i':article,"comment":comment})
    else:        
        message = '页面无法访问'
        return HttpResponse(message)

    
def login(request):
    if request.session.get('is_login', None):
        return redirect('/index')
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        message = "所有字段都必须填写！"
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request, 'login.html', {"message": message})
    return render(request,'login.html')

def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()#注销
    return redirect("/index/")

def register(request):
    #if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        #return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'register.html', locals())
            else:
                same_name_user = User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'register.html', locals())
                same_email_user = User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = User.objects.create()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request,'register.html',locals())

def addArticle(request):
    if request.method == "POST":
        title = request.POST.get('title', None)
        jianjie = request.POST.get('jianjie', None)
        content = request.POST.get('text', None)
        pic_link = request.POST.get('pic_link', None)
        pic_list = request.POST.get('pic_link', None)
        message = "所有字段都必须填写！"
        if title and content and jianjie:  # 确保用户名和密码都不为空
            if len(title) <=100 and len(jianjie) <=50:
                new_article = Article.objects.create()
                new_article.title = title
                new_article.category= jianjie
                new_article.author = request.session.get('user_name', None)
                new_article.content = content
                new_article.photo = pic_link
                new_article.photo_list = pic_list
                new_article.author_email = User.objects.get(name = new_article.author).email.replace('@qq.com','')
                new_article.save()
                f = open(".\\bloghtml\\{}.html".format(str(new_article.id)) ,'w',encoding='utf-8')
                txt = u"{% extends 'new\showArticle.html' %}\n{% block txt %}\n"
                for i in new_article.content.split('\r\n'):
                    txt+= u'<p>{}</p>'.format(i)
                txt += u'\n{% endblock %}'
                f.write(txt)
                f.close()

                return redirect("/index/")
            else:
                message = "标题或简介太长"
            return render(request, 'add.html', {"message": message})
    return render(request,'add.html')



#解码函数

def getkey(dic,value):
    for k in dic.keys():
        if dic[k] == value:
            return k            
def ma(request):
    if request.method == "POST":
        jiami_ac = request.POST.get('jiami', None)
        normal_str = request.POST.get('normal_str', None)#获取字符
        if jiami_ac:#解码函数
            try:
                jiema_str = ''#解码后
                jiami_zz = ''#中式
                for i in jiami_ac.split():
                    jiami_zz +=chr(int(i))
                for i in jiami_zz.split():    
                    j = basic.get(i)
                    if j:
                        jiema_str += j
                    else:
                        jiema_str += '■'            
                return render(request,'ma.html',{'jiema_str':jiema_str})
            except:
                message = "请输入正确的Z式码！"
                return render(request, 'ma.html', {"message": message})
        if normal_str:#加密函数
            jiami_str = ''
            for i in list(normal_str):
                s = getkey(basic,i)
                if s:
                    jiami_str += ' '+s
                else:
                    jiami_str += ' '+'■'
            jiami_str_ac = ''
            for i in list(jiami_str):
                jiami_str_ac += str(ord(i))+' '
            return render(request, 'ma.html', {"jiami_ac": jiami_str_ac})
    return render(request,'ma.html')
def zuifan(request):
    f=open('static\\web\\fanjv.json',encoding='utf-8')
    js = json.load(f)
    f.close()
    return render(request,'new\zuifan.html',{"js":js['data']['list']})