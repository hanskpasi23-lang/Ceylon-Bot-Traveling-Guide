
import database

DOMAIN_DATA = [
    # ==================== VISA & ENTRY ====================
    ("do i need a visa for sri lanka", "Most nationalities need an Electronic Travel Authorization (ETA). Apply online at www.srilankaeta.gov.lk. A 30-day tourist ETA costs ~$50 USD.", "visa", "visa eta entry permit passport"),
    ("how to get a visa", "Apply for an ETA online at srilankaeta.gov.lk before your trip. Processing takes 24 hours. Visa on arrival is also possible but online is recommended.", "visa", "visa eta apply online"),
    ("how to apply for sri lanka visa", "Visit www.srilankaeta.gov.lk, fill the application form, pay ~$50 USD, and receive your ETA via email within 24 hours.", "visa", "visa apply eta online form"),
    ("how long can i stay in sri lanka", "A standard tourist ETA allows 30 days, extendable up to 90 days at the Department of Immigration in Colombo.", "visa", "stay duration visa extend"),
    ("what documents do i need to enter sri lanka", "You need a valid passport (6+ months validity), ETA approval, return ticket, and proof of sufficient funds. No mandatory vaccinations required.", "visa", "documents passport entry requirements"),
    ("can i extend my visa in sri lanka", "Yes! Visit the Department of Immigration in Colombo to extend your ETA up to 90 days. Bring your passport, return ticket, and extension fee.", "visa", "extend visa immigration duration"),

    # ==================== WEATHER & BEST TIME ====================
    ("what is the best time to visit sri lanka", "West/South coast & hill country: December-March. East coast: April-September. Cultural Triangle: January-April. There's always a dry coast!", "weather", "best time visit season month"),
    ("when should i visit sri lanka", "It depends on where you're going! Dec-Mar for west/south beaches, Apr-Sep for east coast, Jan-Apr for cultural sites. Sri Lanka is great year-round.", "weather", "when visit season best month"),
    ("what is the weather like in sri lanka", "Tropical climate. Coastal areas: 27-30°C year-round. Hill country (Nuwara Eliya, Ella): 15-20°C. Two monsoon seasons affect different coasts.", "weather", "weather climate temperature hot cold"),
    ("does it rain a lot in sri lanka", "Two monsoon seasons: southwest (May-Sep) affects west/south coast, northeast (Oct-Jan) affects east coast. There's always a dry side to visit!", "weather", "rain monsoon wet dry season"),
    ("what is the temperature in sri lanka", "Coastal lowlands average 27-30°C. Hill country ranges from 15-20°C. Humidity is generally 70-80%. Pack light clothes and a light jacket for hills.", "weather", "temperature hot cold degrees celsius"),
    ("best time to visit kandy", "October to April is ideal for Kandy — dry weather, pleasant temperatures around 20-25°C. The famous Esala Perahera festival is in July/August.", "weather", "kandy best time visit season"),
    ("best time to visit east coast", "April to September is the best season for the east coast (Trincomalee, Arugam Bay, Batticaloa). Clear skies, calm seas, perfect for beaches and surfing.", "weather", "east coast trincomalee arugam season"),

    # ==================== CURRENCY & BUDGET ====================
    ("what currency is used in sri lanka", "Sri Lankan Rupee (LKR). 1 USD ≈ 300 LKR. ATMs widely available in cities. Credit cards accepted at most hotels and restaurants.", "currency", "currency money rupee lkr exchange rate"),
    ("how much does a trip to sri lanka cost", "Very budget-friendly! Budget: $30-50/day, Mid-range: $50-100/day, Luxury: $150+/day. Covers accommodation, food, transport, and activities.", "budget", "cost budget price expensive cheap"),
    ("is sri lanka expensive", "One of Asia's most affordable destinations. Street food: $1-3, hotel: $20-50/night, tuk-tuk: $1-5. Excellent value for money.", "budget", "expensive cheap affordable cost value"),
    ("where can i exchange money in sri lanka", "Banks, authorized money changers, and airport counters offer currency exchange. ATMs are widespread in cities. Avoid exchanging at unofficial places.", "currency", "exchange money currency bank atm"),
    ("should i tip in sri lanka", "Tipping is appreciated but not mandatory. 10% at restaurants if no service charge. Small tips for drivers, guides ($5-10/day), and hotel staff.", "budget", "tip tipping service charge gratuity"),
    ("how much money should i bring to sri lanka", "Budget travelers: $30-50/day. Mid-range: $50-100/day. Carry some USD cash for emergencies. Most places accept LKR; use ATMs for best rates.", "budget", "money bring budget daily cost"),

    # ==================== TRANSPORT ====================
    ("how to get around sri lanka", "Options: 🚂 Scenic trains (popular!), 🚌 Buses (cheap), 🛺 Tuk-tuks (short trips), 🚗 Private drivers (~$40-60/day), 🚐 PickMe ride-hailing app.", "transport", "transport travel bus train tuk taxi drive around"),
    ("tell me about the train rides", "The Kandy-Ella route is one of the world's most scenic! Passes through tea plantations and misty mountains. Book observation car seats in advance!", "transport", "train ride scenic railway kandy ella beautiful"),
    ("how to get from airport to colombo", "Bandaranaike Airport is 35km from Colombo. Options: Airport taxi (~$15-20, 1hr), Express bus to Colombo Fort, or pre-arranged hotel transfer.", "transport", "airport colombo transfer taxi bus arrive"),
    ("can i rent a car in sri lanka", "You can hire a car with driver ($40-60/day) which is recommended due to local driving conditions. Self-drive is possible with an international license.", "transport", "rent car hire driver self drive license"),
    ("how is the bus system in sri lanka", "Extensive and very cheap! Intercity buses connect all major cities. AC luxury buses available on main routes. Expect crowded conditions during rush hours.", "transport", "bus system public cheap intercity route"),
    ("is uber available in sri lanka", "PickMe is the most popular ride-hailing app (Sri Lanka's Uber). Regular Uber also works in Colombo. Both are affordable and reliable in urban areas.", "transport", "uber pickme ride hailing app taxi"),
    ("how to travel from colombo to kandy", "Train (3.5hrs, scenic), Bus (3hrs, frequent), or Private car (2.5hrs). The train ride is highly recommended for beautiful views of the countryside.", "transport", "colombo kandy travel train bus drive"),
    ("how to travel from kandy to ella", "The famous scenic train takes ~6 hours through tea country. Book 2nd class reserved seats. Alternatively, bus (5hrs) or car (4hrs).", "transport", "kandy ella train scenic travel"),

    # ==================== FOOD & CUISINE ====================
    ("what food should i try in sri lanka", "Must-try: 🍛 Rice & Curry, 🥞 Hoppers & String Hoppers, 🌶️ Kottu Roti, 🍲 Lamprais, 🦀 Jaffna Crab Curry, 🍌 Pol Sambol, and Ceylon Tea!", "food", "food cuisine eat dish rice curry hoppers kottu try"),
    ("what is the traditional food of sri lanka", "Rice and Curry is the staple — rice with multiple curries, sambols, and papadum. Other staples: hoppers, string hoppers, pittu, and kiribath (milk rice).", "food", "traditional food staple rice curry authentic local"),
    ("is sri lankan food spicy", "Generally yes! Uses chili, black pepper, and local spices. Most restaurants can adjust spice levels. Mild options always available — just ask!", "food", "spicy food hot chili mild level"),
    ("where to eat in colombo", "Top picks: Ministry of Crab (famous seafood), Nihonbashi (fusion), Gallery Café (ambiance), Upali's (authentic Sri Lankan), Galle Face Green (street food).", "food", "eat restaurant colombo dining best"),
    ("what is kottu roti", "Kottu is chopped roti stir-fried with vegetables, egg, and/or meat on a hot griddle. You'll hear the rhythmic chopping sound across Sri Lanka. A must-try street food!", "food", "kottu roti street food chopped"),
    ("what is a hopper", "Hoppers (appa) are bowl-shaped crispy pancakes made from rice flour and coconut milk. Egg hoppers have an egg cracked in the center. A classic Sri Lankan breakfast!", "food", "hopper appa egg pancake breakfast"),
    ("what is ceylon tea", "Sri Lanka (formerly Ceylon) is one of the world's top tea producers. Ceylon tea is known for its bright flavor. Visit a tea factory in Nuwara Eliya or Ella!", "food", "ceylon tea plantation factory drink"),
    ("what fruits are available in sri lanka", "Tropical paradise! Try: king coconut (thambili), rambutan, mangosteen, wood apple, papaya, passion fruit, and the famous Sri Lankan bananas.", "food", "fruits tropical fresh mango coconut rambutan"),
    ("is vegetarian food available in sri lanka", "Absolutely! Sri Lankan cuisine has many vegetarian options: dhal curry, vegetable curry, jackfruit curry, pol sambol, and Buddhist restaurants serve fully vegetarian menus.", "food", "vegetarian vegan food options plant diet"),

    # ==================== DESTINATIONS ====================
    ("tell me about sigiriya", "Sigiriya (Lion Rock) — 5th-century fortress, UNESCO site. Ancient frescoes, mirror wall, and water gardens. Climb 1,200 steps for panoramic views. Visit early morning!", "destinations", "sigiriya lion rock fortress climb unesco"),
    ("tell me about kandy", "Cultural capital. Sacred Temple of the Tooth Relic, Kandy Lake, Royal Botanical Gardens (Peradeniya), Kandyan dance shows. Cool climate in the hills.", "destinations", "kandy temple tooth cultural dance lake"),
    ("tell me about galle", "Historic Dutch Fort (UNESCO), walk the fort walls at sunset, boutique shops, cafes, maritime museum, lighthouse. Beautiful colonial architecture.", "destinations", "galle fort dutch colonial heritage sunset"),
    ("tell me about ella", "Charming hill town. Hike Ella Rock & Little Adam's Peak, visit Nine Arches Bridge, zipline at Flying Ravana, stunning views of the Ella Gap.", "destinations", "ella hiking nine arches bridge little adams peak"),
    ("tell me about nuwara eliya", "'Little England' at 1,868m elevation. Cool climate, tea factories, Gregory Lake, Horton Plains, World's End cliff. Strawberry farms and gardens.", "destinations", "nuwara eliya tea little england horton plains cold"),
    ("tell me about yala", "Most popular safari park. Highest leopard density in the world! Also elephants, sloth bears, crocodiles, 200+ bird species. Morning safaris are best.", "destinations", "yala national park safari leopard elephant wildlife"),
    ("tell me about colombo", "Vibrant capital city. Galle Face Green, Gangaramaya Temple, Pettah Market, National Museum, Dutch Hospital shopping precinct, and great nightlife.", "destinations", "colombo capital city urban shopping market"),
    ("tell me about trincomalee", "East coast gem. Beautiful beaches (Nilaveli, Uppuveli), Koneswaram Temple, Pigeon Island snorkeling, whale watching (Mar-Aug), and hot springs.", "destinations", "trincomalee beach east coast pigeon island"),
    ("tell me about jaffna", "Northern cultural hub. Nallur Kandaswamy Temple, Jaffna Fort, vibrant Tamil cuisine (famous crab curry!), Casuarina Beach, Nainativu island.", "destinations", "jaffna north tamil culture temple fort"),
    ("tell me about mirissa", "South coast beach paradise. Famous for whale watching (Nov-Apr), surfing, palm-lined beaches, and the iconic coconut tree hill viewpoint.", "destinations", "mirissa beach whale watching south coast surfing"),
    ("tell me about dambulla", "Golden Cave Temple (UNESCO) — five caves with 150+ Buddha statues and stunning ceiling paintings. Nearby Sigiriya makes it a great day-trip combo.", "destinations", "dambulla cave temple golden buddha unesco paintings"),
    ("tell me about anuradhapura", "Ancient capital (4th century BC). Sacred Bo Tree (Sri Maha Bodhi — oldest historically documented tree!), Ruwanwelisaya, Jetavanaramaya stupas.", "destinations", "anuradhapura ancient capital stupa bo tree sacred"),
    ("tell me about polonnaruwa", "Medieval capital ruins. Gal Vihara rock temple (stunning rock-carved Buddhas), Royal Palace, Parakrama Samudra lake. Great for cycling!", "destinations", "polonnaruwa medieval ruins gal vihara rock buddha"),
    ("tell me about arugam bay", "World-class surfing destination on the east coast! Best waves April-October. Laid-back vibe, beach bars, lagoon safaris, and Kumana National Park nearby.", "destinations", "arugam bay surfing east coast waves beach"),
    ("tell me about unawatuna", "Beautiful crescent-shaped beach near Galle. Great for swimming, snorkeling, diving (Japanese Peace Pagoda nearby). Coral reef and sea turtles!", "destinations", "unawatuna beach galle swimming snorkeling diving"),
    ("tell me about adams peak", "Sacred mountain (2,243m). Pilgrimage site for four religions. Famous sunrise hike — climb 5,500 steps! Season: December-May. Start climb at 2am.", "destinations", "adams peak sri pada sacred mountain sunrise climb pilgrimage"),

    # ==================== SAFETY ====================
    ("is sri lanka safe for tourists", "Yes, very safe! Friendly, hospitable people. Use normal precautions: watch belongings, use licensed transport, be careful with ocean currents on some beaches.", "safety", "safe safety danger crime tourist secure"),
    ("is sri lanka safe for solo travelers", "Very safe for solo travelers including women. Locals are helpful and welcoming. Stick to well-traveled routes and use reputable transport at night.", "safety", "solo travel safe alone single woman female"),
    ("are there any health concerns", "Drink bottled water, use mosquito repellent (dengue prevention), apply sunscreen. No mandatory vaccines; Hep A/B and Typhoid recommended.", "safety", "health medical hospital vaccine mosquito dengue water"),
    ("what are the emergency numbers in sri lanka", "Police: 119, Fire: 110, Ambulance: 1990, Tourist Police: 011-242-1052, Emergency (general): 112. Save these before your trip!", "safety", "emergency number police ambulance fire help"),
    ("is it safe to drink tap water in sri lanka", "No, drink bottled or filtered water only. Bottled water is cheap and available everywhere. Ice in tourist restaurants is usually safe.", "safety", "water drink tap bottled safe filtered"),

    # ==================== CULTURE & CUSTOMS ====================
    ("what language do they speak in sri lanka", "Sinhala and Tamil are official languages. English is widely spoken in tourist areas. Learn: 'Ayubowan' (hello), 'Istuti' (thank you), 'Kohomada' (how are you).", "culture", "language speak sinhala tamil english words"),
    ("what languages are spoken in sri lanka", "Sinhala (74%), Tamil (18%), and English (widely used in tourism, business, education). Most tourist areas have English-speaking staff.", "culture", "language spoken sinhala tamil english percentage"),
    ("what should i know about sri lankan culture", "Dress modestly at temples (cover shoulders/knees), remove shoes at religious sites, avoid pointing with fingers, use right hand for giving/receiving.", "culture", "culture custom tradition etiquette temple dress code respect"),
    ("what are the main religions in sri lanka", "Buddhism (~70%), Hinduism (~12%), Islam (~10%), Christianity (~7%). Beautiful temples, kovils, mosques, and churches across the island.", "culture", "religion buddhism hinduism islam christian temple"),
    ("what should i wear in sri lanka", "Light, breathable clothes for coast. Modest dress at temples (cover shoulders and knees). Light jacket for hill country. Comfortable shoes for hiking.", "culture", "wear clothes dress code pack clothing"),
    ("what are the dos and donts in sri lanka", "DO remove shoes at temples, dress modestly, ask before photographing people. DON'T point with finger, touch Buddha statues, turn your back to Buddha statues.", "culture", "dos donts etiquette rules respect behavior"),
    ("what is the national flag of sri lanka", "The Lion Flag — a golden lion holding a sword on a maroon background, with green and orange stripes representing minorities. One of the oldest flag designs.", "culture", "flag national lion symbol"),

    # ==================== ACTIVITIES & EXPERIENCES ====================
    ("can i go surfing in sri lanka", "Absolutely! Arugam Bay (east coast, Apr-Oct) is world-class. Hikkaduwa and Weligama (south coast, Nov-Apr) are great for beginners.", "activities", "surfing surf waves beach arugam bay hikkaduwa weligama"),
    ("what adventure activities are available", "Surfing, scuba diving, snorkeling, rock climbing, paragliding, white water rafting (Kitulgala), safari jeep tours, trekking, and zip-lining!", "activities", "adventure activity sport diving rafting trekking zipline"),
    ("can i see whales in sri lanka", "Yes! Mirissa (south coast, Nov-Apr) — blue whales and sperm whales. Trincomalee (east coast, Mar-Aug). One of the best whale watching spots globally!", "activities", "whale watching mirissa dolphin ocean marine"),
    ("where can i see elephants", "Udawalawe National Park (herds of 50+), Minneriya ('The Gathering' Jul-Oct — largest Asian elephant gathering), Pinnawala Elephant Orphanage.", "activities", "elephant safari park udawalawe minneriya pinnawala"),
    ("can i go diving in sri lanka", "Great diving! Hikkaduwa (coral reefs), Trincomalee (shipwrecks, HMS Hermes), Pigeon Island (marine life), Batticaloa. Best visibility: Nov-Apr south, Apr-Sep east.", "activities", "diving scuba snorkeling reef coral shipwreck underwater"),
    ("can i go hiking in sri lanka", "Excellent hiking! Ella Rock (3hrs), Little Adam's Peak (1hr), Horton Plains/World's End (9km), Adam's Peak (sunrise climb), Knuckles Mountain Range.", "activities", "hiking trekking walk trail mountain climb"),
    ("where can i go white water rafting", "Kitulgala is THE spot for white water rafting in Sri Lanka! Grade 3-4 rapids on the Kelani River. Also offers kayaking, canyoning, and jungle trekking.", "activities", "rafting white water kitulgala river adventure kayak"),
    ("can i see turtles in sri lanka", "Yes! Five of seven sea turtle species nest here. Visit turtle hatcheries in Kosgoda or Bentota. Rekawa Beach offers nighttime turtle watching (nesting season).", "activities", "turtle sea hatchery kosgoda bentota rekawa nesting"),
    ("best places for photography in sri lanka", "Nine Arches Bridge (Ella), Sigiriya sunrise, tea plantations, Galle Fort, Yala leopards, stilt fishermen (Koggala), temple ceremonies, train rides.", "activities", "photography photo camera instagram scenic beautiful spots"),
    ("what water sports can i do in sri lanka", "Surfing, snorkeling, scuba diving, whale watching, jet skiing, kayaking, stand-up paddleboarding, kitesurfing (Kalpitiya), and deep-sea fishing.", "activities", "water sports surfing diving snorkeling jet ski kayak"),

    # ==================== ACCOMMODATION ====================
    ("where should i stay in sri lanka", "Depends on budget! Hostels ($5-15), guesthouses ($15-30), boutique hotels ($40-100), luxury resorts ($150+). Popular: Colombo, Kandy, Ella, Galle, Unawatuna.", "accommodation", "stay hotel hostel resort guesthouse accommodation book"),
    ("are there luxury resorts in sri lanka", "Yes! Heritance Kandalama, Amanwella (Tangalle), Cape Weligama, Shangri-La Colombo, Jungle Beach by Uga Escapes. World-class luxury!", "accommodation", "luxury resort five star premium hotel high end"),
    ("are there budget hostels in sri lanka", "Many! Colombo, Ella, and Galle have great hostels ($5-15/night). Try Hangover Hostels, Clock Inn, or The Walrus. Book via Hostelworld or Booking.com.", "accommodation", "budget hostel cheap backpacker affordable dormitory"),
    ("can i do homestays in sri lanka", "Homestays are wonderful! Stay with local families, enjoy home-cooked meals, and experience authentic Sri Lankan culture. Available on Airbnb and Booking.com.", "accommodation", "homestay local family airbnb authentic experience"),

    # ==================== SHOPPING ====================
    ("what souvenirs can i buy in sri lanka", "Popular souvenirs: Ceylon tea, spices (cinnamon, cardamom), gemstones, batik fabric, wooden masks, ayurvedic products, elephant figurines, and handloom textiles.", "shopping", "souvenir buy gift shop purchase memento"),
    ("where to go shopping in sri lanka", "Colombo: Odel, Barefoot Gallery, Pettah Market. Kandy: Kandy City Centre. Galle: Fort boutiques. For gems: Ratnapura. For crafts: local village workshops.", "shopping", "shopping market mall store buy purchase"),
    ("is sri lanka known for gems", "Yes! Sri Lanka is called 'Ratna Dweepa' (Gem Island). Famous for blue sapphires, star sapphires, rubies, and cat's eye gems. Ratnapura is the gem capital.", "shopping", "gems gemstones sapphire ruby precious stones ratnapura"),
    ("can i buy spices in sri lanka", "Absolutely! Sri Lanka is the Spice Island. Buy: Ceylon cinnamon (world's finest!), cardamom, clove, nutmeg, pepper, and turmeric. Visit a spice garden in Matale.", "shopping", "spices cinnamon pepper buy spice garden matale"),

    # ==================== FESTIVALS & EVENTS ====================
    ("what festivals are celebrated in sri lanka", "Major festivals: Sinhala & Tamil New Year (April), Vesak (May — Buddha's birthday), Esala Perahera (July/Aug — Kandy), Thai Pongal (January), Christmas.", "festivals", "festival celebration event holiday cultural"),
    ("what is esala perahera", "The Kandy Esala Perahera is Sri Lanka's grandest Buddhist festival (July/August). 10 nights of spectacular processions with decorated elephants, dancers, and fire performers.", "festivals", "esala perahera kandy festival procession elephant"),
    ("what is vesak", "Vesak (May full moon) celebrates Buddha's birth, enlightenment, and passing. Streets are decorated with lanterns (vesak kudu), pandols, and free food stalls (dansala).", "festivals", "vesak buddha festival may lantern celebration"),
    ("when is sinhala and tamil new year", "April 13-14 every year. The biggest cultural celebration! Traditional games, special foods (kiribath, kokis, kavum), family gatherings, and village festivities.", "festivals", "new year april sinhala tamil celebration"),

    # ==================== AYURVEDA & WELLNESS ====================
    ("can i do ayurveda treatments in sri lanka", "Sri Lanka is an Ayurveda paradise! Many resorts offer authentic treatments: herbal massages, detox programs, yoga retreats. Popular in Bentota, Negombo, and Kandy.", "wellness", "ayurveda spa massage treatment wellness herbal"),
    ("are there yoga retreats in sri lanka", "Many! Popular spots: Unawatuna, Hiriketiya, Arugam Bay, and Kandy. Programs range from drop-in classes to multi-week retreats. All levels welcome.", "wellness", "yoga retreat meditation mindfulness wellness"),

    # ==================== HISTORY ====================
    ("what is the history of sri lanka", "Over 2,500 years of recorded history! Ancient kingdoms (Anuradhapura, Polonnaruwa), colonial periods (Portuguese, Dutch, British), independence in 1948.", "history", "history ancient kingdom colonial independence"),
    ("what are the unesco world heritage sites in sri lanka", "Eight UNESCO sites: Sigiriya, Dambulla, Kandy (Temple of Tooth), Galle Fort, Anuradhapura, Polonnaruwa, Sinharaja Forest, Central Highlands.", "history", "unesco world heritage site protected"),
    ("what is the sinharaja rainforest", "Sinharaja is Sri Lanka's last viable primary tropical rainforest — a UNESCO World Heritage Site. Home to 50% of Sri Lanka's endemic species. Great for birdwatching!", "history", "sinharaja rainforest unesco biodiversity endemic birds"),

    # ==================== PRACTICAL INFO ====================
    ("what is the time zone in sri lanka", "Sri Lanka Standard Time (SLST) is UTC+5:30. Same as India. No daylight saving time observed.", "practical", "time zone utc gmt hours difference"),
    ("what plug sockets does sri lanka use", "Type D and Type G sockets (same as UK/India). Voltage is 230V, 50Hz. Bring a universal adapter if visiting from the US/Europe.", "practical", "plug socket adapter charger electricity voltage"),
    ("is wifi available in sri lanka", "Yes! Most hotels, cafes, and restaurants offer free WiFi. Mobile data SIM cards from Dialog or Mobitel cost ~$5-10 for tourist packages with good 4G coverage.", "practical", "wifi internet data sim card mobile phone signal"),
    ("how to get a sim card in sri lanka", "Buy a tourist SIM at the airport or any Dialog/Mobitel shop. Costs ~$5-10 for calls + 10-20GB data. Bring your passport for registration. Takes 5 minutes!", "practical", "sim card phone data mobile dialog mobitel buy"),
    ("what is the capital of sri lanka", "Sri Lanka has two capitals: Sri Jayawardenepura Kotte (legislative capital) and Colombo (commercial/executive capital where most government offices are).", "practical", "capital city colombo kotte government"),
    ("how big is sri lanka", "Sri Lanka is 65,610 sq km — about the size of West Virginia (US) or slightly larger than Croatia. Despite its small size, it has incredible diversity!", "practical", "size area big small island square kilometers"),
    ("what is the population of sri lanka", "Approximately 22 million people. Ethnic composition: Sinhalese (~75%), Tamil (~15%), Moor (~9%), and others. One of South Asia's most diverse nations.", "practical", "population people ethnic sinhalese tamil moor"),

    # ==================== FAMILY & TYPES OF TRAVEL ====================
    ("is sri lanka good for family travel", "Perfect for families! Safe, friendly, affordable. Kids love: elephant safaris, train rides, beaches, turtle hatcheries, and Pinnawala Elephant Orphanage.", "travel_types", "family kids children travel friendly safe"),
    ("is sri lanka good for honeymoon", "Absolutely romantic! Beach resorts in Bentota/Tangalle, private villas in Galle, scenic Ella, luxury train cabins, candlelit dinners, and couples' spa treatments.", "travel_types", "honeymoon romantic couples love wedding anniversary"),
    ("is sri lanka good for solo travel", "One of the best in Asia for solo travelers! Safe, easy to navigate, affordable, friendly locals. Great backpacker infrastructure and easy to meet other travelers.", "travel_types", "solo travel alone single backpacker independent"),
    ("how many days do i need in sri lanka", "Minimum 7-10 days for highlights. 2 weeks is ideal to cover cultural triangle, hill country, and beaches without rushing. 3+ weeks for a comprehensive trip.", "travel_types", "days duration length trip itinerary weeks plan"),
    ("what is the best itinerary for sri lanka", "Classic 10-day route: Colombo → Sigiriya → Kandy → Nuwara Eliya → Ella (train!) → Yala → Mirissa/Galle → Colombo. Covers culture, nature, wildlife, and beaches!", "travel_types", "itinerary route plan schedule day trip"),

    # ==================== NATURE & WILDLIFE ====================
    ("what wildlife can i see in sri lanka", "Leopards (Yala), elephants (Udawalawe/Minneriya), blue whales (Mirissa), sloth bears, crocodiles, 400+ bird species, sea turtles, and dolphins!", "wildlife", "wildlife animals birds species nature biodiversity"),
    ("what national parks are in sri lanka", "Major parks: Yala (leopards), Udawalawe (elephants), Minneriya (elephant gathering), Wilpattu (oldest park), Horton Plains (hiking), Sinharaja (rainforest).", "wildlife", "national park safari reserve protected nature"),
    ("is sri lanka good for birdwatching", "Excellent! 400+ species including 34 endemics. Best spots: Sinharaja, Kitulgala, Bundala, Yala, and Horton Plains. Nov-Apr also has migratory birds.", "wildlife", "bird watching birding species endemic ornithology"),
    ("what is the gathering in minneriya", "The Gathering (Jul-Oct) at Minneriya National Park — the largest Asian elephant congregation! Up to 300 elephants gather around the Minneriya Tank. Truly spectacular.", "wildlife", "gathering minneriya elephant herd migration spectacular"),

    # ==================== ALTERNATE PHRASINGS (improve matching) ====================
    # Visa
    ("can i enter sri lanka without a visa", "Most nationalities need an ETA (Electronic Travel Authorization). Apply online at srilankaeta.gov.lk. Some nationalities may qualify for visa-free entry — check the official site.", "visa", "enter without visa free eta required"),
    ("what is the eta for sri lanka", "ETA is the Electronic Travel Authorization — Sri Lanka's online visa system. Apply at srilankaeta.gov.lk, costs ~$50 USD, and is processed within 24 hours.", "visa", "eta electronic travel authorization online"),
    # Weather
    ("is sri lanka hot", "Yes, coastal areas are warm (27-30°C year-round). Hill country is cooler (15-20°C). Pack light breathable clothing for the coast and a jacket for the hills.", "weather", "hot warm temperature heat humid"),
    ("when is monsoon season in sri lanka", "Southwest monsoon: May-September (affects west/south coast). Northeast monsoon: October-January (affects east coast). Always one dry coast to enjoy!", "weather", "monsoon season rain wet dry wind"),
    # Transport
    ("is it safe to drive in sri lanka", "Driving can be challenging due to narrow roads and local driving habits. Hiring a driver ($40-60/day) is highly recommended over self-driving.", "transport", "drive safe road car dangerous"),
    ("how long does it take from colombo to galle", "About 2-3 hours by car via the Southern Expressway. The coastal road takes 3-4 hours but is more scenic. Buses and trains also available.", "transport", "colombo galle time distance drive hours"),
    # Food
    ("what is string hoppers", "String hoppers (idiyappam) are steamed rice noodle nests, served for breakfast or dinner with curry and coconut sambol. A beloved Sri Lankan staple!", "food", "string hoppers idiyappam noodle rice breakfast"),
    ("what is lamprais", "Lamprais is a Dutch-Burgher dish — rice cooked in stock, wrapped in banana leaf with curries, cutlet, and sambol, then baked. A unique Sri Lankan delicacy!", "food", "lamprais banana leaf dutch burgher rice baked"),
    ("what is pol sambol", "Pol Sambol is a spicy coconut relish made with freshly scraped coconut, chili flakes, lime, onion, and Maldive fish. Essential accompaniment to any Sri Lankan meal!", "food", "pol sambol coconut relish condiment spicy"),
    ("what should i not eat in sri lanka", "Avoid uncooked food from street stalls, tap water, and raw salads at budget eateries. Stick to freshly cooked hot food and bottled water.", "food", "avoid food safe stomach sick hygiene"),
    # Destinations
    ("where should i go in sri lanka", "Top destinations: Sigiriya (ancient fortress), Kandy (cultural capital), Ella (hill country charm), Galle (colonial fort), Yala (wildlife), Mirissa (beaches & whales).", "destinations", "where go place visit best top recommend"),
    ("what are the must visit places in sri lanka", "Must-visits: 1. Sigiriya Rock 2. Kandy Temple 3. Ella train ride 4. Galle Fort 5. Yala Safari 6. Mirissa beaches 7. Nuwara Eliya tea country 8. Dambulla Cave Temple.", "destinations", "must visit top places best destinations essential"),
    ("what is the most beautiful place in sri lanka", "Subjective, but Ella, Nine Arches Bridge, Sigiriya at sunrise, Galle Fort at sunset, and the Kandy-Ella train ride are consistently rated the most breathtaking.", "destinations", "beautiful scenic stunning gorgeous amazing view"),

    # ==================== GEOGRAPHY ====================
    ("how many provinces are there in sri lanka", "Sri Lanka has 9 provinces: Western, Central, Southern, Northern, Eastern, North Western, North Central, Uva, and Sabaragamuwa.", "geography", "provinces districts regions administrative nine"),
    ("how many districts are there in sri lanka", "Sri Lanka has 25 districts spread across 9 provinces. Each district has its own administrative structure and unique cultural characteristics.", "geography", "districts administrative divisions twenty five"),
    ("what are the major cities in sri lanka", "Major cities: Colombo (commercial capital), Kandy (cultural capital), Galle (southern heritage), Jaffna (northern capital), Negombo, Trincomalee, Batticaloa, and Nuwara Eliya.", "geography", "cities major towns urban"),
    ("what is the highest point in sri lanka", "Pidurutalagala (Mount Pedro) at 2,524m is the highest point. It's a military zone and not open to hikers. Adam's Peak (2,243m) is the most famous climbable peak.", "geography", "highest point mountain peak elevation tallest"),
    ("what are the major rivers in sri lanka", "Main rivers: Mahaweli (longest, 335km), Kelani, Kalu, Walawe, and Deduru. The Mahaweli River is crucial for irrigation and hydroelectric power.", "geography", "river rivers mahaweli kelani water longest"),
    ("is sri lanka an island", "Yes! Sri Lanka is an island nation in the Indian Ocean, southeast of India. It's connected to India by a chain of limestone shoals called Adam's Bridge.", "geography", "island country location indian ocean map"),
    ("what continent is sri lanka in", "Sri Lanka is in Asia, specifically South Asia. It's an island nation in the Indian Ocean, separated from India by the Palk Strait (about 30km).", "geography", "continent asia south location"),

    # ==================== BEACHES ====================
    ("what are the best beaches in sri lanka", "Top beaches: Unawatuna (swimming), Mirissa (whale watching), Tangalle (secluded), Nilaveli (pristine), Arugam Bay (surfing), Bentota (water sports), Hikkaduwa (snorkeling).", "beaches", "beach best top beautiful swimming sand coast"),
    ("which beach is best for swimming", "Unawatuna has a calm crescent bay perfect for swimming. Bentota and Nilaveli are also great. Always check for currents — some south coast beaches have strong undertow.", "beaches", "swimming beach safe calm waves family"),
    ("which beach is best for surfing", "Arugam Bay (east coast) is world-class for advanced surfers. Weligama and Hikkaduwa (south coast) are perfect for beginners. Season: Nov-Apr south, Apr-Oct east.", "beaches", "surfing beach waves best beginner advanced"),
    ("are there private beaches in sri lanka", "Most beaches are public. Some luxury resorts (Amanwella, Cape Weligama, Jungle Beach) have semi-private stretches. But even budget travelers enjoy beautiful uncrowded beaches!", "beaches", "private beach resort exclusive secluded"),

    # ==================== TEA ====================
    ("where can i visit tea plantations", "Best areas: Nuwara Eliya (Mackwoods, Pedro Estate), Ella (Lipton's Seat), and Haputale. Most estates offer factory tours with tea tasting for a small fee.", "tea", "tea plantation factory visit tour estate"),
    ("what is ceylon cinnamon", "Ceylon cinnamon (true cinnamon) is native to Sri Lanka and considered the world's finest. It's lighter, sweeter, and more delicate than cassia cinnamon. A premium export!", "tea", "cinnamon ceylon spice true quality"),
    ("can i buy tea directly from estates", "Yes! Most tea factories have shops where you can buy fresh tea at lower prices. Mackwoods, Mlesna, Dilmah, and Pedro are popular brands with estate shops.", "tea", "buy tea estate factory shop brand"),

    # ==================== MEDICAL & HEALTH ====================
    ("are there good hospitals in sri lanka", "Yes! Major cities have good hospitals. Private hospitals: Asiri, Nawaloka, Lanka (Colombo). Government hospitals are free. Travel insurance with medical coverage is recommended.", "medical", "hospital medical doctor healthcare clinic"),
    ("do i need vaccinations for sri lanka", "No mandatory vaccinations, but recommended: Hepatitis A & B, Typhoid, and Tetanus. Bring mosquito repellent for dengue prevention. Consult your doctor before travel.", "medical", "vaccination vaccine immunization injection shot"),
    ("is malaria a risk in sri lanka", "Sri Lanka was declared malaria-free by WHO in 2016! However, dengue fever exists — use mosquito repellent, especially during rainy seasons.", "medical", "malaria dengue mosquito disease fever risk"),
    ("where can i find a pharmacy in sri lanka", "Pharmacies are widely available in all towns and cities. Major chains include Healthguard and SP Pharmacy. Many medications available without prescription.", "medical", "pharmacy medicine drug chemist medication"),

    # ==================== NIGHTLIFE & ENTERTAINMENT ====================
    ("is there nightlife in sri lanka", "Colombo has the best nightlife: rooftop bars (Sky Lounge), clubs (Cleopatra), and beach bars. Hikkaduwa, Unawatuna, and Mirissa have lively beach bar scenes.", "nightlife", "nightlife bar club party dance evening"),
    ("are there casinos in sri lanka", "Yes, Colombo has several casinos: Bally's, Bellagio (MGM), and Marina Colombo. They're open to foreigners. Dress code applies. Entry requires a passport.", "nightlife", "casino gambling gaming bet"),
    ("what is the drinking age in sri lanka", "The legal drinking age is 21. Alcohol is sold in licensed shops, hotels, and restaurants. Poya (full moon) days are dry days — no alcohol sold publicly.", "nightlife", "drinking age alcohol legal beer wine"),

    # ==================== DAY TRIPS ====================
    ("best day trips from colombo", "Top day trips: Negombo (fishing village, 1hr), Galle Fort (2hrs), Sigiriya (4hrs early start), Kandy (3hrs), Pinnawala Elephants (2.5hrs), Bentota Beach (2hrs).", "day_trips", "day trip colombo short excursion"),
    ("best day trips from kandy", "From Kandy: Sigiriya & Dambulla (3hrs), Pinnawala Elephant Orphanage (1.5hrs), Nuwara Eliya (2.5hrs), Knuckles Mountain Range (2hrs), Mahiyanganaya (3hrs).", "day_trips", "day trip kandy short excursion nearby"),
    ("best day trips from ella", "From Ella: Nine Arches Bridge (walk), Ella Rock hike (3hrs), Little Adam's Peak (1hr), Ravana Falls (10min), Udawalawe Safari (2hrs), Lipton's Seat (1.5hrs).", "day_trips", "day trip ella short excursion nearby hike"),

    # ==================== ETIQUETTE & TIPS ====================
    ("how to greet someone in sri lanka", "Say 'Ayubowan' (ah-yu-bo-wan) with palms together — it means 'may you live long.' For Tamil speakers, say 'Vanakkam.' A warm smile is always appreciated!", "etiquette", "greet greeting hello ayubowan vanakkam"),
    ("can i take photos at temples", "Photography is usually allowed in temple grounds but often prohibited inside shrine rooms. Never pose with your back to a Buddha statue. Always ask permission first.", "etiquette", "photo temple photograph camera allowed rules"),
    ("is bargaining acceptable in sri lanka", "Yes, in markets, tuk-tuks, and street vendors — bargaining is expected! Start at 50-60% of the asking price. Fixed prices at malls, supermarkets, and restaurants.", "etiquette", "bargain negotiate price haggle market"),
    ("what should i not do in sri lanka", "Don't: touch someone's head, point with your finger, show the soles of your feet, pose with Buddha statues, wear shoes in temples, or feed wild animals.", "etiquette", "avoid rude offensive forbidden taboo wrong"),

    # ==================== PACKING & PREPARATION ====================
    ("what should i pack for sri lanka", "Essentials: light breathable clothes, swimwear, sunscreen SPF50+, mosquito repellent, comfortable walking shoes, rain jacket, universal power adapter, and a light jacket for hills.", "packing", "pack list clothes bring luggage suitcase"),
    ("do i need a rain jacket in sri lanka", "Yes! Brief tropical showers can happen anytime. A lightweight, packable rain jacket is more practical than an umbrella, especially for hiking.", "packing", "rain jacket umbrella waterproof wet weather"),
    ("what medicine should i bring to sri lanka", "Bring: personal prescriptions, anti-diarrhea tablets, rehydration salts, paracetamol, mosquito repellent (DEET), sunscreen, plasters, and any allergy medication.", "packing", "medicine first aid kit health tablets pills"),

    # ==================== DIGITAL NOMAD & TECH ====================
    ("is sri lanka good for digital nomads", "Yes! Great climate, affordable living, and friendly locals. South coast towns like Hiriketiya, Midigama, and Weligama are massive digital nomad hubs with strong communities.", "digital_nomad", "digital nomad remote work telecommute hub"),
    ("are there coworking spaces in colombo", "Colombo has several excellent coworking spaces with reliable fiber-optic internet, backup generators, and networking events. Popular spots include Hatch Works and Likuid Spaces.", "digital_nomad", "coworking space office desk remote work hatch"),
    ("how fast is the internet in sri lanka", "Mobile 4G data is cheap and reliable in most areas. Fixed fiber-optic broadband in cities and coworking spaces is fast, often reaching 50-100 Mbps.", "digital_nomad", "internet speed wifi connection broadband mbps"),
    ("what is the tech scene like in sri lanka", "Sri Lanka has a growing tech and software development sector, with many full-stack developers and AI startups based in Colombo. Coworking spaces frequently host tech meetups.", "digital_nomad", "tech scene software developers startups networking ai"),
    ("do they have a digital nomad visa", "Sri Lanka introduced a 1-year digital nomad visa designed for remote workers, requiring proof of a minimum monthly income. Standard tourist ETAs can also be extended.", "digital_nomad", "digital nomad visa extend remote work stay"),

    # ==================== HEALTHCARE & MEDICAL ====================
    ("what is the quality of healthcare in sri lanka", "Sri Lanka has a robust healthcare system. Private hospitals in Colombo offer excellent, internationally accredited care. Government hospitals provide free care but can be crowded.", "medical", "healthcare quality hospitals system care doctor"),
    ("where are the best trauma centers", "The National Hospital of Sri Lanka in Colombo has the primary trauma center. Major private hospitals like Asiri Surgical and Nawaloka also operate excellent emergency response units.", "medical", "trauma emergency hospital accident care center injury"),
    ("can foreigners use government hospitals", "Yes, foreigners can access government hospitals in an emergency. However, most tourists prefer private hospitals in Colombo or Kandy for faster service, English-speaking staff, and more comfort.", "medical", "government public hospital foreigner access emergency"),
    ("how to see a doctor in sri lanka", "You can easily channel (book) a specialist at any private hospital via the 'eChannelling' or 'Doc990' mobile apps. Walk-in outpatient departments (OPD) are also widely available.", "medical", "doctor see channel book appointment opd app"),
    ("can i buy antibiotics over the counter", "Many pharmacies will sell basic antibiotics without a prescription, but it is highly recommended to consult a doctor first. Always check expiration dates on purchased medication.", "medical", "antibiotics pharmacy counter prescription medicine pill"),

    # ==================== FITNESS & GYMS ====================
    ("are there gyms in sri lanka", "Yes, major cities like Colombo, Kandy, and Galle have well-equipped commercial gyms. High-end hotels also offer fitness centers. Day and weekly passes are usually available for tourists.", "fitness", "gym fitness workout weights exercise facility"),
    ("can i buy protein powder in sri lanka", "Yes, supplement stores in Colombo and major cities sell imported whey protein, but it can be expensive due to import taxes. It's often cheaper to bring your own supply in your luggage.", "fitness", "protein powder supplements bodybuilding nutrition gym"),
    ("how to maintain muscle while traveling in sri lanka", "Stick to protein-rich local foods like chicken curry, boiled eggs, and fresh seafood. Utilize hotel gyms, or try bodyweight calisthenics on the beach.", "fitness", "muscle fitness physique healthy eat protein maintain"),
    ("are there outdoor workout parks", "Galle Face Green in Colombo and various beachside areas have basic calisthenics bars. Swimming, surfing, and hiking are also excellent ways to stay active during your trip.", "fitness", "outdoor workout calisthenics park active run"),

    # ==================== VEHICLE RENTAL & DRIVING ====================
    ("how to rent a car in sri lanka", "You can rent cars from local agencies or international brands in Colombo. You MUST have your International Driving Permit (IDP) endorsed by the Automobile Association of Ceylon (AA) before driving.", "transport", "rent car hire drive self vehicle idp aa"),
    ("how to check a rental car for damage", "Before accepting a rental, take a continuous video of the car's exterior, interior, and undercarriage. Document all scratches, dents, and the fuel level to avoid disputes upon return.", "transport", "rental damage inspect check scratch insurance claim"),
    ("what happens if i damage a rental car", "Most reputable rentals include comprehensive insurance, but check the deductible. Always request a police report if involved in an accident, as the rental company's insurance will require it.", "transport", "damage accident rental car insurance claim crash"),
    ("are there vintage car tours in colombo", "Yes! You can book classic car city tours in Colombo, often featuring beautifully restored vintage British cars, offering a highly photogenic way to see the city's colonial architecture.", "transport", "vintage classic car tour automotive ride old"),
    ("how to rent a scooter in sri lanka", "Scooters are easily rented in beach towns (approx $5-8/day). Wear a helmet (it's the law!), carry your international license, and drive defensively, as local traffic can be unpredictable.", "transport", "rent scooter bike motorcycle hire ride helmet"),

    # ==================== DEEP DIVE: FOOD ====================
    ("what is isso wade", "Isso Wade are deep-fried lentil patties topped with whole spicy prawns. It's the ultimate Sri Lankan street food, best enjoyed hot at Galle Face Green in Colombo at sunset.", "food", "isso wade prawn lentil street food galle face snack"),
    ("what is watalappam", "A traditional Sri Lankan Malay dessert. It's a rich, steamed coconut custard made with dark kithul jaggery, coconut milk, eggs, cardamom, and nutmeg. Incredibly delicious!", "food", "watalappam dessert sweet pudding jaggery coconut"),
    ("what is kithul treacle", "Kithul is a sweet, smoky syrup tapped from the fishtail palm tree, similar to maple syrup. It's traditionally poured over fresh buffalo curd for a classic local dessert.", "food", "kithul treacle syrup sweet curd honey palm"),
    ("what is achcharu", "Achcharu is Sri Lankan street pickle. It's a sweet, sour, and intensely spicy mix of fruits like raw mango, pineapple, or ambarella tossed in chili powder, sugar, salt, and vinegar.", "food", "achcharu pickle fruit spicy street food sour mango"),
    ("what is a dansala", "During Vesak or Poson Poya days, locals set up 'dansalas' — free food stalls offering full meals, ice cream, or drinks to anyone passing by as an act of Buddhist merit.", "food", "dansala free food vesak poya charity merit festival"),
    ("what is thambili", "Thambili is the bright orange King Coconut, native to Sri Lanka. Vendors slice them open on the street for you to drink the naturally sweet, electrolyte-rich water. Perfect for hydration!", "food", "thambili king coconut water drink hydrate orange"),

    # ==================== SCAMS & ANNOYANCES ====================
    ("what is the spice garden scam", "Tuk-tuk drivers may take you to a 'spice garden' for a free tour. The tour is educational, but the natural medicines and creams sold at the end are heavily overpriced.", "scams", "spice garden scam overpriced trap tourist fake"),
    ("stilt fishermen photo fee", "Stilt fishing is a traditional practice in the south, but today, many 'fishermen' pose purely for tourists and will aggressively demand a fee (often around 1000 LKR) if you take their photo.", "scams", "stilt fishermen photo fee money scam koggala pay"),
    ("tuk tuk meter scam", "Always ask a tuk-tuk to use the meter ('meter eka danna'). If they refuse or say it's broken, negotiate the price BEFORE getting in, or use ride-hailing apps like PickMe.", "scams", "tuk tuk scam meter price negotiate app broken"),
    ("what is the temple shoe scam", "At some temples, locals outside the gates might demand a high fee to 'watch' your shoes. Ignore them and leave your shoes at the official temple counter, which usually costs just 50-100 LKR.", "scams", "temple shoes scam fee watch footwear fake guard"),

    # ==================== DEEP DIVE: DESTINATIONS ====================
    ("tell me about haputale", "A misty, quiet hill town surrounded by sheer drops and tea estates. Less touristy than Ella. Famous for Lipton's Seat, where Sir Thomas Lipton used to survey his tea empire.", "destinations", "haputale hill country tea liptons seat quiet mist"),
    ("tell me about tangalle", "Located on the deep south coast. Known for long, pristine, palm-fringed beaches and a more relaxed, secluded vibe compared to the busy party towns of Mirissa or Unawatuna.", "destinations", "tangalle beach south coast quiet secluded calm"),
    ("tell me about kalpitiya", "A sandy peninsula on the northwest coast. It is one of the best kite-surfing destinations in the world (May-Oct season) and a fantastic spot to take boat tours to see large pods of dolphins.", "destinations", "kalpitiya kitesurfing kite dolphin beach peninsula west"),
    ("tell me about pidurangala", "A massive rock formation right next to Sigiriya. Hiking Pidurangala at sunrise offers the most iconic, breathtaking view OF Sigiriya rock itself. It has a cheaper entry fee and fewer crowds!", "destinations", "pidurangala rock hike view sigiriya sunrise cheaper"),
    ("tell me about badulla", "The terminus of the famous highland railway. Visit the ancient Muthiyangana Temple and the impressive Dunhinda Falls, one of Sri Lanka's most beautiful and powerful waterfalls.", "destinations", "badulla train waterfall dunhinda hill country end"),

    # ==================== DEEP DIVE: SURFING ====================
    ("surfing in hiriketiya", "A stunning horseshoe bay on the south coast. Great for all levels. Has a sandy beach break perfect for beginners and a left-hand reef break for advanced surfers. Vibe is very trendy.", "activities", "hiriketiya surf bay beginner advanced waves south trendy"),
    ("surfing in midigama", "The heart of south coast surf culture. Famous for multiple high-quality reef breaks like Lazy Left, Lazy Right, and Rams. Best suited for intermediate to advanced surfers.", "activities", "midigama surf waves reef break advanced intermediate lazy"),
    ("where to rent a surfboard in sri lanka", "Surfboard rentals are everywhere on the south and east coast beaches. Expect to pay around 1000-1500 LKR for a few hours. Many beach shacks also offer ding repairs and wax.", "activities", "rent surfboard hire shop cost repair wax board"),

    # ==================== DEEP DIVE: HIKING ====================
    ("what is the pekoe trail", "A newly established 300km, 22-stage long-distance walking trail through Sri Lanka's central highlands, winding through historic tea trails, pine forests, and remote mountain villages.", "activities", "pekoe trail hike walk long distance tea highlands"),
    ("hiking the knuckles mountain range", "A UNESCO World Heritage site offering rugged, off-the-beaten-path trekking. Weather changes fast and paths are unmarked. Hiring a local guide is strictly required due to dense, confusing forests.", "activities", "knuckles mountain range hike trek guide nature unesco"),
    ("do i need a guide for adams peak", "No, the main trail (Hatton route) is completely paved with steps, highly trafficked, and well-lit during the pilgrimage season (Dec-May). Just follow the crowd and the lights to the summit!", "activities", "adams peak guide hike steps solo alone pilgrimage light"),
    ("can i hike in horton plains without a guide", "Yes, the 9km loop to World's End and Baker's Falls is a clearly marked, relatively flat path. Guides are not necessary, but arrive by 6 AM before the heavy mist rolls in and ruins the view.", "activities", "horton plains hike world end guide solo flat early"),

    # ==================== DEEP DIVE: TRANSPORTATION ====================
    ("what is 1st class train travel like", "1st class (Observation Car or AC Intercity) has comfortable, reserved seating with air conditioning. However, the windows are sealed shut, making it harder to lean out and take iconic photos.", "transport", "1st class train ac comfortable reserve ticket windows closed"),
    ("what is 2nd class train travel like", "2nd class has padded seats and ceiling fans. Windows open fully, making it the best option for feeling the breeze and taking photos. You can book reserved 2nd class seats in advance.", "transport", "2nd class train windows open photo reserve breeze"),
    ("how to book train tickets in advance", "You can book tickets online via the official Sri Lanka Railways website or the 'Seat Reservation' app. Tickets for popular routes (like Kandy to Ella) sell out weeks in advance, so book early!", "transport", "book train ticket advance online reserve early website"),
    ("can i take a surfboard on the train", "Yes, you can take surfboards on trains and buses. On trains, put them in the luggage carriage. On buses, you may need to pay a small extra luggage fee or buy an extra seat to accommodate it.", "transport", "surfboard train bus transport luggage fee carry"),

    # ==================== PHOTOGRAPHY & DRONES ====================
    ("can i fly a drone in sri lanka", "Yes, but it requires prior approval. You must register your drone with the Civil Aviation Authority of Sri Lanka (CAASL) and get clearance from the Ministry of Defence before flying.", "photography", "drone fly rules caasl aerial photography law legal"),
    ("how to register a drone in sri lanka", "Apply online through the CAASL website at least 2 weeks before arrival. You'll need to submit your drone's specifications, your passport copy, and intended flight locations.", "photography", "register drone caasl approval process form apply advance"),
    ("where are drones banned in sri lanka", "Strictly prohibited near airports, military bases, government buildings in Colombo, and over highly populated areas, national parks (without special wildlife permits), or sacred sites.", "photography", "drone ban illegal no fly zone restricted temple park"),
    ("photography rules at sigiriya", "You can take photos around the gardens and on the climb, but photography is STRICTLY PROHIBITED inside the cave containing the ancient Sigiriya Frescoes to preserve the delicate paint.", "photography", "photography sigiriya rules frescoes allowed banned illegal"),

    # ==================== SUSTAINABLE & ACCESSIBLE TRAVEL ====================
    ("is sri lanka wheelchair accessible", "Accessibility is improving but remains challenging. Sidewalks can be uneven, and public transport is not wheelchair friendly. However, many modern luxury hotels are fully accessible.", "accessibility", "wheelchair accessible disability mobility access disabled friendly"),
    ("are there eco friendly hotels in sri lanka", "Yes, Sri Lanka is a pioneer in eco-tourism. Look for hotels by Jetwing or Heritance, which heavily invest in solar power, wastewater recycling, and local community support.", "sustainable", "eco friendly sustainable green hotel environment solar recycle"),
    ("ethical elephant experiences in sri lanka", "Avoid places offering elephant rides. For ethical encounters, visit national parks like Udawalawe to see them in the wild, or the Elephant Transit Home, which rehabilitates orphaned calves.", "sustainable", "ethical elephant ride wildlife conservation cruelty free orphanage"),

    # ==================== LOCAL CUSTOMS & ETIQUETTE ====================
    ("what is a poya day", "Every full moon is a public holiday (Poya) in Sri Lanka, which is deeply significant for Buddhists. Banks and businesses may close, and the sale of meat and alcohol is strictly prohibited.", "culture", "poya day full moon holiday alcohol closed meat"),
    ("can i buy alcohol on poya days", "No, it is illegal to sell alcohol on Poya days, even in high-end hotels and supermarkets. If you want a drink, you must purchase and stock up the day before.", "culture", "alcohol poya buy drink illegal ban stock up"),
    ("what is the right hand rule", "In Sri Lankan culture, the left hand is historically considered unclean. Always use your right hand to eat your food, hand over money, or give and receive items out of respect.", "culture", "right hand rule eat give respect etiquette clean polite"),

    # ==================== NICHE SHOPPING ====================
    ("how to buy gems safely in sri lanka", "Buy only from licensed jewelers authorized by the National Gem and Jewellery Authority. Always ask for a printed certificate of authenticity. Avoid buying gems from street touts or tuk-tuk drivers.", "shopping", "buy gems safe certificate authentic sapphire fake tout authority"),
    ("what are sri lankan masks", "Traditional wooden masks carved from light Kaduru wood, primarily made in the coastal town of Ambalangoda. They are used in healing rituals (Kolam), dances, and as protective talismans.", "shopping", "mask wooden ambalangoda traditional carve souvenir kolam devil"),
    ("what is sri lankan batik", "A traditional fabric art using complex wax-resist dyeing techniques. You can buy beautiful, colorful batik sarongs, dresses, and wall hangings. You can also visit workshops in Kandy or Galle to see the process.", "shopping", "batik fabric clothes dye traditional art sarong wax color"),

    # ==================== WATERFALLS ====================
    ("what is the tallest waterfall in sri lanka", "Bambarakanda Falls is the tallest at 263 meters (863 feet). It's located in the Kalupahana area. The hike to the base is surrounded by beautiful pine forests and is best visited between March and May.", "waterfalls", "tallest waterfall bambarakanda highest drop kalupahana pine forest"),
    ("tell me about diyaluma falls", "Diyaluma is Sri Lanka's 2nd tallest waterfall (220m). The real magic is hiking to 'Upper Diyaluma' where you'll find a series of natural infinity pools right at the edge of the cliff. A must-do in the Badulla region!", "waterfalls", "diyaluma upper waterfall natural pools infinity cliff hike"),
    ("where is ravana falls", "Ravana Falls is located just a 10-minute drive from Ella town on the main road. It's incredibly easy to access, tied to the Ramayana legend, and very popular for a quick photo stop.", "waterfalls", "ravana falls ella road accessible ramayana legend easy stop"),
    ("what is the little niagara of sri lanka", "St. Clair's Falls is known as the 'Little Niagara of Sri Lanka'. It's incredibly wide and drops through lush green tea estates. You can view it easily from the Hatton-Talawakele main road.", "waterfalls", "st clair little niagara wide tea estate hatton talawakele view"),
    ("tell me about devon falls", "Named after a pioneer English coffee planter, Devon Falls is a striking 97-meter drop. You can get a great view of it from a dedicated viewpoint on the A7 highway near Dimbula.", "waterfalls", "devon falls planter dimbula viewpoint highway drop a7"),
    ("what is bakers falls", "Baker's Falls is a beautiful, wide waterfall located right on the hiking trail inside Horton Plains National Park. It's a perfect resting spot on your way to or from the World's End cliff.", "waterfalls", "baker falls horton plains hike national park trail world end resting"),
    ("where are ramboda falls", "Ramboda Falls is a stunning 109-meter waterfall located in the Pussellawa area, between Kandy and Nuwara Eliya. There is a great viewing deck at the Ramboda Falls Hotel.", "waterfalls", "ramboda pussellawa kandy nuwara eliya view deck hotel drop"),

    # ==================== OFF-THE-BEATEN-PATH DESTINATIONS ====================
    ("tell me about ambuluwawa tower", "Located in Gampola, Ambuluwawa is a biodiversity complex featuring a massive, spiraling white tower. Climbing the narrow spiral staircase to the top offers incredible 360-degree views, but it's not for those afraid of heights!", "destinations", "ambuluwawa tower gampola spiral stairs height views biodiversity"),
    ("is delft island worth visiting", "Yes, if you love remote adventure! Located off the coast of Jaffna, Delft Island (Neduntheevu) features wild horses left by the Dutch, ruins of a coral fort, and a giant Baobab tree. You need to take a ferry to get there.", "destinations", "delft island jaffna ferry wild horses dutch fort baobab remote"),
    ("tell me about mannar", "Mannar Island is in the northwest. It's famous for its ancient baobab trees, the historic Mannar Fort, wild donkeys, and being a major destination for migratory birds like flamingos in the winter.", "destinations", "mannar island baobab fort birds flamingo northwest donkeys"),
    ("what is ritigala", "Ritigala is an ancient Buddhist monastery hidden inside a strict nature reserve in the Cultural Triangle. It features beautiful stone paths winding through a dense, misty jungle. Very quiet and mystical.", "destinations", "ritigala monastery ruins jungle cultural triangle quiet mystical nature"),
    ("what is the rose quartz mountain", "Jathika Namal Uyana is the largest pink quartz mountain in South Asia, located near Dambulla. It is surrounded by an ancient ironwood forest. A highly unique geological and historical site.", "destinations", "rose quartz mountain jathika namal uyana pink ironwood dambulla forest"),
    ("tell me about riverston", "Riverston is a stunning, windy peak in the Knuckles Mountain Range. Nearby, you can visit 'Pitawala Pathana' (a unique grassland with a sheer cliff drop) and Sera Ella waterfall. Great for nature lovers.", "destinations", "riverston knuckles pitawala pathana grassland windy misty peak cliff"),
    ("what is mihintale", "Mihintale is a mountain peak near Anuradhapura, believed to be the meeting site where Buddhism was introduced to Sri Lanka. Climbing the grand stone stairway at sunset is a magical experience.", "destinations", "mihintale anuradhapura buddhism mountain stairs sunset sacred temple"),
    ("what is kataragama", "Kataragama is a deeply sacred pilgrimage town in the south. The main temple complex is visited by Buddhists, Hindus, Muslims, and the indigenous Vedda people. It is a brilliant display of religious harmony.", "destinations", "kataragama sacred pilgrimage temple multi religion harmony south puja"),
    ("can i visit the lotus tower", "Yes! The Colombo Lotus Tower is the tallest freestanding structure in South Asia. For a ticket fee, you can take the elevator to the observation deck for spectacular panoramic views of the city and coastline.", "destinations", "lotus tower colombo observation deck views tall structure ticket"),

    # ==================== VIEWPOINTS & LANDMARKS ====================
    ("what is liptons seat", "Located in Haputale, it's the spectacular viewpoint where Sir Thomas Lipton used to survey his vast tea plantations. Get there before 9 AM, or the rising mist will completely block the view!", "viewpoints", "liptons seat haputale tea viewpoint sir thomas mist early morning"),
    ("what is worlds end", "World's End is a sheer precipice with a 4,000-foot drop located in Horton Plains National Park. The 9km loop hike offers breathtaking views of the valley below, provided you arrive early before the clouds roll in.", "viewpoints", "worlds end horton plains drop cliff hike precipice view mist"),
    ("what is the nine arches bridge", "A marvel of colonial engineering in Ella, built entirely of brick, rock, and cement with no steel. Wait for a train to cross for the perfect photo! It's accessible via a short hike from Ella town.", "viewpoints", "nine arches bridge ella train colonial brick photo spot viaduct"),

    # ==================== HOTEL & ACCOMMODATION TYPES ====================
    ("can i stay in a tea estate", "Absolutely! The hill country (Nuwara Eliya, Hatton, Ella) has many restored colonial tea planter bungalows. Places like Ceylon Tea Trails offer ultra-luxury, all-inclusive experiences with private butlers.", "hotels", "tea estate bungalow planter colonial luxury trails hatton stay"),
    ("are there glamping options in sri lanka", "Yes! Glamping (glamorous camping) is incredibly popular near national parks like Yala, Wilpattu, and Udawalawe. Stay in luxury canvas tents with comfortable beds, en-suite bathrooms, and BBQ dinners under the stars.", "hotels", "glamping luxury tent yala wilpattu safari camp outdoors stars"),
    ("where to stay in galle fort", "Galle Fort is famous for its luxury boutique hotels housed in restored 17th-century Dutch colonial villas. They often feature antique furniture, hidden courtyard pools, and incredible heritage architecture.", "hotels", "galle fort boutique hotel colonial villa heritage antique luxury stay"),
    ("what are eco lodges in sri lanka", "Eco-lodges blend seamlessly with nature, often located in the Cultural Triangle (Sigiriya/Dambulla) or near rainforests. Look for places offering treehouses, mud huts, or cabanas built with sustainable materials.", "hotels", "eco lodge nature treehouse sigiriya sustainable cabana green stay"),
    ("how much are hostels in the south coast", "Hostels in surf towns like Weligama, Mirissa, and Hiriketiya range from $8 to $15 a night. They are highly social, often have pools or cafes, and are perfect for meeting fellow backpackers and surfers.", "hotels", "hostel south coast cheap budget backpacker weligama mirissa bed"),
    ("can i do an ayurvedic retreat", "Yes, Sri Lanka has dedicated Ayurvedic resorts, especially around coastal areas like Bentota and Wadduwa. They offer multi-day packages including doctor consultations, daily herbal treatments, yoga, and specialized diets.", "hotels", "ayurveda resort retreat wellness bentota herbal treatment doctor diet"),
    ("are there water villas in sri lanka", "While not like the Maldives, there are a few unique properties! For example, some eco-resorts have cabanas built on stilts over lakes or marshlands, offering a peaceful, floating experience.", "hotels", "water villa floating lake cabana stilt unique stay"),
    
    # ==================== ISLANDS & BEACH SPECIFICS ====================
    ("tell me about pigeon island", "A marine national park off the coast of Nilaveli (Trincomalee). It has some of the best snorkeling in the country, where you can swim with blacktip reef sharks and sea turtles in clear, shallow waters.", "destinations", "pigeon island nilaveli trincomalee snorkel reef shark turtle marine park"),
    ("what is jungle beach", "There are two famous Jungle Beaches. One is near Galle (Rumassala), accessed by a short hike, offering calm waters. The other is a luxury resort area in Trincomalee. Both offer beautiful, secluded vibes.", "beaches", "jungle beach galle rumassala trincomalee secluded calm hike"),
    ("what is secret beach in mirissa", "It's no longer a huge secret, but it's a beautiful, small cove tucked away from the main Mirissa stretch. You need to hike down a steep path or take a tuk-tuk to reach its rocky pools and small bar.", "beaches", "secret beach mirissa cove hidden hike pool quiet sand"),

]

def seed():
    database.init_db()

    # Clear existing domain knowledge and reload fresh
    conn = database.get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM domain_knowledge")
    conn.commit()
    conn.close()
    print("Cleared existing domain knowledge.")

    database.add_domain_knowledge_bulk(DOMAIN_DATA)
    print(f"Successfully seeded {len(DOMAIN_DATA)} domain knowledge entries!")
    print("\nCategories covered:")
    categories = {}
    for entry in DOMAIN_DATA:
        cat = entry[2]
        categories[cat] = categories.get(cat, 0) + 1
    for cat, count in sorted(categories.items()):
        print(f"  {cat}: {count} entries")

if __name__ == "__main__":
    seed()
