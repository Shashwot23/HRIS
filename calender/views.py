from django.shortcuts import render
from .models import Events
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test

def is_superuser(user):
    return user.is_superuser

# Create your views here.
def calender(request):
    all_events = Events.objects.all().order_by('start')
    context = {
        "events": all_events
    }
    return render(request, 'calender/calender.html', context)

def all_events(request):                                                                                                 
    all_events = Events.objects.all()                                                                                    
    out = []                                                                                                             
    for event in all_events:                                                                                             
        out.append({                                                                                                     
            'title': event.name,                                                                                         
            'id': event.id,  
            'description': event.description,                                                                                            
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),                                                             
        })                                                                                                               
                                                                                                                      
    return JsonResponse(out, safe=False) 

@user_passes_test(is_superuser)
def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    description = request.GET.get("description", None)
    event = Events(name=str(title), start=start, end=end, description=description)
    event.save()
    data = {}
    return JsonResponse(data)

@user_passes_test(is_superuser)
def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)

@user_passes_test(is_superuser)
def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)