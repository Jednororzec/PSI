from django.shortcuts import render
from .models import Event
from django.contrib.auth.decorators import login_required


@login_required
def event(request):
    kwargs = {}
    kwargs['event'] = Event.objects.filter(user=request.user)
    return render(request, 'events.html', kwargs)
