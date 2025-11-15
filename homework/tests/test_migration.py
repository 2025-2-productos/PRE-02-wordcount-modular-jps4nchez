import os

from ..src.wordcount import main


def test_migracion():

    main()

    results_path = "data/output/wordcount.tsv"
    if not os.path.exists(results_path):
        raise FileNotFoundError("El archivo wordcount.tsv no existe.")

    results = {}
    with open(results_path, "r", encoding="utf-8") as f:
        for line in f:
            word, count = line.strip().split("\t")
            results[word] = int(count)

    assert results["computational"] == 3
    assert results["analytics"] == 5
