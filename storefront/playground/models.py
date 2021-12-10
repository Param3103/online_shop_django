from django.db import models
import datetime, os

def filepath(request, filename):
    old_filename = filename
    timeNow  = datetime.datetime.now()
    fileName = "%s%s", (timeNow, old_filename)
    return os.path.join("uploads/", filename)
# Create your models here.
class user(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=2700)
    age = models.TextField(max_length=2700)

