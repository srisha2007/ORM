# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![Screenshot 2024-11-16 103753](https://github.com/user-attachments/assets/3f87ec33-73ae-4d36-b437-d8558efbc15f)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

from django.db import models

from django.contrib import admin

class sks (models.Model):
    loan_id=models.IntegerField(primary_key=True)
    loan_type=models.CharField(max_length=100)
    loan_acc=models.FloatField()
    cust_acno=models.IntegerField()
    cust_name=models.CharField(max_length=100)
 
class sksAdmin(admin.ModelAdmin):
    list_display=('loan_id', 'loan_type','loan_acc','cust_acno','cust_name')



## OUTPUT
![Screenshot 2024-11-15 181707](https://github.com/user-attachments/assets/4c39dbeb-9f1c-4c8a-8dee-97c5d5acb726)





## RESULT
Thus the program for creating a database using ORM hass been executed successfully
