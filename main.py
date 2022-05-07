from downloaders.provider import ProviderGateway
from downloaders.feed import FeedGateway
from updater import UpdateAliexpress
import xml.etree.ElementTree as ET

market_feed = ET.fromstring(FeedGateway().get())

products_from_provider = ProviderGateway().get()

for product_feed in market_feed.findall('shop/offers/offer'):
    product_id_feed = product_feed.attrib['id']
    if str(product_id_feed) in products_from_provider:
        if UpdateAliexpress().update(products_from_provider[str(product_id_feed)], product_feed):
            print('success update')
        else:
            print('error update')
