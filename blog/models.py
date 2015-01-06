#-*-coding=utf-8-*-
from django.db import models
import time
from DjangoUeditor.models import UEditorField

class Category(models.Model):
	name=models.CharField(max_length=100)
	article_num=models.IntegerField(default=0)

	def __unicode__(self):
		return u'%s' %self.name

class Article(models.Model):
	category=models.ForeignKey(Category)
	caption=models.CharField('标题',max_length=200)
	shortcontent=models.TextField(max_length=500)
	content=UEditorField('content')
	createtime=models.DateTimeField(auto_now_add=True)
	hits=models.IntegerField(default=0)
	times=models.TimeField(default=0)
	goods=models.IntegerField(default=0)
	bads=models.IntegerField(default=0)
	def __unicode__(self):
		return u'%s' %self.caption

class Comment(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField()
	content=models.TextField()
	createtime=models.DateTimeField(auto_now_add=True)
	article=models.ForeignKey(Article)
	def __unicode__(self):
		return u'%s' %self.article