import sys
from LeituraXml import LeituraXml
from ExecTipoBuildGit import *
import GitComando

#verificar a necessidade da valiação do main
if __name__ == "__main__":
    quant = len(sys.argv[1:])

    if quant == 3:

        app = sys.argv[1]
        versao = sys.argv[2]
        branch = sys.argv[3]

    elif quant == 4:

        app = sys.argv[1]
        versao = sys.argv[2]
        branch = sys.argv[3]
        prox_versao = sys.argv[4]


    else:
        print("Quantidade de parans invalidos")
        print("O certo é %s aplicação" % sys.argv[0])


    produto = LeituraXml(app)
    produto.readxml(app)

    print("Iniciando o processo de Build da aplicação: %s" % produto.get__nomeaplicacao())
    print("Versão: %s" % versao)
    print("Branch: %s" % branch)
    print("Diretório temporário: %s" % produto.tempdir)


    if(str(branch).__eq__("release")):

        print("Build release")
        tiporelease = ExecTipoBuildGit(branch,produto.get__tempdir(),produto.get__dirgit(),produto.reposgit)
        tiporelease.exec_build_release(versao)


    elif(str(branch).__eq__("develop")):

        print("Build develop")
        tipodevelop = ExecTipoBuildGit(branch,produto.get__tempdir(),produto.get__dirgit(),produto.reposgit)
        tipodevelop.exec_build_develop(versao,prox_versao)

    else:

        print("Build outros")
        tipooutros = ExecTipoBuildGit(branch,produto.get__tempdir(),produto.get__dirgit(),produto.reposgit)
        tipooutros.exec_build_outros(versao,prox_versao)


