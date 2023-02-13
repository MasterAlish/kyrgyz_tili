from kg.lang.etish.chak import KelerChak
from kg.lang.helps.attrs import *
from kg.lang.lang import KyrgyzWord
from kg.tests import KGTestCase


attrs_list = [men, sen, al, biz, siler, alar, siz, sizder]


class KelerChakTest(KGTestCase):
    def test_1(self):

        data = self.get_data()

        for word, expected_forms in data.items():
            chak = KelerChak(KyrgyzWord(word))
            for i in range(len(attrs_list)):
                attrs = attrs_list[i]
                self.assertEqual(chak.make(attrs.jak, attrs.jeke, attrs.sylyk), expected_forms[i])

    def get_data(self):
        return {
            'кара': [
                'карайм', 'карайсың', 'карайт',
                'карайбыз', 'карайсыңар', 'карашат',
                'карайсыз', 'карайсыздар'],

            'сай': [
                'саям', 'саясың', 'саят',
                'саябыз', 'саясыңар', 'сайышат',
                'саясыз', 'саясыздар'],

            'ташы': [
                'ташыйм', 'ташыйсың', 'ташыйт',
                'ташыйбыз', 'ташыйсыңар', 'ташышат',
                'ташыйсыз', 'ташыйсыздар'],

            'ук': [
                'угам', 'угасың', 'угат',
                'угабыз', 'угасыңар', 'угушат',
                'угасыз', 'угасыздар'],

            'чой': [
                'чоём', 'чоёсуң', 'чоёт',
                'чоёбуз', 'чоёсуңар', 'чоюшат',
                'чоёсуз', 'чоёсуздар'],

            'ал': [
                'алам', 'аласың', 'алат',
                'алабыз', 'аласыңар', 'алышат',
                'аласыз', 'аласыздар'],

            'бар': [
                'барам', 'барасың', 'барат',
                'барабыз', 'барасыңар', 'барышат',
                'барасыз', 'барасыздар'],

            'жаса': [
                'жасайм', 'жасайсың', 'жасайт',
                'жасайбыз', 'жасайсыңар', 'жасашат',
                'жасайсыз', 'жасайсыздар'],

            'ич': [
                'ичем', 'ичесиң', 'ичет',
                'ичебиз', 'ичесиңер', 'ичишет',
                'ичесиз', 'ичесиздер'],

            'каз': [
                'казам', 'казасың', 'казат',
                'казабыз', 'казасыңар', 'казышат',
                'казасыз', 'казасыздар'],

            'кий': [
                'кием', 'киесиң', 'киет',
                'киебиз', 'киесиңер', 'кийишет',
                'киесиз', 'киесиздер'],

            'кичирей': [
                'кичиреем', 'кичиреесиң', 'кичиреет',
                'кичиреебиз', 'кичиреесиңер', 'кичирейишет',
                'кичиреесиз', 'кичиреесиздер'],

            'кыл': [
                'кылам', 'кыласың', 'кылат',
                'кылабыз', 'кыласыңар', 'кылышат',
                'кыласыз', 'кыласыздар'],

            'тап': [
                'табам', 'табасың', 'табат',
                'табабыз', 'табасыңар', 'табышат',
                'табасыз', 'табасыздар'],

            'теп': [
                'тебем', 'тебесиң', 'тебет',
                'тебебиз', 'тебесиңер', 'тебишет',
                'тебесиз', 'тебесиздер'],

            'токто': [
                'токтойм', 'токтойсуң', 'токтойт',
                'токтойбуз', 'токтойсуңар', 'токтошот',
                'токтойсуз', 'токтойсуздар'],

            'алай': [
                'алаям', 'алаясың', 'алаят',
                'алаябыз', 'алаясыңар', 'алайышат',
                'алаясыз', 'алаясыздар'],

            'куй': [
                'куям', 'куясың', 'куят',
                'куябыз', 'куясыңар', 'куюшат',
                'куясыз', 'куясыздар'],

            'бойтой': [
                'бойтоём', 'бойтоёсуң', 'бойтоёт',
                'бойтоёбуз', 'бойтоёсуңар', 'бойтоюшат',
                'бойтоёсуз', 'бойтоёсуздар'],

            'былчый': [
                'былчыям', 'былчыясың', 'былчыят',
                'былчыябыз', 'былчыясыңар', 'былчыйышат',
                'былчыясыз', 'былчыясыздар'],

            'кеңей': [
                'кеңеем', 'кеңеесиң', 'кеңеет',
                'кеңеебиз', 'кеңеесиңер', 'кеңейишет',
                'кеңеесиз', 'кеңеесиздер'],

            'буруй': [
                'буруям', 'буруясың', 'буруят',
                'буруябыз', 'буруясыңар', 'буруюшат',
                'буруясыз', 'буруясыздар'],

            'ой': [
                'оём', 'оёсуң', 'оёт',
                'оёбуз', 'оёсуңар', 'оюшат',
                'оёсуз', 'оёсуздар'],

            'акшый': [
                'акшыям', 'акшыясың', 'акшыят',
                'акшыябыз', 'акшыясыңар', 'акшыйышат',
                'акшыясыз', 'акшыясыздар'],

        }
