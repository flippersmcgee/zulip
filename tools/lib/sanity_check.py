import os
import pwd
import sys


def check_venv(filename: str) -> None:
    try:
        import django
        import ujson
        import zulip
        django
        ujson
        zulip
    except ImportError:
        print(f"You need to run {filename} inside a Zulip dev environment.")
        user_id = os.getuid()
        user_name = pwd.getpwuid(user_id).pw_name
        if user_name in ['vagrant', 'zulipdev']:
            print("You can `source /srv/zulip-py3-venv/bin/activate` "
                  "to enter the Zulip development environment.")
        else:
            print("If you are using Vagrant, you can `vagrant ssh` to enter the Vagrant guest.")
        sys.exit(1)
