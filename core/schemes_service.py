from django.utils.translation import gettext_lazy as _

def get_government_schemes(category=None):
    """
    Returns curated government schemes for farmers.
    Supports filtering by category (e.g., Financial, Insurance, Subsidy).
    """
    schemes = [
        {
            'id': 'pm-kisan',
            'title': _("PM-KISAN Samman Nidhi"),
            'category': 'Financial',
            'benefit': _("₹6,000 per year in 3 equal installments"),
            'eligibility': _("Small and marginal farmers holding cultivable land."),
            'description': _("Direct income support to landholding farmer families across the country to enable them to procure inputs for agriculture."),
            'link': 'https://pmkisan.gov.in/',
            'icon': 'bi-cash-coin'
        },
        {
            'id': 'pmfby',
            'title': _("PM Fasal Bima Yojana (PMFBY)"),
            'category': 'Insurance',
            'benefit': _("Comprehensive crop insurance against natural risks"),
            'eligibility': _("Farmers growing notified crops in notified areas."),
            'description': _("Financial support to farmers suffering crop loss/damage arising out of unforeseen events like flood, drought, or disease."),
            'link': 'https://pmfby.gov.in/',
            'icon': 'bi-shield-check'
        },
        {
            'id': 'kcc',
            'title': _("Kisan Credit Card (KCC)"),
            'category': 'Credit',
            'benefit': _("Concessional credit up to ₹3 Lakh at low interest"),
            'eligibility': _("All farmers, tenant farmers, and self-help groups."),
            'description': _("Provides adequate and timely credit support for cultivation requirements, post-harvest expenses, and farm maintenance."),
            'link': 'https://www.myscheme.gov.in/',
            'icon': 'bi-credit-card'
        },
        {
            'id': 'soil-health',
            'title': _("Soil Health Card Scheme"),
            'category': 'Subsidy',
            'benefit': _("Free soil testing report and nutrient guidance"),
            'eligibility': _("All landholding farmers across India."),
            'description': _("Helps farmers know the soil nutrient status of their holding along with advice on dosage of fertilizers."),
            'link': 'https://soilhealth.dac.gov.in/',
            'icon': 'bi-journal-check'
        }
    ]

    if category and category != 'All':
        schemes = [s for s in schemes if s['category'].lower() == category.lower()]

    return schemes