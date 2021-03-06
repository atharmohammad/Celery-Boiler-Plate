from django.shortcuts import render
from task1.forms import ReviewForm
from django.views.generic.edit import FormView
from django.http import HttpResponse
# Create your views here.

class ReviewEmailView(FormView):
    template_name = 'review.html'
    form_class = ReviewForm

    def form_valid(self,form):
        form.send_email()   #this function we defined in the forms 
        msg = 'Thanks For the Review!'
        return HttpResponse(msg)
