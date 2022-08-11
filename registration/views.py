from datetime import timedelta
from random import randrange

from django.utils import timezone############################
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


from account.models import User
from .models import Token
from .forms import SingupForm
from .send_emails import send_return_otp

from dashboard.gen_key import gen_trail

from dashboard.models import Notification



# Create your views here.
def signup(request):
    if request.method=='POST':
        form = SingupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password)
            #generate OTP
            Token(user=user).save()
            login(request, user)
            return redirect('/dashboard/')
        else:
          return render(request, 'registration/signup.html', {'form':form})  
    else:
        form = SingupForm
        context = {'form': form}
        return render(request, 'registration/signup.html', context)


@login_required
def email_verfiy(request):
    user = User.objects.get(pk=request.user.id)
    if user.token.ban == False:
        user.token.trys_num +=1
        if user.token.trys_num > 4:
            user.token.ban = True
            user.token.ban_date = timezone.now()
            user.ban_date = timezone.now()
        user.token.save()

        if request.method=='POST':
            if len(request.POST["OTP"])!=8 or not request.POST["OTP"].isnumeric():
                return render(request, 'registration/email_verfiy.html',{'OTP':'wrong'}) 
                
            if user.token.activation_date + timedelta(minutes=1) > timezone.now():

                if user.token.activation_code == request.POST["OTP"]:
                    user.email_confirmed = True
                    user.save()
                    gen_trail(user)  # gen trail key  
                    Notification(user=user, header='Trail Key', body='You have a new key valid for new device for 14 days.').save()
                    return redirect('/dashboard/')
                else:
                    return render(request, 'registration/email_verfiy.html',{'OTP':'wrong'}) 

            else:
                return render(request, 'registration/email_verfiy.html',{'OTP':'expired'}) 

        else:
            user.token.activation_date = timezone.now()
            user.token.activation_code = send_return_otp(type='confirm', receiver=user.email)
            user.token.save()
            return render(request, 'registration/email_verfiy.html')

    #ban role
    if user.token.ban == True:
        if user.token.ban_date + timedelta(minutes=3) > timezone.now():###################time mities
            context ={
                'baned':True,
                'ban':str(user.token.ban_date + timedelta(minutes=3) - timezone.now())[3:7]
            }
            return render(request, 'registration/email_verfiy.html', context) 
        else:
            user.token.ban = False
            user.token.trys_num = 0
            user.token.activation_date = timezone.now()
            user.token.activation_code = send_return_otp(type='confirm', receiver=user.email)
            user.token.save()
        
        return render(request, 'registration/email_verfiy.html') 


# def reset_password(request):
    
#     if user.token.ban == False:
#         user.token.trys_num +=1
#         if user.token.trys_num > 4:
#             user.token.ban = True
#             user.token.ban_date = timezone.now()
#             user.ban_date = timezone.now()
#         user.token.save()

#         if request.method=='POST':   
#             user = User.objects.get(email=request.POST["email"])
            
#             if len(request.POST["OTP"])!=8 or not request.POST["OTP"].isnumeric():
#                 return render(request, 'registration/reset_password.html',{'OTP':'wrong'}) 
                
#             if user.token.activation_date + timedelta(minutes=1) > timezone.now():

#                 if user.token.activation_code == request.POST["OTP"]:
#                     if 
#                     user.email_confirmed = True
#                     user.save()            
#                     return render(request, 'registration/reset_password.html',{'reset':True})
#                 else:
#                     return render(request, 'registration/reset_password.html',{'OTP':'wrong'}) 

#             else:
#                 return render(request, 'registration/reset_password.html',{'OTP':'expired'}) 

#         else:
#             user.token.activation_date = timezone.now()
#             user.token.activation_code = send_return_otp(type='reset', receiver=user.email)
#             user.token.save()
#             return render(request, 'registration/reset_password.html')


#     #ban role
#     if user.token.ban == True:
#         if user.token.ban_date + timedelta(minutes=1) > timezone.now():
#             context ={
#                 'baned':True,
#                 'ban':user.token.ban_date + timedelta(minutes=3) - timezone.now()
#             }
#             return render(request, 'registration/reset_password.html', context) 
#         else:
#             user.token.ban = False
#             user.token.trys_num = 0
#             user.token.activation_date = timezone.now()
#             user.token.activation_code = send_return_otp(type='reset', receiver=user.email)#2 reset
#             user.token.save()
        
#         return render(request, 'registration/reset_password.html') 










    











    

        





