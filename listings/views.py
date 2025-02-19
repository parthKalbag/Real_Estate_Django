from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import Listing
from listings import choices


def index(request):
    listings = Listing.objects.order_by('-list_data').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)

    context = {'listings': page_listings}
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {'listing': listing}
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_data')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']

        if city:
            queryset_list = queryset_list.filter(
                city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']

        if state:
            queryset_list = queryset_list.filter(
                state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']

        if bedrooms:
            queryset_list = queryset_list.filter(
                bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']

        if price:
            queryset_list = queryset_list.filter(
                price__lte=price)

    context = {'state_choices': choices.state_choices, 'bedroom_choices': choices.bedroom_choices,
               'price_choices': choices.price_choices, 'listings': queryset_list, 'values': request.GET}
    return render(request, 'listings/search.html', context)
