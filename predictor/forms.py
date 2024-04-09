from django import forms
from .models import HeartData


class Parameters(forms.Form):
    age = forms.IntegerField(max_value=120,min_value=1 , widget=forms.NumberInput(attrs={'id':'a1' , 'type':'text','class':'validate'}) , error_messages={'invalid':'Please enter a number'})
    sex= forms.IntegerField(max_value=1,min_value=0,widget=forms.NumberInput(attrs={'id':'a2' , 'type':'text','class':'validate'}))
    cp = forms.IntegerField(max_value=3,min_value=0 ,widget=forms.NumberInput(attrs={'id':'a3' , 'type':'text','class':'validate'}))
    trestbps = forms.IntegerField(max_value=160,min_value=80 ,widget=forms.NumberInput(attrs={'id':'a4' , 'type':'text','class':'validate'}))
    chol = forms.IntegerField(max_value=600,min_value=0 ,widget=forms.NumberInput(attrs={'id':'a5' , 'type':'text','class':'validate'}))
    fbs = forms.IntegerField(max_value=1,min_value=0,widget=forms.NumberInput(attrs={'id':'a6' , 'type':'text','class':'validate'}))
    restcg = forms.IntegerField(max_value=2,min_value=0,widget=forms.NumberInput(attrs={'id':'a7' , 'type':'text','class':'validate'}))
    thalach = forms.IntegerField(max_value=200,min_value=0 ,widget=forms.NumberInput(attrs={'id':'a8' , 'type':'text','class':'validate'}))
    exang = forms.IntegerField(max_value=1,min_value=0 ,widget=forms.NumberInput(attrs={'id':'a9' , 'type':'text','class':'validate'}))
    oldpeak = forms.FloatField(max_value=6,min_value=0 ,widget=forms.NumberInput(attrs={'id':'a10' , 'type':'text','class':'validate'}))
    slope = forms.IntegerField(max_value=2,min_value=0 ,widget=forms.NumberInput(attrs={'id':'a11' , 'type':'text','class':'validate'}))
    ca = forms.IntegerField(max_value=4,min_value=0 ,widget=forms.NumberInput(attrs={'id':'a12' , 'type':'text','class':'validate'}))
    thal= forms.IntegerField(max_value=3,min_value=0 ,widget=forms.NumberInput(attrs={'id':'a13' , 'type':'text','class':'validate'}))
    
