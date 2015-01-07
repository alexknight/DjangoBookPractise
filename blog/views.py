from django.shortcuts import render
from django.template import loader,Context,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
import time
import datetime
from django.db.models import Q
from django.db import connection
import Common,os
import models
from simblog.forms import CommentForm

def r_sidebar(request):
	categorys=models.Category.objects.order_by('-id')
	articles=models.Article.objects.all()

	for category in categorys:
		category.article_num=0
		for article in articles:
			if article.category==category:
				category.article_num+=1
		category.save()
	return categorys

def default(request):
	categorys=r_sidebar(request):
	articles=models.Article.objects.order_by('-id')[0:6]
	return render_to_response('index.html',locals())
	