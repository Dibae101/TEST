from django.db import models

# Create your models here.


class Dept_list(models.Model):
	name = models.CharField(max_length=50)
	img = models.ImageField(upload_to='static/img/dept1')
	TYPES = (
        ('education', 'education'),
        ('transportation', 'transportation'),
        ('health', 'health'),
        ('security', 'security'),
        ('online_form', 'online_form'),
        ('online_verify', 'online_verify'),
    )
	category = models.CharField(max_length=30, choices=TYPES,default="")


	def __str__(self):
		return self.name