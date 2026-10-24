# Disease Knowledge Base for Plant Disease AI
DISEASE_DATA = {
    "Tomato___Bacterial_spot": {
        "id": "Tomato___Bacterial_spot",
        "name": "Bacterial Spot",
        "crop": "Tomato",
        "pathogen_type": "Bacterial",
        "pathogen": "Xanthomonas spp.",
        "severity": "High",
        "severity_color": "red",
        "summary": "Destructive bacterial disease causing dark water-soaked leaf spots, defoliation, and fruit blemishes.",
        "symptoms": [
            "Small (less than 3mm), water-soaked circular lesions on leaves",
            "Spots turn dark brown to black, often with distinct yellow halos",
            "Severe infection causes leaves to scorch, yellow, and drop prematurely",
            "Raised blister-like dark scabs on green fruit, which become brown and rough"
        ],
        "organic_treatment": [
            "Apply copper octanoate (copper soap) or fixed copper fungicides preventatively",
            "Use bio-fungicide sprays containing Bacillus subtilis or Bacillus amyloliquefaciens",
            "Remove and safely dispose of heavily infected bottom leaves",
            "Apply a 2-3 inch organic straw mulch to stop bacterial splashback from soil"
        ],
        "chemical_treatment": [
            "Spray copper hydroxide tank-mixed with mancozeb for enhanced bacterial control",
            "Apply agricultural streptomycin sulfate where locally approved and registered",
            "Rotate chemical modes of action every 7-10 days during rainy conditions"
        ],
        "prevention": [
            "Use only certified pathogen-free seeds and transplants",
            "Avoid overhead irrigation; water exclusively at soil level using drip systems",
            "Sanitize pruning tools and stakes with 10% bleach or isopropyl alcohol between cuts",
            "Practice a strict 2-3 year crop rotation away from solanaceous crops (peppers, eggplants)"
        ]
    },
    "Tomato___Early_blight": {
        "id": "Tomato___Early_blight",
        "name": "Early Blight",
        "crop": "Tomato",
        "pathogen_type": "Fungal",
        "pathogen": "Alternaria solani",
        "severity": "Moderate to High",
        "severity_color": "amber",
        "summary": "Common fungal foliar disease characterized by distinct concentric target-like rings on older leaves.",
        "symptoms": [
            "Brown-to-black circular spots with concentric target-board rings on older lower leaves",
            "Yellow halo (chlorotic ring) surrounding the necrotic leaf spots",
            "Progressive upward leaf yellowing, browning, and premature leaf drop",
            "Dark, sunken, leathery lesions at the stem base (collar rot) and stem-end of fruit"
        ],
        "organic_treatment": [
            "Spray cold-pressed pure neem oil or potassium bicarbonate upon first sign",
            "Apply copper fungicide or Bacillus subtilis to protect healthy foliage",
            "Prune off lower foliage (up to 12-18 inches) once plants reach mature height",
            "Mulch heavily around the root zone to prevent soil spores from splashing up"
        ],
        "chemical_treatment": [
            "Apply Chlorothalonil (e.g. Daconil) every 7-14 days as a protective fungicide",
            "Use systemic fungicides like Azoxystrobin, Pyraclostrobin, or Difenoconazole",
            "Apply Mancozeb preventatively prior to forecasted humid or rainy periods"
        ],
        "prevention": [
            "Stake, cage, or trellis plants to maintain upright growth and promote airflow",
            "Water early in the morning using soaker hoses to allow foliage to dry rapidly",
            "Bury, burn, or destroy infected crop residue immediately after the growing season",
            "Practice 2-3 year rotation with non-solanaceous crops (beans, corn, brassicas)"
        ]
    },
    "Tomato___Late_blight": {
        "id": "Tomato___Late_blight",
        "name": "Late Blight",
        "crop": "Tomato",
        "pathogen_type": "Oomycete / Fungal",
        "pathogen": "Phytophthora infestans",
        "severity": "Critical",
        "severity_color": "rose",
        "summary": "Aggressive, fast-spreading water mold that can wipe out entire tomato crops within days in cool, humid weather.",
        "symptoms": [
            "Large, irregular water-soaked pale green lesions that rapidly turn dark brown to purplish-black",
            "White velvety or fuzzy mold growth on the undersides of infected leaves during humid mornings",
            "Stems develop dark brown to black greasy-looking necrotic lesions",
            "Fruit develops firm, greasy, rough brown surface lesions that rot rapidly"
        ],
        "organic_treatment": [
            "Immediately harvest remaining mature green fruit before infection reaches them",
            "Remove and securely bag entire infected plants on a sunny, dry day; DO NOT compost",
            "Apply copper octanoate or Bordeaux mixture preventatively across uninfected neighboring plants",
            "Solarize or cover soil with plastic to reduce spore survival"
        ],
        "chemical_treatment": [
            "Apply systemic oomycete-targeted fungicides: Mandipropamid, Dimethomorph, or Cyazofamid",
            "Apply preventative tank-mixes containing Chlorothalonil or Mancozeb",
            "Monitor local agricultural Extension blight alert networks for regional outbreaks"
        ],
        "prevention": [
            "Choose Late Blight-resistant varieties (e.g., Defiant PhR, Mountain Magic, Plum Regal)",
            "Maintain wide plant spacing (minimum 24-36 inches) for rapid canopy drying",
            "Eradicate volunteer tomato and potato plants in the vicinity every spring",
            "Never introduce seed potatoes or tomato starts from uncertified sources"
        ]
    },
    "Tomato___Leaf_Mold": {
        "id": "Tomato___Leaf_Mold",
        "name": "Leaf Mold",
        "crop": "Tomato",
        "pathogen_type": "Fungal",
        "pathogen": "Passalora fulva (Cladosporium fulvum)",
        "severity": "Moderate",
        "severity_color": "yellow",
        "summary": "Humidity-driven fungal disease prevalent in greenhouses and high tunnels with poor ventilation.",
        "symptoms": [
            "Pale green to yellowish patches on upper leaf surfaces with indistinct borders",
            "Olive green, velvety, purplish-brown fungal growth on the matching lower leaf surface",
            "Older leaves become curled, wither, and drop prematurely",
            "Blossoms and fruit occasionally show calyx necrosis and fruit rot"
        ],
        "organic_treatment": [
            "Aggressively improve greenhouse airflow using horizontal airflow fans and ridge vents",
            "Keep greenhouse relative humidity below 85% through heating and ventilation",
            "Spray copper octanoate or potassium bicarbonate (MilStop) at weekly intervals",
            "Prune inner leaves to open up the canopy to direct sunlight"
        ],
        "chemical_treatment": [
            "Apply Difenoconazole, Boscalid, or Fluxapyroxad labelled for greenhouse/field tomatoes",
            "Use preventative applications of Chlorothalonil",
            "Alternate fungicide FRAC codes to prevent fungal resistance development"
        ],
        "prevention": [
            "Select resistant cultivars containing Cf resistance genes",
            "Avoid overhead watering and avoid touching wet plants during greenhouse work",
            "Space rows widely apart to avoid dense foliage mats",
            "Steam-clean or disinfect greenhouse framing and plastic between cropping cycles"
        ]
    },
    "Tomato___Septoria_leaf_spot": {
        "id": "Tomato___Septoria_leaf_spot",
        "name": "Septoria Leaf Spot",
        "crop": "Tomato",
        "pathogen_type": "Fungal",
        "pathogen": "Septoria lycopersici",
        "severity": "Moderate to High",
        "severity_color": "amber",
        "summary": "Foliar fungal pathogen producing numerous small circular spots with grayish-white centers and black dots.",
        "symptoms": [
            "Numerous small circular spots (1.5-3mm) with dark brown borders and ash-gray centers",
            "Tiny black speckles (pycnidia / spore-bearing bodies) visible inside spot centers with magnifying glass",
            "Infection starts on lower leaves and progresses rapidly up the vine",
            "Severely affected leaves turn yellow, curl up, die, exposing fruit to sunscald"
        ],
        "organic_treatment": [
            "Remove infected lower foliage early before spores spread upward",
            "Apply organic bio-fungicides such as Bacillus amyloliquefaciens (Serenade)",
            "Spray liquid copper fungicides at first detection",
            "Lay down thick weed barrier cloth or clean wheat straw under plants"
        ],
        "chemical_treatment": [
            "Apply Chlorothalonil or Mancozeb on a strict 7-day schedule in warm, wet weather",
            "Use strobilurin or triazole fungicides (Azoxystrobin, Difenoconazole)",
            "Combine protectant and curative fungicides during high disease pressure"
        ],
        "prevention": [
            "Never work among wet tomato plants as spores spread easily by mechanical contact",
            "Water at the base with drip lines or olla pots",
            "Practice minimum 3-year crop rotation away from solanaceous plants",
            "Clean and sanitize tomato cages, stakes, and twine before reusing"
        ]
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "id": "Tomato___Spider_mites Two-spotted_spider_mite",
        "name": "Two-Spotted Spider Mite",
        "crop": "Tomato",
        "pathogen_type": "Pest / Arachnid",
        "pathogen": "Tetranychus urticae",
        "severity": "Moderate to High",
        "severity_color": "amber",
        "summary": "Microscopic sap-sucking arachnids that multiply explosively in hot, dry, dusty environments.",
        "symptoms": [
            "Fine white to pale yellow speckling (stippling) on upper leaf surfaces",
            "Silken webbing visible across leaf undersides, leaf stems, and growing tips",
            "Foliage takes on a bronze, dusty, faded appearance and dries to a brittle crisp",
            "Tiny moving dots (yellowish-green with two dark spots) visible under magnification"
        ],
        "organic_treatment": [
            "Spray insecticidal soap (potassium salts of fatty acids) thoroughly targeting leaf undersides",
            "Apply cold-pressed neem oil or horticultural mineral oil (avoid spraying during peak midday heat)",
            "Release biological control predators: Phytoseiulus persimilis or Neoseiulus californicus",
            "Blast leaf undersides with a firm stream of clean water to disrupt webs and knock mites off"
        ],
        "chemical_treatment": [
            "Apply selective miticides: Bifenazate (Acramite), Spiromesifen, or Abamectin",
            "Avoid broad-spectrum synthetic pyrethroids as they kill beneficial predator bugs and flare mite populations",
            "Rotate miticide modes of action every generation (7-10 days in warm weather)"
        ],
        "prevention": [
            "Maintain adequate soil moisture and reduce plant water stress",
            "Hose down dusty farm roads or paths bordering tomato fields",
            "Control broadleaf weeds like mallow and nightshade that harbor overwintering mites",
            "Regularly inspect leaf undersides with a 10x hand lens"
        ]
    },
    "Tomato___Target_Spot": {
        "id": "Tomato___Target_Spot",
        "name": "Target Spot",
        "crop": "Tomato",
        "pathogen_type": "Fungal",
        "pathogen": "Corynespora cassiicola",
        "severity": "Moderate",
        "severity_color": "yellow",
        "summary": "Warm-season fungal disease producing pinpoint brown specks that enlarge into zoned necrotic target rings.",
        "symptoms": [
            "Pinpoint brown spots that expand into circular lesions with light brown centres and dark margins",
            "Zonate concentric rings that can resemble early blight lesions",
            "Centers of older lesions may tear or drop out, creating a 'shot-hole' appearance",
            "Sunken, crater-like brown lesions on green and ripening tomato fruit"
        ],
        "organic_treatment": [
            "Apply copper octanoate or copper hydroxide fungicides preventatively",
            "Apply bio-fungicides based on Bacillus subtilis or Trichoderma strains",
            "Promptly prune and remove diseased lower stems and foliage",
            "Maintain good spacing to promote rapid dew evaporation"
        ],
        "chemical_treatment": [
            "Apply Boscalid, Pyraclostrobin, Penthiopyrad, or Fluopyram",
            "Use protectant sprays of Chlorothalonil or Mancozeb",
            "Ensure thorough spray penetration into the lower and inner canopy"
        ],
        "prevention": [
            "Space plants generously to promote rapid air circulation",
            "Eliminate solanaceous weed hosts (black nightshade, groundcherry)",
            "Avoid excessive overhead irrigation; prioritize drip tubes",
            "Incorporate crop residue deep into soil or destroy after final harvest"
        ]
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "id": "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
        "name": "Tomato Yellow Leaf Curl Virus (TYLCV)",
        "crop": "Tomato",
        "pathogen_type": "Viral (Begomovirus)",
        "pathogen": "TYLCV (Transmitted by Bemisia tabaci whiteflies)",
        "severity": "Critical",
        "severity_color": "rose",
        "summary": "Severe whitefly-transmitted viral disease causing severe upward curling, chlorosis, and total yield failure.",
        "symptoms": [
            "Marked upward curling and cupping of leaflet margins",
            "Interveinal yellowing (chlorosis) with reduced leaf blade size",
            "Extreme plant stunting with a bushy, erect, bonsai-like appearance",
            "Severe flower abortion; blossoms drop before setting fruit, resulting in near-total yield loss"
        ],
        "organic_treatment": [
            "Viruses cannot be cured; rogue (pull out) and immediately incinerate/bag infected plants",
            "Erect 50-mesh insect-proof netting over seedling nurseries and greenhouse vents",
            "Deploy bright yellow sticky cards (1 card per 200 sq ft) to monitor and trap whiteflies",
            "Spray neem oil, insecticidal soap, or entomopathogenic fungus Beauveria bassiana against whiteflies"
        ],
        "chemical_treatment": [
            "Control vector whiteflies with systemic insecticides: Imidacloprid, Dinotefuran, or Spirotetramat",
            "Apply insect growth regulators (Pyriproxyfen, Buprofezin) against whitefly nymphs",
            "Rotate insecticide IRAC classes to prevent whitefly pesticide resistance"
        ],
        "prevention": [
            "Plant certified TYLCV-resistant varieties (e.g. Tygress, Invictus, SV0215TY)",
            "Install reflective silver / aluminized plastic mulch to repel flying whiteflies",
            "Establish a 2-month regional tomato-free host break period between seasons",
            "Keep fields clear of alternate whitefly host weeds"
        ]
    },
    "Tomato___Tomato_mosaic_virus": {
        "id": "Tomato___Tomato_mosaic_virus",
        "name": "Tomato Mosaic Virus (ToMV)",
        "crop": "Tomato",
        "pathogen_type": "Viral (Tobamovirus)",
        "pathogen": "Tomato Mosaic Virus (Mechanically transmitted)",
        "severity": "High",
        "severity_color": "red",
        "summary": "Extremely stable, easily transmissible plant virus causing mottled leaves, fern-leaf distortion, and internal fruit browning.",
        "symptoms": [
            "Alternating patches of dark green and light green/yellow mosaic patterns on leaves",
            "Distorted, blistered, puckered foliage; leaves may develop a narrow 'shoestring' or fern-like shape",
            "Stunted plant growth and reduced vigor",
            "Fruit may display uneven ripening, internal brown rings in fruit flesh (internal browning)"
        ],
        "organic_treatment": [
            "No chemical cure exists for infected plants; rogue out and burn/bag infected specimens immediately",
            "Dip hands and pruning tools in a 20% nonfat dry milk solution or 10% trisodium phosphate (TSP)",
            "Do NOT touch healthy plants after touching suspect plants without washing with soap",
            "Prohibit smoking or tobacco use anywhere near the tomato greenhouse or garden"
        ],
        "chemical_treatment": [
            "There are NO chemical viricides for curing plants infected with ToMV",
            "Focus chemical hygiene solely on tool disinfection (quaternary ammonium or Virkon S)"
        ],
        "prevention": [
            "Purchase certified virus-free seed treated with trisodium phosphate or heat",
            "Plant resistant tomato varieties labeled with the 'Tm' or 'ToMV' genetic resistance code",
            "Wash hands thoroughly with soap and water before pruning, tying, or transplanting",
            "Thoroughly steam-sterilize or replace potting soil in seed-starting trays"
        ]
    },
    "Tomato___healthy": {
        "id": "Tomato___healthy",
        "name": "Healthy Tomato Leaf",
        "crop": "Tomato",
        "pathogen_type": "None (Healthy)",
        "pathogen": "None",
        "severity": "None",
        "severity_color": "emerald",
        "summary": "The leaf shows optimal health with vigorous cellular structure, uniform chlorophyll, and no signs of disease.",
        "symptoms": [
            "Uniform, rich green leaf pigmentation with no necrotic spots or chlorotic halos",
            "Firm, flexible, well-hydrated leaf blades and turgid petioles",
            "Smooth leaf surface free from mold, fuzz, stippling, or insect webbing",
            "Active vegetative apical growth with healthy flower and fruit formation"
        ],
        "organic_treatment": [
            "Continue weekly application of balanced organic compost tea or fish hydrolysate",
            "Apply beneficial mycorrhizal fungi and beneficial rhizobacteria to support root health",
            "Maintain a 2-3 inch organic mulch layer of shredded straw or composted bark",
            "Companion plant with sweet basil, marigolds, and borage to deter pests"
        ],
        "chemical_treatment": [
            "Maintain balanced N-P-K nutrition (higher potassium and phosphorus during fruit development)",
            "Ensure adequate soluble calcium (calcium nitrate or gypsum) to prevent blossom end rot",
            "Maintain soil pH between 6.2 and 6.8 for optimal nutrient bioavailability"
        ],
        "prevention": [
            "Maintain consistent drip irrigation (1.5 to 2 inches of water per week)",
            "Prune non-fruiting lower suckers to maximize airflow through the vine canopy",
            "Conduct routine weekly leaf inspections to catch any early pathogen signs early",
            "Keep garden perimeter free of dense weeds and stagnant water"
        ]
    }
}
