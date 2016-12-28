# coding=utf-8
from kg_lang.kyrgyz.helps.attrs import *
from kg_lang.kyrgyz.jondomo import Jondomo
from kg_lang.kyrgyz.lang import KyrgyzWord
from kg_lang.kyrgyz.san import San
from kg_lang.kyrgyz.taandyk import Taandyk
from kg_lang.tests import KGTestCase


attrs_list = [men, sen, al, biz, siler, alar, siz, sizder]


class JondomoIlikAfterTaandykTest(KGTestCase):
    def test_ilik_after_taandyk(self):
        data = {
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
        for word, forms in data.items():
            koptuk = San(KyrgyzWord(word)).koptuk()
            for i in range(len(attrs_list)):
                attr = attrs_list[i]
                jeke_form = forms[0][i]
                taandyk = Taandyk(KyrgyzWord(word)).make(attr.jak, attr.jeke, attr.sylyk)
                jondomo = Jondomo(taandyk)
                self.assertEqual(jondomo.ilik(), jeke_form)

                koptuk_form = forms[1][i]
                taandyk_koptuk = Taandyk(koptuk).make(attr.jak, attr.jeke, attr.sylyk)
                jondomo_koptuk = Jondomo(taandyk_koptuk)
                self.assertEqual(jondomo_koptuk.ilik(), koptuk_form)
