"""
To render html webpages

"""
HTML_STRING = """ <h1>Hello World</h1> """
from django.http import HttpResponse


def home(request):
  """
  Take in a request
  Return HTML as a response(We pick to return the response)

  
  """
  
  
  return HttpResponse(HTML_STRING)