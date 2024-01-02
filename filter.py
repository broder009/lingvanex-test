from functools import reduce
import opusfilter
from opusfilter import filters

def read_data() -> tuple:
    with open('WikiMatrix.en-ru.en', "r", encoding='utf-8') as english, open('WikiMatrix.en-ru.ru', "r", encoding='utf-8') as russian:
        english = english.readlines()
        russian = russian.readlines()
    return english, russian

def concatenate(source: list=[], target: list=[], separator: str='|') -> list:
    result = [(en_line + separator + ru_line) for en_line, ru_line in zip(source, target)]
    return result

def create_output(result: list) -> None:
    with open('output.txt', "w") as output:
        output.writelines(result)