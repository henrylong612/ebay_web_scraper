# project_03

This GitHub repository contains my submission for project_02 of Mike Izbicki's CS40 class. Instructions for project_02 can be found [here](https://github.com/mikeizbicki/cmc-csci040/tree/2022fall/project_03).

My `ebay.dl` file converts eBay search queries into either `.json` or `.csv` files that denote the name of the item (`name`), the price of the item in cents (`price`), the status of the item in terms of whether it is used or new or whatnot (`status`), the price of shipping in cents (`shipping`), a boolean value for whether the item has free returns (`free_returns`), and the number of that item that have already been sold (`items_sold`).

On my computer, to run the python file, I use the following command line (the first part of the command line will vary based on your computer model and file storage):
```
Henrys-MacBook-Air-4:project_03 hankilong$ /usr/local/bin/python3 "/Users/hankilong/Documents/Henry Long Claremont McKenna College/CMC Sophomore/FA 2022/CSCI/project_03/ebay-dl.py" 'bouncy ball'
```
where `'bouncy ball'` can be replaced by the search term of your choice. If your search term contains multiple words, be sure to use quotation marks! By deafult, the program downloads the first 10 pages of the eBay search query. If I want to adjust this to my fancy, I simply use the following command line:
```
Henrys-MacBook-Air-4:project_03 hankilong$ /usr/local/bin/python3 "/Users/hankilong/Documents/Henry Long Claremont McKenna College/CMC Sophomore/FA 2022/CSCI/project_03/ebay-dl.py" 'bouncy ball' --num_pages=5
```
where `5` can be replaced by the number of pages of your choice. By deafult, the program downloads the search queries in `.json` format. If I want to change the download format to `.csv`, I simply use the following command line:
```
Henrys-MacBook-Air-4:project_03 hankilong$ /usr/local/bin/python3 "/Users/hankilong/Documents/Henry Long Claremont McKenna College/CMC Sophomore/FA 2022/CSCI/project_03/ebay-dl.py" 'bouncy ball' --csv=True
```
In this case, I can replace `True` with any "truthy" python value. 
