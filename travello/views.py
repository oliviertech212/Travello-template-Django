from django.shortcuts import render
from .models import Destination
# Create your views here.


def index(request):
    # dest4=Destination()
    # dest4.name='Mumbai'
    # dest4.desc='Beautiful city'
    # dest4.img='destination_3.jpg'
    # dest4.price=400


    # dest1=Destination()
    # dest1.name='Kigali'
    # dest1.desc='fast moving city that never sleeps'
    # dest1.img='destination_1.jpg'
    # dest1.price=400
    # dest1.offer= True

    # dest2 = Destination()
    # dest2.name = 'Hyderabad'
    # dest2.desc = 'First Biryani, Then Sherwani'
    # dest2.img = 'destination_2.jpg'
    # dest2.price = 650
    # dest2.offer= False

    # dest3 = Destination()
    # dest3.name = 'Bengaluru'
    # dest3.desc = 'Beautiful City'
    # dest3.img = 'destination_3.jpg'
    # dest3.price = 750
    # dest3.offer= True

    # dests = [dest1, dest2, dest3]

    dests=Destination.objects.all()
    for dest in dests:
       print(dest.imag)
    return render(request,'index.html',{'dests':dests});