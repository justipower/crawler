import requests
import resp as resp
from bs4 import BeautifulSoup

soup = BeautifulSoup(resp.text, 'lxml')

soup = BeautifulSoup(open('index.html'))

with open("index.html") as f:
    soup = BeautifulSoup(f)