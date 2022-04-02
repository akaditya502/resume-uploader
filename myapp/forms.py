from django import forms
from django.forms import fields
from .models import Resume
genderchoices = [
    ('Male','Male'),('Female','Female')
]
jobcitychoices = [('Delhi','Delhi'),
                    ('Noida','Noida'),
                    ('Mumbai','Mumbai'),
                    ('Dhanbad','Dhanbad'),
                    ('Banglore','Banglore')
]


class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=genderchoices,widget= forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Prefer job locations',choices=jobcitychoices,widget=forms.CheckboxSelectMultiple)
    class Meta:  
        model = Resume
        fields = ['name','dob','gender','locality','city','pin',
        'state','mobile','email','job_city','profile_image','my_file']
        labels = {'name':'Full Name','dob':'Date of birth','pin':'pin Code',
        'mobile':'mobile No','email':'Email Id','profile_image':'profile Image','my_file':'Document'}
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
             

        }        
