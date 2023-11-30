from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

def home(req:HttpRequest):
    if req.method == "GET":
        print(req.user)
        print("hello")
    elif req.method == "POST":
        ...
    return render(req, "index.html", {"user": req.user})

def company_profile(req: HttpRequest):
    return render(req, "company_profile.html")


def sitemap(req):
    return render(req, "sitemap.html")

def get_hired(req: HttpRequest):
    return render(req, "hire_form.html")

def register_company(req: HttpRequest):
    return render(req, "register_company.html")
    ...