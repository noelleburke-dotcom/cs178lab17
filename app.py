from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<h1>Here is a joke! </h1>" \
           "<h2>What's the best thing about Switzerland? The flag is a big plus. </h2>" \
           '<img src="https://imgs.xkcd.com/comics/containers.png">'
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)