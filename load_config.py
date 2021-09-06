import json
import os.path

def load_config(default_config_file = "config.default.json", user_conf_file = "config.user.json"):
    config = {}

    with open(default_config_file) as default_config_file:
        config = json.load(default_config_file)

    # Override default config with user config
    if os.path.isfile(user_conf_file):
        with open(user_conf_file) as user_conf_file:
            user_config = json.load(user_conf_file)

            for prop in user_config:
                config[prop] = user_config[prop]

    return config

    