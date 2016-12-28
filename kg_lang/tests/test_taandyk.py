# coding=utf-8
from kg_lang.kyrgyz.helps.attrs import *
from kg_lang.kyrgyz.lang import KyrgyzWord
from kg_lang.kyrgyz.taandyk import Taandyk
from kg_lang.tests import KGTestCase


attrs_list = [men, sen, al, biz, siler, alar, siz, sizder]


class TaandykTest(KGTestCase):
    def test_1(self):
        data = self.get_data()

        for word, forms in data.items():
            taandyk = Taandyk(KyrgyzWord(word))
            for i in range(len(attrs_list)):
                attrs = attrs_list[i]
                self.assertEqual(taandyk.make(attrs.jak, attrs.jeke, attrs.sylyk).word, forms[i])

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
