from django.db import models


class question(models.Model):
	question_content = models.TextField(max_length=1000)
	question_number = models.IntegerField()
	created_date = models.DateField()
