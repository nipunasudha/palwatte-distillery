import falcon
from waitress import serve
import json
from falcon_cors import CORS
import pprint
from falcon_multipart.middleware import MultipartMiddleware

cors = CORS(allow_all_origins=True)
print("Initialized.")


class QuoteResource:
    def on_post(self, req, resp):
        """Handles POST requests"""
        quote = {
            'quote': 'I\'ve always been more interested in the future than in the past.',
            'author': 'Grace Hopper'
        }
        print(req._param("cmd"))
        resp.body = json.dumps(quote)


api = falcon.API(middleware=[cors.middleware, MultipartMiddleware()])
api.add_route('/post', QuoteResource())
serve(api, host='127.0.0.1', port=5000)
print("Server stopped.")
