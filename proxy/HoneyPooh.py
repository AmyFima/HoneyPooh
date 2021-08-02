import os


def app():
    """
    Run the docker container and stop him when the user want.
    :param: none.
    :return: none.
    """
    os.system("python proxy.py")


if __name__ == '__main__':
    app()
