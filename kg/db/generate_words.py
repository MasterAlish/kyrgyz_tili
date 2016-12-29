# coding=utf-8
from kg.db.models import Word
from kg.lang.affixing import get_word_affixes, get_extra_word_affixes, apply_affix
from kg.lang.lang import KyrgyzWord


def generate(word=None):
    if word:
        found_words = Word.select().where(
            (Word.word == word.lower() + "-") |
            (Word.word == word.lower()) |
            (Word.alt == word.lower())
        )
        if found_words.count() == 0:
            raise Exception((u'Мындай "%s" соз табылган жок' % word))

        for found_word in found_words:
            generate_all_children(found_word)
    else:
        for word in Word.select():
            generate_all_children(word)


def generate_all_children(word):
    word_object = KyrgyzWord(word.word)
    print(word_object.word)
    try:
        features_names = get_word_affixes(word.type)
        features_names.extend(get_extra_word_affixes(word.type))
    except:
        features_names = []
    for feature_name in features_names:
        features = apply_affix(feature_name, word_object)

        for feature in features.values():
            for result in feature.generate_results():
                result = unicode(result)
                print(result)
