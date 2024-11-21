import feedparser
import time_data
import translate_google as tg
import HTT
from balethon import Client
from balethon.conditions import private
from balethon import errors
import asyncio
import download_img as dimg
import data_json

bot = Client("551782720:6CAPNpLG32GDxRj1qdP7dtRDh1eZVHQlGgQatBD1")

async def news_game():
    news = 0
    feed = feedparser.parse("https://www.ign.com/rss/articles/feed?tags=games")
    num_entries = 10
    print(len(feed.entries[:num_entries]))
    for idx, entry in enumerate(reversed(feed.entries[:num_entries]), start=1):
        if data_json.add_new_id("news.json", entry.id) == "True":
            news = news + 1
            texts = '*' + tg.translate('fa', entry.title).replace("بخار", "Steam") + ' *' + '\n\n' + tg.translate('fa', entry.summary).replace("بخار", "Steam") + '\n' + "[لینک کامل خبر در سایت ign.com](" + str(entry.links[0]['href']) + ")"
            texts = texts + '\n' + '#news_game #news #game' + '\n' + "@mmd_own"
            dimg.download_image(entry.media_content[0]['url'], '1.png')
            await bot.send_photo('4470309968', '1.png', texts)
    if news > 0:
        await bot.send_message('325093153', "تعداد اخبار جدید : " + str(news))
        data = await bot.send_document('140932460', 'news.json')
        await bot.forward_message('325093153', '140932460', data.id)

async def review_game():
    news = 0
    feed = feedparser.parse("https://www.ign.com/rss/articles/feed?tags=review%2Cgame")
    num_entries = 10
    print(len(feed.entries[:num_entries]))
    for idx, entry in enumerate(reversed(feed.entries[:num_entries]), start=1):
        if data_json.add_new_id("review.json", entry.id) == "True":
            news = news + 1
            texts = '*' + tg.translate('fa', entry.title).replace("بخار", "Steam") + ' *' + '\n\n' + tg.translate('fa', entry.summary).replace("بخار", "Steam") + '\n' + "[لینک کامل خبر در سایت ign.com](" + str(entry.links[0]['href']) + ")"
            texts = texts + '\n' + '#review_game #review #game' + '\n' + "@mmd_own"
            dimg.download_image(entry.media_content[0]['url'], '1.png')
            await bot.send_photo('4470309968', '1.png', texts)
    if news > 0:
        await bot.send_message('325093153', "تعداد برسی جدید : " + str(news))
        data = await bot.send_document('140932460', 'review.json')
        await bot.forward_message('325093153', '140932460', data.id)

@bot.on_initialize()
async def task(client):
    await client.send_message('325093153', 'بات اجرا شد')
    while True:
        await client.send_message('325093153', "چک کردن اخبار")
        await news_game()
        await client.send_message('325093153', "چک کردن برسی های گیم")
        review_game()
        await asyncio.sleep(900)

@bot.on_message(private)
async def answer_message(message):
    print(message)
    if message.chat.id == 325093153 or message.chat.id == 521884708 :
        await message.reply("به مولا بیدارم")
    else:
        await message.reply("بات اخبار گیمینگ \nساخته شده توسط بلوتون")


bot.run()