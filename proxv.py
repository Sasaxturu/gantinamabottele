
import httpx
import logging
import time
import telebot

API_TOKEN = "8096803805:AAHCvaDwbEYKzeA3AjOh_a6L6X4LmgZPkOQ"
USER_ID = "-1002168419067"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("log.txt"),
    ]
)

bot = telebot.TeleBot(API_TOKEN)

def fetch_and_send_proxies():
    try:
        proxy_sources = [
            "https://shared-proxy-id.xcddos.xyz","https://raw.githubusercontent.com/zevtyardt/proxy-list/main/all.txt","https://sunny9577.github.io/proxy-scraper/generated/socks5_proxies.txt","https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt","https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/xResults/Proxies.txt","https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/xResults/RAW.txt","https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks5.txt","https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&proxy_format=protocolipport&format=text","https://api.mxflower.eu.org/abib/proxy.txt","https://raw.githubusercontent.com/tuanminpay/live-proxy/master/all.txt"
        ]

        all_proxies = []
        for source in proxy_sources:
            response = httpx.get(source)
            if response.status_code == 200:
                all_proxies.extend(response.text.splitlines())
            else:
                logging.error(f"Failed to fetch proxies from {source}")

        # Filter empty elements
        all_proxies = list(filter(None, all_proxies))

        proxy_count = len(all_proxies)
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

        # Create descriptive message
        message = f"Count: {proxy_count}\n" \
                  f"Time: {timestamp}\n" \
                  f"Free Proxy On @sxudiaproxy\n\n"\
                  f"𝗦𝗫𝗨𝗗𝗜𝗔||𝗽𝗥𝗢𝗫𝗬"

        # Save proxies to file
        with open("proxy.txt", 'w') as file:
            file.write('\n'.join(all_proxies))

        # Send message and file together
        with open("proxy.txt", 'rb') as file:
            bot.send_document(USER_ID, file, caption=message)

    except Exception as e:
        logging.error(f"Error: {str(e)}")

# Schedule the task
if __name__ == "__main__":
    interval = 240
    while True:
        try:
            fetch_and_send_proxies()
            time.sleep(interval)
        except Exception as e:
            logging.error(f"Error in main loop: {str(e)}")
            time.sleep(60)  # Retry after 60 seconds on error 
