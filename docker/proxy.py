from datetime import datetime
import flask
from flask import request, Response
import requests
import threading
import remote_code_execution_detection
import bruteForce_dos_sessionPrediction_detection
import elasticsearch_functions
import get_config_data
import devices_detection

ERROR = 401
LOCALHOST = '127.0.0.1'
COOKIE_NAME = 'session'

app = flask.Flask(__name__)


def check_request(request):
    """
    Check if the user block the request.
    :param request: the request.
    :type request: class 'werkzeug.local.LocalProxy'.
    :return: if the request block.
    :rtype: bool.
    """
    blocks = get_config_data.get_blocks()

    if request.remote_addr is blocks["ip"]:
        return True
    elif str(request.environ.get('REMOTE_PORT')) is blocks["port"]:
        return True

    return False


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    data = ''
    exception = False
    request_url = f"http://{LOCALHOST}:{get_config_data.get_server_port()}/{path}"

    if check_request(request):
        return flask.abort(ERROR)

    bruteForce_dos_sessionPrediction_detection.add_request(str(request))

    if request.form:
        data = request.form.to_dict(flat=False)

    try:
        r = requests.request(request.method, request_url, headers=request.headers, cookies=request.cookies, data=data, timeout=10)  # send the request to the server
        response_data = r.text
    except Exception as e:
        exception = True
        response_data = e

    add_log_thread = threading.Thread(target=elasticsearch_functions.add_log, args=[request_url, str(request.remote_addr), str(request.method), request.cookies.get(COOKIE_NAME), str(response_data)])
    add_log_thread.start()

    with open("logs.txt", "a+") as file:
        file.write(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\t{request.remote_addr}\n{request}\n{response_data}\n\t------------------------------------------------\n")

    if exception:
        return flask.abort(ERROR)
    else:
        return Response(flask.render_template_string(response_data), r.status_code)


def manager():
    """
        Start all the processes and manage the proxy.
        :param: none.
        :return: none.
    """
    elasticsearch_functions.open_logs_index()
    elasticsearch_functions.open_locations_index()

    processes_detection_thread = threading.Thread(target=remote_code_execution_detection.run)
    requests_detection_thread = threading.Thread(target=bruteForce_dos_sessionPrediction_detection.check_request)

    processes_detection_thread.start()
    requests_detection_thread.start()

    app.run(host="0.0.0.0", port=get_config_data.get_proxy_port())


if __name__ == '__main__':
    manager()
