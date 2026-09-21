from http.server import BaseHTTPRequestHandler, HTTPServer
from pymongo import MongoClient
import json

client = MongoClient("mongodb://mongodb:27017/")
db = client["profile_db"]
collection = db["profiles"]

default_profile = {
    "name": "陳彥妤",
    "studentId": "11311113",
    "department": "資訊工程學系",
    "email": "你的電子郵件",
    "about": "就讀台東大學資訊工程學系"
}

if collection.count_documents({}) == 0:
    collection.insert_one(default_profile)


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/api/profile":
            profile = collection.find_one({}, {"_id": 0})

            self.send_response(200)
            self.send_header(
                "Content-Type",
                "application/json; charset=utf-8"
            )
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            self.wfile.write(
                json.dumps(
                    profile,
                    ensure_ascii=False
                ).encode("utf-8")
            )
        else:
            self.send_response(404)
            self.end_headers()

    def do_PUT(self):
        if self.path == "/api/profile":
            content_length = int(
                self.headers.get("Content-Length", 0)
            )

            body = self.rfile.read(content_length)

            try:
                data = json.loads(body.decode("utf-8"))

                collection.update_one(
                    {},
                    {"$set": data}
                )

                profile = collection.find_one({}, {"_id": 0})

                self.send_response(200)
                self.send_header(
                    "Content-Type",
                    "application/json; charset=utf-8"
                )
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()

                self.wfile.write(
                    json.dumps(
                        profile,
                        ensure_ascii=False
                    ).encode("utf-8")
                )

            except Exception as e:
                self.send_response(400)
                self.send_header(
                    "Content-Type",
                    "application/json; charset=utf-8"
                )
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()

                self.wfile.write(
                    json.dumps({
                        "error": str(e)
                    }).encode("utf-8")
                )
        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header(
            "Access-Control-Allow-Methods",
            "GET, PUT, OPTIONS"
        )
        self.send_header(
            "Access-Control-Allow-Headers",
            "Content-Type"
        )
        self.end_headers()


server = HTTPServer(("0.0.0.0", 5000), Handler)

print("Backend server running on port 5000...")
server.serve_forever()
