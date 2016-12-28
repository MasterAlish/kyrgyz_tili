# coding=utf-8
from kg.lang.helps.attrs import *
from kg.lang.jondomo import Jondomo
from kg.lang.lang import KyrgyzWord
from kg.lang.san import San
from kg.lang.taandyk import Taandyk
from kg.tests import KGTestCase


attrs_list = [men, sen, al, biz, siler, alar, siz, sizder]


class JondomoIlikAfterTaandykTest(KGTestCase):
    def test_ilik_after_taandyk(self):
        data = self.get_data()
        for word, expected_forms in data.items():
            koptuk = San(KyrgyzWord(word)).koptuk()
            for i in range(len(attrs_list)):
                attr = attrs_list[i]
                jeke_form_expected = expected_forms[0][i]
                taandyk = Taandyk(KyrgyzWord(word)).make(attr.jak, attr.jeke, attr.sylyk)
                jondomo = Jondomo(taandyk)
                self.assertEqual(jondomo.ilik(), jeke_form_expected)

                koptuk_form_expected = expected_forms[1][i]
                taandyk_koptuk = Taandyk(koptuk).make(attr.jak, attr.jeke, attr.sylyk)
                jondomo_koptuk = Jondomo(taandyk_koptuk)
                self.assertEqual(jondomo_koptuk.ilik(), koptuk_form_expected)

    def get_data(self):
        return {
            u'козу': [
                [u'козумдун', u'козуңдун', u'козусунун', u'козубуздун', u'козуңардын', u'козусунун', u'козуңуздун', u'козуңуздардын'],
                [u'козуларымдын', u'козуларыңдын', u'козуларынын', u'козуларыбыздын', u'козуларыңардын', u'козуларынын', u'козуларыңыздын', u'козуларыңыздардын']],
            u'таш': [
                [u'ташымдын', u'ташыңдын', u'ташынын', u'ташыбыздын', u'ташыңардын', u'ташынын', u'ташыңыздын', u'ташыңыздардын'],
                [u'таштарымдын', u'таштарыңдын', u'таштарынын', u'таштарыбыздын', u'таштарыңардын', u'таштарынын', u'таштарыңыздын', u'таштарыңыздардын']],
            u'бозо': [
                [u'бозомдун', u'бозоңдун', u'бозосунун', u'бозобуздун', u'бозоңордун', u'бозосунун', u'бозоңуздун', u'бозоңуздардын'],
                [u'бозолорумдун', u'бозолоруңдун', u'бозолорунун', u'бозолорубуздун', u'бозолоруңардын', u'бозолорунун', u'бозолоруңуздун', u'бозолоруңуздардын']],
            u'там': [
                [u'тамымдын', u'тамыңдын', u'тамынын', u'тамыбыздын', u'тамыңардын', u'тамынын', u'тамыңыздын', u'тамыңыздардын',],
                [u'тамдарымдын', u'тамдарыңдын', u'тамдарынын', u'тамдарыбыздын', u'тамдарыңардын', u'тамдарынын', u'тамдарыңыздын', u'тамдарыңыздардын']]
        }
