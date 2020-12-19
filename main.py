import requests
import os

def Delete(webhook):
    try:
        r = requests.delete(webhook)
        if r.status_code == 204:
            print('\033[92m>\033[39m Deleted\033[92m:\033[39m %s' % (webhook))
            os.system('pause >NUL')
            os._exit(0)
        elif r.status_code == 404:
            print('\033[91m>\033[39m Invalid Webhook!')
            os.system('pause >NUL')
            os._exit(0)
        else:
            pass
    except:
        pass            

if __name__ == "__main__":
    os.system('cls & title [Webhook Deleter] By Dropout')
    print('\033[92m>\033[39m Webhook\033[92m:\033[39m ', end='')
    webhook = input()
    Delete(webhook)
