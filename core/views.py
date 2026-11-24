from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .article_service import get_articles, get_article_by_id

def home(request):
    """Landing Page View."""
    featured_articles = get_articles()[:3]
    context = {
        "title": "KisanMitra | Smart Farming Guidance",
        "featured_articles": featured_articles,
    }
    return render(request, "home.html", context)

def custom_404(request, exception):
    return render(request, "404.html", status=404)

def custom_500(request):
    return render(request, "500.html", status=500)

def custom_403(request, exception):
    
    
    
    return render(request, "403.html", status=403)

from django.shortcuts import render
from django.http import JsonResponse
from .weather_service import get_weather_data

def weather_dashboard(request):
    """
    Renders the Weather Page and handles AJAX requests for dynamic city queries.
    """
    city = request.GET.get('city', '').strip()
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')

    weather = get_weather_data(city_name=city, lat=lat, lon=lon)

    # Return JSON for dynamic frontend AJAX updates
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse(weather)

    popular_cities = [
        'Pune', 'Nashik', 'Ahmednagar', 'Nagpur', 'Chhatrapati Sambhaji Nagar',
        'Solapur', 'Kolhapur', 'Jalgaon', 'Amravati', 'Latur', 'Satara', 'Sangli'
    ]

    context = {
        'weather': weather,
        'popular_cities': popular_cities,
        'selected_city': city or weather.get('city', 'Pune'),
    }
    return render(request, 'core/weather.html', context)

from django.shortcuts import render
from django.http import JsonResponse
from .market_service import get_mandi_prices

def market_prices_view(request):
    """
    Renders Mandi rates dashboard and handles AJAX query filters.
    """
    state = request.GET.get('state', 'Maharashtra').strip()
    district = request.GET.get('district', '').strip()
    commodity = request.GET.get('commodity', '').strip()

    prices = get_mandi_prices(state=state, district=district, commodity=commodity)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'prices': prices,
            'count': len(prices),
            'selected_state': state,
            'selected_district': district,
            'selected_commodity': commodity
        })

    available_districts = [
        'Pune', 'Nashik', 'Ahmednagar', 'Nagpur', 'Chhatrapati Sambhaji Nagar',
        'Solapur', 'Kolhapur', 'Jalgaon', 'Amravati', 'Latur', 'Satara', 'Sangli'
    ]
    available_commodities = [
        'Onion', 'Wheat', 'Soyabean', 'Cotton', 'Gram / Chickpea',
        'Tomato', 'Sugarcane', 'Maize', 'Tur / Arhar', 'Pomegranate',
        'Grapes', 'Banana', 'Potato', 'Groundnut', 'Ginger', 'Turmeric', 'Chilli'
    ]

    context = {
        'prices': prices,
        'selected_state': state,
        'selected_district': district,
        'selected_commodity': commodity,
        'total_count': len(prices),
        'available_districts': available_districts,
        'available_commodities': available_commodities,
    }
    return render(request, 'core/market_prices.html', context)


from django.shortcuts import render
from django.http import JsonResponse
from .schemes_service import get_government_schemes

def government_schemes_view(request):
    """
    Renders the Government Schemes page with optional category filtering.
    """
    category = request.GET.get('category', 'All')
    schemes = get_government_schemes(category=category)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'schemes': schemes})

    context = {
        'schemes': schemes,
        'selected_category': category,
        'categories': ['All', 'Financial', 'Insurance', 'Credit', 'Subsidy']
    }
    return render(request, 'core/schemes.html', context)


from django.shortcuts import render
from django.http import JsonResponse
from .crop_service import get_crop_recommendations, process_ai_advisory_query

def crop_guidance_view(request):
    """
    Renders the Crop Guidance & Advisory Page.
    Handles AJAX requests for crop selection and advisory queries.
    """
    season = request.GET.get('season', 'Kharif')
    soil_type = request.GET.get('soil', 'Black')

    recommendations = get_crop_recommendations(season=season, soil_type=soil_type)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        action = request.GET.get('action')
        
        if action == 'ask_ai':
            query = request.GET.get('query', '')
            advisory = process_ai_advisory_query(query)
            return JsonResponse({'advisory': advisory})
            
        return JsonResponse({'recommendations': recommendations})

    context = {
        'recommendations': recommendations,
        'selected_season': season,
        'selected_soil': soil_type,
        'seasons': ['Kharif', 'Rabi', 'Zaid'],
        'soils': ['Black', 'Alluvial', 'Loamy', 'Sandy', 'Clay']
    }
    return render(request, 'core/crop_guidance.html', context)

def articles(request):
    """
    Renders Farming Articles list with category filter and search.
    """
    category = request.GET.get('category', 'All').strip()
    search = request.GET.get('search', '').strip()

    article_list = get_articles(category=category, search=search)
    categories = [
        'All',
        'Pest & Disease Management',
        'Irrigation & Fertilizer Management',
        'Modern Crop Techniques',
        'Organic Farming',
        'Orchard & Horticulture',
        'Post-Harvest & Market Strategy'
    ]

    context = {
        'articles': article_list,
        'selected_category': category,
        'search_query': search,
        'categories': categories,
        'total_count': len(article_list),
    }
    return render(request, 'core/articles.html', context)

def article_detail(request, article_id):
    """
    Renders detailed view of a specific farming article.
    """
    article = get_article_by_id(article_id)
    if not article:
        raise Http404("Article not found")

    related_articles = [a for a in get_articles() if a['id'] != article_id][:2]

    context = {
        'article': article,
        'related_articles': related_articles,
    }
    return render(request, 'core/article_detail.html', context)