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

        logic.write_hi_score(input_obj['wpm'], input_obj['accuracy']) 
        output_obj = {
                    "hi_scores": logic.get_hi_score()
                    }


        self.send_response(HTTPStatus.OK)
        self.end_headers()
        message = json.dumps(output_obj)
        self.wfile.write(message.encode())