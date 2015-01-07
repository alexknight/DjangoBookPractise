#! /usr/bin/env python
#coding=utf-8
#文章分类
import models
def cate():
    categories = models.Category.objects.order_by('name').all()
    return categories
#文章标题
def caption():
    caption = models.Article.objects.order_by('-id').values('id','caption')[:20]
    return caption


