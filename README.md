# 🍸 Cocktail House

> Discover cocktails by flavor and spirit — 100+ recipes, a quiz and bartender tips.

---

## What is it?

Cocktail House is a web app for anyone who wants to explore cocktails. Browse 100+ classic recipes sorted A–Z, filter by spirit or dominant flavor, read step-by-step instructions with bartender tips, and test your knowledge with a randomised quiz.

Built entirely in Python with Streamlit — no JavaScript required.

---

## Features

- **Bartender Pick** — a random cocktail suggestion every time you open the app
- **A–Z browser** — all cocktails organised alphabetically with pagination
- **Filter by spirit** — Vodka, Gin, Rum, Tequila, Whiskey
- **Filter by flavor** — Sour, Sweet, Bitter, Strong, Fresh
- **Detailed recipes** — ingredients, step-by-step guide, glassware and flavor profile
- **Bartender tips & fun facts** for every cocktail
- **Quiz** — 5 random questions from a bank of 48, new set every round

---

## Cocktails included

100+ classics including:

| Category | Examples |
|---|---|
| Rum | Mojito, Daiquiri, Mai Tai, Dark & Stormy, Piña Colada |
| Gin | Negroni, Gin & Tonic, Last Word, French 75, Aviation |
| Vodka | Cosmopolitan, Espresso Martini, Moscow Mule, White Russian |
| Tequila | Margarita, Paloma, Spicy Margarita, Tequila Sour |
| Whiskey | Old Fashioned, Manhattan, Penicillin, Sazerac, Mint Julep |

---

## Getting started

**Requirements:** Python 3.8+

```bash
pip install -r requirements.txt
streamlit run app.py
```

The app opens automatically at `http://localhost:8501`.

---

## Project structure

```
cocktail-house/
├── app.py                  # Entry point — run this
├── data/
│   ├── cocktails_data.py   # All recipes, spirits and flavor data
│   └── quiz_data.py        # All 48 quiz questions
├── views/
│   ├── explore.py          # All cocktails + Find a cocktail tabs
│   └── quiz.py             # Quiz — questions, answers and scoring
├── utils/
│   ├── filters.py          # Spirit and flavor filtering logic
│   └── glass_icons.py      # SVG glass illustrations per cocktail
├── .streamlit/
│   └── config.toml         # Dark theme and color settings
├── requirements.txt
└── README.md
```

---

## Adding a cocktail

Open `data/cocktails_data.py` and add an object to the `COCKTAILS` list:

```python
{
    "id": 104,                        # Must be unique
    "name": "Gin & Tonic",
    "emoji": "🌿",
    "spirit": "gin",                  # vodka / gin / rum / tequila / whiskey / other
    "spirit_label": "Gin",
    "flavors": ["fresh", "bitter"],
    "difficulty": "Very easy",
    "glass": "Highball glass",
    "ingredients": [
        ("50 ml",   "Gin"),
        ("150 ml",  "Tonic water"),
        ("Garnish", "Lime wedge"),
    ],
    "steps": [
        "Fill a highball glass with ice.",
        "Pour in the gin.",
        "Top with tonic water and garnish.",
    ],
    "fun_fact": "The G&T was invented by British soldiers in India...",
    "tip": "Use Fever-Tree tonic — it makes a huge difference.",
    "flavor_profile": {
        "Sour":   20,
        "Sweet":  10,
        "Bitter": 80,
        "Strong": 50,
        "Fresh":  88,
    },
},
```

The `flavor_profile` key with the **highest value** determines which flavor filter shows this cocktail. If a second value is above 60, the cocktail also appears under that flavor filter.

---

## Deploy for free

1. Push to a public GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub, select your repo, set main file to `app.py`
4. Click Deploy — your app is live in about 2 minutes

No server, no cost, no maintenance.

---

## Tech stack

| Tool | Purpose |
|---|---|
| Python 3.8+ | Language |
| Streamlit | Web framework |
| Custom SVG | Glass illustrations |
| CSS | Dark bar theme |

---

## License

MIT — use it, modify it, share it.
