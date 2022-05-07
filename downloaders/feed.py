import requests


class FeedGateway:

    @staticmethod
    def get():
        response = requests.get('http://alitair.1gb.ru/Intim_Ali_allfids_2.xml')
        return response.text
