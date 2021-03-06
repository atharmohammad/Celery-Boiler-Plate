from django import forms
from task2.tasks import send_email_review_task
class ReviewForm(forms.Form):
    name = forms.CharField(label='FirstName',max_length=256,min_length=5,widget=forms.TextInput(
        attrs={'class':'form-control mb-3','placeholder':'FirstName','id':'form-FirstName'}
    ))
    email = forms.EmailField(
        max_length=200 , widget=forms.TextInput(
            attrs={'class':'form-control mb-3','placeholder':'Email','id':'form-Email'}
    ))
    review = forms.CharField(
        label="Review", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

    def send_email(self):
        #To send the mail we will give task to celery to do it
        send_email_review_task.delay(
        self.cleaned_data['name'],self.cleaned_data['email'],self.cleaned_data['review'])
        #we use delay to send task to celery
        #Now we have to create a tasks to handle this task
