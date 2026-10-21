Ctrl click to launch VS Code Native REPL (https://aka.ms/python-native-repl)
Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from cms.models import Category, Article
>>> c = Category.objects.create(name="Python")
>>> Article.objects.create(title="Wprowadzenie do Pythona", content="...", category=c)
<Article: Wprowadzenie do Pythona>
>>> Article.objects.create(title="Zaawansowane typy danych", content="...", category=c)
<Article: Zaawansowane typy danych>
>>> for article in c.article_set.all():
...     print(article.title)
... 
Wprowadzenie do Pythona
Zaawansowane typy danych
>>> Article.objects.count()
2
>>> c.delete()                              
(3, {'cms.Article': 2, 'cms.Category': 1})
>>> Article.objects.count()
0
>>> c = Category.objects.create(name="Java")  
>>> Article.objects.create(title="Wprowadzenie do Java", content="...", category=c)   
<Article: Wprowadzenie do Java>
>>> Article.objects.create(title="Zaawansowane typy danych Java", content="...", category=c)
<Article: Zaawansowane typy danych Java>
>>> Article.objects.create(title="Java + AI", content="...", category=c)                    
<Article: Java + AI>
>>> Article.objects.count()                 
3
>>> g = Category.objects.create(name="GO")    
>>> Article.objects.create(title="GO + AI", content="...", category=g)  
<Article: GO + AI>
>>> Article.objects.create(title="Wprowadzenie do GO", content="...", category=g)           
<Article: Wprowadzenie do GO>
>>> Article.objects.count()               
5
>>> for article in c.article_set.all():     
...     print(article.title)
... 
Wprowadzenie do Java
Zaawansowane typy danych Java
Java + AI
>>> for article in g.article_set.all():
...     print(article.title)
... 
GO + AI
Wprowadzenie do GO
>>> c.delete()                         
(4, {'cms.Article': 3, 'cms.Category': 1})
>>> Article.objects.count()            
2
>>> g.delete()
(3, {'cms.Article': 2, 'cms.Category': 1})
>>> Article.objects.count()
0