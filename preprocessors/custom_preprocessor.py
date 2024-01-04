import re
from opusfilter import PreprocessorABC


class CharacterPreprocessor(PreprocessorABC):

    def __prepare_strings(self, segment):
        prepared_segment = re.sub(r'[»«”“‟„`]', '"', segment)
        prepared_segment = re.sub(r'\s*,\s*', ', ', prepared_segment)
        prepared_segment = re.sub(r'\.', '.', prepared_segment)
        prepared_segment = re.sub(r'\{\\.*\}', '', prepared_segment)
        prepared_segment = re.sub(r"[|\\/]", ' ', prepared_segment)
        return prepared_segment
    
    def process(self, pairs):
        for segments in pairs:
            yield [self.__prepare_strings(segment) for segment in segments]
            