from django.views import generic
from django.shortcuts import render

class Preferences(generic.ListView):
    admin = {}
    def get(self, request):
        ctx = self.admin.each_context(request)
        return render(request, 'admin/preferences/preferences.html', ctx)
