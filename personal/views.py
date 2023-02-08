from django.shortcuts import render

def index(request):
    return render(request, "index.html")


def hobbies(request):
    return render(request, "hobbies.html")

def contact_me(request):
    return render(request, "contact_me.html")