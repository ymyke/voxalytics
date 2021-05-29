"""NLP helper functions

Requires Spacy package, https://spacy.io/
"""

from collections import Counter
import spacy

_nlp = spacy.load("en_core_web_sm")


def tokenize_and_count(text: str) -> Counter:
    """Tokenize text and return Counter object with all tokens and their counts.
    Lemmatizes and removes stop words, punctuations, symbols, etc.
    """
    return Counter(
        [
            t.lemma_.lower()
            for t in _nlp(text)
            if len(t.lemma_) > 1
            and not t.is_stop
            and not t.pos_ in ["PUNCT", "SYM", "X"]
        ]
    )
