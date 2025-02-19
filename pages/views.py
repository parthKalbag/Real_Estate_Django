from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings import choices


def index(request):
    listings = Listing.objects.order_by('list_data').filter(is_published=True)[:3]
    context = {'listings': listings, 'state_choices': choices.state_choices, 'bedroom_choices': choices.bedroom_choices,
               'price_choices': choices.price_choices}
    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {'realtors': realtors, 'mvp_realtors': mvp_realtors}
    return render(request, 'pages/about.html', context)
