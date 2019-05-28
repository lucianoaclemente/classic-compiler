# coding: utf-8
class IncludeDirective:

    def __init__(self, subtree, level):
        self.value = ""
        self.analyse(subtree, level)
        
    def getToken(self, subtree, level, parent):
        for child in subtree.children:
            if (type(child).__name__ == "Token"):
                self.value = child.value
            else:
                self.getToken(child, level+2, parent)
                
    def analyse(self, subtree, level):
        
        for child in subtree.children:
            if (type(child).__name__ == "Tree"):
                if (child.data == "filename"):        
                    self.getToken(child, level+2, child.data)
                else:
                    self.analyse(child, level+2)    

