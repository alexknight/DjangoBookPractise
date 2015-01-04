#-*-coding=utf-8 -*-
from django.http import HttpResponse,Http404
from django.template import Template,Context
from django.shortcuts import render_to_response
from blog.models import Book
import datetime

def hello(request):
	return HttpResponse("hello world")

def current_datetime(request):
	now=datetime.datetime.now()
	t="<html><body>It is now {{current_date}}.</body></html>"
	html=t.render(Context({'current_date':now}))
	return HttpResponse(html)

def hours_ahead(request,offset):
	try:
		offset=int(offset)
	except ValueError:
		raise Http404
	dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
	html="<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)

def ua_display(request):
	values=request.META.items()
	values.sort()
	html=[]
	for k,v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>'%(k,v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search(request):
	#红色字体默认隐藏
	errors=[]
	#判断是否为get请求
	if "q" in request.GET:
		query_book=request.GET['q']
		#如果为空，error=true，红色字体显示
		if not query_book:
			errors.append('Enter a search term.')
		elif len(query_book) > 5:
			errors.append('Please enter at most 5 characters.')
		else:
			books=Book.objects.filter(title__icontains=query_book)
			return render_to_response('search_results.html',{'query':query_book,'books':books})
	return render_to_response('search_form.html',{'errors':errors})






























def search(request):
	error= False
	if "q" in request.GET:
		query_book=request.GET['q']
		if not query_book:
			error=True
		else:
			books=Book.objects.filter(title__icontains=query_book)
			return render_to_response('search_results.html',{'query':query_book,'books':books})
	return render_to_response('search_form.html',{'error':error})























