# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#
class Main_table(models.Model):
    task_id = models.IntegerField(default=0)
    input_gene = models.TextField()
    input_phenotype = models.TextField()
    result = models.TextField()
    interpretation = models.TextField(default='')
    interpretation_chinese = models.TextField(default='')
    pub_date = models.DateTimeField()
    user_name = models.CharField(max_length=10)
    task_name = models.CharField(max_length=20)

class Raw_input_table(models.Model):
    raw_input_gene = models.TextField()
    raw_input_phenotype = models.TextField()
    user_name = models.CharField(max_length=10, default='')
    task_name = models.CharField(max_length=20, default='')
    pub_date = models.DateTimeField()
    status = models.CharField(max_length=50, default='')
    process_time = models.DecimalField(max_digits=3, decimal_places=1, default=0)