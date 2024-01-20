import boyer_moore_search as bms
import kmp_search as kmp
import rabin_karp_search as rks
from timeit import timeit

EXISTING_STRING_1 = "Фундаментальні знання допомагають дізнатися"
EXISTING_STRING_2 = "Вибір методу представлення даних"


def print_timing(algorithm_name, execution_time, result):
    print(f"{algorithm_name}: {execution_time:.6f} seconds, result: {result}")


for file in ["data/article_1.txt", "data/article_2.txt"]:
    with open(file, "r", encoding="windows-1251") as f:
        text = f.read()

        for pattern in [EXISTING_STRING_1, EXISTING_STRING_2]:
            print(f"File: {file}, Pattern: {pattern}")
            print_timing(
                "Boyer-Moore",
                timeit(
                    "bms.boyer_moore_search(text, pattern)", globals=globals(), number=1
                ),
                bms.boyer_moore_search(text, pattern),
            )
            print_timing(
                "KMP",
                timeit("kmp.kmp_search(text, pattern)", globals=globals(), number=1),
                kmp.kmp_search(text, pattern),
            )
            print_timing(
                "Rabin-Karp",
                timeit(
                    "rks.rabin_karp_search(text, pattern)", globals=globals(), number=1
                ),
                rks.rabin_karp_search(text, pattern),
            )
