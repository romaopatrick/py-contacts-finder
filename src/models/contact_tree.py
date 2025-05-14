from src.models.btree import BNode, BTree


class ContactTree(BTree):
    def __init__(self, initial: list[str] = []):
        super().__init__([i.lower() for i in initial])

    def search_prefix(self, prefix: str) -> list[str]:
        matches = []
        self._search_prefix_recursive(self.root, prefix.lower(), matches)
        return matches

    def _search_prefix_recursive(self, node: BNode, prefix: str, matches: list[str]):
        if not node:
            return

        if str(node.value).startswith(prefix):
            matches.append(str(node.value).capitalize())

        if prefix <= node.value:
            self._search_prefix_recursive(node.left, prefix, matches)
            return

        self._search_prefix_recursive(node.right, prefix, matches)
