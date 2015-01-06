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


def default(request):
	categorys=r_sidebar(request):