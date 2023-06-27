from django.shortcuts import render


def home(request):
    return render(request, "../templates/web/index.html")


def about(request):
    return render(request, "../templates/web/about.html")


def portfolio(request):
    return render(request, "../templates/web/portfolio.html")


def contact(request):
    return render(request, "../templates/web/contact.html")
