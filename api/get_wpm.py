from http.server import BaseHTTPRequestHandler
from speed_typing.back_end.logic import Logic
from urllib import parse
import json

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()

    path = self.path
    url_components = parse.urlsplit(path)
    query_string_list = parse.parse_qsl(url_components.query)
    query = dict(query_string_list)

    logic = Logic()

    wpm = logic.calculate_wpm(query.original, query.comparison, query.time)
    accuracy = logic.calculate_accuracy(query.original, query.comparison)

    obj = {'wpm': f'{wpm}', 'accuracy': f'{accuracy}'}
    message = json.dumps(obj)
    self.wfile.write(message.encode())

    return
