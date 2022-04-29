from django.shortcuts import render
from django.contrib.auth.models import User
from account.models import Client
from .models import Reservation
from rooms.models import Appartment
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json
from django.core import serializers

# Create your views here.
def reservation (request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # data = request.POST
            data = json.loads(request.body)
            print("The data:", data)

            raw_checkin_date = data["checkin_date"]
            raw_checkout_date = data["checkout_date"]
            raw_message = data["message"]
            raw_adults = data["adults"]
            raw_children = data["children"]
            raw_session_id = data["user_id"]
            raw_room = data["room"]
            print("the room: ", raw_room)

            m = User.objects.get(id=raw_session_id)
            print("the user: ", m)

            c = Client.objects.get(client=m.id)
            print("the client: ", c)

            apartment = Appartment.objects.get(id=raw_room)
            print("the apartment", apartment)


            print(raw_checkin_date)
            print(raw_checkout_date)
            print(raw_message)
            print(raw_adults)
            print(raw_children)
            print(raw_room)

            reservation = Reservation(
                client=c,
                appartment=apartment,
                client_name=c.first_name,
                date_Check_In=raw_checkin_date,
                date_Check_Out=raw_checkout_date,
                adult=raw_adults,
                children=raw_children,
                rooms_image=apartment.image,
                comment=raw_message,
            )

            reservation.save ()

            choosen_apart = Appartment.objects.filter(id=raw_room)
            choosen_apart.update(availability=False)

            # feedback = {}

            feedback = {
                'status': True,
                'checkin_date': raw_checkin_date,
                'checkout_date': raw_checkout_date,
                'message_': raw_message,
                'adults': raw_adults,
                'children': raw_children,
                'room': raw_room,
                'message': "Reservation Done Successfully"
            }

            return JsonResponse(feedback)
        else:
            return render(request, 'reservation.html')
    else:
        message = "You are not registered. Kindly register to book an Apartment"
        feedback = {
            'message_not_login': message
        }
        # return render(request, 'home.html')
        return render(request, "reservation.html", feedback) 





def exit_apartment (request):
    if request.method == "GET":
        reservation_uniq_id = request.GET.get('q', '')
        print(reservation_uniq_id)
        print ("Here is the get part")

        if reservation_uniq_id != '':
            the_reservation = Reservation.objects.filter(id=reservation_uniq_id)
            get_the_reservation = Reservation.objects.get(id=reservation_uniq_id)
            print("The reservation: ", the_reservation)
            print("The apparment: ", get_the_reservation.appartment)

            choosen_apart = Appartment.objects.filter(name=get_the_reservation.appartment)
            choosen_apart.update(availability=True)

            

            the_reservation_ = serializers.serialize(
                'json',
                list(the_reservation),
                fields=(
                    "client", 
                    "appartment", 
                    "client_name", 
                    "date_Check_In", 
                    "date_Check_Out", 
                    "adult", 
                    "children",
                    "comment"
                )
            )

            print("The serialized reservation", the_reservation_)

            feedback = {
                'the_room': the_reservation_,
                'exit': True,
                'choosen_apart': choosen_apart
            }

            return render(request, 'user/client_dashboard.html', feedback)

            # return JsonResponse(feedback)
        feedback = {
            'the_room': reservation_uniq_id,
        }

        return JsonResponse(feedback)
    else:
        return render(request, 'home.html')
    













