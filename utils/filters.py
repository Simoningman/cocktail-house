"""
utils/filters.py
Filter cocktails by spirit, flavor and search text.
Flavor matching: dominant flavor always matches, plus any secondary flavor above 60.
"""

from data.cocktails_data import COCKTAILS, SPIRITS


def filter_cocktails(spirit_label: str, flavors: list, search: str) -> list:
    spirit_key = None
    if spirit_label != "All":
        for key, label in SPIRITS.items():
            if label == spirit_label:
                spirit_key = key
                break

    result = []
    for c in COCKTAILS:

        # Filter by spirit
        if spirit_key and c["spirit"] != spirit_key:
            continue

        # Filter by flavor
        if flavors:
            profile = c.get("flavor_profile", {})
            if profile:
                max_val  = max(profile.values())
                dominant = max(profile, key=profile.get).lower()
                # Include secondary flavors that score above 60
                active_flavors = {
                    k.lower() for k, v in profile.items()
                    if v >= 60 or v == max_val
                }
            else:
                active_flavors = set()

            if not any(f.lower() in active_flavors for f in flavors):
                continue

        # Filter by search text
        if search:
            q = search.lower()
            match = (
                q in c["name"].lower()
                or q in c["spirit_label"].lower()
                or any(q in f for f in c["flavors"])
            )
            if not match:
                continue

        result.append(c)

    return result
