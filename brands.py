"""One source of truth for behoss.github.io: every business and open-source project.

Run `python3 build.py` after editing; it writes index.html, llms.txt and sitemap.xml.
"""

SITE = "https://behoss.github.io"
NAME = "Bez"
JOB = "AI systems architect and CTO"
UPDATED = "2026-11-20"
SAME_AS = [
    "https://github.com/behoss",
    "https://x.com/bezhoss",
    "https://www.linkedin.com/in/bhoss",
]

# (section id, heading, strap, [businesses])
# business = (name, url, tag, icon file, description, call to action)
SECTIONS = [
    ("shops", "Online shops", "Delivered across the UK, checkout in a minute.", [
        ("Next Day Gifts", "https://nextdaygifts.co.uk", "Gifts", "nextdaygifts.png",
         "Gifts for every occasion and budget: birthdays, Christmas, gifts for her, him, mum and dad, delivered across the UK.",
         "Shop next day gifts"),
        ("Your Personalised Gifts", "https://yourpersonalisedgifts.co.uk", "Personalised", "yourpersonalisedgifts.png",
         "Personalised gifts made to order: mugs, glasses, baubles, cushions and keepsakes with their name or your message.",
         "Shop personalised gifts"),
        ("Holistic Tree", "https://holistictree.co.uk", "Spiritual", "holistictree.png",
         "The UK crystal shop and witch shop: crystals, tarot cards, incense, spell candles and witchcraft supplies.",
         "Shop crystals and tarot cards"),
        ("Buy Pet Supplies", "https://buypetsupplies.co.uk", "Pets", "buypetsupplies.png",
         "Dog and cat supplies, from harnesses, leads and beds to grooming tools and toys, plus personalised pet gifts.",
         "Shop dog and cat supplies"),
        ("eSIMology", "https://esimology.com", "Travel", "esimology.png",
         "Travel eSIMs for 200+ countries from £3.99, delivered by email in a minute, with every price and network shown.",
         "Get a travel eSIM"),
    ]),
    ("checks", "Free checks and comparisons", "The answer people search for, with the whole market in one place.", [
        ("GetFreeCarCheck", "https://getfreecarcheck.co.uk", "Cars", "getfreecarcheck.svg",
         "Free car check by registration: full MOT history, mileage record, ULEZ, tax and recalls in seconds, from official DVSA data.",
         "Run a free car check"),
        ("BuyingExpert", "https://buyingexpert.co.uk", "Bills", "buyingexpert.svg",
         "Compare UK broadband, mobile and energy deals, with prices checked every day and ranked by what you really pay.",
         "Compare broadband and energy deals"),
        ("SuggestedTech", "https://suggestedtech.com", "Tech", "suggestedtech.png",
         "The right tech to buy in the UK in one minute: one clear pick for every need and budget, laptops to phones.",
         "Find the best tech to buy"),
        ("Beauty Comparison", "https://beautycomparison.com", "Beauty", "beautycomparison.png",
         "Skincare, haircare and makeup compared by what is really inside, with every ingredient list decoded.",
         "Compare skincare by ingredients"),
    ]),
    ("codes", "Codes and sign-up bonuses", "Free money and real savings, verified against each brand's own terms.", [
        ("HonestCodes", "https://honestcodes.co.uk", "Codes", "honestcodes.png",
         "UK discount codes, referral codes and sign-up offers for banking, mobile, travel and cashback, checked daily.",
         "Get UK discount codes"),
        ("TopReferrals", "https://topreferrals.co.uk", "Referrals", "topreferrals.png",
         "The UK ranking of referral bonuses: the exact reward from 170+ referral codes, link-checked every day.",
         "See the best UK referral codes"),
        ("HelloBonus", "https://hellobonus.co.uk", "Bonuses", "hellobonus.png",
         "The biggest UK sign-up bonuses and free-money offers, each one dated and verified against the brand's terms.",
         "Find the best sign-up bonuses"),
    ]),
    ("services", "Services", "Real experts, booked online.", [
        ("Softgen", "https://softgen.co.uk", "AI development", "softgen.svg",
         "AI app development agency in London: AI apps, SaaS platforms, MVPs, web and mobile apps, fixed price and live in weeks.",
         "Build your AI app with Softgen"),
        ("Lift Republic", "https://liftrepublic.com", "Coaching", "liftrepublic.png",
         "Online personal training with your own qualified coach: a training and nutrition plan made for you and a 1-to-1 check-in every week.",
         "Start with a personal coach"),
        ("Online Personal Trainer", "https://onlinepersonaltrainer.uk", "Fitness", "onlinepersonaltrainer.png",
         "A real online personal trainer in the UK: your own plan and a weekly check-in to lose weight, get fit and feel strong.",
         "Get your online training plan"),
        ("Study UK Now", "https://studyuknow.com", "Education", "studyuknow.png",
         "Study in the UK: see the universities that will say yes, then get UCAS, visa and arrival handled for you.",
         "Get into a UK university"),
        ("Lamp Dating", "https://lampdating.com", "Dating", "lampdating.png",
         "The AI dating app for real relationships: matched on personality and values, not photos. Free on iOS.",
         "Try the AI dating app"),
    ]),
    ("news", "AI news", "The AI race, sourced and read in full, every day.", [
        ("WireRead", "https://wireread.com", "Breaking", "wireread.png",
         "Breaking AI news, sourced and verified: OpenAI, Anthropic, Google, xAI and the technology industry.",
         "Read breaking AI news"),
        ("InsidersFeed", "https://insidersfeed.com", "Analysis", "insidersfeed.png",
         "The insider read on AI deals, money and power: the sharp, sourced take on the labs.",
         "Read the AI insider take"),
        ("FeaturedDaily", "https://featureddaily.com", "Daily brief", "featureddaily.png",
         "The daily brief on the AI race: the models, the business and the policy, in clear English.",
         "Get the daily AI brief"),
    ]),
]

# (repo, language tag, description, business name it serves, business url)
OPEN_SOURCE = [
    ("uk-mot-history", "Python · TypeScript",
     "Client for the official DVSA MOT History API: tests, mileage and defects by registration or VIN.",
     "GetFreeCarCheck", "https://getfreecarcheck.co.uk"),
    ("geo-kit", "TypeScript",
     "Make a Next.js site quotable by ChatGPT and AI search: JSON-LD builders, llms.txt, AI-crawler rules and an audit CLI.",
     "Softgen", "https://softgen.co.uk"),
    ("esim-coverage", "Open data",
     "Which mobile networks a travel eSIM connects to, country by country, in JSON and CSV.",
     "eSIMology", "https://esimology.com"),
    ("skincare-ingredients", "Open data",
     "INCI cosmetic ingredient names decoded in plain English, with free-from flags.",
     "Beauty Comparison", "https://beautycomparison.com"),
    ("beauty-label-audit-2026", "Open data",
     "1,641 cosmetic ingredient lists decoded against 12 ingredient families.",
     "Beauty Comparison", "https://beautycomparison.com"),
    ("neo4j-graphrag", "Python",
     "Knowledge-graph RAG on Neo4j and Gemini, with entity resolution and graph-plus-vector search.",
     "Softgen", "https://softgen.co.uk"),
    ("computer-use", "Python",
     "A macOS desktop agent on Gemini's Computer Use API: give it a goal and an app, it sees the screen and acts.",
     "Softgen", "https://softgen.co.uk"),
]

# Repos that publish their own GitHub Pages docs at SITE/<repo>/
PAGES_REPOS = {"uk-mot-history", "geo-kit", "esim-coverage", "skincare-ingredients"}
