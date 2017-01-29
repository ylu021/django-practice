from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Question(models.Model):
	question_text = models.CharField(max_length=200) #like sql setting vartype
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1) #example
class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE) #similar to sql
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
                return self.choice_text #print out what is inside the object


