import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord import Option
import asyncio
import logging

bot = discord.Bot()




@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="The ACRP Discord server"))

    # Fetch the channel by its ID
    channel_id = 1216935182788202597
    channel = bot.get_channel(channel_id)

    if channel:
        # Send the startup message
        await channel.send("Startup Sucessful")
    else:
        print(f"Channel with ID {channel_id} not found.")


embed = discord.Embed(
        title="Welcome!",
        description=("Startup has been successful! Thank you for using ACRP Util!"),
        color=discord.Colour.blurple(), # Pycord provides a class with default colors you can choose from
    )

embed.set_footer(text="ACRP! Thrive") # footers can have icons too

class A(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="Yes", style=discord.ButtonStyle.success) # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self, button, interaction):
         if interaction.channel.id == 1216935158628880475:
             
                await interaction.response.send_message(f"Someone asked a mod to log permission to play a whitelisted RP!, Heres the info {requestor} requested to do the following RP: {rp}", ephemeral=False)
         else:
            await interaction.response.send_message("This button is not allowed in this channel.", ephemeral=True)
class B(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="No", style=discord.ButtonStyle.danger) # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self, button, interaction):
         if interaction.channel.id == 1216935158628880475:
             
                await interaction.response.send_message("Cancelling...", ephemeral=True)
         else:
            await interaction.response.send_message("This button is not allowed in this channel.", ephemeral=True)
        

@bot.slash_command( description="Sends the bot's latency.", guild_ids=[1216934285668388966])
async def ping(ctx): # a slash command will be created with the name "ping"
    await ctx.respond(f"Pong! Latency is {bot.latency}")

@bot.slash_command(description="Account Creation Date", guild_ids=[1216934285668388966])  # create a user command for the supplied guilds
async def account_creation_date(ctx, member: discord.Member):  # user commands return the member
    await ctx.respond(f"{member.name}'s account was created on {member.created_at}")

@bot.user_command(name="Account Creation Date", guild_ids=[1216934285668388966])  # create a user command for the supplied guilds
async def account_creation_date(ctx, member: discord.Member):  # user commands return the member
    await ctx.respond(f"{member.name}'s account was created on {member.created_at}")

@bot.message_command(name="Get Message ID", guild_ids=[1216934285668388966])  # creates a global message command. use guild_ids=[] to create guild-specific commands.
async def get_message_id(ctx, message: discord.Message):  # message commands return the message
    await ctx.respond(f"Message ID: `{message.id}`")

@bot.slash_command(description="Get Message ID", guild_ids=[1216934285668388966])  # creates a global message command. use guild_ids=[] to create guild-specific commands.
async def get_message_id(ctx, message: discord.Message):  # message commands return the message
    await ctx.respond(f"Message ID: `{message.id}`")

@bot.slash_command(description="Sets the slowmode of the current channel", guild_ids=[1216934285668388966])
@commands.has_permissions(manage_messages = True)
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.respond(f"Set the slowmode delay in this channel to {seconds} seconds!", ephemeral=True)
    await ctx.send(f"@here Slowmode has been set to {seconds} seconds via bot by <@{ctx.author.id}>.")

@bot.slash_command(description="Bans a member", guild_ids=[1216934285668388966])
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.respond(f"Done, <@{ctx.author.id}> Banned <@{member.id}>")
    if member is None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself")
        return
    
@bot.slash_command(name="dm", description="Sends a DM to a user")
#@commands.has_permissions(Administrator = True)
async def direct(ctx, user: discord.User, *, message=None):
    message = message or "This Message is sent via DM"
    await user.send(f"{message} ~ Signed <@{ctx.author.id}>")
    await ctx.respond("Completed!", ephemeral=True)
    await ctx.send(f"<:important_mod:1222378567598342235> <@{user.id}> An important message form the mods have been sent to your DMs")

# @bot.slash_command(guild_ids=[1216934285668388966])
#@discord.option("Requestor", description="Enter the requestor's username.")
#@discord.option("RP Type", description="What RP is being requested")
#async def hello(ctx: discord.ApplicationContext, requestor: str, rp: str):
    # Accessing the values provided by the user through ctx
 #   requestor_username = requestor
  #  rp_type = rp
#
 #   await ctx.respond(f"Just to confirm, you said: {requestor_username} requested permission to do the following whitelisted RP: {rp_type}", ephemeral=True)
  #  await ctx.respond("Is this information correct?", ephemeral=True)
logging.basicConfig(level=logging.INFO) 
load_dotenv("/.env")
TOKEN = os.getenv("DISCO_TOKEN")
bot_token = os.getenv("DISCO_TOKEN")
load_dotenv()
bot_token = os.getenv("DISCO_TOKEN")
print("Bot Token from .env:", bot_token)
if bot_token is None:
    print("Error: DISCO_TOKEN environment variable is not set.")
else:
    logging.info("Token to be used: " + bot_token)
    bot.run(bot_token)
# if you re-load your token then edit the value of .env to update your token
# Example change it from: IDSCORD_TOKEN=MTYblahblahblah to: disco_token=TOKENNEW