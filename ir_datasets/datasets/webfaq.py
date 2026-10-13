import ir_datasets
from ir_datasets.datasets.base import Dataset, YamlDocumentation
from ir_datasets.formats import JsonlDocs, JsonlQueries, TrecQrels
from ir_datasets.formats.trec import TrecScoredDocs
from ir_datasets.util.download import DownloadConfig
from ir_datasets.util.fileio import RelativePath, TarExtractAll

NAME = "webfaq"

QREL_DEFS = {
    1: "The document is a confirmed answer to the FAQ question.",
}

LANGS = (
    "ara",
    "dan",
    "deu",
    "eng",
    "fas",
    "fra",
    "hin",
    "ind",
    "ita",
    "jpn",
    "kor",
    "nld",
    "pol",
    "por",
    "rus",
    "spa",
    "swe",
    "tur",
    "vie",
    "zho",
)


def _init():
    documentation = YamlDocumentation(f'docs/{NAME}.yaml')
    base_path = ir_datasets.util.home_path() / NAME
    dlc = DownloadConfig.context(NAME, base_path)

    base = Dataset(documentation("_"))

    subsets = {}

    for lang in LANGS:
        source = TarExtractAll(dlc[lang], base_path / lang)

        # The current archives contain:
        # webfaq/{lang}/documents.jsonl
        # webfaq/{lang}/training/...
        # webfaq/{lang}/test/...
        archive_root = f"webfaq/{lang}"

        docs = JsonlDocs(
            RelativePath(source, f"{archive_root}/documents.jsonl"),
            namespace=f"{NAME}/{lang}",
            lang=lang,
            count_hint=ir_datasets.util.count_hint(f"{NAME}/{lang}"),
            docstore_path=base_path / f"{lang}.pklz4",
        )

        subsets[lang] = Dataset(
            docs,
            documentation(lang),
        )

        subsets[f"{lang}/train"] = Dataset(
            docs,
            JsonlQueries(
                RelativePath(source, f"{archive_root}/training/queries.jsonl"),
                namespaec=f"{NAME}/{lang}",
                lang=lang,
            ),
            TrecQrels(
                RelativePath(source, f"{archive_root}/training/qrels"),
                qrels_defs=QREL_DEFS,
            ),
            TrecScoredDocs(
                RelativePath(source, f"{archive_root}/training/BGE-M3.res"),
            ),
            documentation(f"{lang}/train"),
        )

        subsets[f"{lang}/test"] = Dataset(
            docs,
            JsonlQueries(
                RelativePath(source, f"{archive_root}/test/queries.jsonl"),
                namespaec=f"{NAME}/{lang}",
                lang=lang,
            ),
            TrecQrels(
                RelativePath(source, f"{archive_root}/test/qrels"),
                qrels_defs=QREL_DEFS,
            ),
            documentation(f"{lang}/test"),
        )

    ir_datasets.registry.register(NAME, base)
    for s in sorted(subsets):
        ir_datasets.registry.register(f"{NAME}/{s}", subsets[s])

    return base, subsets

base, subsets = _init()
