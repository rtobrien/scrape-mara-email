# scrape-mara-email
A scraping project for pulling publicly available info from an Australian government website. An initial json object is collected from which URLs with subsequent data are collected and requested. Writes to a CSV. Format can be edited as necessary.

Run from either command line or shell (python main.py). Code can be interrupted and will restart, built in due to poor internet connections. Backup file will automatically be saved after ~100 successful requests.
