import os;
import discord;
token="";
prefix="/";

bot = discord.Client()

@bot.event
async def on_message(mes):
    resu=mes.content;
    if str(resu)=="test":
        await bot.send_message(mes.channel,"message resu 5/5");
bot.run(token);
os.system('pause');
