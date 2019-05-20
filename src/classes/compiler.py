# coding: utf-8
from classes.project import Project
from classes.parsers.ebnf import EBNF
from classes.analyser import Analyser

import os.path
import os
import fnmatch

class Compiler:
    
    def find(self, pattern, path):
        result = []

        for root, dirs, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    result.append(os.path.join(root, name))
					
        return result

    def __init__(self, project):
        self.project = project
        self.analyser = Analyser()
        self.files = []         
         
        grammarFile = "./grammar/" + self.project.config['language'] + ".lark"
         
        if (os.path.exists(grammarFile)):
             self.parser = EBNF(grammarFile)
        else:
            raise Exception(_("Arquivo de linguagem não encontrado: %s") % self.config["language"])         

    def parseFile(self, program):
        self.files.append([program, self.parser.parse(program)])
    
    def __createDeclarations(self, tree):
        self.analyser.createDeclarations(tree)         
         
    def compile(self):
		# procurando arquivo principal
        fileList = self.find('main.*', self.project.project_path)

        if (len(fileList) == 1):
            mainFile = fileList[0]
		
            # nivel 1 
            # parser / analyser 
            # Lexica / sintatica
		
            self.parseFile(mainFile)
        
            # nivel 2 
            # varre a arvore e cria todos os elementos 
			
            for file in self.files:
                filename = file[0]
                tree = file[1]
			
                self.__createDeclarations(tree)
        else:
            raise Exception(_("Arquivo principal não foi encontrado"))   
         
         
         