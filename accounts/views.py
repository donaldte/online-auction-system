from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from auctionItem.models import Contact,Wishlist,Seller

# Create your views here.

def register(request):
    if request.method =='POST':
        # messages.add_message(request, messages.ERROR, 'Username taken')
        # return redirect('register'
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirmPassword=request.POST['confirmPassword']
        
        if password == confirmPassword:
            if User.objects.filter(username=username).exists():
                messages.add_message(request, messages.ERROR, 'Username taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.add_message(request, messages.ERROR, 'Email Already Exist')
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
                    user.save()
                    messages.add_message(request, messages.SUCCESS, 'You are now register,please log in')
                    return redirect('login')
                
        else:
            messages.add_message(request, messages.ERROR, 'Passwords does not match')
            return redirect('register')
            
    return render(request,'register.html')

def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.add_message(request, messages.SUCCESS, 'You have now logged in successfully')
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Credentials')
            return redirect('login')
   
    else:
        return render(request,'login.html')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, 'You have been logged out successfullt')
        return redirect('home-page')
        
        
    return redirect('home-page')

def dashboard(request):
    contact_dashboard=Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)  
    
    seller = Seller.objects.filter(name=request.user.username)
    sel = False
    if seller:
        sel = True
    context={
        'contacts':contact_dashboard,
        'sel': sel
      
    }
    return render(request,'dashboard.html',context)

def wishlist(request):
    seller = Seller.objects.filter(name=request.user.username)
    sel = False
    if seller:
        sel = True
   
    contact_wishlist=Wishlist.objects.order_by('-Wishlisted_date').filter(user_id=request.user.id)  
   
    context={
        'wishlists':contact_wishlist,
        'sel': sel
      
    }
    return render(request,'wishlist.html',context)



def become_seller(request):
    seller = Seller.objects.filter(name=request.user.username)
    sel = False
    if seller:
            sel = True
    context={
            'sel': sel
        
        }
    if request.method == 'POST':
        seller_picture = request.FILES.get('seller_picture')
        contact_number = request.POST.get('contact_number')
        seller_email = request.POST.get('seller_email')
        profile_description = request.POST.get('profile_description')
        region = request.POST.get('regions')
        location = request.POST.get('location')

        # Create a new Seller object and save it to the database
        seller = Seller(
            name=request.user.username,
            seller_photo=seller_picture,
            contact_no=contact_number,
            email=seller_email,
            description=profile_description,
            region=region,
            location=location
        )
        try:
            seller.save()
        except:
            messages.error(request, "Sorry Your are already a seller")    
        messages.success(request, "Congratulations you're now a seller on our aution platform in Cameroon")


    return render(request, 'become_seller.html', context)