import asyncio
import subprocess
import random
from datetime import datetime

from telethon import TelegramClient, events
from telethon.tl.functions.messages import SetTypingRequest
from telethon.tl.functions.account import UpdateProfileRequest


api_id = '26265545'
api_hash = '4700f72987c9b8d2cc4be156860f1720'

client = TelegramClient('name_session', api_id, api_hash)

# 
async def auto_change_name():
    names = [
        '᭖͜͡𝘼𝙗𝙞𝙗 𝙆𝙖𝙘𝙖𝙬🌌',
        '𝐒𝐗𝐔𝐃𝐈𝐀 𝐒𝐓𝐑𝐄𝐄𝐒𝐄𝐑🌌',
        '𝐥𝐨𝐯𝐞𝐧𝐜𝐡𝐢𝐢💋💗',
        '𝑨𝑩𝑰𝑩 𝑺𝒀𝑵🌪️💥'
    ]
    index = 0
    while True:
        new_name = names[index % len(names)]
        try:
            await client(UpdateProfileRequest(first_name=new_name))
            print(f"[{datetime.now()}] Changed profile name to: {new_name}")
        except Exception as e:
            print(f"[{datetime.now()}] Error updating profile name: {e}")
        index += 1
        await asyncio.sleep(100)

async def main():
    asyncio.create_task(auto_change_name())
    print("Auto name changer started.")
    await client.run_until_disconnected()
    
client.start()
client.loop.run_until_complete(main())