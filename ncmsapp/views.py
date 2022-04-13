from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from ncmsapp.models import order_placed
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'index.html')

def signIn(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        # is_private = request.POST.get('is_private', False)
        user = authenticate(username = username, password = pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'index.html', {'fname': fname})
        
        else:
            messages.error(request, "Wrong Credentials!")
            return redirect('home')

    return render(request,'signIn.html')

def signUp(request):

    if request.method == "POST":
        # username = request.POST.get('usrename')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your Account has been successfully created.")

        return redirect('signIn')

    return render(request,'signUp.html')

def aboutUs(request):
    return render(request,'aboutUs.html')

def images(request):
    return render(request,'images.html')

def index(request):
    return render(request, 'index.html')

def signOut(request):
    logout(request)
    messages.success(request,"Logged Out Successfully!")
    return redirect('home')

def saveEnquiry(request):

    if request.method == "POST":
        order_number = request.POST.get('order_number')
        item_number = request.POST.get('item_number')
        time_order_placed = request.POST.get('time_order_placed')
        quantity = request.POST.get('quantity')
        customer_id = request.POST.get('customer_id')

        en = order_placed(order_number=order_number, item_number= item_number, time_order_placed=time_order_placed, quantity=quantity, customer_id=customer_id)

        en.save()

    return render(request, 'index.html')