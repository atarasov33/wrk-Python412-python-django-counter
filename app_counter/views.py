from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse,redirect
from app_counter.models import Counter


def index(request):

    counters = Counter.objects.all()

    return render(
        request=request,
        template_name="app_counter/index.html",
        context={
            "counters": counters
        }
    )


@login_required
def counter(request):

    try:
        counter = Counter.objects.get(user=request.user)
    except Counter.DoesNotExist:
        counter = None

    return render(
        request=request,
        template_name="app_counter/counter.html",
        context={
            "counter": counter
        }
    )


@login_required
def create_counter(request):

    # if not request.user.counters.all():
    #     counter = Counter.objects.create(user=request.user)
    #     counter.save()
    # return redirect('app_counter:counter')
    counter = request.user.counters.create(value=0)
    if request.user.counters.count() == 1:
        counter.is_favorite=True
        counter.save()
    return redirect('app_counter:manage_counter')

@login_required
def increase_counter(request):

    Counter.objects.filter(user=request.user).update(value=F('value') + 1)

    return HttpResponseRedirect(redirect_to=reverse("app_counter:counter"))


@login_required
def decrease_counter(request):

    Counter.objects.filter(user=request.user).update(value=F('value') - 1)

    return HttpResponseRedirect(redirect_to=reverse("app_counter:counter"))


@login_required()
def manage_counter(request):
    counters = request.user.counters.all()
    return  render(
        request=request,
        template_name="app_counter/manage_counter.html",
        context={
            "counters":counters
        }
    )
@login_required()
def set_favorit(request):
    pass

