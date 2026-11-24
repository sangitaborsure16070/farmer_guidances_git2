from django.utils.translation import gettext_lazy as _

ARTICLES_DATABASE = [
    {
        'id': 'onion-thrips-purple-blotch',
        'title': 'Integrated Management of Purple Blotch and Thrips in Onion Crops',
        'subtitle': 'Essential spraying schedules and nutrient planning to boost onion yields by 25–30%',
        'category': 'Pest & Disease Management',
        'badge_class': 'bg-danger',
        'icon': '🧅',
        'read_time': '5 mins read',
        'date': 'October 12, 2026',
        'author': 'Dr. S. Patil (Senior Agricultural Scientist)',
        'summary': 'A comprehensive scientific guide to combating thrips and fungal purple blotch in onions through crop hygiene, biological defenses, and precision chemical treatments.',
        'key_takeaways': [
            'Install 20 to 25 yellow and blue sticky traps per acre for early thrips detection and mass trapping.',
            'Always include a non-ionic silicon surfactant/sticker when spraying on waxy onion leaves.',
            'Spray strictly in the early morning (before 9 AM) or late evening (after 4 PM) for optimal leaf uptake.',
            'Avoid excessive split doses of Urea/Nitrogen, which soften leaf cuticles and trigger fungal outbreaks.'
        ],
        'sections': [
            {
                'heading': '1. Symptoms and Economic Crop Damage',
                'content': 'Purple Blotch (Alternaria porri) first appears on older onion leaves as small, water-soaked whitish lesions that rapidly turn purplish-brown with yellow halos. Simultaneously, Onion Thrips (Thrips tabaci) colonize leaf sheaths and suck cellular sap, resulting in silvery patches and upward leaf curling. The combined assault severely impairs photosynthetic capacity, stunts bulb expansion, and leads to undersized, unmarketable onions.'
            },
            {
                'heading': '2. Preventive and Bio-Control Protocols',
                'content': 'Management must begin at the nursery stage. Dip seedling roots in a suspension of Trichoderma viride (5 g per liter of water) for 15 minutes before transplanting. Maintain a 15-day prophylactic spray cycle with 5% cold-pressed Neem Seed Kernel Extract (NSKE) or Neem oil (10,000 ppm at 2 ml/L) to deter juvenile thrips nymphs and disrupt their reproductive cycle.'
            },
            {
                'heading': '3. Chemical Spraying Schedule & Approved Dosages',
                'content': 'When insect thresholds exceed 15–20 thrips per plant or purple blotch spots are spotted on more than 5% of foliage, apply the following proven remedies immediately:',
                'table': {
                    'headers': ['Target Pest / Disease', 'Recommended Chemical / Active', 'Dose (per Litre of Water)', 'Stage / Remarks'],
                    'rows': [
                        ['Thrips (Early Infestation)', 'Fipronil 5% SC', '1.5 ml', 'Initial vegetative stage'],
                        ['Thrips (Severe Outbreak)', 'Spinetoram 11.7% SC', '0.9 ml', 'Rapid knock-down effect'],
                        ['Purple Blotch (Preventive)', 'Mancozeb 75% WP', '2.5 g', 'At first symptom onset'],
                        ['Purple Blotch (Advanced)', 'Azoxystrobin 18.2% + Difenoconazole 11.4% SC', '1.0 ml', 'Curative systemic action']
                    ]
                }
            },
            {
                'heading': '4. Expert Advisory on Surfactants and Resistance',
                'content': 'Onion leaves possess an exceptionally thick, waxy epidermal cuticle that causes chemical droplets to roll off harmlessly onto the soil. It is mandatory to blend 0.5 ml of a quality silicon spreader (adjuvant) per liter of spray mix. Rotate chemicals with different Modes of Action (MoA) to prevent pesticide resistance in thrips populations.'
            }
        ]
    },
    {
        'id': 'drip-fertigation-management',
        'title': 'Drip Irrigation and Fertigation: Precision Crop Nutrition Guide',
        'subtitle': 'Save 40% water and fertilizer costs while maximizing root nutrient uptake and crop yield',
        'category': 'Irrigation & Fertilizer Management',
        'badge_class': 'bg-primary',
        'icon': '💧',
        'read_time': '6 mins read',
        'date': 'October 10, 2026',
        'author': 'Er. Ramesh Kulkarni (Irrigation & Soil Specialist)',
        'summary': 'Learn how to deliver 100% water-soluble fertilizers directly into the active crop root zone through calibrated venturi systems, including stage-wise nutrient schedules.',
        'key_takeaways': [
            'Match fertilizer grades to crop growth stages (12:61:00 for roots, 19:19:19 for vegetative, 00:00:50 for fruit sizing).',
            'Run plain irrigation for 15 minutes before and 15 minutes after fertigation to flush salt build-up.',
            'Never blend Calcium Nitrate directly with Sulphate or Phosphate fertilizers in the same stock solution tank.',
            'Perform monthly acid treatments (Nitric or Phosphoric acid) to dissolve carbonate clogging inside drippers.'
        ],
        'sections': [
            {
                'heading': '1. The Science and Efficiency of Fertigation',
                'content': 'Conventional soil broadcasting results in 40–60% of applied fertilizers being lost to volatilization, leaching, or fixed in soil complexes. Fertigation places 100% water-soluble nutrients directly into the wetted root zone at precise concentrations. Plants absorb ionic nutrients with minimal metabolic effort, resulting in uniform canopy growth and faster crop maturation.'
            },
            {
                'heading': '2. Crop Stage-Wise Water-Soluble Fertilizer Schedule',
                'content': 'Apply nutritional grades according to physiological demands as outlined below:',
                'table': {
                    'headers': ['Growth Stage', 'Recommended Soluble Fertilizer', 'Primary Physiological Role', 'Typical Window'],
                    'rows': [
                        ['Root Establishment', '12:61:00 (Mono Ammonium Phosphate)', 'Deep white root proliferation & vigor', 'Days 15–30 after sowing'],
                        ['Vegetative Branching', '19:19:19 or 20:20:20 (Balanced NPK)', 'Sturdy shoot elongation & foliage', 'Days 30–55'],
                        ['Flowering & Fruit Set', '13:40:13 or 00:52:34 (Mono Potassium Phosphate)', 'Prevents flower drop, promotes set', 'Days 55–80'],
                        ['Fruit Filling & Maturity', '00:00:50 (Potassium Sulphate)', 'Maximizes fruit density, brix & color', '20 days before harvest']
                    ]
                }
            },
            {
                'heading': '3. Venturi System Operation and Anti-Clogging Protocols',
                'content': 'Dissolve fertilizers fully in a clean plastic drum before starting injection. Calibrate the venturi suction rate by regulating the pressure difference across the primary bypass valve. Once injection finishes, keep the irrigation line pressurized for at least 15 minutes with clean water to flush out chemical residues from sub-mains and lateral emitters.'
            }
        ]
    },
    {
        'id': 'soybean-cotton-intercropping',
        'title': 'Soybean and Cotton Intercropping: Maximizing Land Productivity & Profit',
        'subtitle': 'Climate risk mitigation and sustainable income through smart intercrop row arrangements',
        'category': 'Modern Crop Techniques',
        'badge_class': 'bg-success',
        'icon': '🌱',
        'read_time': '7 mins read',
        'date': 'October 08, 2026',
        'author': 'Prof. V. Shinde (Department of Agronomy)',
        'summary': 'Discover how pairing soybean with pigeon pea (tur) or cotton with green gram creates climate resilience, improves soil biological activity, and reduces weed pressure.',
        'key_takeaways': [
            'Soybean + Pigeon Pea (4:2 or 3:1 row ratio) is the most proven climate-resilient intercropping model.',
            'Cotton + Soybean (1:1 or 1:2) drastically suppresses early-stage weed growth while diversifying harvest windows.',
            'Leguminous root nodules fix atmospheric nitrogen, enhancing residual soil fertility for future cycles.',
            'Acts as biological financial insurance against localized drought or erratic unseasonal monsoon dry spells.'
        ],
        'sections': [
            {
                'heading': '1. Agronomic Rationale and Economic Buffering',
                'content': 'Monoculture farming leaves farmers vulnerable to weather shocks, pest invasions, and volatile market swings. Intercropping optimizes solar interception, canopy cover, and moisture utilization. When early-maturing soybean is harvested at 90 days, intercropped pigeon pea or cotton expands its canopy into the open space without root competition, providing a second harvest at zero extra land preparation cost.'
            },
            {
                'heading': '2. Recommended Spatial Row Configurations',
                'content': 'For soybean-pigeon pea intercropping, adopt a 4:2 pattern (4 rows of soybean at 30 cm spacing followed by 2 rows of pigeon pea) or a 3:1 pattern. In cotton fields, sow a single row of short-duration soybean or black gram between wide cotton rows (4 feet apart). The legume acts as a live mulch, lowering soil surface evaporation and smothering weed seeds.'
            },
            {
                'heading': '3. Weed Management and Selective Herbicides',
                'content': 'Herbicide selection in intercropped fields requires extra caution. Only apply pre-emergence chemicals approved for both crop families (such as Pendimethalin 30% EC at 1.0 kg a.i./ha within 48 hours of sowing). Once crops germinate, mechanical intercultural operations (hoeing and hand weeding) should be prioritized over post-emergence chemical sprays.'
            }
        ]
    },
    {
        'id': 'organic-jeevamrut-vermicompost',
        'title': 'Organic Farming Blueprint: Preparation and Use of Jeevamrut & Dashparni Ark',
        'subtitle': 'Slash input costs by 80% while restoring indigenous earthworms and vital soil carbon',
        'category': 'Organic Farming',
        'badge_class': 'bg-success',
        'icon': '🌿',
        'read_time': '8 mins read',
        'date': 'October 05, 2026',
        'author': 'Anandrao Deshmukh (Organic Farming Practitioner)',
        'summary': 'A hands-on, step-by-step recipe to formulate liquid microbial Jeevamrut and multi-leaf botanical Dashparni Ark using indigenous cow dung, urine, and locally sourced medicinal leaves.',
        'key_takeaways': [
            'Jeevamrut is not a chemical fertilizer substitute, but a powerful microbial culture for native soil bacteria.',
            'Apply 200 liters of diluted Jeevamrut per acre every 15 days through drip or flood irrigation.',
            'Dashparni Ark offers broad-spectrum biological repellent action against sucking pests and borers.',
            'Consistent use elevates Soil Organic Carbon (SOC) above 1.0%, doubling moisture retention capacity.'
        ],
        'sections': [
            {
                'heading': '1. Standard Recipe for Liquid Jeevamrut (Per Acre)',
                'content': 'Ingredients: 200 liters of water, 10 kg of fresh desi cow dung, 5–10 liters of cow urine, 2 kg of unrefined organic jaggery, 2 kg of pulse flour (gram/chickpea flour), and a handful of uncontaminated virgin soil from the farm bund. Stir clockwise with a wooden stick twice daily in a shaded barrel. The bacterial microbial culture multiplies rapidly and is ready for application within 48–72 hours.'
            },
            {
                'heading': '2. Preparation of 10-Leaf Botanical Dashparni Ark',
                'content': 'Crush 2 kg leaves each of Neem, Karanj, Calotropis (Rui), Datura, Custard Apple, Castor, Lantana camara, Papaya, Nirgundi, and Guduchi in 200 liters of water with cow dung and urine. Allow the mixture to ferment in the shade for 30–40 days. Strain the concentrated botanical extract. Dilute at 200–250 ml per 15-liter knapsack sprayer to control aphids, thrips, jassids, and caterpillar infestations without harming beneficial bees.'
            },
            {
                'heading': '3. Observable Impact on Soil Biological Health',
                'content': 'Field trials demonstrate that two consecutive seasons of Jeevamrut and vermicompost applications restore neutral soil pH, stimulate dormant local earthworm populations, and improve soil crumb porosity. Crops exhibit deeper root penetration, reduced irrigation requirements, and significantly extended shelf life in harvested produce.'
            }
        ]
    },
    {
        'id': 'orchard-pruning-bahar-treatment',
        'title': 'Orchard Management: Pruning Science and Bahar Treatment in Pomegranate & Grapes',
        'subtitle': 'Pruning rules, regulated water stress, and canopy illumination for export-grade fruit',
        'category': 'Orchard & Horticulture',
        'badge_class': 'bg-warning text-dark',
        'icon': '🍇',
        'read_time': '6 mins read',
        'date': 'October 02, 2026',
        'author': 'Dr. Sambhaji Sawant (Horticulture Scientist)',
        'summary': 'Master the art of selecting between Mrig, Hasta, and Ambe Bahar, enforcing regulated water deficit, and executing prophylactic pruning hygiene against bacterial blight and downy mildew.',
        'key_takeaways': [
            'Select Bahar timing strictly based on annual water security and premium market price windows.',
            'Disinfect pruning shears with sodium hypochlorite and immediately coat cut ends with 10% Bordeaux paste.',
            'Break water stress gradually with light irrigation; sudden flooding causes root shock and premature bud drop.',
            'Avoid heavy synthetic chemical spraying during peak flowering (anthesis) to protect pollinating bees.'
        ],
        'sections': [
            {
                'heading': '1. Bahar Selection and Regulated Water Stress',
                'content': 'Pomegranate and grapes require synchronized vegetative dormancy before initiating floral buds. In drought-prone regions, Hasta Bahar (August–September) or Mrig Bahar (May–June) is preferred over Ambe Bahar. Impose controlled water stress for 40–50 days until leaves turn pale yellow and shed naturally, signaling that carbohydrate reserves have migrated to fruit spurs.'
            },
            {
                'heading': '2. Sanitary Pruning Guidelines and Bordeaux Protection',
                'content': 'Remove deadwood, criss-crossing twigs, water sprouts, and blighted shoots. Open the central canopy to allow 360-degree sunlight penetration. Swab cut surfaces with 10% Bordeaux paste (1 kg Copper Sulphate + 1 kg Lime in 10 L water) and spray the entire orchard canopy with 1% Bordeaux mixture within 24 hours to create a bactericidal protective shield.'
            },
            {
                'heading': '3. Flowering, Micronutrient Support, and Sunburn Prevention',
                'content': 'When flower buds swell, supply foliar sprays of Solubor (Boron 20% at 1 g/L) and chelated Zinc (1 g/L). Boron facilitates pollen tube elongation and reduces fruit splitting by up to 80%. After fruit set, maintain adequate vegetative leaf cover or use paper bagging to safeguard maturing fruits against severe sunburn and bird pecking.'
            }
        ]
    },
    {
        'id': 'post-harvest-storage-market-timing',
        'title': 'Post-Harvest Storage and Market Timing: Strategy to Secure 30% Higher Realizations',
        'subtitle': 'Eliminate distress selling at harvest; leverage warehouse receipts and e-NAM price discovery',
        'category': 'Post-Harvest & Market Strategy',
        'badge_class': 'bg-info',
        'icon': '📈',
        'read_time': '5 mins read',
        'date': 'September 28, 2026',
        'author': 'Sanjay Patil (Agri-Business & Marketing Consultant)',
        'summary': 'A practical guide for farmers on moisture grading, scientific commodity storage, taking out 70% pledge loans via Warehouse Receipts (WR), and tracking interstate mandi price cycles.',
        'key_takeaways': [
            'Mandi spot prices hit annual seasonal lows during peak harvesting weeks due to market supply glut.',
            'Maintain grain and oilseed moisture strictly below 10% before warehousing to avert fungal aflatoxins.',
            'State Warehousing Corporations (MSWC/CWC) issue Negotiable Warehouse Receipts (NWR) eligible for bank pledge loans.',
            'Utilize electronic National Agriculture Market (e-NAM) to solicit competitive bids from out-of-state buyers.'
        ],
        'sections': [
            {
                'heading': '1. Cleaning, Grading, and Moisture Standardization',
                'content': 'Never rush freshly harvested crops directly to the market yard without grading. Sort produce by size, remove chaff and broken kernels, and dry under shade until moisture content is under 10% for grains and oilseeds, or properly cured for onions. Well-graded, uniform lots command a ₹200 to ₹500 premium per quintal over ungraded heaps in major mandis.'
            },
            {
                'heading': '2. Unlocking Liquidity via Negotiable Warehouse Receipts (NWR)',
                'content': 'When spot prices drop during harvesting gluts, deposit the cleaned commodity in accredited government warehouses (MSWC or WDRA-certified godowns). The warehouse issues an official Negotiable Warehouse Receipt (NWR), against which scheduled commercial banks disburse instant pledge loans up to 70% of commodity value at subsidized agricultural interest rates, relieving urgent cash flow pressure.'
            },
            {
                'heading': '3. Price Intelligence and Phased Selling Tactics',
                'content': 'Track mandi price trends across neighboring district APMCs via KisanMitra and the Agmarknet portal. Instead of selling entire stocks in a single transaction, sell in three phased tranches across the off-season. This disciplined dollar-cost averaging strategy consistently outperforms single-day spot sales and secures top average realizations.'
            }
        ]
    }
]

def get_articles(category=None, search=None):
    """
    Returns list of curated articles, optionally filtered by category or search term.
    """
    results = ARTICLES_DATABASE
    if category and category != 'All' and category != 'All Articles':
        cat_lower = category.lower().strip()
        results = [a for a in results if cat_lower in a['category'].lower()]
    
    if search:
        s_lower = search.lower().strip()
        results = [
            a for a in results
            if s_lower in a['title'].lower() or 
               s_lower in a['subtitle'].lower() or 
               s_lower in a['summary'].lower() or
               s_lower in a['category'].lower()
        ]
    return results

def get_article_by_id(article_id):
    """
    Returns single article by ID or None.
    """
    if not article_id:
        return None
    for article in ARTICLES_DATABASE:
        if article['id'] == article_id:
            return article
    return None
