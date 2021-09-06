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
            merge_config(config, user_config)

    return config

    
def merge_config(confA, confB):
    for key in confB.keys():
        if isinstance(confB[key], dict):
            merge_config(confA[key], confB[key])
        else:
            confA[key] = confB[key]
