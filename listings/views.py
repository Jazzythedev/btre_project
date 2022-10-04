from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices



def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # to display with page numbers
    paginator = Paginator(listings, 3)
    page =request.GET.get('page')
    paged_listings = paginator.get_page(page)
       
    
    context = {
        'listings': paged_listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices
        
    }
    
    return render(request, 'listings/listings.html',context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk =listing_id)
    
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

    
def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    
    #API CALL- for keywords field in search container. GET req from API to DB to retrieve data.(description__icontains=keywords means search the description of each listing for keywords typed in.
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    
    # APT call for city. let the city entered match exactly to cities in the db.
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
            
    # API call for state. 
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
    
    # API call for bedrooms. shows number less than or equal to the number of bedroom searched for
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
            
    # API call for price. shows number less than or equal to the price searched for
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
   
   
    
    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }
     
    return render(request, 'listings/search.html', context)
    
