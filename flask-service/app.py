from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>Hello {name} from {service_name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "world"), 
                       service_name=os.getenv("SERVICE_NAME", "flask-service"),
                       hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
