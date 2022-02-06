
USPS-adress validation
==============================

This scraper reads a csv-file of addresses (Input.csv), and submits them to USPS-site to check if they are valid or not and write result in Output.csv

(app using `requests` and `pandas`)

URL usps-site
----
https://tools.usps.com/zip-code-lookup.htm?byaddress

Installation and run
---

```
$ pip install -r requirements.txt
```
    
```
python main.py
```
