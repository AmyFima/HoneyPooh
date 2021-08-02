from requests import get

LOCALHOST = '127.0.0.1'


def get_location_by_ip(ip):
    """
    Find the location by ip.
    :param ip: ip address.
    :type ip: string.
    :return: dict of the location.
    :type: list.
    """

    if ip == LOCALHOST:
        ip = get('http://ip.42.pl/raw').text

    response = get(f'http://api.ipapi.com/api/{ip}?access_key=defd1de2e6b60005d8db9142bc0fd17f&fields=latitude,longitude').text.split(':')
    return [response[1].split(',')[0], response[2].split('}')[0]]  # [response['latitude'], response['longitude']]
