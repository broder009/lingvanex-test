from opusfilter import FilterABC
from opusfilter import CLEAN_FALSE, CLEAN_TRUE


class EngInBctFilter(FilterABC):

    score_direction = CLEAN_FALSE

    @staticmethod
    def __check_eng_in_bkt(sentence):
        if '(англ.)' in sentence:
                return True
        return False

    def score(self, pairs):
        for pair in pairs:
            yield [self.__check_eng_in_bkt(sentence) for sentence in pair]
    
    def accept(self, score):
        return not any(score)
