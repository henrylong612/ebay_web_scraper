# eBay Web Scraper

This GitHub repository contains my submission for project_03 of Mike Izbicki's CS40 class. Instructions for project_03 can be found [here](https://github.com/mikeizbicki/cmc-csci040/tree/2022fall/project_03).

My `ebay.dl` file converts eBay search queries into either `.json` or `.csv` files that denote the name of the item (`name`), the price of the item in cents (`price`), the status of the item in terms of whether it is used or new or whatnot (`status`), the price of shipping in cents (`shipping`), a boolean value for whether the item has free returns (`free_returns`), and the number of that item that have already been sold (`items_sold`).

To run the python file, use the following command line:
```
$ python3 ebay-dl.py 'bouncy ball'
```
where `'bouncy ball'` can be replaced by the search term of your choice. If your search term contains multiple words, be sure to use quotation marks! By deafult, the program downloads the first 10 pages of the eBay search query. If you wish to adjust this to your fancy, simply use the following command line:
```
$ python3 ebay-dl.py 'bouncy ball' --num_pages=5
```
where `5` can be replaced by the number of pages you want. By deafult, the program downloads the search queries in `.json` format. If you wish to change the download format to `.csv`, simply add the command line flag `--csv` like below:
```
$ python3 ebay-dl.py 'bouncy ball' --csv
```
