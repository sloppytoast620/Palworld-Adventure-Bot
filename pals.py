from discord.ext import commands
from characters import characters  # Import character storage

# Deterministic zones
zones = {
    "forest": "Flufftail",
    "lake": "Splashfin",
    "mountain": "Rockhorn"
}

# ---- Explore Command ----
@commands.command(name="explore")
async def explore_command(ctx, zone: str):
    char = characters.get(ctx.author.id)
    if not char:
        await ctx.send("You need to create a character first! Use !createchar.")
        return

    zone = zone.lower()
    if zone not in zones:
        await ctx.send(f"Unknown zone! Available zones: {', '.join(zones.keys())}")
        return

    pal = zones[zone]

    await ctx.send(
        f"You explored the **{zone.title()}**.\n"
        f"You encountered a {pal}!\n"
        f"Exploration successful!"
    )
