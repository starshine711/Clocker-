from .models import User,RegisterForm,Article,Comment
id = input('>>>')
article = Article.objects.get(id=id)
print(article.content)
input(....ok)