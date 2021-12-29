from http.server import BaseHTTPRequestHandler
import json
from http.server import HTTPStatus
from speed_typing.back_end.logic import Logic

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        datalen = int(self.headers["Content-Length"])
        data = self.rfile.read(datalen)
        input_obj = json.loads(data)

        logic = Logic()
        wpm = logic.calculate_wpm(input_obj['original'], input_obj['comparison'], input_obj['time'])
        accuracy = logic.calculate_accuracy(input_obj['original'], input_obj['comparison']) 
        output_obj = {
                    "wpm": f"{wpm}", 
                    "accuracy": f"{accuracy}"
                    }


        self.send_response(HTTPStatus.OK)
        self.end_headers()
        message = json.dumps(output_obj)
        self.wfile.write(message.encode())