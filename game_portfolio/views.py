from django.shortcuts import render


def home_principal(request):
    return render(request, 'algum_template.html')
