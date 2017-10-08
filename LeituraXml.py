#https://docs.python.org/2/library/xml.etree.elementtree.html
#https://pythonhelp.wordpress.com/2012/06/22/propriedades-em-python/
#https://docs.python.org/3/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET
import sys

class LeituraXml:


    __arquivoxml = "C:\\Users\\andrej\\Desktop\\Python_Build\\produtos_core.xml"

    """
    Construtor que recebe uma aplicação

    """
    def __init__(self,nomeaplicacao):
        self.__nomeaplicacao = nomeaplicacao


    def readxml(self,app):

        tree = ET.ElementTree(file=self.__arquivoxml)
        root = tree.getroot()
        aplicacoes = []

        for child in root.findall('sistema'):
            self.nomesigla = child.find('sigla').text
            if self.nomesigla == app:
                aplicacoes.append(self.nomesigla)
                self.nomeaplicacao = child.find('aplicacao').text
                self.reposgit = child.find('reposgit').text
                self.versaomaven = child.find('versaomaven').text
                self.dirgit = child.find('dirgit').text

        """Validar se a aplicação existe no xml"""
        """A primeira forma que encontrei"""
        if not app in aplicacoes:
            print("Aplicação %s não cadastrada no xml" % app)
            print("É necessário cadastrar a aplicação e as tags no arquivo produtos_core.xml")
            sys.exit(1)#sai do programa

        for child in root.findall('configuracoes'):
            self.tempdir = child.find('temp_dir').text


    def get__sigla(self):
        return self.nomesigla

    def set__sigla(self,nomesigla):
        self.nomesigla = nomesigla

    def get__maven(self):
        return self.versaomaven

    def set__maven(self, versaomaven):
        self.versaomaven = versaomaven

    def get__nomeaplicacao(self):
        return self.nomeaplicacao

    def set__nomeaplicacao(self,nomeaplicacao):
        self.nomeaplicacao = nomeaplicacao

    def get__reposgit(self):
        return self.reposgit

    def set__reposgit(self,reposgit):
        self.reposgit = reposgit

    def get__dirgit(self):
        return self.dirgit

    def set__sigla(self, dirgit):
        self.dirgit = dirgit

    def get__tempdir(self):
        return self.tempdir

    def set__tempdir(self, tempdir):
        self.tempdir = tempdir


