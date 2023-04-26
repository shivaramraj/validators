from django import forms

def Check_Name(value):
    if value[0].lower()=='a':
        raise forms.ValidationError('not a valid data')
    




class StudentForm(forms.Form):
    name=forms.CharField(max_length=20,validators=[Check_Name])
    age=forms.IntegerField()
    email=forms.EmailField()
    re_enter_email=forms.EmailField()

    def clean(self):
        email=self.cleaned_data['email']
        remail=self.cleaned_data['re_enter_email']
        if email != remail:
            raise forms.ValidationError('not valid')
        return 