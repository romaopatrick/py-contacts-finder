from pytest_benchmark.fixture import BenchmarkFixture
from src.models.contact_tree import ContactTree


def test_benchmark_search_prefix(benchmark: BenchmarkFixture):
    contacts = ["A", "B", "C", "Z", "F", "I", "H"]
    prefix = "h"
    ctree = ContactTree(initial=contacts)
    result = benchmark(ctree.search_prefix, prefix)
    assert result[0] == "H"

def test_benchmark_normal_prefix_search(benchmark: BenchmarkFixture):
    contacts = ["A", "B", "C", "Z", "F", "I", "H"]
    prefix = "h"

    def compare_func(contacts: list[str], prefix: str) -> list[str]:
        search_results = [it.capitalize() for it in contacts if it.lower().startswith(prefix)]
        return search_results

    result2 = benchmark(compare_func, contacts, prefix)

    assert result2[0] == 'H'
