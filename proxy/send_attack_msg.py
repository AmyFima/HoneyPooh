import get_config_data

try:
    from pushbullet import Pushbullet
    have_pushbullet = True
except ModuleNotFoundError as e:
    have_pushbullet = False


def send_attack_msg(attack_type, website):
    """
        Add attack to the attacks index in elasticsearch.
        :param attack_type: the type of attack.
        :type attack_type: string.
        :param website: the website attacked.
        :type website: string.
        :return: none.
    """
    if have_pushbullet:
        api_key = get_config_data.get_api_key()
        if api_key != "":
            pb = Pushbullet(api_key)
            pb.push_note("Attack Message", f"Your honeypot find {attack_type} attack on {website}")

