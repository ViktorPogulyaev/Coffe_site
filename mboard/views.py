from django.http import HttpResponse
from django.shortcuts import render
from .models import BB, Classification
from django.views.generic.edit import CreateView
from .forms import BBForm
from django.urls import reverse_lazy
from django.template import loader

def index(request):
    #template = loader.get_template('mboard\index.html')
    bbs = BB.objects.all()
    classifications = Classification.objects.all()
    context = {'bbs': bbs, 'classifications': classifications}
    #return HttpResponse(template.render(context,request))
    return render(request, 'mboard/index.html', context)


def by_classification(request, classification_id):
    bbs = BB.objects.filter(classification=classification_id)
    classifications = Classification.objects.all()
    current_classification = Classification.objects.get(pk=classification_id)
    context = {'bbs': bbs, 'classifications': classifications, 'current_classification': current_classification}
    return render(request, 'mboard/by_classification.html', context)

class BBCreateView(CreateView):
    template_name = 'mboard/create.html'
    form_class = BBForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classifications'] = Classification.objects.all()
        return context