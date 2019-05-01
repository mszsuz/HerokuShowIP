from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def main_route():
    return 'Salaam. Your IP is: %s' % request.remote_addr


if __name__ == '__main__':
    port_number = 8080
    app.run('0.0.0.0', port_number, threaded=True, debug=__debug__)
