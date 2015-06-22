# settting.py

import os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

TEMPLATE_DIRS = (
  os.path.join(PROJECT_ROOT, 'templates'),
  )

# appel du template welcome.html dans le views
from django.shortcuts import render_to_response

def welcome(request):
  return render_to_response('welcome.html')
  
# urls.py
from django.conf.urls import patterns
from views import welcome # !!!!!

urlpatterns = patterns('',
  ('^welcome$',welcome),
  )

# ecrire en XHTML
DEFAULT_CONTENT_TYPE = 'application/xhtml+xml'


# dynamiser le welcome.html

<?xml version="1.0" encoding='UTF-8' ?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title> Trombinoscope </title>
</head>
<body>
<p> Bienvenue. Nous sommes le {{current_date_time}}.</p>
</body>
</html>


 # transmission
 from django.shortcuts import render_to_response
 from datetime import datetime
 
 def welcome(request):
   return render_to_response('welcome.html',{'current_date_time': datetime.now})
