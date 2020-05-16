#passos Automatizados disponíveis em https://wiki.matera.com/wiki/Fechamento_Manual_de_Versões_que_estão_no_GIT

from GitComando import *
from LeituraXml import *

class ExecTipoBuildGit():

    def __init__(self,tipo,diretoriotemp,nomediretorioprojeto,urlprojeto):
        self.tipo = tipo  # tipo branch
        self.diretoriotemp = diretoriotemp  # tipo branch
        self.nomediretorioprojeto = nomediretorioprojeto  # tipo branch
        self.urlprojeto = urlprojeto  # tipo branch

    def exec_build_release(self,versaobuild):
        print("Executando a build no branch de release")
        print("Informações para Build:")
        print("Versão para Build %s" % versaobuild)
        print("******")
        buildrelease = GitComando
        buildrelease.gitclone(self.diretoriotemp,self.nomediretorioprojeto,self.urlprojeto)

    def exec_build_develop(self,versao,proximaversao):
        print("Executando a build no branch de develop")
        print("Informações para Build:")
        print("Versão para Build %s" % versao)
        print("Próxima versão %s" % proximaversao)
        print("******")
        builddevelop = GitComando
        builddevelop.gitclone(self.diretoriotemp,self.nomediretorioprojeto,self.urlprojeto)

    def exec_build_outros(self,versao,proximaversao):
        print("Executando a build em outros branches")
        print("Informações para Build:")
        print("Versão para Build %s" % versao)
        print("Próxima versão %s" % proximaversao)
        print("******")
        buildoutros = GitComando
        buildoutros.gitclone(self.diretoriotemp,self.nomediretorioprojeto,self.urlprojeto)