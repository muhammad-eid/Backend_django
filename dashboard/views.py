from django.shortcuts import redirect, render

from account.models import User
from .models import GiftMessage

from django.contrib.auth.decorators import login_required

from dashboard.gen_key import gen_purchased
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ObjectDoesNotExist

from .forms import ImagePurchasedForm





# Create your views here.
@login_required
def dashboard(request):
    user = User.objects.get(pk=request.user.id)
    #user login
    # if not user.is_mod:
    if request.method=='POST':
        try:
            if request.FILES:
                key = user.key_set.filter(state='Suspended')
                if key.exists():
                    key = user.key_set.get(state='Suspended')
                    form = ImagePurchasedForm(request.POST, request.FILES, instance=key)
                    if form.is_valid() :
                        form.save()
                        key.state = 'Waiting'
                        key.is_active = True
                        key.save()

        except MultiValueDictKeyError:
            pass
        except:
            pass
        try:
            user.notification_set.filter(id=request.POST["notification_id"]).delete()
        except MultiValueDictKeyError:
            pass
        
        try:
            if request.POST["get_gift_message"] != '':
                user.giftmessage.body = request.POST["get_gift_message"]
                user.giftmessage.save()

        except ObjectDoesNotExist:
            GiftMessage(user=user, body = request.POST["get_gift_message"]).save()

        except MultiValueDictKeyError:
            pass

        try:
            if request.POST["generate_purchased_key"]:
                if not user.key_set.filter(state='Suspended').exists() and not user.key_set.filter(state='Waiting').exists():
                    gen_purchased(user=user)
        except MultiValueDictKeyError:
            pass


        context = {
            'user':user,
            'keys':user.key_set.all(),
            'notifications':user.notification_set.all(),
            # 'gift_message': user.giftmessage.body
            'ImageForm':ImagePurchasedForm
        }
        return render(request, 'dashboard/dashboard.html', context)

    elif request.method=='GET':
        if user.email_confirmed == False:
            return redirect('/email_verfiy/')#add reverse
        context = {
            'user':user,
            'keys':user.key_set.all(),
            'notifications':user.notification_set.all(),
            'ImageForm':ImagePurchasedForm
        }
        return render(request, 'dashboard/dashboard.html', context)



    # #admin login
    # elif user.is_mod:
    #     if request.method=='POST':
    #         pass
    #     elif request.method=='GET':
    #         context = {
    #             'user':user,
    #             'keys':user.key_set.all()
    #         }
    #         return render(request, 'dashboard/dashboard.html', context)