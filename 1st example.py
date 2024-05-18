import pyqrcode
import png
from pyqrcode import QRCode

address = 'https://suchen.mobile.de/fahrzeuge/details.html?id=371975378&damageUnrepaired=NO_DAMAGE_UNREPAIRED&isSearchRequest=true&pageNumber=1&scopeId=C&sortOption.sortBy=relevance&action=topOfPage&top=1:1&searchId=e6e567d8-0cfd-5800-0212-4f4f9682fc83&ref=srp'
url = pyqrcode.create(address)
url.png('audi', scale=8)