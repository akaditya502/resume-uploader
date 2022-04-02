from django.contrib import admin
from .models import Resume

# Register your models here.
admin.site.register(Resume)
list_display = ['id','name','dob','gender','locality',
'city','pin','state','mobile','job_city','profile_image','my_file']



