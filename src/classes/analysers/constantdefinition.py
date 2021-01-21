# coding: utf-8
from classes.common import Common
from classes.helpers.labelmanager import LabelManager
class ConstantDefinition:

    def __init__(self):
        self.items = { }
        
    def getToken(self, subtree, level, parent):
        for child in subtree.children:
            if (type(child).__name__ == "Token"):
                if (parent == "identifier"):
                    self.items["class"] = "constant"
                    self.items["name"] = child.value
                    LabelManager.next("constant", child.value)
                else:
                    self.items["type"] = child.type
                    self.items["value"] = child.value
            else:
                self.getToken(child, level+2, parent)
                
    def analyse(self, subtree, level):
        
        for child in subtree.children:
            if (type(child).__name__ == "Tree"):
                if (child.data == "identifier") or (child.data == "constant"):     
                    self.getToken(child, level+2, child.data)
                else:
                    self.analyse(child, level+2)

        return self.items