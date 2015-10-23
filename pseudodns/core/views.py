from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from core import models


def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


def home(request):
    template = 'home.html'
    return render(request, template)


def status(request, name):
    instance = get_object_or_404(models.Mapper, name=name)
    data = {'name': instance.name,
            'ip': instance.ip,
            'poweron': instance.poweron,
            'stamp': instance.stamp}
    return JsonResponse(data)


def poweron(request, name, pwd):
    instance = get_object_or_404(models.Mapper, name=name)
    if instance.checkpwd(pwd):
        ip = get_client_ip(request)
        instance.ip = ip
        instance.poweron = True
        instance.save()
        return redirect('status', name=name)
    else:
        return redirect('unauthorized')


def poweroff(request, name, pwd):
    instance = get_object_or_404(models.Mapper, name=name)
    if instance.checkpwd(pwd):
        instance.poweron = False
        instance.save()
        return redirect('status', name=name)
    else:
        return redirect('unauthorized')


def unauthorized(request):
    template = 'unauthorized.html'
    return render(request, template)


def add(request):
    data = {}
    template = 'add.html'
    if request.method == 'GET':
        data['form'] = models.MapperForm()
    elif request.method == 'POST':
        form = models.MapperForm(request.POST)
        data['form'] = form
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            data['form'] = form
    return render(request, template, data)
