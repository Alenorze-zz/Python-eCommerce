from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.views.generic import UpdateView
from django.shortcuts import render, redirect

from .forms import MarketingPreferenceForm
from .models import MarketingPreference


class MarketingPreferenceUpdateView(SuccessMessageMixin, UpdateView):
    form_class = MarketingPreferenceForm
    template_name = 'base/forms.html'
    success_url = '/settings/email/'
    success_message = 'Your preferences was updated.'

    def dispatch(self, *args, **kwargs):
        user = self.request.user
        if not user.is_authenticated():
            return redirect("/login/?next=/settings/email")
        return super(MarketingPreferenceUpdateView, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(MarketingPreferenceUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Email Preferences'
        return context

    def get_object(self):
        user = self.request.user
        obj, created = MarketingPreference.objects.get_or_create(user=user)
        return obj 
