# coding=utf-8
import re

from kg.lang.helps.change import WordChange


class WordEndingTypes(object):
    UNSUZ_JOK = "UJ"
    UNSUZ_KATKALAN = "UK"
    UNSUZ_JUMSHAK_UYAN = "UJU"
    UNSUZ_UYAN_RYI = "URYI"

    UNDUU_JOON_ERINSIZ ="UAY"
    UNDUU_JOON_ERINDUU ="UOU"
    UNDUU_ICHKE_ERINSIZ ="UEI"
    UNDUU_ICHKE_ERINDUU ="U_OU"


class KyrgyzWord:
    ALPHABET = u"абвгдеёжзийклмнңоөпрстуүфхцчшщьыъэюя"
    ALPHABET_CAPS = u"АБВГДЕЁЖЗИЙКЛМНҢОӨПРСТУҮФХЦЧШЩЬЫЪЭЮЯ"
    EXTRA_ALLOWED_CHARS = u" -"

    def __init__(self, word, is_name=False):
        self.initial_word = word.strip()
        self.word = self._delete_chars_in_the_end(self._make_lower(self.initial_word))
        self.original_word = self.word
        self.is_name = is_name
        self.unduu_type = None
        self.prepared = False
        self.unduu_type_jaaktuu = False
        self.unsuz_end_type = None
        self.change_history = []

    def __unicode__(self):
        return self.word

    def __str__(self):
        return self.word.encode("utf-8")

    def _is_correct_word(self):
        for letter in self.word:
            if letter not in self.ALPHABET + self.ALPHABET_CAPS + self.EXTRA_ALLOWED_CHARS:
                return False
        return True

    def prepare(self):
        """
        Подготовливает объект слова для дальнейших преобразований. Определяет его свойства.
        """
        if self.prepared:
            return

        ayagynda_belgi = re.compile(u"[%s]$" % Ashykcha.belgiler)

        if ayagynda_belgi.findall(self.word):
            self.original_word = self.word
            self.word = self.word[0:-1]

        ayagynda_yottoshkon = re.compile(u"[%s]$" % Ashykcha.yottoshkon)
        ayagynda_unduu = re.compile(u"[%s]$" % Unduu.all)
        ayagynda_jumshak_uyan_unsuz = re.compile(u"[%s]$" % (Unsuz.jumshak+Unsuz.uyan))
        ayagynda_uyan_ryi_unsuz = re.compile(u"[%s]$" % Unsuz.uyan_ryi)
        ayagynda_katkalan_unsuz = re.compile(u"[%s]$" % Unsuz.katkalan)

        if ayagynda_yottoshkon.findall(self.word):
            self.unsuz_end_type = WordEndingTypes.UNSUZ_JOK
        if ayagynda_unduu.findall(self.word):
            self.unsuz_end_type = WordEndingTypes.UNSUZ_JOK
        elif ayagynda_jumshak_uyan_unsuz.findall(self.word):
            self.unsuz_end_type = WordEndingTypes.UNSUZ_JUMSHAK_UYAN
        elif ayagynda_uyan_ryi_unsuz.findall(self.word):
            self.unsuz_end_type = WordEndingTypes.UNSUZ_UYAN_RYI
        elif ayagynda_katkalan_unsuz.findall(self.word):
            self.unsuz_end_type = WordEndingTypes.UNSUZ_KATKALAN

        joon_erinsiz_unduu = re.compile(u"[%s][^%s]*$" % (Unduu.ay, Unduu.ay_dan_bashka))
        ichke_erinsiz_unduu = re.compile(u"[%s][^%s]*$" % (Unduu.ei, Unduu.ei_den_bashka))
        joon_erinduu_unduu = re.compile(u"[%s][^%s]*$" % (Unduu.ou, Unduu.ou_dan_bashka))
        ichke_erinduu_unduu = re.compile(u"[%s][^%s]*$" % (Unduu._ou, Unduu._ou_don_bashka))

        if joon_erinsiz_unduu.findall(self.word):
            self.unduu_type = WordEndingTypes.UNDUU_JOON_ERINSIZ
        elif ichke_erinsiz_unduu.findall(self.word):
            self.unduu_type = WordEndingTypes.UNDUU_ICHKE_ERINSIZ
        elif joon_erinduu_unduu.findall(self.word):
            self.unduu_type = WordEndingTypes.UNDUU_JOON_ERINDUU
        elif ichke_erinduu_unduu.findall(self.word):
            self.unduu_type = WordEndingTypes.UNDUU_ICHKE_ERINDUU

        jaaktuu = re.compile(u"[%s][^%s]*$" % (Unduu.jaaktuu, Unduu.jaaksyz))

        if jaaktuu.findall(self.word):
            self.unduu_type_jaaktuu = True

        self.prepared = True

    def _make_lower(self, word):
        lower = u"%s" % word
        for letter in word:
            if letter in self.ALPHABET_CAPS:
                index = self.ALPHABET_CAPS.index(letter)
                lower = lower.replace(letter, self.ALPHABET[index])
        return lower

    def _delete_chars_in_the_end(self, word):
        if word[-1] == '-':
            return word[:-1]
        return word

    def change(self, start, end, affix, attrs=None):
        """
        Создает новый объект слова составленный из текущего с применением указанного аффикса
        """
        new_word_object = KyrgyzWord(start+end, self.is_name)
        new_word_object.change_history.extend(self.change_history)
        new_word_object.change_history.append(WordChange(affix, len(start), attrs))
        return new_word_object

    def last_change_attrs(self):
        return self.change_history[-1].attrs if len(self.change_history) > 0 else None

    def has_history(self):
        return len(self.change_history) > 0

    def last_affix(self):
        return self.change_history[-1].affix if len(self.change_history) > 0 else None


class Unduu(object):
    all = u"аоуыэеиөү"
    joon = u"аоуы"
    ichke = u"иэеөү"
    erinduu = u"оуөү"
    erinsiz = u"аэеыи"
    jaaktuu = u"аоөэеяё"
    jaaksyz = u"уүыию"

    ay = u"аыя"
    ei = u"эеи"
    ou = u"оуёю"
    _ou = u"өү"

    ay_dan_bashka = u"оуэеиөүёю"
    ei_den_bashka = u"аоуыөүяю"
    ou_dan_bashka = u"аыэеиөүя"
    _ou_don_bashka = u"аоуыэеияё"

    sozulgandar = {
        u'а': u'аа',
        u'о': u'оо',
        u'у': u'уу',
        u'ы': u'ыы',
        u'э': u'ээ',
        u'е': u'ээ',
        u'ө': u'өө',
        u'ү': u'үү',
        u'и': u'ии',
    }


class Unsuz(object):
    all = u"цкшщхфпрчстйнгзвлджмбң"
    katkalan = u"цкшщхфпчст"
    jumshak = u"гзвджмб"
    uyan = u"мнңл"
    uyan_ryi = u"рй"


class Ashykcha(object):
    yottoshkon = u'ёяю'
    belgiler = u'ъь'


def select_for_attrs(jak, jeke, sylyk, men, sen, al, biz, siler, alar, siz, sizder):
    if jak == 1:
        return men if jeke else biz
    elif jak == 2:
        if sylyk:
            return siz if jeke else sizder
        else:
            return sen if jeke else siler
    else:
        return al if jeke else alar