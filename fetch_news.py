#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests
import sys


def line_sender(message):
    URL = "https://notify-api.line.me/api/notify"
    headers = {'Authorization': 'Bearer ' + sys.argv[1]}
    payload = {'message': message}
    requests.post(URL, headers=headers, params=payload)


def main():
    URL = "https://news.yahoo.co.jp/"
    response = requests.get(URL)
    html = BeautifulSoup(response.text, "html.parser")
    texts = []

    for count in range(1, 8):
        selector = "li.sc-dNLxif:nth-child(" + str(count) + ")"
        href_selector = selector + " > a:nth-child(1)"
        texts.append("TITLE: " + html.select(selector)[0].get_text()+"\n")
        texts.append("URL: " + html.select(href_selector)
                     [0].get("href")+(2*"\n"))
    line_sender("".join(texts))


main()
