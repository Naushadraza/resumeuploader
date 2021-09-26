from django.contrib import admin
from .models import Resume

@admin.register(Resume)
class Resumeupload(admin.ModelAdmin):
    list_display = ['id', 'name', 'dob', 'locality', 'city', 'email', 'pin', 
    'mobile', 'state','job_city','gender','profile_img', 'my_file'
    ]

