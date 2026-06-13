import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


class TextProcessor:
    def __init__(self):
        try:
            nltk.data.find("corpora/stopwords")
        except LookupError:
            nltk.download("stopwords", quiet=True)

        self.stemmer_ru = SnowballStemmer("russian")
        self.stemmer_en = SnowballStemmer("english")

        self.stop_words = set(stopwords.words("russian")).union(set(stopwords.words("english")))

        self.word_pattern = re.compile(r'[a-zA-Zа-яА-Я0-9]+')

    def _stem_word(self, word: str) -> str:
        if re.search(r'[а-яА-Я]', word):
            return self.stemmer_ru.stem(word)
        return self.stemmer_en.stem(word)

    def process(self, text: str) -> list[str]:
        if not text:
            return []

        lowercased_text = text.lower()

        tokens = self.word_pattern.findall(lowercased_text)

        processed_tokens = [
            self._stem_word(token)
            for token in tokens
            if token not in self.stop_words
        ]

        return processed_tokens