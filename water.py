import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Please drink water now!",
            message = "About 20 cups (3.7 liters) of fluids for men.",
            # app_icon = "water.ico",
            timeout = 100
        )
        time.sleep(60*60)