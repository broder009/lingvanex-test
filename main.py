from opusfilter import opusfilter
import pathlib
import json
import logging

class OpusRuner:

    def __init__(self):
        self.__config = self.__get_config()

    @staticmethod
    def __get_config():
        try:
            with open(str(pathlib.Path().resolve()) + "/config.json", "r") as file:
                config = json.load(file)
            return config
        except FileNotFoundError as e:
            logging.exception(e)

    def return_opus_instance(self):
        return opusfilter.OpusFilter(configuration=self.__config)


if __name__ == '__main__':
    opus_runer = OpusRuner()
    opus_instance = opus_runer.return_opus_instance()
    opus_instance.execute_steps()
