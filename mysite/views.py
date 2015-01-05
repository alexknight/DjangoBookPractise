#-*-coding=utf-8 -*-
from django.http import HttpResponse,Http404
from django.template import Template,Context
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
# from django.views.decorators.csrf import csrf_exempt
from mysite.forms import ContactForm
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
	errors=[]
	if "q" in request.GET:
		query_book=request.GET['q']
		if not query_book:
			errors.append('Enter a search term.')
		elif len(query_book) > 5:
			errors.append('Please enter at most 5 characters.')
		else:
			books=Book.objects.filter(title__icontains=query_book)
			return render_to_response('search_results.html',{'query':query_book,'books':books})
	return render_to_response('search_form.html',{'errors':errors})

# @csrf_exempt
# def contact(request):
# 	errors=[]
# 	if request.method=="POST":
# 		if not request.POST.get('subject',''):
# 			errors.append('Enter a subject.')
# 		if not request.POST.get('message',''):
# 			errors.append('Enter a message.')
# 		if request.POST.get('email') and '@' not in request.POST['email']:
# 			errors.append('Enter a valid e-mail address.')
# 		if not errors:
# 			send_mail(
# 				request.POST['subject'],
# 				request.POST['message'],
# 				request.POST.get('email','qqliao_shu_feng@163.com'),
# 				['619692290@qq.com'],
# 				)
# 			return HttpResponseRedirect('/contact/thanks/')
# 	return render_to_response('contact_form.html',
# 		{
# 		'errors':errors,
# 		'subject':request.POST.get('subject',''),
# 		'message':request.POST.get('message',''),
# 		'email':request.POST.get('email', ''),
# 		})

def contact(request):
	if request.method=='POST':
		form=ContactForm(request.POST)
		if forms.is_valid():
			cd=form.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email','qqliao_shu_feng@163.com'),
				['619692290@qq.com'],
				)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form=ContactForm(initial={'subject':'I love your site!','message':'hello','email':'619692290@qq.com'})
	return render_to_response('contact_form.html',{'form':form})






















































