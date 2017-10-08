from os import system
from os import path
from os import chdir


class GitComando:

    """Método para adicionar os artefatos no Git"""
    def gitadd(self):
        system("git add --all")

    """Comando de reset"""
    def gitreset(self):
        system("git reset --hard")

    """Checkout a branch"""
    """Tipos de nomes de branch:release/nome, develop e feature/nome"""
    def git_checkout(self, nomebranch_or_tag):
        system("git checkout %s" % nomebranch_or_tag)

    """Cria um branch novo a partir da versão local"""
    def git_create_branch(self, nomebranch):
        system("git checkout -b  %s" % nomebranch)

    """Commit das alterações"""
    def git_commit(self, msg):
        system("git commit -m \"%s\"" % msg)

    """Realiza o merge ours no branches"""
    def gitmergeours(self,nomebranch):
        system("git merge --no-ff %s" % nomebranch)

    """Push das alterações para o branch"""
    def gitpush(self, nomebranch_or_tag):
        system("git push origin %s" % nomebranch_or_tag)

    """Passa a tag no repositório"""
    def gitpush(self, nomebranch_or_tag):
        system("git push origin %s" % nomebranch_or_tag)

    """Valida se o diretório do projeto existe (se já foi clonado, caso contrário, realiza o clone do mesmo)"""
    def gitclone(diretoriotemp,nomediretorioprojeto,urlprojeto):

            if path.isdir(diretoriotemp):
                if path.exists(nomediretorioprojeto):
                    print("Não é necessário realizar o clone do projeto")
                    chdir(path.join(diretoriotemp,nomediretorioprojeto))
                else:
                    print("Realizando o clone do projeto")
                    chdir(diretoriotemp)
                    system("git clone %s" % urlprojeto)
            else:
                print("Ocorreu algum problema para acessar o diretório %s" % diretoriotemp)
                #essa verificação é somente para garantir que nada vai acontecer até esse ponto
                #pois essa verificação vai estar em outra parte do inicio do processo


    """Merge utilizado na build do branch de develop"""
    def gitmerge_release_into_develop(self, nomebranch_or_tag):
        system("git merge --no-ff -s ours -m \"Merging %s into develop using ours strategy\" %s" % (nomebranch_or_tag,nomebranch_or_tag))


#todo
#Trocar o system por http://www.bogotobogo.com/python/python_subprocess_module.php