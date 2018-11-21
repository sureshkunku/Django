import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')
django.setup()
from testapp.models import *
from faker import Faker
from random import *
faker=Faker()

def populate(n):
    for i in range(n):
        feno=randint(10000,99999)
        fename=faker.name()
        fesal=randint(40000,10000000)
        feaddr=faker.address()
        emp_records=Employee.objects.get_or_create(E_NO=feno,E_NAME=fename,E_SAL=fesal,E_ADDRESS=feaddr)

populate(5)

