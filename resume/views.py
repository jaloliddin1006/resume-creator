
import datetime
from django.views.generic.base import TemplateView 


class IndexView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        context['now'] = datetime.datetime.now()
        return context