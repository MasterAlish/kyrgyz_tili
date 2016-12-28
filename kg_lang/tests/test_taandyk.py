# coding=utf-8
from kg_lang.kyrgyz.chak import UchurChak, OtkonChak
from kg_lang.kyrgyz.lang import KyrgyzWord
from kg_lang.kyrgyz.taandyk import Taandyk
from kg_lang.tests import KGTestCase

Jeke = True
Sylyk = True
Kop = False
SylykEmes = False


class TaandykTest(KGTestCase):
    def test_1(self):
        keys = [(1, Jeke, SylykEmes), (2, Jeke, SylykEmes), (3, Jeke, SylykEmes),
                (1, Kop, SylykEmes), (2, Kop, SylykEmes), (3, Kop, SylykEmes),
                (2, Jeke, Sylyk), (2, Kop, Sylyk)]

        data = self.get_data()

        for word, forms in data.items():
            taandyk = Taandyk(KyrgyzWord(word, False))
            for i in range(len(keys)):
                jak, san, sylyk = keys[i]
                self.assertEqual(taandyk.make(jak, san, sylyk).word, forms[i])

    def get_data(self):
        return {
            u'кий': [
                u'кийим', u'кийиң', u'кийи',
                u'кийибиз', u'кийиңер', u'кийи',
                u'кийиңиз', u'кийиңиздер'],

            u'таш': [
                u'ташым', u'ташың', u'ташы',
                u'ташыбыз', u'ташыңар', u'ташы',
                u'ташыңыз', u'ташыңыздар'],

            u'кыл': [
                u'кылым', u'кылың', u'кылы',
                u'кылыбыз', u'кылыңар', u'кылы',
                u'кылыңыз', u'кылыңыздар'],

            u'каз': [
                u'казым', u'казың', u'казы',
                u'казыбыз', u'казыңар', u'казы',
                u'казыңыз', u'казыңыздар'],

            u'сай': [
                u'сайым', u'сайың', u'сайы',
                u'сайыбыз', u'сайыңар', u'сайы',
                u'сайыңыз', u'сайыңыздар'],

            u'ич': [
                u'ичим', u'ичиң', u'ичи',
                u'ичибиз', u'ичиңер', u'ичи',
                u'ичиңиз', u'ичиңиздер'],

            u'токтом': [
                u'токтомум', u'токтомуң', u'токтому',
                u'токтомубуз', u'токтомуңар', u'токтому',
                u'токтомуңуз', u'токтомуңуздар'],

            u'ой': [
                u'ойум', u'ойуң', u'ойу',
                u'ойубуз', u'ойуңар', u'ойу',
                u'ойуңуз', u'ойуңуздар'],

            u'бала': [
                u'балам', u'балаң', u'баласы',
                u'балабыз', u'балаңар', u'баласы',
                u'балаңыз', u'балаңыздар'],

            u'көл': [
                u'көлүм', u'көлүң', u'көлү',
                u'көлүбүз', u'көлүңөр', u'көлү',
                u'көлүңүз', u'көлүңүздөр'],

        }
