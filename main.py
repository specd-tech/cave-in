import httpx
from httpx import RequestError
from time import sleep
from os import system

# list interfaces: netsh interface show interface

ip = ""
url = "https://api.ipify.org"
poll_rate = 1

transport = httpx.HTTPTransport(retries=1)
client = httpx.Client(transport=transport)


def disable_network():
    system('netsh interface set interface "Local Area Connection" DISABLED')


try:
    while True:
        response = client.get(url)

        if response.text != ip:
            disable_network()
        else:
            sleep(poll_rate)

except RequestError:
    disable_network()

finally:
    client.close()
