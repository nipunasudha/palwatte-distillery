import falcon
from waitress import serve
import json
from falcon_cors import CORS

cors = CORS(allow_all_origins=True)


class QuoteResource:
    def on_post(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': 'I\'ve always been more interested in the future than in the past.',
            'author': 'Grace Hopper'
        }

        resp.body = json.dumps(quote)


api = falcon.API(middleware=[cors.middleware])
api.add_route('/post', QuoteResource())
serve(api, host='127.0.0.1', port=5000)
print("I can do other stuff too")
