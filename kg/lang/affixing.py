# coding=utf-8
from kg.lang.bashka._dagy import DagyZatMuchosu
from kg.lang.etish._ba import BaEtishMuchosu
from kg.lang.etish._bash import BashEtishMuchosu
from kg.lang.etish._chu import ChuEtishMuchosu
from kg.lang.etish._chuday import ChudayEtishMuchosu
from kg.lang.etish._gan import GanEtishMuchosu
from kg.lang.etish.chak import KelerChak
from kg.lang.etish.chak import OtkonChak
from kg.lang.etish.chak import UchurChak
from kg.lang.etish.kyimyl_atooch import KyimylAtooch
from kg.lang.helps.attrs import *
from kg.lang.jondomo import Jondomo
from kg.lang.san import San
from kg.lang.suroo._by import ByZatMuchosu
from kg.lang.syn._dai import DaiZatMuchosu
from kg.lang.syn._luu import LuuZatMuchosu
from kg.lang.syn._syz import SyzZatMuchosu
from kg.lang.syn_atooch import SalyshtyrmaSynAtooch
from kg.lang.taandyk import Taandyk

ZAT_ATOOCH = 1  # Существительное
SYN_ATOOCH = 2  # Прилагательное
SAN_ATOOCH = 3  # Числительное
AT_ATOOCH = 4  # Местоимение
ETISH = 5  # Глагол
TAKTOOCH = 6  # Наречие
TUURAMES_ETISH = 7  # Неправильный глагол какой-то (Я не знаю что это, мне дали список)
SYRDYK = 8  # Междометие
KYZMATCHY = 9  # Вспомогательные слова
KYIMYL_ATOOCH = 10  # Существительное определяющее процесс действия(глагол + суффикс)
TUURANDY = 11   # Подражательные слова


# README: Affix - какое-либо доступное преобразование для слова или любая операция
#                   которую можно провести над этим словом


class NoAffixesException(Exception):
    message = "Бул сөздү жөндөй албаймын"


def get_word_affixes(word_type):
    """
    Возвращает список имен основных преобразований для указанного типа слова.
    Преобразования могут быть многоуровневыми
    :param word_type: Часть речи слова
    """
    if word_type == ZAT_ATOOCH:
        return ["info", "jondomo", "taandyk", {'taandyk': ['jondomo']}]
    if word_type == KYIMYL_ATOOCH:
        return ["info", "jondomo", "taandyk", {'taandyk': ['jondomo']}]
    elif word_type == SYN_ATOOCH:
        return ["info", "jondomo", "salyshtyrma"]
    elif word_type == SAN_ATOOCH:
        return ["info", "jondomo"]
    elif word_type == AT_ATOOCH:
        return ["info", "jondomo"]
    elif word_type == ETISH or word_type == TUURAMES_ETISH:
        return ["info", "chak", "kyimyl_atooch"]
    elif word_type in [TAKTOOCH, SYRDYK, KYZMATCHY, TUURANDY]:
        return ["info"]
    else:
        raise NoAffixesException()


def get_extra_word_affixes(word_type):
    """
    Возвращает список имен дополнительных преобразований для указанного типа слова.
    Преобразования могут быть многоуровневыми
    :param word_type: Часть речи слова
    """
    if word_type == ZAT_ATOOCH:
        return ["dai", "luu", "syz", 'by', 'dagy']
    if word_type == KYIMYL_ATOOCH:
        return ["dai", "syz", 'by', 'dagy']
    elif word_type == SYN_ATOOCH:
        return ["dai", 'by']
    elif word_type == SAN_ATOOCH:
        return ["dai", "syz", 'by']
    elif word_type == AT_ATOOCH:
        return ['by']
    elif word_type == ETISH or type == TUURAMES_ETISH:
        return ['ba', 'bash', 'chu', 'chuday', 'gan', {'kyimyl_atooch2': ['chak']}, {'gan': ['jondomo']},
                {'ba': ['chu', 'chuday', 'gan', {'gan': ['jondomo']}]}]
    elif word_type in [TAKTOOCH]:
        return ['by']
    elif word_type in [SYRDYK, KYZMATCHY, TUURANDY]:
        return []
    else:
        raise NoAffixesException()


def apply_affix(affix_name, word_object):
    """
    Применяет аффикс по имени для указанного слова, подбирая соответсвующий класс Аффиксов
    :type word_object: kg_lang.kyrgyz.lang.KyrgyzWord
    """

    if affix_name == 'jondomo':
        jondomos = {'word_jondomo': Jondomo(word_object)}
        if word_object.last_affix() != "taandyk":
            jondomos['word_koptuk_jondomo'] = Jondomo(San(word_object).koptuk())
        return jondomos

    if affix_name == 'taandyk':
        return {'word_taandyk': Taandyk(word_object),
                'word_koptuk_taandyk': Taandyk(San(word_object).koptuk())}

    if affix_name == 'chak':
        return {'otkon_chak': OtkonChak(word_object),
                'uchur_chak': UchurChak(word_object),
                'keler_chak': KelerChak(word_object)}

    if affix_name == 'kyimyl_atooch':
        return {'kyimyl_atooch_jondomo': Jondomo(KyimylAtooch(word_object).make())}

    muchos = {
        'salyshtyrma': SalyshtyrmaSynAtooch,
        'dai': DaiZatMuchosu,
        'gan': GanEtishMuchosu,
        'syz': SyzZatMuchosu,
        'luu': LuuZatMuchosu,
        'by': ByZatMuchosu,
        'dagy': DagyZatMuchosu,
        'ba': BaEtishMuchosu,
        'bash': BashEtishMuchosu,
        'chu': ChuEtishMuchosu,
        'chuday': ChudayEtishMuchosu,
    }

    if isinstance(affix_name, str) and affix_name in muchos:
        mucho_class = muchos[affix_name]
        return {affix_name: mucho_class(word_object)}

    if isinstance(affix_name, dict):
        result_affixes = {}
        for first_step_affix, next_steps in affix_name.items():
            affixes = apply_affix(first_step_affix, word_object).values()
            first_step_words = []
            for affix_name in affixes:
                if affix_name.is_pluralable():
                    first_step_words.append(affix_name.make(*men.as_args()))
                    first_step_words.append(affix_name.make(*sen.as_args()))
                    first_step_words.append(affix_name.make(*al.as_args()))
                    first_step_words.append(affix_name.make(*biz.as_args()))
                    first_step_words.append(affix_name.make(*siler.as_args()))
                    first_step_words.append(affix_name.make(*alar.as_args()))
                    first_step_words.append(affix_name.make(*siz.as_args()))
                    first_step_words.append(affix_name.make(*sizder.as_args()))
                else:
                    for transformer in affix_name.transformers():
                        if callable(transformer):
                            first_step_words.append(transformer(affix_name))
            for i in range(len(first_step_words)):
                new_word = first_step_words[i]
                for second_step_affix in next_steps:
                    for key, affix_inner in apply_affix(second_step_affix, new_word).items():
                        result_affixes['%s_%d_%s' % (first_step_affix, i, key)] = affix_inner
        return result_affixes
    return {}
