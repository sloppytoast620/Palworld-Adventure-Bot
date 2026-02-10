from discord.ext import commands

# In-memory storage for characters
characters = {}

#startwrs
starter_list = ["Paldachu", "Flamifox", "Aquabun", "Leafleon"]


@commands.command(name="createchar")
async def create_character_command(ctx, name: str, starter: str, pclass: str = "Explorer"):
    if ctx.author.id in characters:
        await ctx.send("You already have a character!")
        return

    if starter not in starter_list:
        await ctx.send(
            f"Invalid starter! Choose one of: {', '.join(starter_list)}"
        )
        return

    characters[ctx.author.id] = {
        "name": name,
        "starter": starter,
        "class": pclass
    }

    await ctx.send(
        f"**Character Created!**\n"
        f"Name: {name}\n"
        f"Starter Pal: {starter}\n"
        f"Class: {pclass}\n"
        f"Available starters: {', '.join(starter_list)}"
    )

@commands.command(name="charinfo")
async def character_info_command(ctx):
    char = characters.get(ctx.author.id)
    if not char:
        await ctx.send("⚠️ You don't have a character yet! Use `!createchar` to begin your adventure.")
        return

    await ctx.send(
        f"📜 **Your Palworld Trainer Card** 📜\n\n"
        f"👤 **Name:** {char['name']}\n"
        f"🐾 **Starter Pal:** {char['starter']}\n"
        f"🎒 **Class:** {char['class']}\n\n"
        f"🌍 Use `!explore` to find wild Pals!"
    )

@commands.command(name="explore")
async def explore_command(ctx, zone: str):
    char = characters.get(ctx.author.id)
    if not char:
        await ctx.send("❌ Create a character first with `!createchar`")
        return

    zone = zone.lower()
    if zone not in ZONES:
        await ctx.send(f"🌍 Available zones: {', '.join(ZONES.keys())}")
        return

    pal = random.choice(ZONES[zone])
    stats = PAL_STATS[pal]

    await ctx.send(
        f"🌍 **{ctx.author.name} explores the {zone.title()}...**\n\n"
        f"🐾 A wild **{pal}** appears!\n"
        f"❤️ HP: {stats['hp']}  ⚔️ ATK: {stats['atk']}  🛡️ DEF: {stats['def']}\n\n"
        f"Type `!capture` to try catching it!"
    )
