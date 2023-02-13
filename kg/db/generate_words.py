from kg.db.models import Word
from kg.lang.affixing import get_word_affixes, get_extra_word_affixes, apply_affix
from kg.lang.lang import KyrgyzWord


def generate(word: str = None):
    result = []
    if word:
        found_words = Word.select().where(
            (Word.word == word.lower() + "-") |
            (Word.word == word.lower()) |
            (Word.alt == word.lower())
        )
        if found_words.count() == 0:
            raise Exception(f'Мындай "{word}" соз табылган жок')
        for found_word in found_words:
            result.extend(generate_all_children(found_word))
    else:
        for word in Word.select():
            result.extend(generate_all_children(word))
    return result


def generate_all_children(word: Word):
    words = []
    word_object = KyrgyzWord(word.word)
    words.append(word_object.word)
    try:
        features_names = get_word_affixes(word.type)
        features_names.extend(get_extra_word_affixes(word.type))
    except:
        features_names = []
    for feature_name in features_names:
        features = apply_affix(feature_name, word_object)

        for feature in features.values():
            for result in feature.generate_results():
                words.append(result)
    return words
