from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    #email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'username',
            'id':'username',
            'type':'text',
            'placeholder':'IsraelIsraeli123',
            'maxlength':'16',
            'minlength':'6',
            })
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'first_name',
            'id':'last_name',
            'type':'text',
            'placeholder':'Israel',
            'maxlength':'16',
            'minlength':'6',
            })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'last_name',
            'id':'last_name',
            'type':'text',
            'placeholder':'Israeli',
            'maxlength':'16',
            'minlength':'6',
            })
        #self.fields['email'].widget.attrs.update({
        #    'class': 'form-input',
        #    'required':'',
        #    'name':'email',
        #    'id':'email',
        #    'type':'text',
        #    'placeholder':'IsraelIsraeli@gmail.com',
        #    })
        self.fields['password1'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'password1', 
            'id':'password1', 
            'type':'password', 
            'placeholder':'password', 
            'maxlength':'22',  
            'minlength':'4' 
            }) 
        self.fields['password2'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'password1', 
            'id':'password1', 
            'type':'password', 
            'placeholder':'password', 
            'maxlength':'22',  
            'minlength':'4' 
            }) 
    username = forms.CharField(max_length=20) 
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','password1','password2')



class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields=["first_name","last_name", "email", "phone", "address","city","state","zipcode"]

class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields=["first_name","last_name", "email", "phone", "address","city","state","zipcode"]
    
    #create_at = models.DateTimeField(auto_now_add=True)
    #first_name=  models.CharField(max_length=50)
    #last_name= models.CharField(max_length=50)
    #email = models.CharField(max_length=50)
    #phone = models.CharField(max_length=50)
    #address = models.CharField(max_length=50)
    #city = models.CharField(max_length=50)
    #state = models.CharField(max_length=50)
    #zipcode = models.CharField(max_length=50)
 