# coding: utf-8
from classes.helpers.labelmanager import LabelManager
class ConstantDefinition:

    value = []

    def __init__(self, subtree, level):
        self.value = []
        self.analyse(subtree, level)
        
    def getToken(self, subtree, level, parent):
        for child in subtree.children:
            if (type(child).__name__ == "Token"):
                self.value.append(child.type)
                self.value.append(child.value)
                
                if (parent == "identifier"):
                    LabelManager.next("constant", child.value)
            else:
                self.getToken(child, level+2, parent)
                
    def analyse(self, subtree, level):
        
        for child in subtree.children:
            if (type(child).__name__ == "Tree"):
                if (child.data == "identifier") or (child.data == "constant"):        
                    self.getToken(child, level+2, child.data)
                else:
                    self.analyse(child, level+2)
