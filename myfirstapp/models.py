#from typing_extensions import Required
from django.db import models
from django.db.models.fields import CharField

# Create your models here.



class complaint(models.Model):
	name=models.CharField(max_length=30)
	phone_no=models.CharField(max_length=30, null=True)
	types=models.CharField(max_length=50)
	desc=models.CharField(max_length=10)
	area=models.CharField(max_length=10)


class complaint_register(models.Model):
	name=models.CharField(max_length=50)
	phone_no=models.CharField(max_length=15)
	complaint_category=models.CharField(max_length=50)
	complaint_description=models.CharField(max_length=10)
	area_of_complaint=models.CharField(max_length=10)
	date_of_complaint=models.DateField(auto_now_add=True)
	acknowledgement_of_complaint=models.CharField(max_length=20,default='Not Applicable')
	complaint_status=models.CharField(max_length=20,default='Not Applicable')
	steps_taken=models.CharField(max_length=3000,default='Not Applicable')
	date_of_update=models.CharField(max_length=20,default='Not Applicable')


class super_user_details(models.Model):
	emp_id=models.CharField(max_length=20)
	super_user_name=models.CharField(max_length=50)
	passcode=models.CharField(max_length=20)
	position=models.CharField(max_length=50)
	department=models.CharField(max_length=20)


