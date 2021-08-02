from elasticsearch import Elasticsearch, exceptions
from datetime import datetime
import json
import get_location_by_ip


def search_index(index_name):
    """
        Search index in elasticsearch.
        :param index_name: the request to search.
        :type index_name: string.
        :return: if the index found.
        :rtype: bool.
    """
    elastic = Elasticsearch(['localhost'], port=9200)

    try:
        ret_val = elastic.search(index=index_name)
    except exceptions.NotFoundError:
        ret_val = 0

    elastic.close()
    return ret_val


def open_attacks_index():
    """
        Open the attacks index in elasticsearch if him don't exist.
        :param: none.
        :return: none.
    """
    if not search_index('attacks'):
        elastic = Elasticsearch(['localhost'], port=9200)
        body = {
             "mappings": {
                 "properties": {
                         "date":
                         {
                             "type": "date"
                         },
                         "attack-type":
                         {
                             "type": "text"
                         }
                     },
                 },
             }

        response = elastic.indices.create(
             index="attacks",
             body=json.dumps(body)
        )
        elastic.close()


def open_logs_index():
    """
        Open the logs index in elasticsearch if him don't exist.
        :param: none.
        :return: none.
    """
    if not search_index('logs'):
        elastic = Elasticsearch(['localhost'], port=9200)
        body = {
             "mappings": {
                 "properties": {
                         "date":
                         {
                             "type": "date"
                         },
                         "website":
                         {
                             "type": "text"
                         },
                         "ip":
                         {
                             "type": "ip"
                         },
                         "ip_location":
                         {
                             "type": "geo_point"
                         },
                         "request-type":
                         {
                             "type": "text"
                         },
                         "session-cookie":
                         {
                             "type": "integer"
                         },
                         "response":
                         {
                             "type": "text"
                         }
                     },
                 },
             }

        response = elastic.indices.create(
             index="logs",
             body=json.dumps(body)
        )
        elastic.close()


def open_processes_index():
    """
        Open the processes index in elasticsearch if him don't exist.
        :param: none.
        :return: none.
    """
    if not search_index('processes'):
        elastic = Elasticsearch(['localhost'], port=9200)
        body = {
             "mappings": {
                 "properties": {
                         "date":
                         {
                             "type": "date"
                         },
                         "process":
                         {
                             "type": "text"
                         }
                     },
                 },
             }

        response = elastic.indices.create(
             index="processes",
             body=json.dumps(body)
        )
        elastic.close()


def add_attack(attack_type, website):
    """
        Add attack to the attacks index in elasticsearch.
        :param attack_type: the type of attack.
        :type attack_type: string.
        :param website: the website attacked.
        :type website: string.
        :return: none.
    """
    elastic = Elasticsearch(['localhost'], port=9200)
    r = elastic.index('attacks', {
        "date": datetime.utcnow(),
        "attack-type": attack_type,
        "website": website
    })
    elastic.close()


def add_log(website, ip, request_type, session_cookie, response):
    """
        Add log to the logs index in elasticsearch.
        :param website: the website requested.
        :type website: string.
        :param ip: the attacker's IP.
        :type ip: string.
        :param request_type: the type of request.
        :type request_type: string.
        :param session_cookie: the session number.
        :type session_cookie: int.
        :param response: the server response.
        :type response: string.
        :return: none.
    """

    ip_location = get_location_by_ip.get_location_by_ip(ip)

    elastic = Elasticsearch(['localhost'], port=9200)
    r = elastic.index('logs', {
        "date": datetime.utcnow(),
        "website": website,
        "ip": ip,
        "ip_location":
        {
            "lat": float(ip_location[0]),
            "lon": float(ip_location[1])
        },
        "request-type": request_type,
        "session-cookie": session_cookie,
        "response": response
    })
    elastic.close()


def add_process(process):
    """
        Add log to the logs index in elasticsearch.
        :param process: the process started.
        :type process: string.
        :return: none.
    """
    elastic = Elasticsearch(['localhost'], port=9200)
    r = elastic.index('processes', {
        "date": datetime.utcnow(),
        "process": process
    })
    elastic.close()


