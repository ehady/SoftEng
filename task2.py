import requests
from bs4 import BeautifulSoup

url = "https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/warszawa/?search%5Bdistrict_id%5D=377&search" \
      "%5Bfilter_enum_builttype%5D%5B0%5D=blok&search%5Bfilter_enum_market%5D%5B0%5D=secondary&search" \
      "%5Bfilter_float_m%3Afrom%5D=40&search%5Bfilter_float_price%3Afrom%5D=400000&search%5Bfilter_float_price%3Ato" \
      "%5D=500000&search%5Border%5D=created_at%3Adesc"

response = requests.get(url)

tree = BeautifulSoup(response.content, 'html.parser')

listings = tree.findAll('div', {'data-testid': 'listing-grid'})

prices = []
all_listings = []

for listing in listings[0]:
    all_listings.append(listing)
    price_element = listing.find('p', {'data-testid': 'ad-price'})
    if price_element:
        prices.append(price_element.getText())

print(len(all_listings))
print(prices)

min_price = min(prices)
max_price = max(prices)

print(min_price)
print(max_price)

# prices = []

# for price in listings:
#   prices.append(price.getText())

# print(prices)


# listings = tree.findAll('p', class_='css-10b0gli er34gjf0')
