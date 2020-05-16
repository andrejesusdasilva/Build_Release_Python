import os
import sys
import paramiko

"""
baseado no arquivo de configuração utilizado para fazer a conexão usando o vscode

Exemplo do arquivo ~/.ssh/config:

Host bastionserver
    Hostname x.x.xx.xx
    User bastion
    IdentityFile /home/andrej/bastion.pem
    Port 22    

Host Brinks-devm
    HostName x.x.xx.xx
    User andre.jesus
    IdentityFile /home/andrej/.ssh/id_rsa
    ProxyCommand ssh -q -W %h:%p bastionserver
"""

# TODO adicionar validação do arquivo config
# TODO por algum motivo precisa mapear a porta 22 (precisa testar)

class AcessClientProxy:
    def __init__(self,hostname):
        self.hostname = hostname
        self.client = paramiko.SSHClient()
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        conf = paramiko.SSHConfig()
        conf.parse(open(os.path.expanduser('~/.ssh/config')))
        host = conf.lookup(self.hostname)

        self.client.connect(
            host['hostname'],
            username=host['user'],
            key_filename=host['identityfile'],
            banner_timeout=200,
            sock=paramiko.ProxyCommand(host.get('proxycommand'))
        )

    def exec_comando(self,command):
        #percorre a lista de comandos
        for comands in command:
            (stdin, stdout, stderr) = self.client.exec_command(comands)
            #não sei por que não printa a saida direto então precisa verificar as saidas
            if stderr.channel.recv_exit_status() != 0:
                print(stderr.read())
            else:
                for filelist in stdout.readlines():
                    print(filelist.strip('\n'))

if __name__ == '__main__':

    list = []
    list.append("pwd")
    list.append("free -h")
    list.append("df -h")

    #tem que passar o mesmo nome da chave do arquivo ./.ssh/config
    client1 = AcessClientProxy("herabank-hml_gateway")
    #client1.exec_comando(list)
    #client1.client.close()