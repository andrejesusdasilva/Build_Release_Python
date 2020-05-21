import csv

class CsvFile:
    def __init__(self,cvsfile):
        self.csvfile = cvsfile

    def opencsvfile(self):
        hashClientes = {}
        line_count = 0
        #TODO adicionar validações para o arquivo
        with open(self.csvfile,mode='r') as file:
            linescsv = csv.reader(file, delimiter=',')

            for row in linescsv:
                if line_count == 0:
                    line_count += 1
                else:
                    #print(f'Linhas processadas {line_count}.')
                    hashClientes[row[0]] = {'gateway': row[1],
                                           'oracle': row[2],
                                           'tomcat': row[3]}
                    line_count += 1

            return hashClientes

    def create_config_file_local(self,hashclientes,newfile):
        """ As informações do bastion acredito que não vá mudar"""
        #TODO parametrizar outras informações

        line_count = 0
        templatebastion = """
                Host bastionserver
                Hostname x.xx.xx.xx
                User bastion
                IdentityFile /home/andrej/bastion.pem
                StrictHostKeyChecking no
                UserKnownHostsFile=/dev/null
                Port 22
                        """
        # adiciona somente o template do bastion no inicio do arquivo
        with open(newfile, mode='a') as configfile:
            configfile.write(templatebastion)

        for row in hashclientes.items():
            ambientestemplate = '''
                Host {ambiente}
                HostName {gateway_ip}
                User andre.jesus
                IdentityFile ~/.ssh/id_rsa
                ProxyCommand ssh -q -W %h:%p bastionserver
                StrictHostKeyChecking no
                UserKnownHostsFile=/dev/null
                Port 22
    
                Host {ambiente}_oracle
                HostName {oracle}
                User andre.jesus
                IdentityFile ~/.ssh/id_rsa
                ProxyCommand ssh -q -W %h:%p {ambiente}
                StrictHostKeyChecking no
                UserKnownHostsFile=/dev/null
                Port 22
    
                Host {ambiente}_tomcat
                HostName {tomcat}
                User andre.jesus
                IdentityFile ~/.ssh/id_rsa
                ProxyCommand ssh -q -W %h:%p {ambiente}
                Port 22
                StrictHostKeyChecking no
                UserKnownHostsFile=/dev/null
                    '''.format(ambiente=row[0], gateway_ip=row[1]['gateway'], oracle=row[1]['oracle'], tomcat=row[1]['tomcat'])

            with open(newfile, mode='a') as configfile:
                configfile.write(ambientestemplate)
            line_count += 1






