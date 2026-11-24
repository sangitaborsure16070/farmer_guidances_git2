from django.core.management.base import BaseCommand
from accounts.models import State, District, Taluka, Village

LOCATION_DATA = {
    "Maharashtra": {
        "name_mr": "महाराष्ट्र",
        "name_hi": "महाराष्ट्र",
        "districts": {
            "Pune": {
                "name_mr": "पुणे",
                "talukas": {
                    "Haveli": {
                        "name_mr": "हवेली",
                        "villages": [
                            ("Wagholi", "वाघोली"),
                            ("Uruli Kanchan", "उरुळी कांचन"),
                            ("Loni Kalbhor", "लोणी काळभोर"),
                            ("Hadapsar", "हडपसर"),
                            ("Khadakwasla", "खडकवासला"),
                            ("Manjari", "मांजरी"),
                            ("Khed Shivapur", "खेड शिवापूर"),
                        ]
                    },
                    "Baramati": {
                        "name_mr": "बारामती",
                        "villages": [
                            ("Malegaon Bk", "माळेगाव बु."),
                            ("Karhati", "कऱ्हाटी"),
                            ("Songaon", "सोनगाव"),
                            ("Jalochi", "जलोची"),
                            ("Supa", "सुपा"),
                            ("Rui", "रुई"),
                            ("Katewadi", "काटेवाडी"),
                            ("Morgaon", "मोरगाव"),
                        ]
                    },
                    "Junnar": {
                        "name_mr": "जुन्नर",
                        "villages": [
                            ("Narayangaon", "नारायणगाव"),
                            ("Alephata", "आळेफाटा"),
                            ("Otur", "ओतूर"),
                            ("Rajur", "राजूर"),
                            ("Dingore", "डिंगोरे"),
                            ("Bori", "बोरी"),
                        ]
                    },
                    "Khed": {
                        "name_mr": "खेड",
                        "villages": [
                            ("Chakan", "चाकण"),
                            ("Rajgurunagar", "राजगुरुनगर"),
                            ("Alandi", "आळंदी"),
                            ("Chas", "चास"),
                            ("Kadus", "कांदूस"),
                        ]
                    },
                    "Ambegaon": {
                        "name_mr": "आंबेगाव",
                        "villages": [
                            ("Manchar", "मंचर"),
                            ("Ghodegaon", "घोडेगाव"),
                            ("Kalamb", "कळंब"),
                            ("Pargaon", "पारगाव"),
                            ("Shinoli", "शिनोली"),
                        ]
                    },
                    "Shirur": {
                        "name_mr": "शिरूर",
                        "villages": [
                            ("Shikrapur", "शिक्रापूर"),
                            ("Sanaswadi", "सनसवाडी"),
                            ("Nighoj", "निघोज"),
                            ("Mandavgan", "मांडवगण"),
                            ("Talegaon Dhamdhere", "तळेगाव ढमढेरे"),
                        ]
                    },
                    "Daund": {
                        "name_mr": "दौंड",
                        "villages": [
                            ("Patas", "पाटस"),
                            ("Yavat", "यवत"),
                            ("Kedgaon", "केडगाव"),
                            ("Kurkumbh", "कुरकुंभ"),
                            ("Boribel", "बोरीबेल"),
                        ]
                    },
                    "Indapur": {
                        "name_mr": "इंदापूर",
                        "villages": [
                            ("Bhigwan", "भिगवण"),
                            ("Nimgaon Ketki", "निमगाव केतकी"),
                            ("Bawada", "बावडा"),
                            ("Walchandnagar", "वालचंद Care"),
                            ("Anthurne", "अंथुर्णे"),
                        ]
                    },
                }
            },
            "Nashik": {
                "name_mr": "नाशिक",
                "talukas": {
                    "Niphad": {
                        "name_mr": "निफाड",
                        "villages": [
                            ("Lasalgaon", "लासलगाव"),
                            ("Pimpalgaon Baswant", "पिंपळगाव बसवंत"),
                            ("Ozar", "ओझर"),
                            ("Ranwad", "रानवड"),
                            ("Kundewadi", "कुंदेवाडी"),
                            ("Vinchur", "विंचूर"),
                        ]
                    },
                    "Sinnar": {
                        "name_mr": "सिन्नर",
                        "villages": [
                            ("Pandhurli", "पांढुर्ली"),
                            ("Wavi", "वावी"),
                            ("Musalgaon", "मुसळगाव"),
                            ("Dodi", "डोडी"),
                            ("Naygaon", "नायगाव"),
                        ]
                    },
                    "Yeola": {
                        "name_mr": "येवला",
                        "villages": [
                            ("Andarsul", "अंदरसुल"),
                            ("Nagarsul", "नगरसुल"),
                            ("Mukhed", "मुखेड"),
                            ("Kotamgaon", "कोतमगाव"),
                        ]
                    },
                    "Malegaon": {
                        "name_mr": "मालेगाव",
                        "villages": [
                            ("Dabhadi", "दाभाडी"),
                            ("Ravalgon", "रावळगाव"),
                            ("Zodga", "झोडगे"),
                            ("Camp", "कॅम्प"),
                            ("Nimgaon", "निमगाव"),
                        ]
                    },
                    "Dindori": {
                        "name_mr": "दिंडोरी",
                        "villages": [
                            ("Vani", "वणी"),
                            ("Nanashi", "नानाशी"),
                            ("Mhasrul", "म्हसरूळ"),
                            ("Khedgaon", "खेडगाव"),
                        ]
                    },
                    "Kalwan": {
                        "name_mr": "कळवण",
                        "villages": [
                            ("Abhona", "आभोणा"),
                            ("Kanashi", "कनाशी"),
                            ("Deoli", "देवळी"),
                            ("Besur", "बेसूर"),
                        ]
                    },
                }
            },
            "Ahmednagar": {
                "name_mr": "अहमदनगर",
                "talukas": {
                    "Rahata": {
                        "name_mr": "राहाता",
                        "villages": [
                            ("Shirdi", "शिर्डी"),
                            ("Babhaleshwar", "बाभळेश्वर"),
                            ("Loni", "लोणी"),
                            ("Sakori", "साकोरी"),
                            ("Kolhar", "कोलहार"),
                        ]
                    },
                    "Shrirampur": {
                        "name_mr": "श्रीरामपूर",
                        "villages": [
                            ("Belapur", "बेलापूर"),
                            ("Padhegaon", "पाधेगाव"),
                            ("Taklibhan", "टाकळीभान"),
                            ("Undirgaon", "उंदीरगाव"),
                        ]
                    },
                    "Sangamner": {
                        "name_mr": "संगमनेर",
                        "villages": [
                            ("Ghulewadi", "घुलेवाडी"),
                            ("Ashwi", "आश्वी"),
                            ("Talegaon", "तळेगाव"),
                            ("Jorve", "जोर्वे"),
                        ]
                    },
                    "Kopargaon": {
                        "name_mr": "कोपरगाव",
                        "villages": [
                            ("Pohegaon", "पोहेगाव"),
                            ("Dhamori", "धामोरी"),
                            ("Yesgaon", "येसगाव"),
                        ]
                    },
                    "Newasa": {
                        "name_mr": "नेवासा",
                        "villages": [
                            ("Kukana", "कुकणा"),
                            ("Sonai", "सोनाई"),
                            ("Bhenda", "भेंडा"),
                            ("Vakod", "वाकोद"),
                        ]
                    },
                }
            },
            "Nagpur": {
                "name_mr": "नागपूर",
                "talukas": {
                    "Nagpur (Rural)": {
                        "name_mr": "नागपूर (ग्रामीण)",
                        "villages": [
                            ("Wadi", "वाडी"),
                            ("Bori", "बोरी"),
                            ("Besa", "बेसा"),
                            ("Pipla", "पिंपळा"),
                        ]
                    },
                    "Katol": {
                        "name_mr": "काटोल",
                        "villages": [
                            ("Kondhali", "कोंढाळी"),
                            ("Yenwa", "येनवा"),
                            ("Paradsinga", "पारडसिंगा"),
                        ]
                    },
                    "Saoner": {
                        "name_mr": "सावनेर",
                        "villages": [
                            ("Khapa", "खापा"),
                            ("Kelod", "केलोद"),
                            ("Waki", "वाकी"),
                        ]
                    },
                    "Ramtek": {
                        "name_mr": "रामटेक",
                        "villages": [
                            ("Mansar", "मानसर"),
                            ("Nagardhan", "नगरधन"),
                            ("Salai", "सलाई"),
                        ]
                    },
                }
            },
            "Chhatrapati Sambhaji Nagar": {
                "name_mr": "छत्रपती संभाजीनगर",
                "talukas": {
                    "Aurangabad": {
                        "name_mr": "औरंगाबाद",
                        "villages": [
                            ("Chikalthana", "चिकलठाणा"),
                            ("Waluj", "वाळूज"),
                            ("Shendra", "शेंद्रा"),
                            ("Harsul", "हर्सूल"),
                        ]
                    },
                    "Paithan": {
                        "name_mr": "पैठण",
                        "villages": [
                            ("Balegaon", "बाळेगाव"),
                            ("Bidkin", "बिडकीन"),
                            ("Georai", "गेवराई"),
                        ]
                    },
                    "Vaijapur": {
                        "name_mr": "वैजापूर",
                        "villages": [
                            ("Rotegaon", "रोटेगाव"),
                            ("Shiur", "शिऊर"),
                            ("Khandala", "खंडाळा"),
                        ]
                    },
                    "Gangapur": {
                        "name_mr": "गंगापूर",
                        "villages": [
                            ("Bhendala", "भेंडाळा"),
                            ("Lakhani", "लाखणी"),
                            ("Valan", "वळण"),
                        ]
                    },
                }
            },
            "Solapur": {
                "name_mr": "सोलापूर",
                "talukas": {
                    "Pandharpur": {
                        "name_mr": "पंढरपूर",
                        "villages": [
                            ("Kasegaon", "कासेगाव"),
                            ("Bhalwani", "भालवणी"),
                            ("Korti", "कोर्टी"),
                            ("Tungat", "तुंगत"),
                        ]
                    },
                    "Barshi": {
                        "name_mr": "बार्शी",
                        "villages": [
                            ("Vairag", "वैराग"),
                            ("Pangri", "पांगरी"),
                            ("Gaudgaon", "गौडगाव"),
                        ]
                    },
                    "Kurduwadi / Madha": {
                        "name_mr": "माढा",
                        "villages": [
                            ("Kurduwadi", "कुर्डूवाडी"),
                            ("Ranjani", "रांजणी"),
                            ("Modnimb", "मोडनिंब"),
                        ]
                    },
                    "Karmala": {
                        "name_mr": "करमाळा",
                        "villages": [
                            ("Jeur", "जेऊर"),
                            ("Korti", "कोर्टी"),
                            ("Kem", "केम"),
                        ]
                    },
                }
            },
            "Kolhapur": {
                "name_mr": "कोल्हापूर",
                "talukas": {
                    "Karveer": {
                        "name_mr": "करवीर",
                        "villages": [
                            ("Shiroli", "शिरोली"),
                            ("Ujalaiwadi", "उचगाव"),
                            ("Vadange", "वडणगे"),
                            ("Chikhali", "चिखली"),
                        ]
                    },
                    "Hatkanangle": {
                        "name_mr": "हातकणंगले",
                        "villages": [
                            ("Ichalkaranji", "इचलकरंजी"),
                            ("Rukadi", "रुकडी"),
                            ("Hupari", "हुपरी"),
                            ("Pattankodoli", "पट्टणकोडोली"),
                        ]
                    },
                    "Shirol": {
                        "name_mr": "शिरोळ",
                        "villages": [
                            ("Jaysingpur", "जयसिंगपूर"),
                            ("Kurundwad", "कुरुंदवाड"),
                            ("Narsobawadi", "नरसोबावाडी"),
                        ]
                    },
                    "Gadhinglaj": {
                        "name_mr": "गडहिंग्लज",
                        "villages": [
                            ("Nesarigi", "नेसरी"),
                            ("Halkarni", "हलकर्णी"),
                            ("Bhadgaon", "भाडगाव"),
                        ]
                    },
                }
            },
            "Jalgaon": {
                "name_mr": "जळगाव",
                "talukas": {
                    "Jalgaon": {
                        "name_mr": "जळगाव",
                        "villages": [
                            ("Mhasawad", "म्हासावद"),
                            ("Neri", "नेरी"),
                            ("Asoda", "असोदा"),
                        ]
                    },
                    "Raver": {
                        "name_mr": "रावेर",
                        "villages": [
                            ("Sawda", "सावदा"),
                            ("Khiroda", "खिरोदा"),
                            ("Pal", "पाल"),
                        ]
                    },
                    "Chopda": {
                        "name_mr": "चोपडा",
                        "villages": [
                            ("Hated", "हातेड"),
                            ("Gorgaon", "गोरगाव"),
                            ("Adgaon", "आडगाव"),
                        ]
                    },
                    "Bhusawal": {
                        "name_mr": "भुसावळ",
                        "villages": [
                            ("Varangaon", "वरणगाव"),
                            ("Fekari", "फेकरी"),
                            ("Kandari", "कंडारी"),
                        ]
                    },
                }
            },
            "Amravati": {
                "name_mr": "अमरावती",
                "talukas": {
                    "Amravati": {
                        "name_mr": "अमरावती",
                        "villages": [
                            ("Badnera", "बडनेरा"),
                            ("Walgaon", "वळगाव"),
                            ("Shirala", "शिराळा"),
                        ]
                    },
                    "Achalpur": {
                        "name_mr": "अचलपूर",
                        "villages": [
                            ("Paratwada", "परतवाडा"),
                            ("Pathrot", "पाथ्रोट"),
                            ("Shirasgaon", "शिरसगाव"),
                        ]
                    },
                    "Morshi": {
                        "name_mr": "मोर्शी",
                        "villages": [
                            ("Dhamangaon", "धामणगाव"),
                            ("Ner Pinglai", "नेर पिंगळाई"),
                            ("Rithpur", "ऋद्धपूर"),
                        ]
                    },
                    "Warud": {
                        "name_mr": "वरुड",
                        "villages": [
                            ("Shendurjana Ghat", "शेंदूरजना घाट"),
                            ("Benoda", "बेनोडा"),
                            ("Pusla", "पुसला"),
                        ]
                    },
                }
            },
            "Latur": {
                "name_mr": "लातूर",
                "talukas": {
                    "Latur": {
                        "name_mr": "लातूर",
                        "villages": [
                            ("Murud", "मुरुड"),
                            ("Harangul", "हारंगुळ"),
                            ("Babhalgaon", "बाभळगाव"),
                        ]
                    },
                    "Ausa": {
                        "name_mr": "औसा",
                        "villages": [
                            ("Killari", "किल्लारी"),
                            ("Lamjana", "लामजाना"),
                            ("Matola", "मातोळा"),
                        ]
                    },
                    "Nilanga": {
                        "name_mr": "निलंगा",
                        "villages": [
                            ("Aurad Shahajani", "औरद शहाजानी"),
                            ("Kasarsirshi", "कासारसिरसी"),
                            ("Nitur", "निटूर"),
                        ]
                    },
                    "Udgir": {
                        "name_mr": "उदगीर",
                        "villages": [
                            ("Deoni", "देवणी"),
                            ("Nalgir", "नळगीर"),
                            ("Togari", "तोगरी"),
                        ]
                    },
                }
            },
            "Satara": {
                "name_mr": "सातारा",
                "talukas": {
                    "Satara": {
                        "name_mr": "सातारा",
                        "villages": [
                            ("Medha", "मेढा"),
                            ("Shendre", "शेंद्रे"),
                            ("Padali", "पाडळी"),
                        ]
                    },
                    "Karad": {
                        "name_mr": "कराड",
                        "villages": [
                            ("Ogalewadi", "ओगलेवाडी"),
                            ("Kole", "कोळे"),
                            ("Masur", "मसूर"),
                            ("Shenoli", "शेणोली"),
                        ]
                    },
                    "Phaltan": {
                        "name_mr": "फलटण",
                        "villages": [
                            ("Taradgaon", "तरडगाव"),
                            ("Barad", "बरड"),
                            ("Sakharwadi", "साखरवाडी"),
                        ]
                    },
                    "Wai": {
                        "name_mr": "वाई",
                        "villages": [
                            ("Bhuinj", "भुईंज"),
                            ("Pasure", "पासुरे"),
                            ("Surur", "सुरुळ"),
                        ]
                    },
                }
            },
            "Sangli": {
                "name_mr": "सांगली",
                "talukas": {
                    "Miraj": {
                        "name_mr": "मिरज",
                        "villages": [
                            ("Kavathepiran", "कवठेपिरान"),
                            ("Kupwad", "कुपवाड"),
                            ("Malgaon", "माळगाव"),
                        ]
                    },
                    "Tasgaon": {
                        "name_mr": "तासगाव",
                        "villages": [
                            ("Savlaj", "सावळज"),
                            ("Manerajuri", "मणेराजुरी"),
                            ("Chinchani", "चिंचणी"),
                        ]
                    },
                    "Walwa (Islampur)": {
                        "name_mr": "वाळवा (इस्लापूर)",
                        "villages": [
                            ("Islampur", "इस्लामपूर"),
                            ("Ashta", "आष्टा"),
                            ("Kasegaon", "कासेगाव"),
                        ]
                    },
                    "Atpadi": {
                        "name_mr": "आटपाडी",
                        "villages": [
                            ("Dighanchi", "दिघंची"),
                            ("Kharpudi", "खरपुडी"),
                            ("Nellore", "नेल्लूर"),
                        ]
                    },
                }
            },
        }
    },
    "Gujarat": {
        "name_mr": "गुजरात",
        "name_hi": "गुजरात",
        "districts": {
            "Rajkot": {
                "name_mr": "राजकोट",
                "talukas": {
                    "Rajkot": {
                        "name_mr": "राजकोट",
                        "villages": [("Gondal", "गोंडल"), ("Jasdan", "जसदन"), ("Jetpur", "जेतपूर")]
                    }
                }
            },
            "Surat": {
                "name_mr": "सुरत",
                "talukas": {
                    "Surat City": {
                        "name_mr": "सुरत शहर",
                        "villages": [("Bardoli", "बारडोली"), ("Kamrej", "कामरेज"), ("Olpad", "ओल्पड")]
                    }
                }
            }
        }
    },
    "Madhya Pradesh": {
        "name_mr": "मध्य प्रदेश",
        "name_hi": "मध्य प्रदेश",
        "districts": {
            "Indore": {
                "name_mr": "इंदूर",
                "talukas": {
                    "Indore": {
                        "name_mr": "इंदूर",
                        "villages": [("Mhow", "महू"), ("Sanwer", "सांवेर"), ("Depalpur", "देपालपूर")]
                    }
                }
            },
            "Ujjain": {
                "name_mr": "उज्जैन",
                "talukas": {
                    "Ujjain": {
                        "name_mr": "उज्जैन",
                        "villages": [("Badnagar", "बडनगर"), ("Mahidpur", "महिदपूर"), ("Nagda", "नागदा")]
                    }
                }
            }
        }
    },
    "Karnataka": {
        "name_mr": "कर्नाटक",
        "name_hi": "कर्नाटक",
        "districts": {
            "Belagavi": {
                "name_mr": "बेळगाव",
                "talukas": {
                    "Belagavi": {
                        "name_mr": "बेळगाव",
                        "villages": [("Chikkodi", "चिक्कोडी"), ("Gokak", "गोकाक"), ("Bailhongal", "बैलहोंगल")]
                    }
                }
            }
        }
    }
}

class Command(BaseCommand):
    help = "Seeds initial states, districts, talukas, and villages into database."

    def handle(self, *args, **options):
        self.stdout.write("Seeding locations...")
        total_states = 0
        total_districts = 0
        total_talukas = 0
        total_villages = 0

        for state_name, state_info in LOCATION_DATA.items():
            state, _ = State.objects.get_or_create(
                name=state_name,
                defaults={"name_mr": state_info.get("name_mr"), "name_hi": state_info.get("name_hi")}
            )
            total_states += 1

            for dist_name, dist_info in state_info.get("districts", {}).items():
                district, _ = District.objects.get_or_create(
                    state=state,
                    name=dist_name,
                    defaults={"name_mr": dist_info.get("name_mr")}
                )
                total_districts += 1

                for taluka_name, taluka_info in dist_info.get("talukas", {}).items():
                    taluka, _ = Taluka.objects.get_or_create(
                        district=district,
                        name=taluka_name,
                        defaults={"name_mr": taluka_info.get("name_mr")}
                    )
                    total_talukas += 1

                    for village_info in taluka_info.get("villages", []):
                        v_name, v_name_mr = village_info
                        Village.objects.get_or_create(
                            taluka=taluka,
                            name=v_name,
                            defaults={"name_mr": v_name_mr}
                        )
                        total_villages += 1

        self.stdout.write(self.style.SUCCESS(
            f"Successfully seeded: {total_states} States, {total_districts} Districts, {total_talukas} Talukas, {total_villages} Villages."
        ))
