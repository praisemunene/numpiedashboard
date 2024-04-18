from datetime import datetime# import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse
from .models import Users, UploadedCSV, getsenderid
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import check_password
from django.contrib.sessions.models import Session
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.utils import timezone
import csv
import pandas as pd
import json
from . import settings
import os
from django.core.files.base import ContentFile


def index(request):
    if 'email' not in request.session:
        return redirect('login')
    user = Users.objects.get(email=request.session['email'])
    
    # Pass user object in context
    context = {'user': user}
    return render(request, 'index.html', context)

def error(request):
    if 'email' not in request.session:
        return redirect('login')
    user = Users.objects.get(email=request.session['email'])
    
    # Pass user object in context
    context = {'user': user}
    return render(request, '404.html', context)

def changepassword(request):
    if 'email' not in request.session:
        return redirect('login')
    user = Users.objects.get(email=request.session['email'])
    
    # Pass user object in context
    context = {'user': user}
    return render(request, 'changepassword.html', context)

def creategroup(request):
    if 'email' not in request.session:
        return redirect('login')
    user = Users.objects.get(email=request.session['email'])
    
    # Pass user object in context
    context = {'user': user}
    return render(request, 'creategroup.html', context)

def failapi(request):
    if 'email' not in request.session:
        return redirect('login')
    user = Users.objects.get(email=request.session['email'])
    
    # Pass user object in context
    context = {'user': user}
    return render(request, 'failapi.html', context)

def forgotpassword(request):
    return render(request, 'forgot-password.html')


def changemypassword(request):
    if request.method == 'POST':
        old_password = request.POST.get('oldpassword')
        new_password = request.POST.get('newpassword')
        
        # Retrieve the user object based on the session email
        try:
            user = Users.objects.get(email=request.session['email'])
        except Users.DoesNotExist:
            return HttpResponse("User not found", status=404)
        
        # Check if the old password matches
        if check_password(old_password, user.password):
            # Hash the new password
            hashed_new_password = make_password(new_password)
            
            # Update the user's password in the database
            user.password = hashed_new_password
            user.save()
            return HttpResponse("Password change request received successfully!")
        else:
            # Return an error response if old password doesn't match
            return HttpResponse("Old password is incorrect", status=400)

    # Handle GET requests or other cases
    return HttpResponse("This endpoint only accepts POST requests.")

def managegroup(request):
    if 'email' not in request.session:
        return redirect('login')
    user = Users.objects.get(email=request.session['email'])
    uploaded_csv_data = UploadedCSV.objects.filter(useremail=user.email)

    # Pass user object and uploaded_csv_data in context
    print(uploaded_csv_data)
    context = {
        'user': user,
        'csvdata': uploaded_csv_data,
    }
    return render(request, 'managegroup.html', context)

def misreport(request):
    if 'email' not in request.session:
        return redirect('login')
    user = Users.objects.get(email=request.session['email'])
    
    # Pass user object in context
    context = {'user': user}
    return render(request, 'misreport.html', context)

def pay(request):
    if 'email' not in request.session:
        return redirect('login')
    user = Users.objects.get(email=request.session['email'])
    
    # Pass user object in context
    context = {'user': user}
    return render(request, 'pay.html', context)

def register(request):
    return render(request, 'register.html')

def senderid(request):
    if 'email' not in request.session:
        return redirect('login')
    user = Users.objects.get(email=request.session['email'])
    
    # Pass user object in context
    context = {'user': user}
    return render(request, 'senderid.html', context)

def sendsms(request):
    if 'email' not in request.session:
        return redirect('login')
    user = Users.objects.get(email=request.session['email'])
    
    # Pass user object in context
    context = {'user': user}
    return render(request, 'sendsms.html', context)

def smspersonalised(request):
    if 'email' not in request.session:
        return redirect('login')
    user = Users.objects.get(email=request.session['email'])
    
    # Pass user object in context
    context = {'user': user}
    return render(request, 'smspersonalized.html',context)

def smsstatus(request):
    if 'email' not in request.session:
        return redirect('login')
    user = Users.objects.get(email=request.session['email'])
    
    # Pass user object in context
    context = {'user': user}
    return render(request, 'smsstatus.html', context)

def templates(request):
    if 'email' not in request.session:
        return redirect('login')
    user = Users.objects.get(email=request.session['email'])
    
    # Pass user object in context
    context = {'user': user}
    return render(request, 'templates.html', context)

def ussd(request):
    if 'email' not in request.session:
        return redirect('login')
    user = Users.objects.get(email=request.session['email'])
    context = {'user': user}
    return render(request, 'ussd.html', context)
    

def invoice(request):
    if 'email' not in request.session:
        return redirect('login')
    user = Users.objects.get(email=request.session['email'])
    # Pass user object in context
    row_id = request.GET.get('id')
    try:
        # Retrieve the row with the given ID
        row = getsenderid.objects.get(id=row_id)
        # Serialize the row data
        row_data = {
            'id': row.id,
            'useremail': row.useremail,
            'senderid': row.senderid,
            'smstype': row.smstype,
            'serviceprovider': row.serviceprovider,
            'requestedon': row.requestedon,
            'approvedon': row.approvedon,
            'status': row.status
        }
        # Return the row data as JSON response
        context = {'user': user, 'row': row_data}
        return render(request, 'invoice.html', context)
    except getsenderid.DoesNotExist:
        # If row with given ID does not exist, return an error response
        return redirect('senderid')
    # Print the row id in the terminal

    


def logout(request):
    # Clear the user's session
    request.session.flush()
    # Redirect the user to the login page
    return redirect('login')

def login(request):
    return render(request, 'login.html')
# views.py


def registration(request):
    if request.method == 'POST':
        # This is an AJAX request
        query_dict = request.POST
        # Process the form data here
        
        # For example, print the form data
        first_name = query_dict.get('firstname')
        last_name = query_dict.get('lastname')
        email = query_dict.get('email')
        password = query_dict.get('password')

        hashed_password = make_password(password)
        existing_user = Users.objects.filter(email=email).exists()

        if existing_user:
            # User already exists, return a JSON response with an error message
            return JsonResponse({'message': 'User with this email already exists'}, status=400)
        # Create a new user instance
        else:
            new_user = Users(firstname=first_name, lastname=last_name, email=email, password=hashed_password)
            
            # Save the user to the database
            new_user.save()
            # Return a JSON response indicating success
            return JsonResponse({'message': 'Registration successful'}, status=200)
    else:
        # Handle non-AJAX requests here
        return JsonResponse({'message': 'Invalid request'}, status=400)



def loginform(request):
    if request.method == 'POST':
        # Get form data
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Find user by email
        user = Users.objects.filter(email=email).first()
        

        if user:
        # Check password
            if check_password(password, user.password):
                # Passwords match, login successful
                request.session['email'] = user.email
                # Return success response
                return JsonResponse({'success': True, 'message': 'Login successful'})
            else:
                # Passwords don't match, login failed
                return JsonResponse({'success': False, 'message': 'Invalid credentials'})
        else:
            return JsonResponse({'success': False, 'message': 'user doesnt exist'})
            
    else:
        # Redirect to login page if not a POST request
        return redirect('login')
    

def uploadcsv(request):
    if request.method == 'POST':
        try:
            for uploaded_file in request.FILES.getlist('csv_upload'):
                file_name = default_storage.save(uploaded_file.name, ContentFile(uploaded_file.read()))
                filename = uploaded_file.name
                user_email = request.session.get('email')
                custom_filename = request.POST.get('groupname')
                print(filename)
                print(custom_filename)
                

                with uploaded_file.open() as csv_file:
                    # Initialize the line count
                    mobile_count = 0
                    # Iterate over each line in the file
                    for line in csv_file:
                        # Increment the line count for each line
                        mobile_count += 1
                print(mobile_count)
                uploaded_csv = UploadedCSV.objects.create(
                    useremail=user_email,
                    filename=filename,
                    customfilename=custom_filename,
                    createdat=timezone.now(),
                    mobilecount=mobile_count - 1
                )
            return JsonResponse({'message': 'CSV file(s) uploaded successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'No files uploaded'}, status=400)


def getuserdata(request):
    try:
        # Assuming you have a 'email' field in your session
        user_email = request.session['email']
        # Retrieve the user object based on the email
        user = Users.objects.get(email=user_email)
        # Serialize user data to JSON format
        user_data = {
            'id': user.id,
            'username': user.firstname + " " + user.lastname,
            'firstname': user.firstname,
            'lastname': user.lastname,
            'email': user.email,
            # Add more fields as needed
        }
        # Return user data as JSON response
        return JsonResponse({'user': user_data}, status=200)
    except Users.DoesNotExist:
        # Handle case where user does not exist
        return JsonResponse({'error': 'User not found'}, status=404)
    except KeyError:
        # Handle case where 'email' key is not present in session
        return JsonResponse({'error': 'Email not found in session'}, status=400)



from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from .models import getsenderid

def applysenderid(request):
    if request.method == 'POST':
        # Extract form data
        user_email = request.session['email']
        senderid = request.POST.get('senderid')
        smstype = request.POST.get('messagetype')
        serviceprovider = request.POST.get('provider')
        requested_on = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Save files using default_storage
        applicationletter_file = request.FILES.get('applicationletter')
        cr12_file = request.FILES.get('compcr12')
        cr13_file = request.FILES.get('bizcr13')
        certincorp_file = request.FILES.get('compincorp')
        bussinesscert_file = request.FILES.get('bizcert')


        # Create the 'senderid' folder if it doesn't exist
        senderid_folder = os.path.join(settings.MEDIA_ROOT, 'senderid')
        os.makedirs(senderid_folder, exist_ok=True)



        applicationletter_path = default_storage.save(os.path.join('senderid', applicationletter_file.name), ContentFile(applicationletter_file.read()))
        cr12_path = default_storage.save(os.path.join('senderid', cr12_file.name), ContentFile(cr12_file.read())) if cr12_file else ''
        cr13_path = default_storage.save(os.path.join('senderid', cr13_file.name), ContentFile(cr13_file.read())) if cr13_file else ''
        certincorp_path = default_storage.save(os.path.join('senderid', certincorp_file.name), ContentFile(certincorp_file.read())) if certincorp_file else ''
        bussinesscert_path = default_storage.save(os.path.join('senderid', bussinesscert_file.name), ContentFile(bussinesscert_file.read())) if bussinesscert_file else ''

        # Save form data in the database
        getsenderid.objects.create(
            senderid=senderid,
            useremail=user_email,
            smstype=smstype,
            serviceprovider=serviceprovider,
            applicationletter=applicationletter_path,
            cr12=cr12_path,
            cr13=cr13_path,
            certincorp=certincorp_path,
            bussinesscert=bussinesscert_path,
            requestedon=requested_on
        )

        # If you want to return an HTTP response
        return HttpResponse(json.dumps({'message': 'Form data received and saved successfully.'}), content_type='application/json')
    
    # Handle other HTTP methods or cases
    return HttpResponse(json.dumps({'error': 'This endpoint only accepts POST requests.'}), content_type='application/json')




def getsenderids(request):
    if 'email' in request.session:
        user_email = request.session['email']
        sender_ids = getsenderid.objects.filter(useremail=user_email).values()
        return JsonResponse({'senderids': list(sender_ids)})
    else:
        return JsonResponse({'error': 'User email not found in session.'})


def updateprofile(request):
    if request.method == 'POST':
        # Retrieve form data
        user_email = request.session['email']
        firstname = request.POST.get('updatefirstname')
        lastname = request.POST.get('updatelastname')
        email = request.POST.get('updateemail')
        phonenumber = request.POST.get('updatephone')

        # Get the current user's profile
        user_profile = Users.objects.get(email=user_email)

        # Update profile fields
        user_profile.firstname = firstname
        user_profile.lastname = lastname
        user_profile.email = email
        # user_profile.phonenumber = phonenumber

        # Save the updated profile
        user_profile.save()
        request.session['email'] = email
        # Return a success response
        return JsonResponse({'message': 'Profile updated successfully'})

    else:
        # Handle GET request
        return JsonResponse({'error': 'GET method not allowed for this endpoint'}, status=405)