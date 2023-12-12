from django import forms
# class studentform(forms.Form):
#     student_ID = forms.IntegerField()
#     student_name = forms.CharField()
#     course = forms.CharField()
#     jdate = forms.DateField()

# creating a form using models
from django.forms import ModelForm
from Hello.models import students

class studentform(ModelForm):
    class Meta:
        model = students
        # fields = 'all' #this will import all fields directly
        fields = ['student_ID','student_name','course','jdate']
        # labels = {'student_ID':'ID','student_name':'Name','course':'Course','jdate':'Joining_Date'} #like this key-value pair can be given
# creating form to add as a student
form = studentform()