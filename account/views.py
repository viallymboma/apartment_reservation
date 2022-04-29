from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Client
from reservations.models import Reservation
from rooms.models import Appartment
import json
from django.http import JsonResponse, HttpResponse
import sys
from django.core import serializers

# Create your views here.
def register(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            data = json.loads(request.body)
            raw_firstname = data["firstname"]
            raw_lastname = data["lastname"]
            raw_dob = data["dob"]
            raw_email = data["email"]
            raw_phone = data["phone"]
            raw_address = data["address"]
            raw_city = data["city"]
            # raw_save_reservation_boolean = data["save_reservation_boolean"]
            # print(raw_save_reservation_boolean)

            
            raw_password_1 = data["password_1"]
            raw_password_2 = data["password_2"]
            print(raw_city)
            print(raw_city)
            print(raw_firstname)
            print(raw_lastname)
            print(raw_dob)
            print(raw_email)
            print(raw_phone)
            print(raw_address)
            print(raw_city)
            # username = str(get_random_string(length=10))
            # username = ''.join((string.ascii_letters, string.digits))

            # Process storing the data
            try:
                # making email lower case
                email = raw_email.lower()
                # checking if email is already in the system
                if not User.objects.filter(email=email):

                    # checking if the 2 passwords match
                    if raw_password_1 == raw_password_2:
                        # saving the client in user table
                        user = User(
                            username=email,
                            email=email,
                            password=raw_password_1
                        )
                        # Saving the data
                        user.set_password(user.password)
                        user.save()
                        print("successufl creations of user...")

                        getting_user = User.objects.get(email=email)

                        print("our user: ", getting_user)
                        print("our user again: ", getting_user)

                        message_user_saved = ""
                        user_created = False

                        print("Before saving the client")

                        client = Client(
                            client=getting_user,
                            first_name=raw_firstname,
                            last_name=raw_lastname,
                            email=raw_email,
                            address=raw_address,
                            date_of_birth=raw_dob,
                            city=raw_city,
                            phone=raw_phone,
                        )

                        client.save()
                        print("Before saving the client")

                        user_created = True
                        print("Client created: ", user_created)

                        result = {
                            'status': True,
                            'message': "Registration Done Successfully"
                        }

                        return JsonResponse(result)

                    # check if passwords do not match
                    elif raw_password_1 and raw_password_2 and raw_password_1 != raw_password_2:
                        result = {
                            # 'email_status': False,
                            'status': False,
                            'message': "Les mots de passe ne sont pas identiques"
                        }
                        # return JsonResponse(feedback)

                elif User.objects.filter(email=email):
                    # raise ValidationError("Email already exists")
                    result = {
                        # 'email_status': False,
                        'status': False,
                        'message': "Email exist deja"
                    }
                    # return JsonResponse(feedback)

                # return redirect('registration/success.html')

            except OSError as err:
                print("OS error: {0}".format(err))
                result = {
                    # 'email_status': False,
                    'status': False,
                    'message': "OS error: {0}".format(err),
                }
                return JsonResponse(result)
            except ValueError:
                print("Post is having an invalid value. not saving at all!!!!")
                result = {
                    # 'email_status': False,
                    'status': False,
                    'message': "Post is having an invalid value. not saving at all!!!!",
                }
                return JsonResponse(result)
            except:
                print("Unexpected error:", sys.exc_info()[0])
                result = {
                    # 'email_status': False,
                    'status': False,
                    'message': "Unexpected error:".sys.exc_info()[0],
                }
                raise
                return JsonResponse(result)
            # return JsonResponse(result)
        else:
            variable = "Nothing to show"
            return render(request, 'register.html', {
                'form': variable
            })
    else:
        return render (request, 'register.html')
        # return render(request, 'home.html')

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            # data = request.POST
            data = json.loads(request.body)
            print("The data:", data)

            raw_username = data["email"]
            raw_password = data["password"]
            raw_checker = data["book_new_user"]

            print(raw_username)
            print(raw_password)
            print(raw_checker)

            feedback = {}

            try:
                print("-------------", raw_checker)
                m = User.objects.get(email=raw_username)
                print("_____the mail", m)
                
                if m:
                    print(m)
                    print("^^^^^____^^^^^^", m.id)
                    c = Client.objects.get(client=m.id)
                    print("The C: ", c)
                    # client_name = Client.objects.get(first_name=raw_username)
                    client_name = c.first_name
                    # user_type = c.user_type_client
                    print("client name: ", client_name)
                    # print("user type: ", user_type)

                    if c:
                        print("C's name ", c)
                        user = authenticate(request, username=raw_username, password=raw_password)
                        print("C's name after: ", c)
                        request.session['id'] = m.id
                        request.session['client_session_id'] = c.id
                        request.session['first_name'] = client_name
                        request.session['email'] = m.email
                        # # request.session['user_type'] = user_type
                        # request.session['image'] = c.image.url
                        # print("Image URL:", request.session['image'])
                        print("Client ID:", request.session['client_session_id'])

                        # request.session['user_client'] = c.user_client
                        print("session variable: ", request.session['id'])
                        print("That user: -------- ", user)
                        # print("session variable email: ", request.session['user_client'])

                        if user is not None:
                            print("Now let's log him in...")
                            print("That user: -------- ", user)

                            try:
                                login(request, user)
                                print("He has logged in...")
                                message = "Client is connected."
                                
                                client = "client"
                                feedback = {
                                    'message': message,
                                    'u_type': client,
                                    'status': True,
                                }

                                print("Well logged in++++++++++++")
                                return JsonResponse(feedback)
                            except:
                                message = "Client is not connected."
                                feedback = {
                                    'message': message,
                                    'u_type': client,
                                    'status': False,
                                }
                                print("Not logged in++++++++++++")
                                return JsonResponse(feedback)

                        else:
                            message = "User not in the database."
                            feedback = {
                                'message': message,
                                "status": False
                            }
                            return JsonResponse(feedback)

                    else:
                        message = "Wrong Password."
                        feedback = {
                            'message': "Password is not correct",
                            "status": False
                        }
                        return JsonResponse(feedback)

            except:
                message = "Something went wrong"
                feedback = {
                    'message': message,
                    # 'client': client,
                    "status": False
                }

                print("Not logged in---------")
                return JsonResponse(feedback)
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'home.html')


def client_dashboard (request):
    # client_dashboard.html
    if request.user.is_authenticated:
        the_user_id = request.session['id']

        m = User.objects.get(id=the_user_id)
        print("the user: ", m)
        c = Client.objects.get(client=m.id)
        print("the client: ", c)

        print("the user", the_user_id)
        # all_reservation = Reservation.objects.all()
        # print("All reservations: ", all_reservation)
        user_reservation = Reservation.objects.filter(client=c).latest("id")
        print("The reservation: ", user_reservation)
        # user_reservation_ = Reservation.objects.get(client=c)
        # ap_na = Reservation.objects.filter().only("appartment")
        # ap_na = user_reservation.appartment
        # print("Appart-----------: ", ap_na)
        appart_id = user_reservation.id
        appart_name = user_reservation.appartment
        appart_client = user_reservation.client_name
        appart_date_chk_in = user_reservation.date_Check_In
        appart_date_chk_out = user_reservation.date_Check_Out
        appart_adult = user_reservation.adult
        appart_children = user_reservation.children
        appart_comment = user_reservation.comment
        appart_image = user_reservation.rooms_image

        print("The reservation_appart_name: ", appart_name)
        print("The reservation_appart_client: ", appart_client)
        print("The reservation_ appart_date_chk_in: ", appart_date_chk_in)
        print("The reservation_appart_date_chk_out: ", appart_date_chk_out)
        print("The reservation_appart_adult: ", appart_adult)
        print("The reservation_appart_children: ", appart_children)
        print("The reservation_appart_comment: ", appart_comment)

        # ----------------------------------------------------------------------------
        # ------Getting the object in filter and turning them into somoething that can be used
        # ------In javascript as array 
        # ------Since i use it to get only one row, i make sure to get the last item in the array
        # ------on the javascript side------------------------------------------------------------
        user_reservation_it = Reservation.objects.filter(client=c)
        one_reservation = serializers.serialize(
            'json',
            list(user_reservation_it),
            fields=(
                  "client_name", 
                  "appartment", 
                  "phone", 
                  "date_Check_In", 
                  "date_Check_Out", 
                  "adult", 
                  "children", 
                  "rooms_image", 
                  "comment"
            )
        )
        print("My reservation-------- ", one_reservation)
        print("--------------------------")
        specific_reservation = json.loads(one_reservation)
        print("Refined---_____: ", specific_reservation)
        print("--------------------------")
        # ----------------------------------------------------------------------------
        # ----------------------------------------------------------------------------
        # ----------------------------------------------------------------------------


        the_room = Appartment.objects.filter(name=appart_name)
        the_room_ = Appartment.objects.get(name=appart_name)
        # the_rooms_name = the_room.code
        print("THe code of the room: ", the_room)
        print("THe code of the room code: ", the_room_.code)
        print("Th Status: ", the_room_.availability)


        feedback = {
            "the_room_code": the_room_.code,
            "the_room_image": the_room_.image,
            "the_room_description": the_room_.description,
            "the_room_status": the_room_.availability,
            "the_room_name": appart_name,

            "appart_id": appart_id,
            "appart_client": appart_client,
            "appart_date_chk_in": appart_date_chk_in,
            "appart_date_chk_out": appart_date_chk_out,
            "appart_adult": appart_adult,
            "appart_children": appart_children,
            "appart_comment": appart_comment,

            "my_reservation": specific_reservation
        }

        # console.log(appart_client)
        # console.log(appart_date_chk_in)
        # console.log(appart_date_chk_out)
        # console.log(appart_adult)
        # console.log(appart_children)
        # console.log(appart_comment)


        if request.method == 'POST':
            # the_user_id = request.session['id']
            # print(the_user_id)
            # room_uniq_id = request.POST.get('q', '')
            # print ("Here is the post part")
            feedback = {}
        else:
            return render (request, 'user/client_dashboard.html', feedback)
        # return JsonResponse(feedback)

    elif not request.user.is_authenticated:
        return render(request, 'home.html')


def logout_view(request):
    logout(request)
    # return HttpResponseRedirect('/')



# Admin
def room_management(request):
    return render (request, 'admin/admin_dashboard.html')

def add_rooms(request):
    return render (request, 'admin/add_rooms.html')