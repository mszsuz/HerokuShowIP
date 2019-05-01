from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def main_route():
    responses = []
    responses.extend(['X-Forwarded-For', request.headers.get('X-Forwarded-For')])
    responses.extend(['HTTP_X_FORWARDED_FOR', request.headers.get('HTTP_X_FORWARDED_FOR')])
    responses.extend(['REMOTE_ADDR', request.headers.get('REMOTE_ADDR')])
    responses.extend(['X-Real-IP', request.headers.get('X-Real-IP')])
    responses.extend(['X-Real-IP', request.headers.get('X-Real-IP')])
    responses.extend(['FLASK.remote_addr', request.remote_addr])
    return 'Salaam. Your IP is: \r\n%s' % ', '.join(str(i) for i in responses)


if __name__ == '__main__':
    port_number = 8080
    app.run('0.0.0.0', port_number, threaded=True, debug=__debug__)
