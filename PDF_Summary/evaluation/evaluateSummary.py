# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import sys
import os
from itertools import chain
from docopt import docopt
from sumy import __version__
from sumy.utils import ItemsCount, get_stop_words, fetch_url
from sumy.models import TfDocumentModel
from sumy._compat import to_string
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.sum_basic import SumBasicSummarizer
from sumy.summarizers.kl import KLSummarizer
from sumy.nlp.stemmers import Stemmer
from content_based import cosine_similarity, unit_overlap
from coselection import precision, recall, f_score
from rouge import rouge_1, rouge_2, rouge_l_summary_level
#from rouge import  rouge_l_sentence_level

PARSERS = {
    "plaintext": PlaintextParser,
}

language="english"

def build_luhn(parser, language):
    summarizer = LuhnSummarizer(Stemmer(language))
    summarizer.stop_words = get_stop_words(language)

    return summarizer


def build_lsa(parser, language):
    summarizer = LsaSummarizer(Stemmer(language))
    summarizer.stop_words = get_stop_words(language)

    return summarizer


def build_text_rank(parser, language):
    summarizer = TextRankSummarizer(Stemmer(language))
    summarizer.stop_words = get_stop_words(language)

    return summarizer


def build_lex_rank(parser, language):
    summarizer = LexRankSummarizer(Stemmer(language))
    summarizer.stop_words = get_stop_words(language)

    return summarizer


def build_sum_basic(parser, language):
    summarizer = SumBasicSummarizer(Stemmer(language))
    summarizer.stop_words = get_stop_words(language)

    return summarizer


def build_kl(parser, language):
    summarizer = KLSummarizer(Stemmer(language))
    summarizer.stop_words = get_stop_words(language)

    return summarizer


def evaluate_cosine_similarity(evaluated_sentences, reference_sentences):
    evaluated_words = tuple(chain(*(s.words for s in evaluated_sentences)))
    reference_words = tuple(chain(*(s.words for s in reference_sentences)))
    evaluated_model = TfDocumentModel(evaluated_words)
    reference_model = TfDocumentModel(reference_words)

    return cosine_similarity(evaluated_model, reference_model)


def evaluate_unit_overlap(evaluated_sentences, reference_sentences):
    evaluated_words = tuple(chain(*(s.words for s in evaluated_sentences)))
    reference_words = tuple(chain(*(s.words for s in reference_sentences)))
    evaluated_model = TfDocumentModel(evaluated_words)
    reference_model = TfDocumentModel(reference_words)

    return unit_overlap(evaluated_model, reference_model)


AVAILABLE_METHODS = {
    "1": build_luhn,
    "2": build_lsa,
    "3": build_text_rank,
    "4": build_lex_rank,
    "5": build_sum_basic,
    "6": build_kl,
    "0": exit,
}

AVAILABLE_EVALUATIONS = (
    ("Precision", False, precision),
    ("Recall", True, recall),
    ("F-score", True, f_score),
    ("Cosine similarity", False, evaluate_cosine_similarity),
    ("Cosine similarity (document)", True, evaluate_cosine_similarity),
    ("Unit overlap", False, evaluate_unit_overlap),
    ("Unit overlap (document)", True, evaluate_unit_overlap),
    ("Rouge-1", False, rouge_1),
    ("Rouge-2", False, rouge_2),
#    ("Rouge-L (Sentence Level)",True,rouge_l_sentence_level),
    ("Rouge-L (Summary Level)", False, rouge_l_summary_level)
)


def main(args=None):
    summarizer, document, items_count, reference_summary = handle_arguments()

    evaluated_sentences = summarizer(document, items_count)
    reference_document = PlaintextParser.from_string(reference_summary,
        Tokenizer(language))
    reference_sentences = reference_document.document.sentences

    for name, evaluate_document, evaluate in AVAILABLE_EVALUATIONS:
        if evaluate_document:
            result = evaluate(evaluated_sentences, document.sentences)
        else:
            result = evaluate(evaluated_sentences, reference_sentences)
        print("%s: %f" % (name, result))

    return 0


def handle_arguments():
    document_format = "plaintext"
    sourceFile=raw_input("Enter Soruce file path \n")
    if sourceFile is not None:
        parser = PARSERS.get(document_format, PlaintextParser)
        with open(sourceFile, "rb") as file:
            document_content = file.read()
    else:
        parser = PARSERS["plaintext"]
        document_content = sys.stdin.read()
    summarizer_builder = AVAILABLE_METHODS["1"]
    method = AVAILABLE_METHODS[raw_input("Select Algorithm \n press 1 and enter for luhn. \n press 2 and enter for lsa. \n press 3 and enter for lex-rank. \n press 4 and enter for text-rank. \n press 5 and enter for sum-basic.\n press 6 and enter for kl.\n press 0 and enter to exit. \n")]
    for method, builder in AVAILABLE_METHODS.items():
        if method:
            summarizer_builder = builder
            break

    items_count = ItemsCount(25)

    parser = parser(document_content, Tokenizer(language))
    
    reference_summary=raw_input("Enter reference_summary file with path \n")
    with open(reference_summary, "r") as file:
        reference_summmary = file.read().decode("utf-8")

    return summarizer_builder(parser, language), parser.document, items_count, reference_summmary

main()

