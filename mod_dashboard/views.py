import psutil
import shutil
import datetime



from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from account.models import User
from dashboard.models import Key, GiftMessage
from project import settings


@login_required
def mod_dashboard_overview(request):
    user = User.objects.get(pk=request.user.id)
    if not user.is_mod:
        return redirect('/dashboard/')

    if request.method=='POST':
        pass


    current_month = str(datetime.datetime.now().month).zfill
    statistic = {
        'cpu_usage': int(psutil.cpu_percent()),
        'ram_usage': float(psutil.virtual_memory().percent),
        'disk_total':shutil.disk_usage('/').total,
        'disk_usage':shutil.disk_usage('/').used,
        'disk_free':shutil.disk_usage('/').free,

        'total_keys':Key.objects.all().count(),
        'total_keys_activated':Key.objects.all().filter(activated=True).count(),
        'total_keys_running':Key.objects.all().filter(state="Running").count(),
        'total_keys_activated_this_month':Key.objects.all().filter(activated=True).filter(act_date__month=datetime.datetime.now().month).count(),
        'total_keys_expired':Key.objects.all().filter(state="Expired").count(),
        'total_keys_expired_this_month':Key.objects.all().filter(state="Expired").filter(act_date__month=datetime.datetime.now().month).count(),

        'trail_keys':Key.objects.all().filter(type='Trail').count(),
        'trail_keys_activated':Key.objects.all().filter(type='Trail').filter(activated=True).count(),
        'trail_keys_running':Key.objects.all().filter(type='Trail').filter(state="Running").count(),
        'trail_keys_activated_this_month':Key.objects.all().filter(type='Trail').filter(activated=True).filter(act_date__month=datetime.datetime.now().month).count(),
        'trail_keys_expired':Key.objects.all().filter(type='Trail').filter(state="Expired").count(),
        'trail_keys_expired_this_month':Key.objects.all().filter(type='Trail').filter(state="Expired").filter(act_date__month=datetime.datetime.now().month).count(),

        'gift_keys':Key.objects.all().filter(type='Gift').count(),
        'gift_keys_activated':Key.objects.all().filter(type='Gift').filter(activated=True).count(),
        'gift_keys_running':Key.objects.all().filter(type='Gift').filter(state="Running").count(),
        'gift_keys_activated_this_month':Key.objects.all().filter(type='Gift').filter(activated=True).filter(act_date__month=datetime.datetime.now().month).count(),
        'gift_keys_expired':Key.objects.all().filter(type='Gift').filter(state="Expired").count(),
        'gift_keys_expired_this_month':Key.objects.all().filter(type='Gift').filter(state="Expired").filter(act_date__month=datetime.datetime.now().month).count(),

        'purchased_keys':Key.objects.all().filter(type='Purchased').count(),
        'purchased_keys_activated':Key.objects.all().filter(type='Purchased').filter(activated=True).count(),
        'purchased_keys_running':Key.objects.all().filter(type='Purchased').filter(state="Running").count(),
        'purchased_keys_activated_this_month':Key.objects.all().filter(type='Purchased').filter(activated=True).filter(act_date__month=datetime.datetime.now().month).count(),
        'purchased_keys_expired':Key.objects.all().filter(type='Purchased').filter(state="Expired").count(),
        'purchased_keys_expired_this_month':Key.objects.all().filter(type='Purchased').filter(state="Expired").filter(act_date__month=datetime.datetime.now().month).count(),
        
    }
    context = {
        'statistic': statistic,
        'MEDIA': settings.MEDIA_URL,
        'purchased_keys_to_activate': Key.objects.all().filter(type='Purchased').filter(state='Waiting'),
        'gift_keys_to_activate': GiftMessage.objects.all()
    }
    print(context['statistic']['ram_usage'])
    return render(request, 'mod_dashboard/overview.html', context)





@login_required
def mod_dashboard_control(request):
    user = User.objects.get(pk=request.user.id)
    if not user.is_mod:
        return redirect('/dashboard/')

    if request.method=='POST':
        pass

    elif request.method=='GET':
        context = {
            'user':user,
            'keys':user.key_set.all()
        }
        return render(request, 'mod_dashboard/control.html', context)




@login_required
def mod_dashboard_settings(request):
    user = User.objects.get(pk=request.user.id)
    if not user.is_mod:
        return redirect('/dashboard/')

    if request.method=='POST':
        pass

    elif request.method=='GET':
        context = {
            'user':user,
            'keys':user.key_set.all()
        }
        return render(request, 'mod_dashboard/settings.html', context)