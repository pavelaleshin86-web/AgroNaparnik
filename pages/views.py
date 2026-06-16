from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import ContactForm


def home(request):
    return render(request, "pages/home.html")


def about(request):
    return render(request, "pages/about.html")


def services(request):
    return render(request, "pages/services.html")


def portfolio(request):
    return render(request, "pages/portfolio.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()

            send_mail(
                subject=f"Новая заявка от {contact_message.name}",
                message=(
                    f"Имя: {contact_message.name}\n"
                    f"Email: {contact_message.email}\n\n"
                    f"{contact_message.message}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_NOTIFY_EMAIL],
                fail_silently=True,
            )

            messages.success(request, "Спасибо! Сообщение отправлено.")
            return redirect("contact")
    else:
        form = ContactForm()

    return render(request, "pages/contact.html", {"form": form})
