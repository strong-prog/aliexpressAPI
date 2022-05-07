import requests
import xml.etree.ElementTree as ET


class ProviderGateway:

    @staticmethod
    def get():
        response = requests.get('http://stripmag.ru/datafeed/p5s_full_stock.xml')
        root = ET.fromstring(response.text)
        product_dict = {}

        for product in root.findall('product'):
            product_id = product.get('prodID')
            product_price = product.find('price')
            product_assort = product.find('assortiment/assort')

            product_dict[product_id] = {
                'price': {
                    'retail': product_price.get('RetailPrice'),
                    'base_retail': product_price.get('BaseRetailPrice'),
                    'whole': product_price.get('WholePrice'),
                    'base_whole': product_price.get('BaseWholePrice')},
                'sklad': product_assort.get('sklad')}

        return product_dict
