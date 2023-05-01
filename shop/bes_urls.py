class BES_Urls:
    def __init__(self):
        self.back_end_server_host = "194.87.99.230"
        self.back_end_server_port = 5002
        self.back_end_server_url = "http://{}:{}".format(self.back_end_server_host, self.back_end_server_port)

    def get_basket_location_url(self, basketId):
        return "{}/baskets/{}".format(self.back_end_server_url, basketId)

    def get_url_for_posting_basket(self):
        return "{}/baskets".format(self.back_end_server_url)

    def get_url_for_posting_invoice(self):
        return "{}/invoices".format(self.back_end_server_url)