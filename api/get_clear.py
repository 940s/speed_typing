from http.server import BaseHTTPRequestHandler
from speed_typing.back_end.logic import Logic
import json
from urllib import parse

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()

    logic = Logic()
    text = logic.clear_json()
    obj = {"hi_scores": "cleared"}
    message = json.dumps(obj)
    self.wfile.write(message.encode())

    return 