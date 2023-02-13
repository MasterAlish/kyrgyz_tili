from kg.lang.affixing import apply_affix
from kg.lang.lang import KyrgyzWord
from kg.tests import KGTestCase


class JondomoAfterGanMuchoTest(KGTestCase):
    def test_jondomo_after_gan(self):
        data = self.get_data()

        for word, expected_forms in data.items():
            word_object = KyrgyzWord(word)
            affixes = apply_affix({'gan': ['jondomo']}, word_object)
            generated = set()
            for affix in affixes.values():
                for result in affix.generate_results():
                    generated.add(str(result))
            self.assertEqual(generated, set(expected_forms))

    def get_data(self):
        return {
            'сай': [
                'сайгандардын',
                'сайгандарга',
                'сайгандарды',
                'сайгандарда',
                'сайгандардан',
                'сайгандын',
                'сайганга',
                'сайганды',
                'сайганда',
                'сайгандан',
            ],
            'топто': [
                'топтогондордун',
                'топтогондорго',
                'топтогондорду',
                'топтогондордо',
                'топтогондордон',
                'топтогондун',
                'топтогонго',
                'топтогонду',
                'топтогондо',
                'топтогондон',
            ],
            'ташта': [
                'таштагандардын',
                'таштагандарга',
                'таштагандарды',
                'таштагандарда',
                'таштагандардан',
                'таштагандын',
                'таштаганга',
                'таштаганды',
                'таштаганда',
                'таштагандан',
            ]
        }
