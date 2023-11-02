import json
import requests
import logging


class QuoteService:
    QUOTE_URL = "https://zenquotes.io/api/random"

    @staticmethod
    def get_quote():
        logging.debug(f"Getting quote from {QuoteService.QUOTE_URL}")
        response = requests.get(QuoteService.QUOTE_URL)
        json_data = json.loads(response.text)
        logging.debug(f"Response = {json_data}")
        quote = json_data[0]["q"] + " -" + json_data[0]["a"]
        return quote
