from discord.ext import commands
from characters import characters
import random

PAL_STATS = {
  "Lamball": {"hp":70,"atk":70,"def":70},
"Cattiva": {"hp":70,"atk":70,"def":70},
"Chikipi": {"hp":60,"atk":60,"def":60},
"Lifmunk": {"hp":75,"atk":70,"def":70},
"Foxparks": {"hp":65,"atk":75,"def":70},
"Fuack": {"hp":60,"atk":80,"def":60},
"Sparkit": {"hp":60,"atk":75,"def":70},
"Tanzee": {"hp":80,"atk":70,"def":70},
"Rooby": {"hp":75,"atk":70,"def":75},
"Pengullet": {"hp":70,"atk":75,"def":70},
"Penking": {"hp":95,"atk":95,"def":95},
"Jolthog": {"hp":70,"atk":75,"def":70},
"Gumoss": {"hp":70,"atk":70,"def":70},
"Vixy": {"hp":70,"atk":70,"def":70},
"Hoocrates": {"hp":70,"atk":70,"def":80},
"Teafant": {"hp":70,"atk":60,"def":70},
"Depresso": {"hp":70,"atk":70,"def":70},
"Cremis": {"hp":70,"atk":70,"def":75},
"Daedream": {"hp":70,"atk":75,"def":60},
"Rushoar": {"hp":80,"atk":70,"def":70},
"Nox": {"hp":75,"atk":85,"def":70},
"Fuddler": {"hp":65,"atk":80,"def":50},
"Killamari": {"hp":60,"atk":60,"def":70},
"Mau": {"hp":70,"atk":60,"def":70},
"Celaray": {"hp":80,"atk":70,"def":80},
"Direhowl": {"hp":80,"atk":90,"def":75},
"Tocotoco": {"hp":60,"atk":75,"def":70},
"Flopie": {"hp":75,"atk":65,"def":70},
"Mozzarina": {"hp":90,"atk":50,"def":80},
"Bristla": {"hp":80,"atk":80,"def":80},
"Gobfin": {"hp":90,"atk":90,"def":75},
"Hangyu": {"hp":80,"atk":70,"def":70},
"Mossanda": {"hp":100,"atk":90,"def":90},
"Woolipop": {"hp":70,"atk":70,"def":90},
"Caprity": {"hp":100,"atk":70,"def":90},
"Melpaca": {"hp":90,"atk":75,"def":90},
"Eikthyrdeer": {"hp":95,"atk":80,"def":80},
"Nitewing": {"hp":100,"atk":95,"def":80},
"Ribbuny": {"hp":75,"atk":65,"def":70},
"Incineram": {"hp":95,"atk":100,"def":85},
"Cinnamoth": {"hp":70,"atk":80,"def":80},
"Arsox": {"hp":85,"atk":95,"def":95},
"Dumud": {"hp":100,"atk":70,"def":95},
"Cawgnito": {"hp":75,"atk":95,"def":80},
"Leezpunk": {"hp":80,"atk":80,"def":50},
"Loupmoon": {"hp":80,"atk":100,"def":80},
"Galeclaw": {"hp":75,"atk":85,"def":60},
"Robinquill": {"hp":90,"atk":105,"def":80},
"Gorirat": {"hp":90,"atk":95,"def":90},
"Beegarde": {"hp":80,"atk":90,"def":90},
"Elizabee": {"hp":90,"atk":105,"def":100},
"Grintale": {"hp":110,"atk":80,"def":80},
"Swee": {"hp":60,"atk":60,"def":60},
"Sweepa": {"hp":100,"atk":90,"def":90},
"Chillet": {"hp":90,"atk":80,"def":80},
"Univolt": {"hp":80,"atk":105,"def":105},
"Foxcicle": {"hp":90,"atk":95,"def":105},
"Pyrin": {"hp":100,"atk":105,"def":90},
"Reindrix": {"hp":100,"atk":80,"def":90},
"Rayhound": {"hp":90,"atk":100,"def":80},
"Kitsun": {"hp":100,"atk":100,"def":80},
"Dazzi": {"hp":70,"atk":90,"def":70},
"Lunaris": {"hp":90,"atk":100,"def":100},
"Dinossom": {"hp":110,"atk":80,"def":100},
"Surfent": {"hp":100,"atk":80,"def":90},
"Maraith": {"hp":80,"atk":105,"def":90},
"Digtoise": {"hp":80,"atk":100,"def":120},
"Tombat": {"hp":95,"atk":90,"def":80},
"Lovander": {"hp":100,"atk":90,"def":90},
"Flambelle": {"hp":70,"atk":70,"def":70},
"Vanwyrm": {"hp":110,"atk":100,"def":80},
"Bushi": {"hp":80,"atk":125,"def":80},
"Beakon": {"hp":105,"atk":120,"def":110},
"Ragnahawk": {"hp":100,"atk":125,"def":100},
"Katress": {"hp":105,"atk":100,"def":80},
"Wixen": {"hp":100,"atk":100,"def":80},
"Verdash": {"hp":100,"atk":110,"def":100},
"Vaelet": {"hp":90,"atk":110,"def":90},
"Sibelyx": {"hp":110,"atk":110,"def":100},
"Elphidran": {"hp":110,"atk":100,"def":110},
"Kelpsea": {"hp":65,"atk":70,"def":80},
"Azurobe": {"hp":110,"atk":120,"def":110},
"Cryolinx": {"hp":120,"atk":130,"def":110},
"Blazehowl": {"hp":100,"atk":110,"def":100},
"Relaxaurus": {"hp":110,"atk":110,"def":100},
"Broncherry": {"hp":110,"atk":90,"def":90},
"Petallia": {"hp":100,"atk":110,"def":100},
"Reptyro": {"hp":110,"atk":120,"def":120},
"Kingpaca": {"hp":120,"atk":100,"def":100},
"Mammorest": {"hp":120,"atk":100,"def":110},
"Wumpo": {"hp":110,"atk":100,"def":100},
"Warsect": {"hp":110,"atk":100,"def":120},
"Fenglope": {"hp":110,"atk":110,"def":100},
"Felbat": {"hp":100,"atk":120,"def":90},
"Quivern": {"hp":105,"atk":120,"def":110},
"Blazamut": {"hp":100,"atk":125,"def":120},
"Helzephyr": {"hp":110,"atk":120,"def":110},
"Astegon": {"hp":100,"atk":125,"def":125},
"Menasting": {"hp":100,"atk":120,"def":130},
"Anubis": {"hp":120,"atk":130,"def":100},
"Jormuntide": {"hp":130,"atk":150,"def":100},
"Suzaku": {"hp":120,"atk":125,"def":105},
"Grizzbolt": {"hp":105,"atk":120,"def":100},
"Lyleen": {"hp":110,"atk":110,"def":110},
"Faleris": {"hp":100,"atk":120,"def":110},
"Orserk": {"hp":110,"atk":130,"def":100},
"Shadowbeak": {"hp":120,"atk":130,"def":120},
"Paladius": {"hp":130,"atk":120,"def":145},
"Necromus": {"hp":130,"atk":145,"def":120},
"Frostallion": {"hp":140,"atk":140,"def":120},
"Jetragon": {"hp":110,"atk":140,"def":110}
}
ZONES = {
    "meadow": ["Lamball", "Cattiva", "Chikipi", "Vixy", "Cremis"],
    "forest": ["Lifmunk", "Tanzee", "Daedream", "Rushoar", "Nox"],
    "lake": ["Fuack", "Pengullet", "Celaray", "Surfent", "Kelpsea"],
    "mountain": ["Eikthyrdeer", "Direhowl", "Digtoise", "Fenglope"],
    "volcano": ["Foxparks", "Arsox", "Blazamut", "Ragnahawk"],
    "sky": ["Nitewing", "Vanwyrm", "Helzephyr", "Jetragon"],
    "legendary": ["Paladius", "Necromus", "Frostallion"]
}

@commands.command(name="explore")
async def explore_command(ctx, zone: str = None):
    char = characters.get(ctx.author.id)
    if not char:
        await ctx.send("❌ You need a character first! Use `!createchar` to begin your adventure.")
        return

    # If no zone was chosen, show help menu
    if zone is None:
        await ctx.send(
            "🧭 **Palworld Exploration Guide** 🧭\n\n"
            "To explore, choose a zone:\n"
            "🌾 `!explore meadow`\n"
            "🌲 `!explore forest`\n"
            "🌊 `!explore lake`\n"
            "⛰️ `!explore mountain`\n"
            "🌋 `!explore volcano`\n"
            "☁️ `!explore sky`\n"
            "✨ `!explore legendary`\n\n"
            "Where would you like to go?"
        )
        return

    zone = zone.lower()
    if zone not in ZONES:
        await ctx.send(
            f"❌ **Unknown zone!**\n"
            f"Available zones: {', '.join(ZONES.keys())}"
        )
        return

    pal = random.choice(ZONES[zone])
    stats = PAL_STATS[pal]

    await ctx.send(
        f"🌍 **{ctx.author.name} travels to the {zone.title()}...**\n\n"
        f"🍃 The wind shifts… something is nearby.\n"
        f"🐾 A wild **{pal}** appears!\n\n"
        f"❤️ **HP:** {stats['hp']}   ⚔️ **ATK:** {stats['atk']}   🛡️ **DEF:** {stats['def']}\n\n"
        f"🎯 Type `!capture` to try catching it!\n"
        f"🏃 Type `!run` to flee."
    )
__all__ = ["explore_command"]
