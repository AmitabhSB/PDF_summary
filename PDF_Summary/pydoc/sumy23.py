# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Lsa
from sumy.summarizers.luhn import LuhnSummarizer as Luhn
from sumy.summarizers.text_rank import TextRankSummarizer as TxtRank
from sumy.summarizers.lex_rank import LexRankSummarizer as LexRank
from sumy.summarizers.sum_basic import SumBasicSummarizer as SumBasic
from sumy.summarizers.kl import KLSummarizer as KL
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "English"
SENTENCES_COUNT = 30


if __name__ == "__main__":
    # For plain text files
    parser = PlaintextParser.from_file("split_All Because Of My Hair.txt", Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    
    summarizer = KLSummarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print (sentence)
