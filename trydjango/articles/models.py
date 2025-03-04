from django.db import models


## Installed apps mein app daal dena yaad se.
# Don't forget to run python manage.py makemigrations
# Don't forget to run python manage.py migrate  After creating every model.


# Create your models here.
class Article(models.Model):
  title = models.TextField()
  content = models.TextField()

