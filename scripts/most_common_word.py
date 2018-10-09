#!/usr/bin/env python
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation
import requests
import sys
import re


def main():
    url = sys.argv[1]

    response = requests.get('http://{}'.format(url))

    data = response.content

    soup = BeautifulSoup(data, features='html.parser')

    joined_text = (''.join(s.findAll(text=True)) for s in soup.body.findAll())

    c = Counter((x.rstrip(punctuation).lower() for y in joined_text for x in y.split()))

    print("Most common word: {}".format(c.most_common(1)[0][0]))


if __name__ == '__main__':
    main()

