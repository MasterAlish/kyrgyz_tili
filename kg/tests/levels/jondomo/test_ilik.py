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
            'козу': [
                ['козумдун', 'козуңдун', 'козусунун', 'козубуздун', 'козуңардын', 'козусунун', 'козуңуздун', 'козуңуздардын'],
                ['козуларымдын', 'козуларыңдын', 'козуларынын', 'козуларыбыздын', 'козуларыңардын', 'козуларынын', 'козуларыңыздын', 'козуларыңыздардын']],
            'таш': [
                ['ташымдын', 'ташыңдын', 'ташынын', 'ташыбыздын', 'ташыңардын', 'ташынын', 'ташыңыздын', 'ташыңыздардын'],
                ['таштарымдын', 'таштарыңдын', 'таштарынын', 'таштарыбыздын', 'таштарыңардын', 'таштарынын', 'таштарыңыздын', 'таштарыңыздардын']],
            'бозо': [
                ['бозомдун', 'бозоңдун', 'бозосунун', 'бозобуздун', 'бозоңордун', 'бозосунун', 'бозоңуздун', 'бозоңуздардын'],
                ['бозолорумдун', 'бозолоруңдун', 'бозолорунун', 'бозолорубуздун', 'бозолоруңардын', 'бозолорунун', 'бозолоруңуздун', 'бозолоруңуздардын']],
            'там': [
                ['тамымдын', 'тамыңдын', 'тамынын', 'тамыбыздын', 'тамыңардын', 'тамынын', 'тамыңыздын', 'тамыңыздардын',],
                ['тамдарымдын', 'тамдарыңдын', 'тамдарынын', 'тамдарыбыздын', 'тамдарыңардын', 'тамдарынын', 'тамдарыңыздын', 'тамдарыңыздардын']]
        }
