from django.core.context_processors import csrf
from django.core import serializers
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from converter.forms import *



def home(request):
    # default = {
    #     'list': seen_models,
    # }
    # form = DropDownList(default)
    
    # if request.method == "POST":
    #     form = DropDownList(request.POST)
    #     if form.is_valid():
    #         chosen = form.cleaned_data.get['list']
    #         context = RequestContext(request,{
    #             'chosen': chosen,
    #         })
    #         return render_to_response('result.html', context)

    # print dir(request.GET)

    items = request.GET.items

    # data = Student.objects.all() 

    model = eval(request.GET.get("model"))

    data = serializers.serialize("json", model.objects.all())
    print data
    return HttpResponse(data)
    # form = DropDownList()
    # context = RequestContext(request, {
    #     'form': form,
    # })
    # return render_to_response('main.html', context)