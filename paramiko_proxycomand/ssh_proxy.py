import os
import sys
import paramiko

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
            timeout=20,
            banner_timeout=100,
            sock=paramiko.ProxyCommand(host.get('proxycommand')))

    def exec_list_commands(self,command):
        #percorre a lista de comandos
        for comands in command:
            #get_pty=True padrao é false. Sem essa opção não era possivel trocar para o user oracle
            (stdin, stdout, stderr) = self.client.exec_command(comands,get_pty=True)
            print("Resultado comando: %s" % comands)
            #não sei por que não printa a saida direto então precisa verificar as saidas
            if stderr.channel.recv_exit_status() != 0:
                print("Erro ao executar os comandos no ambiente:  %s" % self.hostname)
                print(stderr.read())
            else:
                for filelist in stdout.readlines():
                    print(filelist.strip('\n'))
                    self.create_logfile(self.hostname + ".txt",filelist.strip('\n'))
            print('\n')

    def create_logfile(self,log,msg):
        with open(log, mode='a') as logfile:
            logfile.write(msg.strip('\n'))