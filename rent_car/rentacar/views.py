from django.shortcuts import render
from .models import *
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from datetime import datetime, date
from django.views.decorators.csrf import csrf_exempt
from rentacar.forms import OrderForm
from django.utils.dateparse import parse_datetime
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .forms import ContactForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# def index(request):
#     car = Car.objects.all()
#     return render(request, 'main/base.html', {'cars': cars})


def message(request):
    # if request.method == 'POST':
    #     message = request.POST['message']
    #
    #     send_mail('Contact Form',
    #         message,
    #         settings.EMAIL_HOST_USER,
    #         ['tsybinivan94@gmail.com'],
    #         fail_silently=False)
    return render(request, 'main/message.html')


def sendanemail(request):
    if request.method == 'POST':
        to = request.POST.get('toemail')
        content = request.POST.get('content')
        # print(to, content)
        send_mail('New order',
                  content,
                  settings.EMAIL_HOST_USER,
                  [to],
                  )
        return render(request, 'main/email.html', {'title': 'send an email'})
    else:
        return render(request, 'main/email.html', {'title': 'send an email'})


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def cars(request):
    top_cars = Car.objects.all()
    return render(request, 'main/cars.html', context={'top_cars': top_cars})


def reviews(request):
    return render(request, 'main/reviews.html')


def accept(request):
    return render(request, 'main/accept.html')


def makeOrder(request, pk):
    car = Car.objects.get(id=pk)
    start_date = request.POST['start_date']
    end_date = request.POST['end_date']

    format = "%d/%m/%Y"

    if request.method == 'POST' and end_date > start_date:
        start_date = datetime.strftime(start_date, format)
        end_date = datetime.strftime(end_date, format)
        daysTotal = end_date - start_date
        days = int(daysTotal.days)
        priceCar = Car.price()
        Price = priceCar * days
        totalPrice = int(Price, str="$")

    context = {
        'car': car,
        'start date': start_date,
        'end date': end_date,
        'total price': totalPrice,
    }

    return render(request, 'accept.html', context)


def new_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        print(request.POST)
        if form.is_valid():
            car = get_object_or_404(Car, id=request.POST['car'])
            start_date = parse_datetime(request.POST['start_date'])
            end_date = parse_datetime(request.POST['end_date'])
            total_days = end_date - start_date
            order = form.save(commit=False)
            max_order = Order.objects.values_list('number', flat=True).order_by("-number").first()
            order.number = (max_order or 0) + 1
            order.price = car.price * total_days.days
            order.save()

            return redirect('accept')
    else:
        form = OrderForm()

    return render(request, 'main/message.html', context={'form': form})
