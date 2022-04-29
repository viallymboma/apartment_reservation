from django.shortcuts import render
from rooms.models import Appartment
from django.http import JsonResponse, HttpResponse
import json
from django.core import serializers

# Create your views here.

def allRooms (request):

   rooms = Appartment.objects.all()

   context = {
      'rooms': rooms
   }

   return render(request, 'rooms.html', context)

def get_all_rooms (request):
   if request.method == "GET":
        get_all_appartments = Appartment.objects.all()

        all_appartments = serializers.serialize(
            'json',
            list(get_all_appartments),
            fields=(
                "name", 
                "code", 
                "price", 
                "description", 
                "image", 
                "availability", 
            )
        )

        # print(all_appartments)
        specific_time_arr = json.loads(all_appartments)
        # print(specific_time)
        array_of_all_appartments = []

        for x in specific_time_arr:
            print(x)
            # array_of_all_appartments.append(x['fields']['name'])
            array_of_all_appartments.append(x)

        print(array_of_all_appartments)

        feedback = {
            'all_appartments': array_of_all_appartments,
        }

        return JsonResponse(feedback, safe=False)


def get_a_room (request):
   if request.method == "GET":
      get_all_appartments = Appartment.objects.all()
      room_uniq_id = request.GET.get('q', '')
      print(room_uniq_id)

      if room_uniq_id != '':
         the_room = get_all_appartments.filter(id=room_uniq_id)
         # a_room = Appartment.objects.get(id=room_uniq_id)
         print("-----------------------------------------------", the_room)
         # print(a_room.name)

         all_appartments = serializers.serialize(
            'json',
            list(the_room),
            fields=(
                  "name", 
                  "code", 
                  "price", 
                  "description", 
                  "image", 
                  "availability", 
            )
         )

         # print(all_appartments)
         specific_time_arr = json.loads(all_appartments)
         # print(specific_time)
         array_of_all_appartments = []
         image_link = []

         for x in specific_time_arr:
            print(x)
            # array_of_all_appartments.append(x['fields']['name'])
            array_of_all_appartments.append(x)
            image_link.append(x['fields']['image'])

         print(array_of_all_appartments)
         image_str = "".join(image_link)
         print(image_link)
         print(image_str)

         feedback = {
            'all_appartments': array_of_all_appartments,
            'the_room': the_room, 
            'image': image_str
         }

      # return JsonResponse(feedback, safe=False)
      return render(request, "reservation.html", feedback)













