from django.shortcuts import render





def home(request):

    return render(request, "pages/home.html")





def about(request):

    return render(request, "pages/about.html")





def services(request):

    return render(request, "pages/services.html")





def portfolio(request):

    return render(request, "pages/portfolio.html")





def contact(request):

    return render(request, "pages/contact.html")

