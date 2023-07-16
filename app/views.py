from django.shortcuts import render, HttpResponse
def index(request):
    con={
        'var':"69",
        'kar':"Wanna",
        "mark":"?"
    }
    return render(request,'index.html',con)
def about(request):
    return render(request,'about.html')
def contact(request):
    # return HttpResponse("This is the Fucking Contact Page")
    return render(request,'templates.html')

