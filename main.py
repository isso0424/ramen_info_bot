import discord
import toke
import datetime
TOKEN = toke.toke()
client = discord.Client()

regular_holiday = {
    "現代": [1],
    "大進": [0, 1],
    "えむず": [0],
    "むじゃき": [3],
    "つしま": [2],
    "ななや": [],
    "俺の麺": [],
    "精福楼": [2],
    "しゅう": [],
    "かつじゅん": [0],
    "ダルニー食堂": [6],
    "らーめんどう楽": [],
    "虎ノ道": [1],
    "大大": [1]
}
# 大大が火曜休みの週
daidai = [2, 4]


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content[0] == "/":
        mess = message.content[1:]
        if "Ramen" in mess:
            ramen_list = ramen()
            if mess in " ":
                shop = mess[6:]
                if shop in ramen_list:
                    await message.channel.send("{}は今日やっています".format(shop))
                else:
                    await message.channel.send("{}は今日やっていません".format(shop))
            send_text = "今日やっているラーメン屋は\n"
            for r in ramen_list:
                send_text += r + "\n"
            send_text += "です"
            await message.channel.send(send_text)
        else:
            await message.channel.send("Error: Input invalid command.\nPlease check command list to type \"/help\"")


def ramen():
    today_weekday = datetime.date.today().weekday()
    day = int(datetime.date.today().day)
    week = get_today_week(day)
    today_shop_list = []
    for shop, holiday in regular_holiday.items():
        if today_weekday in holiday or shop == "大大" and week in daidai and today_weekday == 1:
            continue
        today_shop_list.append(shop)
    return today_shop_list


def get_today_week(day):
    n = day
    week = 0
    while n > 0:
        week += 1
        n -= 7
    return week


client.run(TOKEN)
