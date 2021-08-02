
def get_sudo_password():
    """
    Split the config data, find the sudo password of the user and remove it.
    :param: none.
    :return: the user sudo password.
    :rtype: string.
    """
    with open('config', 'r') as file:
        data_in_lines = file.read().split('\n')

    password = data_in_lines[0]

    with open('config', 'w') as file:
        file.write('\n'.join(data_in_lines[1::]))

    return password


def get_server_port():
    """
    Split the config data and find the server port.
    :param: none.
    :return: the server port.
    :rtype: int.
    """
    with open('config', 'r') as file:
        server_port = int(file.read().split('\n')[0].split('=')[-1])

    return server_port


def get_proxy_port():
    """
        Split the config data and find the proxy port.
        :param: none.
        :return: the proxy port.
        :rtype: int.
    """
    with open('config', 'r') as file:
        proxy_port = int(file.read().split('\n')[1].split('=')[-1])

    return proxy_port


def get_api_key():
    """
        Split the config data and find the api key of the user.
        :param: none.
        :return: the user api key.
        :rtype: string.
    """
    with open('config', 'r') as file:
        api_key = file.read().split('\n')[2].split('=')[-1]

    return api_key


def get_blocks():
    """
    Split the config data and find the data for block.
    :param: none.
    :return: the data for block.
    :rtype: dict.
    """
    blocks = {}

    with open('config', 'r') as file:
        blocks_data = file.read().split('\n')[-1].split('=')[-1].split(';')

    for block in blocks_data:
        blocks[block.split('-')[0]] = block.split('-')[1]

    return blocks
