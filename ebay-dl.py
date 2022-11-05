import argparse
import requests
from bs4 import BeautifulSoup
import json
import csv

def parse_items_sold(text):
    '''
    Takes as input a string and returbns the number of items sold as specified in the string

    >>> parse_items_sold('872 sold')
    872
    >>> parse_items_sold('2 watchers')
    
    >>> parse_items_sold('Almost gone')
    
    '''
    numbers=''
    for c in text:
        if c in '1234567890':
            numbers+=c
    if 'sold' in text:
        return int(numbers)
    else:
        return None

def parse_price(text):
    '''
    >>> parse_price('$219.99')
    21999
    >>> parse_price('$0.99 to $39.98')
    99
    >>> parse_price('Tap item to see current priceSee price')
    
    '''
    numbers=''
    if text[0]=='$':
        for c in text:
            if c in '1234567890':
                numbers+=c
            elif c==' ':
                break
        return int(numbers)
    else:
        return None

def parse_shipping(text):
    '''
    >>> parse_shipping('Free shipping')
    0
    >>> parse_shipping('+$10.60 shipping')
    1060
    >>> parse_shipping('+$5.99 shipping')
    599
    '''
    numbers=''
    if text[0]=='+':
        for c in text:
            if c in '1234567890':
                numbers+=c
            elif c==' ':
                break
        return int(numbers)
    else:
        return 0


#only run code below when python is run normally
if __name__=='__main__':


    #get search term from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('search_term')
    parser.add_argument('--num_pages',default=10)
    parser.add_argument('--csv',action='store_true')
    #fixme
    args = parser.parse_args()

    items=[]
    for page_number in range(1,int(args.num_pages)+1):

        #progress report
        print('starting page '+str(page_number))

        #build url
        url='https://www.ebay.com/sch/i.html?_from=R40&_nkw='
        url+=args.search_term
        url+='&_sacat=0&LH_TitleDesc=0&_pgn='
        url+=str(page_number)
        url+='&rt=nc'

        #download html
        r = requests.get(url)
        html = r.text

        #process html
        soup=BeautifulSoup(html,'html.parser')

        tags_items=soup.select('.s-item')

        for tag_item in tags_items[1:]:

            tags_name=tag_item.select('.s-item__title')
            name=None
            for tag in tags_name:
                name=tag.text

            tags_price=tag_item.select('.s-item__price')
            price=None
            for tag in tags_price:
                price=parse_price(tag.text)

            tags_status=tag_item.select('.SECONDARY_INFO')
            status=None
            for tag in tags_status:
                status=tag.text
            
            tags_shipping=tag_item.select('.s-item__shipping, .s-item__freeXDays')
            shipping=None
            for tag in tags_shipping:
                shipping=parse_shipping(tag.text)

            tags_free_returns=tag_item.select('.s-item__free-returns')
            free_returns=False
            for tag in tags_free_returns: 
                free_returns=True

            items_sold=None
            tags_items_sold=tag_item.select('.s-item__hotness, .s-item__additionalItemHotness')
            for tag in tags_items_sold:
                if tag:
                    items_sold=parse_items_sold(tag.text)
                else:
                    items_sold=0

            item={
                'name': name,
                'price': price,
                'status': status,
                'shipping': shipping,
                'free_returns': free_returns,
                'items_sold': items_sold
            }
            items.append(item)

    if args.csv==True:
        field_names=list(items[0].keys())
        filename=args.search_term+'.csv'
        with open(filename,'w',encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(items)
    else:
        filename=args.search_term+'.json'
        with open(filename,'w',encoding='utf-8') as f:
            f.write(json.dumps(items))



