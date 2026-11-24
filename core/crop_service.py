from django.utils.translation import gettext_lazy as _

def get_crop_recommendations(season='Kharif', soil_type='Black'):
    """
    Returns recommended crops based on season and soil type.
    """
    crops_database = [
        {
            'name': _('Cotton'),
            'season': 'Kharif',
            'soil': ['Black', 'Alluvial'],
            'water_requirement': 'Medium to High',
            'duration': '150-180 days',
            'icon': 'bi-tree',
            'description': _('Ideal for deep black soils with good drainage. Sowing during early monsoon.')
        },
        {
            'name': _('Soybean'),
            'season': 'Kharif',
            'soil': ['Black', 'Loamy'],
            'water_requirement': 'Medium',
            'duration': '90-100 days',
            'icon': 'bi-flower2',
            'description': _('Rich in protein and oil content. Requires well-drained fertile loamy or black soil.')
        },
        {
            'name': _('Wheat'),
            'season': 'Rabi',
            'soil': ['Alluvial', 'Clay', 'Black'],
            'water_requirement': 'Medium',
            'duration': '120-140 days',
            'icon': 'bi-grass',
            'description': _('Requires cool climate during growth and warm conditions during harvest.')
        },
        {
            'name': _('Gram / Chickpea'),
            'season': 'Rabi',
            'soil': ['Black', 'Loamy', 'Sandy'],
            'water_requirement': 'Low',
            'duration': '90-110 days',
            'icon': 'bi-circle',
            'description': _('Drought-tolerant leguminous crop that restores soil nitrogen levels.')
        },
        {
            'name': _('Groundnut'),
            'season': 'Zaid',
            'soil': ['Sandy', 'Loamy'],
            'water_requirement': 'Medium',
            'duration': '105-120 days',
            'icon': 'bi-egg',
            'description': _('Requires loose, well-drained sandy loam soil to facilitate easy pod formation.')
        }
    ]

    # Filter recommendations based on inputs
    filtered = [
        crop for crop in crops_database
        if crop['season'].lower() == season.lower() and soil_type in crop['soil']
    ]

    return filtered if filtered else crops_database[:3]


def process_ai_advisory_query(query_text):
    """
    Simulates AI advisory response for crop disease identification and farm management queries.
    Can be replaced or integrated with LLM/vision model APIs.
    """
    query_lower = query_text.lower()

    if 'pest' in query_lower or 'insect' in query_lower or 'worm' in query_lower:
        return {
            'topic': _('Pest Management'),
            'advice': _('Inspect the underside of leaves for eggs/nymphs. Consider spraying Neem-based bio-pesticides (5%) or recommended systemic insecticides early morning or late evening.'),
            'urgency': 'Medium'
        }
    elif 'yellow' in query_lower or 'fertilizer' in query_lower or 'nitrogen' in query_lower:
        return {
            'topic': _('Nutrient Deficiency'),
            'advice': _('Yellowing of older leaves typically indicates Nitrogen deficiency. Apply split doses of Urea or balanced NPK (19:19:19) via foliar spray.'),
            'urgency': 'Low'
        }
    elif 'fungus' in query_lower or 'spot' in query_lower or 'rot' in query_lower:
        return {
            'topic': _('Fungal / Leaf Disease'),
            'advice': _('Isolate affected plants. Avoid overhead watering to reduce humidity. Apply Copper Oxychloride (3g/L) or Carbendazim fungicide.'),
            'urgency': 'High'
        }
    else:
        return {
            'topic': _('General Farm Advisory'),
            'advice': _('Ensure optimal irrigation schedule based on weather forecast. Monitor crop health weekly and maintain proper crop spacing for aeration.'),
            'urgency': 'Low'
        }