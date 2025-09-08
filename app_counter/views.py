from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse,redirect
from app_counter.models import Counter


# def index(request):
#
#     counters = request.user.counters.all()
#
#     return render(
#         request=request,
#         template_name="app_counter/index.html",
#         context={
#             "counters": counters
#         }
#     )

def index(request):
    if request.user.is_authenticated:

        counters = request.user.counters.all()
    else:


        counters = Counter.objects.none()

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
        counter = request.user.counters.get(is_favorite=True)
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

    request.user.counters.update(value=F('value') + 1)

    return HttpResponseRedirect(redirect_to=reverse("app_counter:counter"))


@login_required
def decrease_counter(request):

    request.user.counters.update(value=F('value') - 1)

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
def set_favorit(request, counter_id):
    try:
        counter = request.user.counters.get(pk=counter_id)
        counter.is_favorite=True
        counter.save()

    except Counter.DoesNotExist:
        pass
    return HttpResponseRedirect(redirect_to=reverse("app_counter:manage_counter"))


