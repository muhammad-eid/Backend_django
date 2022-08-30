from django.shortcuts import render

# Create your views here.

def home(request):
    if request.method=='POST':
        pass

    elif request.method=='GET':
        context = {
            # 'user':user,
            # 'keys':user.key_set.all()
            'data':'data'
        }
        return render(request, 'home/index.html', context)
