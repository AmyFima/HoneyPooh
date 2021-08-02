import os
import get_config_data


def app():
    """
    Run the docker container and stop him when the user want.
    :param: none.
    :return: none.
    """
    sudo_password = get_config_data.get_sudo_password()
    proxy_port = get_config_data.get_proxy_port()

    os.system("echo %s | sudo -S docker build -t python-barcode ." % sudo_password)
    os.system(f"echo {sudo_password} | sudo docker run -p {proxy_port}:{proxy_port} --net=\"host\" python-barcode")


if __name__ == '__main__':
    app()
