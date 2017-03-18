import configparser


# configparser
# https://wiki.python.org/moin/ConfigParserExamples
# https://docs.python.org/3/library/configparser.html


def read_settings(filepath="config.ini"):
    config = configparser.ConfigParser()
    config.read(filepath)
    return config


def write_settings(config, filepath="config.ini"):
    with open(filepath, 'w') as configfile:
        config.write(configfile)
