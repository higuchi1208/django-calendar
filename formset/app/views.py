from django.shortcuts import render
from .models import TestModel
from django import forms
from django.http import HttpResponse

# Create your views here.

def make_test_modelformset(request):
    TestModelFormSet = forms.modelformset_factory(
      model = TestModel,
      fields  =('text',),
      extra=3,
    )
    if request.method == 'POST':
        formset = TestModelFormSet(request.POST,queryset=TestModel.objects.none())
        if formset.is_valid():
            formset.save()

            data = [x.text for x in TestModel.objects.all()]
            return HttpResponse(repr(data))
    else:
        formset = TestModelFormSet(queryset=TestModel.objects.none())
    return render(request, 'app/form1.html', {'formset': formset})