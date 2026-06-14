"""
data/quiz_data.py
All quiz questions for Cocktail House.
"""

"""
data/quiz_data.py
All quiz questions for Cocktail House.
"""

QUIZ_QUESTIONS = [
    {
        "question": "Which glass is traditionally used for an Old Fashioned?",
        "answer": "Rocks glass (Old Fashioned glass)",
        "wrong": ["Martini glass", "Highball glass", "Coupe glass"],
        "fact": "The Old Fashioned glass is wide and short — perfect for a large ice cube and a drink meant to be sipped slowly.",
    },
    {
        "question": "What is the difference between Ginger Beer and Ginger Ale?",
        "answer": "Ginger Beer is spicier and more intense",
        "wrong": ["They are exactly the same", "Ginger Ale is stronger", "Ginger Beer contains alcohol"],
        "fact": "A Moscow Mule needs Ginger Beer for the right spicy kick. Ginger Ale is milder and sweeter — wrong choice for this drink!",
    },
    {
        "question": "What does it mean to 'muddle' ingredients?",
        "answer": "Gently press to release oils and flavours",
        "wrong": ["Shake vigorously in a shaker", "Blend with an electric mixer", "Freeze the ingredients"],
        "fact": "In a Mojito you muddle mint — you press gently to release the oils without shredding the leaves, which creates bitterness.",
    },
    {
        "question": "Why do you pour prosecco BEFORE Aperol in an Aperol Spritz?",
        "answer": "To preserve the bubbles",
        "wrong": ["It makes no difference", "Aperol is heavier and sinks", "Prosecco is cheaper"],
        "fact": "Prosecco first preserves the carbonation. If you pour Aperol into an empty glass first, you lose half the bubbles instantly!",
    },
    {
        "question": "What does 'double straining' (fine strain) do in cocktail mixing?",
        "answer": "Creates a smooth, silky texture with no ice chips",
        "wrong": ["Filters out the alcohol", "Cools the drink faster", "Makes the drink stronger"],
        "fact": "Straining through both the shaker strainer and a fine mesh strainer gives a silky texture — classic for a Daiquiri!",
    },
    {
        "question": "What is the ratio for a classic Negroni?",
        "answer": "1:1:1 — equal parts gin, Campari and vermouth",
        "wrong": ["2:1:1 — double gin", "1:2:1 — double Campari", "3:1:1 — triple gin"],
        "fact": "The 1:1:1 ratio makes the Negroni easy to remember and almost impossible to get wrong!",
    },
    {
        "question": "What are 'bitters' and what do they do in a cocktail?",
        "answer": "Concentrated herbal extract that balances and deepens flavour",
        "wrong": ["Sugar syrup with a bitter taste", "A cheap substitute for spirits", "Sparkling water with flavour"],
        "fact": "Angostura Bitters in an Old Fashioned contains gentian, quassia bark and cinnamon. It's the bartender's salt and pepper — just 2–3 dashes transform the whole drink!",
    },
    {
        "question": "Why should vermouth be stored in the fridge?",
        "answer": "Vermouth is a wine and oxidises once opened",
        "wrong": ["It doesn't need to be — it's spirits", "To improve the colour", "The cold enhances the flavour"],
        "fact": "Vermouth is a fortified wine with around 15–18% alcohol. Old vermouth can ruin an entire Negroni — replace it after 1–2 months!",
    },
    {
        "question": "Who invented the Negroni and where?",
        "answer": "Count Camillo Negroni in Florence, 1919",
        "wrong": ["Ernest Hemingway in Cuba", "A Hollywood bartender in 1941", "An unknown bartender in New York"],
        "fact": "Count Negroni ordered his Americano with gin instead of soda water — and a classic was born.",
    },
    {
        "question": "What is the formula for a classic 'sour' cocktail (e.g. Daiquiri)?",
        "answer": "Spirit + citrus juice + sweetener",
        "wrong": ["Spirit + soda water + bitters", "Spirit + vermouth + garnish", "Spirit + cream + syrup"],
        "fact": "The sour formula — spirit, sour, sweet — is the foundation of hundreds of cocktails. Master it and you can improvise freely!",
    },
    {
        "question": "What spirit is used in a classic Daiquiri?",
        "answer": "White rum",
        "wrong": ["Vodka", "Gin", "Tequila"],
        "fact": "The Daiquiri is one of rum's greatest showcases \u2014 white rum's clean, slightly sweet character lets the lime and sugar shine.",
    },
    {
        "question": "What makes a Negroni different from an Americano?",
        "answer": "Gin replaces soda water",
        "wrong": ["Campari is replaced with Aperol", "Vermouth is removed", "Ice is not used"],
        "fact": "Count Negroni asked his bartender to replace the soda water in his Americano with gin \u2014 and accidentally invented one of the world's great cocktails.",
    },
    {
        "question": "What does 'on the rocks' mean?",
        "answer": "Served over ice",
        "wrong": ["Served frozen", "Served warm", "Served without garnish"],
        "fact": "'On the rocks' simply means served over ice cubes. The term comes from the days when blocks of ice were cut from frozen lakes and stored in 'ice houses'.",
    },
    {
        "question": "Which cocktail is known as the 'King of Cocktails'?",
        "answer": "Martini",
        "wrong": ["Manhattan", "Old Fashioned", "Negroni"],
        "fact": "The Martini has been called the king of cocktails since the early 1900s. Its simplicity \u2014 gin and vermouth \u2014 demands perfect execution and the best ingredients.",
    },
    {
        "question": "What is orgeat syrup made from?",
        "answer": "Almonds, sugar and orange flower water",
        "wrong": ["Coconut and lime", "Grenadine and sugar", "Passion fruit and vanilla"],
        "fact": "Orgeat is a sweet almond syrup essential to tiki cocktails like the Mai Tai. Its name comes from the French word for barley, which was used in the original recipe.",
    },
    {
        "question": "What does 'dry' mean when ordering a Martini?",
        "answer": "Less vermouth",
        "wrong": ["No ice", "More gin", "Shaken not stirred"],
        "fact": "A 'dry' Martini has very little vermouth. An 'extra dry' Martini has almost none at all \u2014 some bartenders simply wave the vermouth bottle over the glass.",
    },
    {
        "question": "Which country does the Mojito originate from?",
        "answer": "Cuba",
        "wrong": ["Brazil", "Mexico", "Puerto Rico"],
        "fact": "The Mojito is Cuba's most famous cocktail. It was a favourite of Ernest Hemingway, who spent much of his life in Havana.",
    },
    {
        "question": "What is the main botanical in gin?",
        "answer": "Juniper berries",
        "wrong": ["Lavender", "Coriander", "Citrus peel"],
        "fact": "By law, gin must taste predominantly of juniper berries. The name 'gin' comes from the Dutch word 'jenever', meaning juniper.",
    },
    {
        "question": "What plant is tequila made from?",
        "answer": "Blue agave",
        "wrong": ["Cactus", "Sugarcane", "Corn"],
        "fact": "Tequila can only be made from blue agave grown in specific regions of Mexico, primarily the state of Jalisco.",
    },
    {
        "question": "What is the difference between shaking and stirring a cocktail?",
        "answer": "Shaking aerates and dilutes faster; stirring gives a silkier texture",
        "wrong": ["There is no difference", "Stirring makes it stronger", "Shaking makes it warmer"],
        "fact": "Shaking adds tiny air bubbles and dilutes the drink more \u2014 perfect for citrus cocktails. Stirring gives a clear, silky result \u2014 ideal for spirit-forward drinks.",
    },
    {
        "question": "What gives Campari its distinctive red colour?",
        "answer": "Artificial colouring (originally carmine from insects)",
        "wrong": ["Blood orange", "Pomegranate", "Red wine"],
        "fact": "Campari was originally coloured with carmine dye made from crushed cochineal insects. The recipe switched to artificial colouring in 2006.",
    },
    {
        "question": "What is a 'float' in cocktail making?",
        "answer": "Pouring a liquid slowly over the back of a spoon to layer it on top",
        "wrong": ["Adding a fruit garnish", "Freezing the top of a drink", "Blending with ice"],
        "fact": "Floating exploits the density differences between liquids. A Dark & Stormy floats dark rum on top of ginger beer.",
    },
    {
        "question": "Which cocktail follows the '3-2-1 rule'?",
        "answer": "Aperol Spritz",
        "wrong": ["Negroni", "Margarita", "Manhattan"],
        "fact": "The Aperol Spritz follows the Italian 3-2-1 rule: 3 parts prosecco, 2 parts Aperol, 1 part soda water.",
    },
    {
        "question": "What is 'simple syrup' made from?",
        "answer": "Equal parts sugar and water",
        "wrong": ["Honey and lemon", "Corn syrup and vanilla", "Sugar and lime juice"],
        "fact": "Simple syrup (1:1) dissolves easily in cold drinks, unlike granulated sugar. A 'rich' simple syrup uses 2 parts sugar to 1 part water.",
    },
    {
        "question": "What does IBA stand for in cocktails?",
        "answer": "International Bartenders Association",
        "wrong": ["International Bar Academy", "Italian Bartending Arts", "Independent Bar Alliance"],
        "fact": "The IBA maintains an official list of cocktails with standardised recipes used in international bartending competitions.",
    },
    {
        "question": "What is grenadine made from?",
        "answer": "Pomegranate syrup",
        "wrong": ["Cherry juice", "Raspberry syrup", "Strawberry extract"],
        "fact": "'Grenadine' comes from the French word for pomegranate. Most commercial grenadines today use artificial flavouring.",
    },
    {
        "question": "What spirit is in a Cosmopolitan?",
        "answer": "Vodka",
        "wrong": ["Gin", "Rum", "Tequila"],
        "fact": "The Cosmopolitan uses citrus vodka, triple sec, cranberry juice and lime juice. It became iconic through Sex and the City in the late 1990s.",
    },
    {
        "question": "What does 'neat' mean when ordering spirits?",
        "answer": "Poured straight with no ice or mixers",
        "wrong": ["On the rocks", "With soda water", "Double measure"],
        "fact": "'Neat' means the spirit is poured directly from the bottle into the glass \u2014 no ice, no water, no mixer.",
    },
    {
        "question": "What is the purpose of bitters in a cocktail?",
        "answer": "To add complexity, balance sweetness and deepen flavour",
        "wrong": ["To make the drink stronger", "To add sweetness", "To change the colour"],
        "fact": "Bitters are the bartender's seasoning \u2014 just a dash or two can transform a drink.",
    },
    {
        "question": "Which cocktail is stirred, never shaken?",
        "answer": "Negroni",
        "wrong": ["Daiquiri", "Margarita", "Cosmopolitan"],
        "fact": "Spirit-forward cocktails like the Negroni, Manhattan and Martini should always be stirred.",
    },
    {
        "question": "What is the classic ratio for a Negroni?",
        "answer": "1:1:1 \u2014 equal parts gin, Campari and vermouth",
        "wrong": ["2:1:1 \u2014 double gin", "1:2:1 \u2014 double Campari", "3:1:1 \u2014 triple gin"],
        "fact": "The equal parts ratio makes the Negroni one of the easiest cocktails to remember and most perfectly balanced.",
    },
    {
        "question": "What is Cointreau?",
        "answer": "A French triple sec orange liqueur",
        "wrong": ["An Italian bitter aperitif", "A rum liqueur", "A Spanish brandy"],
        "fact": "Cointreau is a premium triple sec used in Margaritas, Cosmopolitans and Sidecars.",
    },
    {
        "question": "What does 'double strain' mean?",
        "answer": "Straining through both the shaker strainer and a fine mesh sieve",
        "wrong": ["Using two shakers", "Straining twice through the same strainer", "Adding ice twice"],
        "fact": "Double straining removes ice chips and fine particles, giving a perfectly smooth cocktail.",
    },
    {
        "question": "What is the Sidecar's base spirit?",
        "answer": "Cognac",
        "wrong": ["Bourbon", "Rum", "Gin"],
        "fact": "The Sidecar uses cognac, triple sec and lemon juice \u2014 the same sour family as the Margarita and Daiquiri.",
    },
    {
        "question": "What makes a Moscow Mule different from a regular vodka soda?",
        "answer": "Ginger beer and lime juice instead of soda water",
        "wrong": ["It uses flavoured vodka", "It is served hot", "It contains mint"],
        "fact": "The Moscow Mule was invented in 1941 specifically to sell vodka and ginger beer together.",
    },
    {
        "question": "What is mezcal?",
        "answer": "A smoky Mexican spirit made from any agave variety",
        "wrong": ["A type of tequila made from blue agave only", "A Mexican beer", "A rum made in Mexico"],
        "fact": "All tequila is mezcal, but not all mezcal is tequila. The smokiness comes from roasting agave hearts in underground pits.",
    },
    {
        "question": "What is cacha\u00e7a?",
        "answer": "A Brazilian spirit distilled from fresh sugarcane juice",
        "wrong": ["A Mexican tequila substitute", "A Cuban rum variant", "A South American vodka"],
        "fact": "Cacha\u00e7a is Brazil's national spirit and the base of the Caipirinha.",
    },
    {
        "question": "What does 'expressed' mean when talking about citrus peel garnish?",
        "answer": "Squeezing the peel over the drink to release its oils onto the surface",
        "wrong": ["Placing the peel inside the drink", "Grating the peel into the drink", "Soaking the peel in the spirit"],
        "fact": "Expressing a citrus peel releases aromatic oils onto the surface of the drink, dramatically changing the aroma.",
    },
    {
        "question": "What is the French 75 named after?",
        "answer": "A French 75mm artillery field gun used in WWI",
        "wrong": ["A Paris street address", "The year it was invented", "A famous French bartender"],
        "fact": "The French 75 was said to hit with the same kick as the 75mm artillery gun.",
    },
    {
        "question": "What distinguishes an Old Fashioned from a Manhattan?",
        "answer": "Old Fashioned uses sugar and bitters; Manhattan uses sweet vermouth",
        "wrong": ["They use different glasses", "Manhattan is always shaken", "Old Fashioned uses rye, Manhattan uses bourbon"],
        "fact": "The Old Fashioned is simpler \u2014 just whiskey, sugar, bitters and water. The Manhattan adds sweet vermouth.",
    },
    {
        "question": "What is 'falernum'?",
        "answer": "A Caribbean syrup of lime, ginger, almond and cloves",
        "wrong": ["A type of rum from Barbados", "An Italian bitter liqueur", "A Mexican chili salt"],
        "fact": "Falernum has been produced in Barbados since the 1700s \u2014 the secret weapon in tiki drinks.",
    },
    {
        "question": "What does 'proof' mean in relation to alcohol?",
        "answer": "Twice the ABV percentage \u2014 80 proof = 40% ABV",
        "wrong": ["The same as ABV percentage", "The age of the spirit in years", "The number of distillations"],
        "fact": "The proof system originated in Britain where sailors tested rum by soaking gunpowder in it.",
    },
    {
        "question": "What is the Last Word cocktail made of?",
        "answer": "Equal parts gin, Green Chartreuse, maraschino and lime juice",
        "wrong": ["Bourbon, Aperol, lemon and elderflower", "Rum, Campari, vermouth and orange", "Vodka, triple sec, cranberry and lime"],
        "fact": "The Last Word dates to Prohibition-era Detroit. Green Chartreuse is made by monks from 130 herbs.",
    },
    {
        "question": "What is Fernet-Branca?",
        "answer": "An intensely bitter Italian amaro herbal liqueur",
        "wrong": ["A sweet Italian dessert wine", "A French champagne aperitif", "A Spanish rum liqueur"],
        "fact": "Fernet-Branca is the unofficial drink of bartenders worldwide.",
    },
    {
        "question": "Why is the Vesper Martini significant?",
        "answer": "It was invented by Ian Fleming and ordered by James Bond in Casino Royale",
        "wrong": ["It was the first cocktail ever documented", "It was Queen Elizabeth II's favourite drink", "It was invented at the Ritz in Paris"],
        "fact": "Fleming's original recipe uses gin, vodka and Kinia Lillet. Bond famously ordered it 'shaken, not stirred'.",
    },
    {
        "question": "What is the Sazerac considered to be?",
        "answer": "Possibly the world's first cocktail, originating in New Orleans in the 1830s",
        "wrong": ["A modern craft cocktail from New York", "A 1970s disco drink", "A Scottish whisky tradition"],
        "fact": "The Sazerac is New Orleans' official cocktail using rye whiskey, Peychaud's bitters, sugar and an absinthe rinse.",
    },
    {
        "question": "What does 'ABV' stand for?",
        "answer": "Alcohol By Volume",
        "wrong": ["Alcohol Blend Variation", "Aged Barrel Vintage", "Alcoholic Beverage Value"],
        "fact": "ABV is the standard measure of alcohol content. Beer is typically 4\u20138%, wine 12\u201315%, spirits 37.5\u201360%+.",
    },
    {
        "question": "What is the Paper Plane cocktail?",
        "answer": "Equal parts bourbon, Aperol, Amaro Nonino and lemon juice",
        "wrong": ["Gin, elderflower, prosecco and cucumber", "Rum, Campari, lime and ginger beer", "Vodka, triple sec, orange and cranberry"],
        "fact": "The Paper Plane was created in 2008 at Death & Co in New York by Sam Ross, named after the M.I.A. song.",
    },

]