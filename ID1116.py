#!/usr/bin/python3
from bs4 import BeautifulSoup

input_data = ""
try:
    while(1):
        input_data += input()
except EOFError:
    pass

soup = BeautifulSoup(input_data, 'html.parser')

print(soup.prettify())