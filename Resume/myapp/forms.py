from django import forms
from django.forms import widgets
from .models import Resume

GENDER_CHOICE= [
    ('Male', 'Male'),
    ('Female', 'Female')
]
job_city= [
    ('Delhi', 'Delhi'),
    ('Moradabad', 'Moradabad'),
    ('Gaziyabad', 'Gaziyabad'),
    ('Noida', 'Noida')
]

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICE, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='prepared jobs location', choices= job_city, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields = ['name', 'dob',  'locality', 'city', 'email', 'pin',
        'mobile', 'state','job_city','gender','profile_img', 'my_file'
    ]
        labels= {'name':'Full Name', 'dob':'Date Of Birth', 'pin':'Pin code'}
        widgets= {
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
        'locality':forms.TextInput(attrs={'class':'form-control'}),
        'city':forms.TextInput(attrs={'class':'form-control'}),
        'state':forms.Select(attrs={'class':'form-control'}),
        'pin':forms.NumberInput(attrs={'class':'form-control'}),
        'mobile':forms.NumberInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        }    


        