import modules.status as status
import modules.webhook as webhook
import time


stat = status.get_status()

last = webhook.send_status_webhook(stat)

while True:
    time.sleep(300)
    webhook.delete_id(last)
    last = webhook.send_status_webhook(stat)

