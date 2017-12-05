# coding: utf-8

from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.http import HttpResponseRedirect


from catalog.models import Products
from .forms import ContactForm

class IndexView(TemplateView):

    template_name = "index.html"

    
class ContactView(FormView):

    template_name = "contact_section.html"
    form_class = ContactForm
    success_url = '/sucesso/'

    # opção 1
    def form_valid(self, form):
        super(ContactView, self).form_valid(form)
        # If the form is valid, redirect to the supplied URL.
        form.send_mail()
        return HttpResponseRedirect(self.get_success_url())

    # opção 2
    """ 
    def post(self, request, *args, **kwargs):
    super(ContactView, self).post(request, *args, **kwargs)
    
    form = self.get_form()
    if form.is_valid():
        form.send_mail()
        return self.form_valid(form)
    else:
        return self.form_invalid(form)
    """


class ContactSuccessView(TemplateView):

    template_name = "contact_success.html"

index = IndexView.as_view()
contact = ContactView.as_view()
success = ContactSuccessView.as_view()



"""
def home(request):
    template = 'highLight_products.html'
    return render(request, template)

def contact(request):
    template = 'contact_section.html'
    return render(request, template)

"""