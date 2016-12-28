from kg_lang.kyrgyz.lang import WordEndingTypes


class Affix(object):
    def make(self, jak=1, jeke=True, sylyk=False):
        pass

    def transformers(self):
        return []

    def is_pluralable(self):
        return False

    def get_pluralizations(self):
        return [
            self.make(1, False, False),
            self.make(1, True, False),
            self.make(2, False, False),
            self.make(2, True, False),
            self.make(2, False, True),
            self.make(2, True, True),
            self.make(3, False, True),
            self.make(3, True, True),
        ]

    indexes = {
        WordEndingTypes.UNSUZ_JOK: {
            WordEndingTypes.UNDUU_JOON_ERINSIZ: (0, 0),
            WordEndingTypes.UNDUU_JOON_ERINDUU: (0, 1),
            WordEndingTypes.UNDUU_ICHKE_ERINSIZ: (0, 2),
            WordEndingTypes.UNDUU_ICHKE_ERINDUU: (0, 3),
        },
        WordEndingTypes.UNSUZ_JUMSHAK_UYAN: {
            WordEndingTypes.UNDUU_JOON_ERINSIZ: (1, 0),
            WordEndingTypes.UNDUU_JOON_ERINDUU: (1, 1),
            WordEndingTypes.UNDUU_ICHKE_ERINSIZ: (1, 2),
            WordEndingTypes.UNDUU_ICHKE_ERINDUU: (1, 3),
        },
        WordEndingTypes.UNSUZ_UYAN_RYI: {
            WordEndingTypes.UNDUU_JOON_ERINSIZ: (2, 0),
            WordEndingTypes.UNDUU_JOON_ERINDUU: (2, 1),
            WordEndingTypes.UNDUU_ICHKE_ERINSIZ: (2, 2),
            WordEndingTypes.UNDUU_ICHKE_ERINDUU: (2, 3),
        },
        WordEndingTypes.UNSUZ_KATKALAN: {
            WordEndingTypes.UNDUU_JOON_ERINSIZ: (3, 0),
            WordEndingTypes.UNDUU_JOON_ERINDUU: (3, 1),
            WordEndingTypes.UNDUU_ICHKE_ERINSIZ: (3, 2),
            WordEndingTypes.UNDUU_ICHKE_ERINDUU: (3, 3),
        }
    }

    def generate_results(self):
        if self.is_pluralable():
            for pluralized in self.get_pluralizations():
                yield pluralized
        else:
            for transformer in self.transformers():
                if callable(transformer):
                    yield transformer(self)
