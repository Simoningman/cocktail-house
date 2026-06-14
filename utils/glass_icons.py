"""
utils/glass_icons.py
SVG glass illustrations for each glass type.
"""

GLASS_SVGS = {
    "martini": """<svg width="32" height="40" viewBox="0 0 32 40" fill="none" xmlns="http://www.w3.org/2000/svg">
        <polygon points="2,4 30,4 16,22" fill="none" stroke="#c9a84c" stroke-width="1.5" stroke-linejoin="round"/>
        <line x1="16" y1="22" x2="16" y2="36" stroke="#c9a84c" stroke-width="1.5"/>
        <line x1="10" y1="36" x2="22" y2="36" stroke="#c9a84c" stroke-width="1.5" stroke-linecap="round"/>
    </svg>""",

    "highball": """<svg width="28" height="40" viewBox="0 0 28 40" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="4" y="4" width="20" height="32" rx="2" fill="none" stroke="#c9a84c" stroke-width="1.5"/>
        <line x1="4" y1="14" x2="24" y2="14" stroke="#c9a84c" stroke-width="1" stroke-dasharray="2,2" opacity="0.4"/>
    </svg>""",

    "rocks": """<svg width="32" height="36" viewBox="0 0 32 36" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M4 6 L28 6 L26 32 L6 32 Z" fill="none" stroke="#c9a84c" stroke-width="1.5" stroke-linejoin="round"/>
        <line x1="6" y1="14" x2="26" y2="14" stroke="#c9a84c" stroke-width="1" stroke-dasharray="2,2" opacity="0.4"/>
    </svg>""",

    "coupe": """<svg width="34" height="40" viewBox="0 0 34 40" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M2 6 Q2 24 17 24 Q32 24 32 6 Z" fill="none" stroke="#c9a84c" stroke-width="1.5" stroke-linejoin="round"/>
        <line x1="17" y1="24" x2="17" y2="36" stroke="#c9a84c" stroke-width="1.5"/>
        <line x1="11" y1="36" x2="23" y2="36" stroke="#c9a84c" stroke-width="1.5" stroke-linecap="round"/>
    </svg>""",

    "wine": """<svg width="28" height="44" viewBox="0 0 28 44" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M6 4 Q4 16 14 22 Q24 16 22 4 Z" fill="none" stroke="#c9a84c" stroke-width="1.5" stroke-linejoin="round"/>
        <line x1="14" y1="22" x2="14" y2="38" stroke="#c9a84c" stroke-width="1.5"/>
        <line x1="8" y1="38" x2="20" y2="38" stroke="#c9a84c" stroke-width="1.5" stroke-linecap="round"/>
    </svg>""",

    "flute": """<svg width="20" height="44" viewBox="0 0 20 44" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M4 4 L6 28 Q10 32 10 32 Q10 32 14 28 L16 4 Z" fill="none" stroke="#c9a84c" stroke-width="1.5" stroke-linejoin="round"/>
        <line x1="10" y1="32" x2="10" y2="40" stroke="#c9a84c" stroke-width="1.5"/>
        <line x1="5" y1="40" x2="15" y2="40" stroke="#c9a84c" stroke-width="1.5" stroke-linecap="round"/>
    </svg>""",

    "tiki": """<svg width="30" height="42" viewBox="0 0 30 42" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M5 6 L6 34 Q15 38 24 34 L25 6 Q20 2 15 2 Q10 2 5 6 Z" fill="none" stroke="#c9a84c" stroke-width="1.5" stroke-linejoin="round"/>
        <path d="M8 12 Q15 10 22 12" stroke="#c9a84c" stroke-width="1" opacity="0.5"/>
        <path d="M8 18 Q15 16 22 18" stroke="#c9a84c" stroke-width="1" opacity="0.5"/>
        <line x1="15" y1="34" x2="15" y2="38" stroke="#c9a84c" stroke-width="1.5"/>
    </svg>""",

    "collins": """<svg width="24" height="44" viewBox="0 0 24 44" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="3" y="3" width="18" height="36" rx="3" fill="none" stroke="#c9a84c" stroke-width="1.5"/>
        <line x1="3" y1="12" x2="21" y2="12" stroke="#c9a84c" stroke-width="1" stroke-dasharray="2,2" opacity="0.4"/>
    </svg>""",

    "hurricane": """<svg width="30" height="44" viewBox="0 0 30 44" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M8 4 Q2 12 4 22 Q6 30 15 34 Q24 30 26 22 Q28 12 22 4 Z" fill="none" stroke="#c9a84c" stroke-width="1.5" stroke-linejoin="round"/>
        <line x1="15" y1="34" x2="15" y2="40" stroke="#c9a84c" stroke-width="1.5"/>
        <line x1="9" y1="40" x2="21" y2="40" stroke="#c9a84c" stroke-width="1.5" stroke-linecap="round"/>
    </svg>""",

    "copper": """<svg width="30" height="38" viewBox="0 0 30 38" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M3 6 Q3 32 15 34 Q27 32 27 6 Z" fill="none" stroke="#c9a84c" stroke-width="1.5" stroke-linejoin="round"/>
        <ellipse cx="15" cy="6" rx="12" ry="3" fill="none" stroke="#c9a84c" stroke-width="1.5"/>
        <line x1="3" y1="6" x2="3" y2="10" stroke="#c9a84c" stroke-width="2.5" stroke-linecap="round" opacity="0.6"/>
    </svg>""",

    "default": """<svg width="28" height="40" viewBox="0 0 28 40" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M4 4 L6 32 L22 32 L24 4 Z" fill="none" stroke="#c9a84c" stroke-width="1.5" stroke-linejoin="round"/>
        <line x1="6" y1="32" x2="22" y2="32" stroke="#c9a84c" stroke-width="1.5"/>
    </svg>""",
}

def get_glass_svg(glass_str: str) -> str:
    """Return the right SVG based on glass description."""
    g = glass_str.lower()
    if any(x in g for x in ["martini", "cocktail glass"]):
        return GLASS_SVGS["martini"]
    if any(x in g for x in ["coupe"]):
        return GLASS_SVGS["coupe"]
    if any(x in g for x in ["highball"]):
        return GLASS_SVGS["highball"]
    if any(x in g for x in ["rocks", "old fashioned", "lowball"]):
        return GLASS_SVGS["rocks"]
    if any(x in g for x in ["wine"]):
        return GLASS_SVGS["wine"]
    if any(x in g for x in ["flute", "champagne"]):
        return GLASS_SVGS["flute"]
    if any(x in g for x in ["tiki", "zombie"]):
        return GLASS_SVGS["tiki"]
    if any(x in g for x in ["collins"]):
        return GLASS_SVGS["collins"]
    if any(x in g for x in ["hurricane"]):
        return GLASS_SVGS["hurricane"]
    if any(x in g for x in ["copper", "mug"]):
        return GLASS_SVGS["copper"]
    return GLASS_SVGS["default"]
