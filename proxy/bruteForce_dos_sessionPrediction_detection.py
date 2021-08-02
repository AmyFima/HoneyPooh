import elasticsearch_functions
import send_attack_msg
import get_config_data
from datetime import datetime


MIN_REQUESTS_IN_ATTACK = 4
MIN_REQUESTS_FOR_CHECK = 2


def get_requests():
    """
    Return the requests.
    :param: none.
    :return: the requests.
    :rtype: array.
    """
    requests = []

    try:
        with open('requests.txt', 'r') as file:
            requests = file.read().split('\n')
    except FileNotFoundError as e:
        pass

    if (len(requests)) and (requests[-1] == ''):
        requests.pop()

    return requests


def count_requests(request):
    """
    Find the last requests in requests.txt.
    :param request: the request to count.
    :type request: string.
    :return: The number of times the request appears.
    :rtype: int.
    """
    requests = get_requests()
    return requests.count(request)


def get_last_user_requests():
    """
    Find the last requests in requests.txt.
    :param: none.
    :return: the last request at this moment.
    :rtype: array.
    """
    requests = get_requests()
    ret_requests = []

    if len(requests) >= MIN_REQUESTS_FOR_CHECK:
        ret_requests = [requests[-1], requests[-2]]

        for request in requests:
            if (request.split('<')[0] != ret_requests[0].split('<')[0]) and (
                    request.split('> ')[-1] == ret_requests[0].split('> ')[-1]):
                ret_requests[1] = request

    return ret_requests


def check_request():
    """
    Find if brute force is happening.
    :param: none.
    :return: none.
    """
    requests_len = len(get_requests())
    print("Restart the requests system")

    while True:
        new_requests_len = len(get_requests())

        if (new_requests_len > 0) and (new_requests_len > requests_len):
            requests_len = new_requests_len
            requests = get_last_user_requests()

            if (count_requests(requests[0]) > MIN_REQUESTS_IN_ATTACK) and (
                    count_requests(requests[1]) < MIN_REQUESTS_IN_ATTACK):
                elasticsearch_functions.add_attack('BruteForce', str(requests[0].split("'")[-2]))
                send_attack_msg.send_attack_msg('BruteForce', str(requests[0].split("'")[-2]))
                print(f"attack: Brute Force    {requests[0]}")


def add_request(request, ip):
    """
    Add request for requests.txt.
    :param request: summary request.
    :type request: string.
    :param ip: user ip.
    :type ip: string.
    :return: none.
    """
    server_port = get_config_data.get_server_port()
    proxy_port = get_config_data.get_proxy_port()

    with open("requests.txt", "a+") as file:  # requests.txt - file for the attacks detection
        file.write(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\t{request.replace(str(proxy_port), str(server_port))} {ip}\n")

