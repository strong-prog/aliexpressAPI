from top import api, appinfo


class UpdateAliexpress:

    def update(self, from_provider, from_feed):
        try:
            request_data = {
                'product_id': from_feed.attrib['ae_intim4_id'],
                'sku_info_list': [
                    {
                        'price': from_provider['price']['retail'],
                        'inventory': from_provider['sklad']
                    }
                ]
            }

            return self.send_request(request_data)
        except:
            return False

    @staticmethod
    def send_request(request_data):
        url = 'gw.api.taobao.com'
        port = 80

        appkey = 'xxxxxxxx'
        secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        sessionkey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

        req = api.AliexpressSolutionProductEditRequest(url, port)
        req.set_app_info(appinfo(appkey, secret))

        req.edit_product_request = request_data

        resp = req.getResponse(sessionkey)

        return 'aliexpress_solution_product_edit_response' in resp


