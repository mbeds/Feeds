#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import libraries
import urllib2
from bs4 import BeautifulSoup

# specify the url
url = "http://www.bondwolfeauctions.com/auction/1537/?status=unsold&show=-1&location=&radius=&type=&minprice=&maxprice=&orderby=lotnumber&auction_id=null"
page = urllib2.urlopen(url)

soup = BeautifulSoup(page)
