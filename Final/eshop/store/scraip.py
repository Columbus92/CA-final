from bs4 import BeautifulSoup
import requests


soup = BeautifulSoup(html, "html.parser")
print(type(soup))

x = soup.find_all(class_='special')
print(x)
y = soup.select('#first')
# print(y)

# html = requests.get(<a class="ks-new-product-image" href="/p/lempute-philips-led-a60-neutrali-balta-e27-8-w-806-lm/lmz3?mtd=search&amp;pos=regular&amp;src=searchnode"><img alt="Lemputė Philips LED, A60, neutrali balta, E27, 8 W, 806 lm" src="https://ksd-images.lt/display/aikido/cache/6bedefb27bb34ea35710c7f57db9bb00.jpeg?&amp;op=fit&amp;w=748&amp;h=540"></a>)
# print(html)

# for elementas in x:
#     print(elementas.text)

url="https://www.senukai.lt/c/isparduotuve/prekes-su-pazeista-pakuote/visos-prekes-su-pazeista-pakuote/tci"
responce = requests.get(url)

# print(responce.text)

senukai_html = responce.content

soup = BeautifulSoup(senukai_html, "html.parser")

image = soup.find_all(class_="catalog-taxons-product__image-anchor")

for x in image:
    print(x.find('img')['src'])

