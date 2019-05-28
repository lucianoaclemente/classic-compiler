# coding: utf-8
from classes.common import Common
from classes.project import Project
from classes.parsers.ebnf import EBNF
from classes.analyser import Analyser

import os.path
import os
import fnmatch

class Compiler:
    
    root_path = ""
    project_path = ""
    
    def find(self, pattern, path):
        result = []

        for root, dirs, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    result = [root, name]
					
        return result

    def __init__(self, project):
        self.project = project
        self.analyser = Analyser()
        self.files = []         
         
        grammarFile = os.path.join(Common.params["root_path"], "grammar/") + self.project.config['language'] + ".lark"
         
        if (os.path.exists(grammarFile)):
             self.parser = EBNF(grammarFile)
        else:
            raise Exception(_("Arquivo de linguagem não encontrado: %s") % self.project.config["language"])         

    def parseFile(self, rootPath, program):
        tree = self.parser.parse(os.path.join(rootPath, program))
    
        self.files.append([program, tree])
        currentFile = self.files[len(self.files)-1];

        includes = []

        self.analyser.checkIncludes(tree, includes)

        for includeFile in includes:
            self.parseFile(rootPath, includeFile.value)   
    
    def __checkDeclarations(self, tree):
        self.analyser.checkDeclarations(tree)         
         
    def compile(self):
		# procurando arquivo principal
        fileList = self.find('main.*', Common.params["project_path"])

        if (len(fileList) == 2):
            
            rootPath = fileList[0]
            mainFile = fileList[1]
            
            # nivel 1 
            # parser / analyser 
            # Lexica / sintatica
		
            self.parseFile(rootPath, mainFile)
        
            # nivel 2 
            # varre a arvore e cria todos os elementos 
			
            for file in self.files:
                filename = file[0]
                tree = file[1]
			
                self.__checkDeclarations(tree)
        else:
            raise Exception(_("Arquivo principal não foi encontrado"))   
         
         
         