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

Host Brinks-devm
    HostName x.x.xx.xx
    User andre.jesus
    IdentityFile /home/andrej/.ssh/id_rsa
    ProxyCommand ssh -q -W %h:%p bastionserver
```

# Executando o script

``` python
python paramiko_ssh.py
```

Dentro da classe, tem o parametro do ambiente a ser acessado e executado alguns comandos, exemplo: 

``` python
client1 = AcessClientProxy("herabank-hml_gateway")
```

# Referências

* https://www.cyberciti.biz/faq/linux-unix-ssh-proxycommand-passing-through-one-host-gateway-server/

* https://github.com/paramiko/paramiko 