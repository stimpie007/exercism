from json import dumps

class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children or []

    def __dict(self):
        return {self.label: [c.__dict() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict() == other.__dict()

    def from_pov(self, from_node):
        path = []
        if not self._search(from_node, self, path):
            raise ValueError(f"node {from_node} does not exist")
        for i, node in enumerate(path):
            if i < len(path) - 1:
                node.children.remove(path[i + 1])
            if i > 0:
                node.children.append(path[i - 1])
        return path[-1]

    def path_to(self, from_node, to_node):
        root, path = self.from_pov(from_node), []
        if not self._search(to_node, root, path):
            raise ValueError(f"node {to_node} does not exist")
        return [node.label for node in path]

    def _search(self, label, node, path):
        path.append(node)
        if node.label == label:
            return True

        for c in node.children:
            if self._search(label, c, path):
                return True
            path.pop()
        return False