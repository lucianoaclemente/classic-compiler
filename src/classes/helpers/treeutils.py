class TreeUtils:

    def __init__(self):
        None

    def readTokens(self, node, json, parent):
        for child in node.children:
            if (type(child).__name__ == "Tree"):
                parent = child.data
                json = self.readTokens(child, json, parent)
            else:
                if (parent not in json):
                    json[parent] = []
                     
                json[parent].append(child)

        return json
