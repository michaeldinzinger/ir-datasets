import math
import re
import unittest

import ir_datasets
from ir_datasets.datasets.webfaq import QREL_DEFS
from ir_datasets.formats import GenericDoc, GenericQuery, GenericScoredDoc, TrecQrel

from .base import DatasetIntegrationTest


class TestWebFaq(DatasetIntegrationTest):
    def test_docs(self):
        self._test_docs('webfaq/ara', count=141089, items={
            0: GenericDoc('0', 'التحميد متوفر لفترة مستقبلة تبدا من تاريخ ارسال الطلب ولا يمكن ايقاف او تجميد الاشتراك عن فترات سابقة'),
            9: GenericDoc('9', re.compile(r'^في العادة لا يكون هنالك سبب خطير وراء هذه الشكوى اذا لم تكن مصاحبة باعراض اخرى\nفي اغلب الاحيان يكون .{188}ن المهم متابعة الاعراض اذا لم تتحسن يرجى مراجعة الطبيب اخصائي الاعصاب للخضوع لفحص سريري لتحديد السبب$', flags=48)),
            62098: GenericDoc('62689', re.compile(r'^خروج البول من المهبل قد يدل على وجود ناسور شرجي مهبلي، ولا بد من الفحص الطبي للتأكد من الموضوع، أما .{331}ة لاجراء الفحوصات الهرمونية اللازمة وكذلك فحص بجهاز الموجات الفوق صوتية للرحم والمبايض لتشخيص حالتك\.$', flags=48)),
            141088: GenericDoc('142663', 'عند السفر من براغ ، ستستخدم أحد المطارات التالية: روزين المطار. ستصل إلى هذه المطارات: الملك عبد العزيز العالمية المطار.'),
        })
        self._test_docs('webfaq/dan', count=136939, items={
            0: GenericDoc('0', re.compile(r'^Når du skal vælge en lægtehammer, er der flere faktorer, du bør overveje\. For det første er vægten a.{433} lægtehammer af høj kvalitet og holdbarhed, så den kan modstå gentagen brug og have en lang levetid\.$', flags=48)),
            9: GenericDoc('9', 'Det mest passende tidspunkt at besøge Ramnagar og reservere et hotel er fra november til juni, hvor vejret er behageligt.'),
            136938: GenericDoc('137685', re.compile(r'^Når du har søgt efter hoteller på KAYAK, kan du finjustere din søgning efter nabolag, så du kan vælg.{106}mt beliggenhed, f\.eks\. centrum af Amritsar Besøg vores Amritsar\-side for at finde de seneste tilbud!$', flags=48)),
        })

    def test_queries(self):
        self._test_queries('webfaq/ara/train', count=132664, items={
            0: GenericQuery('135771', 'كم يكلف تصنيع تصميم غرفة النوم'),
            9: GenericQuery('75193', 'هل الصراحة أهم من الحب؟'),
            132663: GenericQuery('76952', 'هل يتواجد لشركة نجوم الخليج فروع أخرى غيرشركة عزل اسطح بالدمام؟'),
        })
        self._test_queries('webfaq/ara/test', count=10000, items={
            0: GenericQuery('14384', 'هل استئصال المراره بالجراحه المفتوحه افضل من المنظار فى حالة وجود فتق بالسره وسمنه\nالسن 60 سنه ؟'),
            9: GenericQuery('90565', 'هل تتوفر خدمة الواي فاي في الداماي؟'),
            9999: GenericQuery('30805', 'هل يحتوي Xbox One على تقنية Bluetooth؟'),
        })
        self._test_queries('webfaq/dan/train', count=127686, items={
            0: GenericQuery('68046', 'Hvad gør jeg hvis min ordre er blevet skadet under levering?'),
            9: GenericQuery('98530', 'Kan et mobilt klimaanl�g bruges p� arbejdspladsen?'),
            127685: GenericQuery('59265', 'Hvad sker der, hvis jeg ikke henter min pakke indenfor den angivne tid?'),
        })
        self._test_queries('webfaq/dan/test', count=10000, items={
            0: GenericQuery('26645', 'Hvordan er området omkring Penzion Pleso?'),
            9: GenericQuery('55051', 'Hvor kan jeg finde brugsbetingelserne for jeres hjemmeside?'),
            9999: GenericQuery('55188', 'Hvad skal jeg gøre, hvis jeg modtog en defekt/forkert/plettet vare?'),
        })

    def test_qrels(self):
        self._test_qrels('webfaq/ara/train', count=132664, items={
            0: TrecQrel('135771', '99651', 1, '0'),
            9: TrecQrel('75193', '108312', 1, '0'),
            132663: TrecQrel('76952', '111451', 1, '0'),
        })
        self._test_qrels('webfaq/ara/test', count=10000, items={
            0: TrecQrel('14384', '43102', 1, '0'),
            9: TrecQrel('90565', '85256', 1, '0'),
            9999: TrecQrel('30805', '122902', 1, '0'),
        })
        self._test_qrels('webfaq/dan/train', count=127686, items={
            0: TrecQrel('68046', '54718', 1, '0'),
            9: TrecQrel('98530', '102829', 1, '0'),
            127685: TrecQrel('59265', '67543', 1, '0'),
        })
        self._test_qrels('webfaq/dan/test', count=10000, items={
            0: TrecQrel('26645', '99403', 1, '0'),
            9: TrecQrel('55051', '105898', 1, '0'),
            9999: TrecQrel('55188', '40902', 1, '0'),
        })

    def test_scoreddocs(self):
        self._test_webfaq_scoreddocs('ara', count=6336393, query_count=32000, items={
            0: GenericScoredDoc('60766', '108738', 0.99853515625),
            9: GenericScoredDoc('60766', '94981', 0.071044921875),
            6336392: GenericScoredDoc('7062', '98801', 1.5914440155029297e-05),
        })
        self._test_webfaq_scoreddocs('dan', count=6123062, query_count=32000, items={
            0: GenericScoredDoc('78410', '7331', 0.340576171875),
            9: GenericScoredDoc('78410', '38148', 0.004085540771484375),
            6123061: GenericScoredDoc('126557', '97913', 1.6033649444580078e-05),
        })

    def _test_webfaq_scoreddocs(self, language, count, query_count, items):
        dataset = ir_datasets.load(f'webfaq/{language}/train')
        document_ids = {doc.doc_id for doc in dataset.docs_iter()}
        training_query_ids = {query.query_id for query in dataset.queries_iter()}
        remaining_items = dict(items)
        seen_query_ids = set()
        current_query_id = None
        current_doc_ids = set()
        previous_score = None
        actual_count = 0

        for index, scoreddoc in enumerate(dataset.scoreddocs_iter()):
            actual_count += 1
            if index in remaining_items:
                self._assert_namedtuple(scoreddoc, remaining_items.pop(index))
            if scoreddoc.query_id not in training_query_ids:
                self.fail(f'Unknown {language} scoreddoc query ID: {scoreddoc.query_id}')
            if scoreddoc.doc_id not in document_ids:
                self.fail(f'Unknown {language} scoreddoc document ID: {scoreddoc.doc_id}')
            if not math.isfinite(scoreddoc.score):
                self.fail(f'Non-finite {language} score: {scoreddoc.score}')

            if scoreddoc.query_id != current_query_id:
                if scoreddoc.query_id in seen_query_ids:
                    self.fail(f'Non-contiguous {language} scoreddoc query: {scoreddoc.query_id}')
                seen_query_ids.add(scoreddoc.query_id)
                current_query_id = scoreddoc.query_id
                current_doc_ids = set()
                previous_score = None
            if scoreddoc.doc_id in current_doc_ids:
                self.fail(
                    f'Duplicate {language} scoreddoc pair: '
                    f'{scoreddoc.query_id}/{scoreddoc.doc_id}'
                )
            if previous_score is not None and scoreddoc.score > previous_score:
                self.fail(f'Unsorted {language} scores for query {scoreddoc.query_id}')
            current_doc_ids.add(scoreddoc.doc_id)
            previous_score = scoreddoc.score

        self.assertEqual(count, actual_count)
        self.assertEqual({}, remaining_items)
        self.assertEqual(query_count, len(seen_query_ids))

    def test_referential_integrity(self):
        expected_counts = {
            'ara': {'docs': 141089, 'train': 132664, 'test': 10000},
            'dan': {'docs': 136939, 'train': 127686, 'test': 10000},
        }
        for language, counts in expected_counts.items():
            collection = ir_datasets.load(f'webfaq/{language}')
            documents = list(collection.docs_iter())
            document_ids = {doc.doc_id for doc in documents}
            document_texts = {doc.text for doc in documents}
            with self.subTest(language=language, component='documents'):
                self.assertEqual(counts['docs'], len(documents))
                self.assertEqual(counts['docs'], len(document_ids))
                self.assertEqual(counts['docs'], len(document_texts))

            query_ids_by_split = {}
            for split in ('train', 'test'):
                dataset = ir_datasets.load(f'webfaq/{language}/{split}')
                queries = list(dataset.queries_iter())
                query_ids = {query.query_id for query in queries}
                qrel_query_ids = set()
                with self.subTest(language=language, split=split):
                    self.assertEqual(counts[split], len(queries))
                    self.assertEqual(counts[split], len(query_ids))
                    for qrel in dataset.qrels_iter():
                        self.assertEqual(1, qrel.relevance)
                        self.assertIn(qrel.query_id, query_ids)
                        self.assertIn(qrel.doc_id, document_ids)
                        self.assertNotIn(qrel.query_id, qrel_query_ids)
                        qrel_query_ids.add(qrel.query_id)
                    self.assertEqual(query_ids, qrel_query_ids)
                query_ids_by_split[split] = query_ids
            self.assertTrue(
                query_ids_by_split['train'].isdisjoint(query_ids_by_split['test'])
            )

    def test_dataset_components(self):
        expected_components = {
            'webfaq': (False, False, False, False),
            'webfaq/ara': (True, False, False, False),
            'webfaq/ara/train': (True, True, True, True),
            'webfaq/ara/test': (True, True, True, False),
            'webfaq/dan': (True, False, False, False),
            'webfaq/dan/train': (True, True, True, True),
            'webfaq/dan/test': (True, True, True, False),
        }
        for dataset_id, expected in expected_components.items():
            with self.subTest(dataset=dataset_id):
                dataset = ir_datasets.load(dataset_id)
                actual = (
                    dataset.has_docs(),
                    dataset.has_queries(),
                    dataset.has_qrels(),
                    dataset.has_scoreddocs(),
                )
                self.assertEqual(expected, actual)

        for language in ('ara', 'dan'):
            with self.assertRaises(KeyError):
                ir_datasets.load(f'webfaq/{language}/validation')

    def test_metadata(self):
        for language in ('ara', 'dan'):
            collection = ir_datasets.load(f'webfaq/{language}')
            train = ir_datasets.load(f'webfaq/{language}/train')
            test = ir_datasets.load(f'webfaq/{language}/test')
            with self.subTest(language=language):
                self.assertIs(collection.docs_handler(), train.docs_handler())
                self.assertIs(collection.docs_handler(), test.docs_handler())
                self.assertEqual(f'webfaq/{language}', collection.docs_namespace())
                self.assertEqual(language, collection.docs_lang())
                self.assertEqual(f'webfaq/{language}', train.queries_namespace())
                self.assertEqual(f'webfaq/{language}', test.queries_namespace())
                self.assertEqual(language, train.queries_lang())
                self.assertEqual(language, test.queries_lang())
                self.assertEqual(QREL_DEFS, train.qrels_defs())
                self.assertEqual(QREL_DEFS, test.qrels_defs())
                self.assertEqual(GenericDoc, collection.docs_cls())
                self.assertEqual(GenericQuery, train.queries_cls())
                self.assertEqual(TrecQrel, train.qrels_cls())
                self.assertEqual(GenericScoredDoc, train.scoreddocs_cls())

    def test_documentation(self):
        expected_citations = {
            'webfaq': ['Dinzinger2025WebFAQ', 'Dinzinger2026WebFAQ2'],
            'webfaq/ara': ['Dinzinger2025WebFAQ'],
            'webfaq/ara/train': ['Dinzinger2025WebFAQ', 'Dinzinger2026WebFAQ2'],
            'webfaq/ara/test': ['Dinzinger2025WebFAQ'],
            'webfaq/dan': ['Dinzinger2025WebFAQ'],
            'webfaq/dan/train': ['Dinzinger2025WebFAQ', 'Dinzinger2026WebFAQ2'],
            'webfaq/dan/test': ['Dinzinger2025WebFAQ'],
        }
        for dataset_id, citations in expected_citations.items():
            with self.subTest(dataset=dataset_id):
                documentation = ir_datasets.load(dataset_id).documentation()
                self.assertIn('WebFAQ', documentation['desc'])
                self.assertEqual(citations, documentation['bibtex_ids'])


if __name__ == '__main__':
    unittest.main()
