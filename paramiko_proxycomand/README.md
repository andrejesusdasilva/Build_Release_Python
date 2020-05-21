# Usando Paramiko como proxy para acesso a ambientes que passam por um gateway

Exemplo da arquitetura:

MAQUINALOCAL ----------->    BASTIONSERVER   ------------> GATEWAY  --------------> ORACLE/TOMCAT SERVER

# Arquivo ~/.ssh/config

```sh
Exemplo do arquivo ~/.ssh/config:

Host bastionserver
    Hostname x.x.xx.xx
    User bastion
    IdentityFile /home/andrej/bastion.pem
    Port 22

Host ambiente-andrej_gateway
    HostName x.x.xx.xx
    User andre.jesus
    IdentityFile /home/andrej/.ssh/id_rsa
    ProxyCommand ssh -q -W %h:%p bastionserver

Host ambiente-andrej_oracle
    HostName x.x.xx.xx
    User andre.jesus
    IdentityFile /home/andrej/.ssh/id_rsa
    ProxyCommand ssh -q -W %h:%p ambiente-andrej_gateway
```

# Executando o script

``` python
python main.py
```

Dentro da classe, tem o parametro do ambiente a ser acessado e executado alguns comandos, exemplo: 

``` python
#comandos que serão executados nos ambientes e ser direcionados nos arquivos de logs
listComandosSOOracle = []
listComandosSOOracle.append("echo \"Total de memória: \" && free -h")

client1 = AcessClientProxy("ambiente-andrej_gateway")
client1.exec_list_commands(listComandosSOTomcat)
```

# Referências

* https://www.cyberciti.biz/faq/linux-unix-ssh-proxycommand-passing-through-one-host-gateway-server/
* https://github.com/paramiko/paramiko