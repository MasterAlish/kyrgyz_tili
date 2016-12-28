# coding=utf-8
from kg_lang.kyrgyz.affixes import apply_affix
from kg_lang.kyrgyz.lang import KyrgyzWord
from kg_lang.tests import KGTestCase


class JondomoAfterGanMuchoTest(KGTestCase):
    def test_jondomo_after_gan(self):
        data = self.get_data()

        for word, expected_forms in data.items():
            word_object = KyrgyzWord(word)
            affixes = apply_affix({'gan': ['jondomo']}, word_object)
            generated = []
            for affix in affixes.values():
                for result in affix.generate_results():
                    generated.append(unicode(result))
            self.assertEqual(generated, expected_forms)

    def get_data(self):
        return {
            u'сай': [
                u'сайгандардын',
                u'сайгандарга',
                u'сайгандарды',
                u'сайгандарда',
                u'сайгандардан',
                u'сайгандын',
                u'сайганга',
                u'сайганды',
                u'сайганда',
                u'сайгандан',
            ],
            u'топто': [
                u'топтогондордун',
                u'топтогондорго',
                u'топтогондорду',
                u'топтогондордо',
                u'топтогондордон',
                u'топтогондун',
                u'топтогонго',
                u'топтогонду',
                u'топтогондо',
                u'топтогондон',
            ],
            u'ташта': [
                u'таштагандардын',
                u'таштагандарга',
                u'таштагандарды',
                u'таштагандарда',
                u'таштагандардан',
                u'таштагандын',
                u'таштаганга',
                u'таштаганды',
                u'таштаганда',
                u'таштагандан',
            ]
        }
