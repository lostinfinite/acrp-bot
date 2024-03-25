import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord import Option
import asyncio

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

class A(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="Yes", style=discord.ButtonStyle.success) # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("You clicked the button!")
class B(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="No", style=discord.ButtonStyle.danger) # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("You clicked the button!")

@bot.slash_command(guild_ids=[1216934285668388966])
@discord.option("Requestor", description="Enter the requestors username.")
@discord.option("RP Type", description="What RP is being requested")
# @discord.InvalidArgument(view=MyView())
async def hello(ctx: discord.ApplicationContext, requestor: str, rp: str):
    # await ctx.respond("Choose a RP!", view=MyView(), ephemeral=True)
    await ctx.respond(f"Just to confirm you said: {requestor} requested permission to do the following whitelisted RP: {rp}",view=A(), ephemeral=True)
    await ctx.respond("Is this info incorrect?", view=B(), ephemeral=True)

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot_token = os.getenv("DISCORD_TOKEN")
if bot_token is None:
    print("Error: DISCORD_TOKEN environment variable is not set.")
else:
    bot.run(bot_token)