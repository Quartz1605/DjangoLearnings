"""
To render html webpages

"""


HTML_STRING = """ <h1>Hello World</h1> """
from django.http import HttpResponse
from articles.models import Article


def home(request):
  """
  Take in a request
  Return HTML as a response(We pick to return the response)

  
  """
  
  
  article_obj = Article.objects.get(id=1)
  article_content = article_obj.content
  article_title = article_obj.title

  Html_string = f"<h1>Title is `{article_title}` and its content is `{article_content}` .</h1>??"

  
  return HttpResponse(Html_string)