# coding=utf-8
from kg_lang.kyrgyz.bashka._dagy import DagyZatMuchosu
from kg_lang.kyrgyz.etish._ba import BaEtishMuchosu
from kg_lang.kyrgyz.etish._bash import BashEtishMuchosu
from kg_lang.kyrgyz.etish._chu import ChuEtishMuchosu
from kg_lang.kyrgyz.etish._chuday import ChudayEtishMuchosu
from kg_lang.kyrgyz.etish._gan import GanEtishMuchosu
from kg_lang.kyrgyz.etish.chak import KelerChak
from kg_lang.kyrgyz.etish.chak import OtkonChak
from kg_lang.kyrgyz.etish.chak import UchurChak
from kg_lang.kyrgyz.etish.kyimyl_atooch import KyimylAtooch
from kg_lang.kyrgyz.helps.attrs import *
from kg_lang.kyrgyz.jondomo import Jondomo
from kg_lang.kyrgyz.san import San
from kg_lang.kyrgyz.suroo._by import ByZatMuchosu
from kg_lang.kyrgyz.syn._dai import DaiZatMuchosu
from kg_lang.kyrgyz.syn._luu import LuuZatMuchosu
from kg_lang.kyrgyz.syn._syz import SyzZatMuchosu
from kg_lang.kyrgyz.syn_atooch import SalyshtyrmaSynAtooch
from kg_lang.kyrgyz.taandyk import Taandyk

ZAT_ATOOCH = 1  # Существительное
SYN_ATOOCH = 2  # Прилагательное
SAN_ATOOCH = 3  # Числительное
AT_ATOOCH = 4  # Местоимение
ETISH = 5  # Глагол
TAKTOOCH = 6  # Наречие
TUURAMES_ETISH = 7  # Неправильный глагол какой-то (Я не знаю что это, мне дали список)
SYRDYK = 8  # Междометие
KYZMATCHY = 9  # Вспомогательные слова
KYIMYL_ATOOCH = 10  # Существительное определяющее процесс действия(глагол + окончание)
TUURANDY = 11   # Подражательные слова


# README: Affix - какое-либо доступное преобразование для слова или любая операция
#                   которую можно провести над этим словом


class NoAffixesException(Exception):
    message = "Бул сөздү жөндөй албаймын"


def get_word_affixes(word_type):
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


def apply_affix(affix, word_object):
    """:type word_object: kg_lang.kyrgyz.lang.KyrgyzWord """

    if affix == 'jondomo':
        jondomos = {'word_jondomo': Jondomo(word_object)}
        if word_object.last_affix() != "taandyk":
            jondomos['word_koptuk_jondomo'] = Jondomo(San(word_object).koptuk())
        return jondomos

    if affix == 'taandyk':
        return {'word_taandyk': Taandyk(word_object),
                'word_koptuk_taandyk': Taandyk(San(word_object).koptuk())}

    if affix == 'chak':
        return {'otkon_chak': OtkonChak(word_object),
                'uchur_chak': UchurChak(word_object),
                'keler_chak': KelerChak(word_object)}

    if affix == 'kyimyl_atooch':
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

    if isinstance(affix, str) and affix in muchos:
        mucho_class = muchos[affix]
        return {affix: mucho_class(word_object)}

    if isinstance(affix, dict):
        result_affixes = {}
        for first_step_affix, next_steps in affix.items():
            affixes = apply_affix(first_step_affix, word_object).values()
            first_step_words = []
            for affix in affixes:
                if affix.is_pluralable():
                    first_step_words.append(affix.make(*men.as_args()))
                    first_step_words.append(affix.make(*sen.as_args()))
                    first_step_words.append(affix.make(*al.as_args()))
                    first_step_words.append(affix.make(*biz.as_args()))
                    first_step_words.append(affix.make(*siler.as_args()))
                    first_step_words.append(affix.make(*alar.as_args()))
                    first_step_words.append(affix.make(*siz.as_args()))
                    first_step_words.append(affix.make(*sizder.as_args()))
                else:
                    for transformer in affix.transformers():
                        if callable(transformer):
                            first_step_words.append(transformer(affix))
            for i in range(len(first_step_words)):
                new_word = first_step_words[i]
                for second_step_affix in next_steps:
                    for key, affix_inner in apply_affix(second_step_affix, new_word).items():
                        result_affixes['%s_%d_%s' % (first_step_affix, i, key)] = affix_inner
        return result_affixes
    return {}
