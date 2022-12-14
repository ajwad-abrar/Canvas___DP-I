
from authentication_user.models import User
from django.contrib.auth import login, authenticate ,logout
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from events.models import Event,Images, Genre,Participant
from django.views.generic import ListView, DetailView


# Create your views here.

def Admin_auth(request):  
    if request.method=='POST' and 'loginbtn' in request.POST:
        #email= request.POST.get('email')
        name= request.POST.get('name')
        password = request.POST.get('password')  
        print("done")
        user = authenticate(request, username=name , password = password)
        if (user is not None and user.isAdmin==True):
                login(request, user)
                print("success")
                return redirect('/Admin/Admin_home/')
                
        else:
                # messages.info(request, "Username or Password is incorrect.")
                print("error")

    
    return render(request, 'Admin/Admin_auth.html') 

@login_required
def Admin_home(request):  
    objects= Event.objects.filter(is_accepted= False, is_rejected= False).order_by('start_date')
    accepted= Event.objects.filter(is_accepted= True,is_rejected= False)
    rejected= Event.objects.filter(is_accepted= False,is_rejected= True)
    u_info = User.objects.all()

    if request.method == 'POST' and 'create_genre' in request.POST:
        g = request.POST.get('genre')

        genre = Genre.objects.create(genre_name=g)

        genre.save()
    
    if request.method == 'POST' and 'ac' in request.POST:
        eid= request.POST.get('eid')
        e = Event.objects.get(event_id= eid)
        e.is_accepted= True
        e.save()
    
    elif request.method == 'POST' and 'rj' in request.POST:
        eid= request.POST.get('eid')
        e = Event.objects.get(event_id= eid)
        e.is_rejected= True
        e.save()

    context={
        'objects': objects,
        'accepted': accepted,
        'rejected': rejected,
        'u_info' : u_info
    }

    return render(request, 'Admin/Admin_home.html',context) 


@login_required
def Admin_logout(request):  
    logout(request)
    return render(request, 'Admin/Admin_auth.html') 



def Admin_profile(request):  
    # return HttpResponse("Starting the project")
    return render(request, 'Admin/Admin_profile.html') 


class EventDetail(DetailView):
    model= Event
    template_name= 'Admin/event_details.html'     

    context_object_name= 'event_id'
    
    def get_context_data(self, **kwargs):
        context=super(EventDetail,self).get_context_data(**kwargs)
        context['image']= Images.objects.filter(event_id= self.object)
        return context