from ssh_proxy import *
from read_csv_file import *

if __name__ == '__main__':

    #### Comandos S.O: Oracle
    listComandosSOOracle = []
    listComandosSOOracle.append("echo \"Total de memória: \" && free -h")
    listComandosSOOracle.append("echo \"Quantidade de Discos: \" && df -h ")
    listComandosSOOracle.append("echo \"Versão S.O: \" && more /etc/os-release")
    listComandosSOOracle.append("echo \"Tipo da Instancia\" && curl http://169.254.169.254/latest/meta-data/instance-type | xargs")

    #### Comandos S.O: Tomcat
    listComandosSOTomcat = []
    listComandosSOTomcat.append("echo \"Total de memória: \" && free -h")
    listComandosSOTomcat.append("echo \"Quantidade de Discos: \" && df -h ")
    listComandosSOTomcat.append("echo \"Versão S.O: \" && more /etc/os-release")
    listComandosSOTomcat.append("echo \"Tipo da Instancia\" && curl http://169.254.169.254/latest/meta-data/instance-type | xargs")
    listComandosSOTomcat.append("echo \"Versão do Java:\" && export JAVA_VERSION=$(ps -ef | grep java | awk {'print $8'} | grep -v \"grep\") && echo $JAVA_VERSION | cut -f2 -d= | awk {'print $1'} | cut -d'/' -f 4")
    listComandosSOTomcat.append("echo \"Versão do Tomcat:\" && export APACHE_CONFIG=$(ps -ef | grep java | awk {'print $9'}) && echo $APACHE_CONFIG | cut -f2 -d= | awk {'print $1'} | cut -d'/' -f 4")
    listComandosSOTomcat.append("export XMX=$(ps -ef | grep java | awk {'print $12'}) && echo \"Parametro Java -Xmx: $XMX\"")
    listComandosSOTomcat.append("echo \"Pamametros do Servidor (conf/server.xml):\" && sudo su - andrej -c \'export APACHE_CONFIG1=$(ps -ef | grep java | awk {\"print $9\"}) && export SERVERXML=$(echo $APACHE_CONFIG1 | cut -f2 -d= | awk {\"print $1\"} | cut -d\/ -f 1,2,3,4) && cat $SERVERXML\/conf\/server.xml | grep \"connectionTimeout\"\'")
    listComandosSOTomcat.append("echo \"Pamametros do Servidor (conf/server.xml):\" && sudo su - andrej -c \'export APACHE_CONFIG1=$(ps -ef | grep java | awk {\"print $9\"}) && export SERVERXML=$(echo $APACHE_CONFIG1 | cut -f2 -d= | awk {\"print $1\"} | cut -d\/ -f 1,2,3,4) && cat $SERVERXML\/conf\/server.xml | grep \"redirectPort\"\'")
    listComandosSOTomcat.append("echo \"Pamametros do Servidor (conf/server.xml):\" && sudo su - andrej -c \'export APACHE_CONFIG1=$(ps -ef | grep java | awk {\"print $9\"}) && export SERVERXML=$(echo $APACHE_CONFIG1 | cut -f2 -d= | awk {\"print $1\"} | cut -d\/ -f 1,2,3,4) && cat $SERVERXML\/conf\/server.xml | grep \"proxyName\"\'")
    listComandosSOTomcat.append("echo \"Pamametros do Servidor (conf/server.xml):\" && sudo su - andrej -c \'export APACHE_CONFIG1=$(ps -ef | grep java | awk {\"print $9\"}) && export SERVERXML=$(echo $APACHE_CONFIG1 | cut -f2 -d= | awk {\"print $1\"} | cut -d\/ -f 1,2,3,4) && cat $SERVERXML\/conf\/server.xml | grep \"port\"\'")
    listComandosSOTomcat.append("sudo su - andrej -c \'export MCONFIG=$(ps -ef | grep java | awk -F \"-Dandrej.configFolder=\" \"{print substr(\$2,0,24)}\" | grep \"andrej-config\" | sed -e 's/[[:blank:]]*$//') && echo \"Lista de aplicações no diretório andrej-config: $apps\"\'")
    listComandosSOTomcat.append("sudo su - andrej -c \'export MCONFIG=$(ps -ef | grep java | awk -F \"-Dandrej.configFolder=\" \"{print substr(\$2,0,24)}\" | grep \"andrej-config\" | sed -e 's/[[:blank:]]*$//') && for apps in `ls $MCONFIG`; do if [ -d \"$MCONFIG/$apps\" ] && [ -e \"$MCONFIG/$apps/application.properties\" ];then echo \"Application.properties sistema $MCONFIG/$apps\" && tail \"$MCONFIG/$apps/application.properties\";fi;done\'")
    listComandosSOTomcat.append("sudo su - andrej -c \'export MCONFIG=$(ps -ef | grep java | awk -F \"-Dandrej.configFolder=\" \"{print substr(\$2,0,24)}\" | grep \"andrej-config\" | sed -e 's/[[:blank:]]*$//') && for apps in `ls $MCONFIG`; do if [ -d \"$MCONFIG/$apps\" ] && [ -e \"$MCONFIG/$apps/application.properties\" ];then echo \"Database.properties sistema $MCONFIG/$apps\" && tail \"$MCONFIG/$apps/database.properties\";fi;done\'")
    
    listComandosSOTomcat.append("sudo su - andrej -c \'export MCONFIG=$(ps -ef | grep java | awk -F \"-Dandrej.configFolder=\" \"{print substr(\$2,0,24)}\" | grep \"andrej-config\" | sed -e 's/[[:blank:]]*$//') && for apps in `ls $MCONFIG`; do if [ -d \"$MCONFIG/sca\" ] && [ -e \"$MCONFIG/sca/db.properties\" ];then echo \"Application.properties sistema $MCONFIG/$apps\" && tail \"$MCONFIG/sca/db.properties\";fi;done\'")

    #### Comandos Base de dados
    listComandosOracle = []
    #### Comandos Base de dados: Parametros bases
    listComandosOracle.append("echo \"Parametro oracle _optim_peek_user_binds:\" && sudo su - oracle -c \"echo 'show parameter _optim_peek_user_binds;' | sqlplus / as sysdba\"")
    listComandosOracle.append("echo \"Parametro oracle parameter _pga_max_size:\" && sudo su - oracle -c \"echo 'show parameter _pga_max_size;' | sqlplus / as sysdba\"")
    listComandosOracle.append("echo \"Parametro oracle _realfree_heap_pagesize_hint:\" && sudo su - oracle -c \"echo 'show parameter _realfree_heap_pagesize_hint;' | sqlplus / as sysdba\"")
    listComandosOracle.append("echo \"Parametro oracle  _use_realfree_heap:\" && sudo su - oracle -c \"echo 'show parameter _use_realfree_heap;' | sqlplus / as sysdba\"")
    listComandosOracle.append("echo \"Parametro oracle _aq_tm_processes:\" && sudo su - oracle -c \"echo 'show parameter aq_tm_processes;' | sqlplus / as sysdba\"")
    listComandosOracle.append("echo \"Parametro oracle _optimizer_index_caching:\" && sudo su - oracle -c \"echo 'show parameter optimizer_index_caching;' | sqlplus / as sysdba\"")
    listComandosOracle.append("echo \"Parametro oracle _optimizer_index_cost_adj:\" && sudo su - oracle -c \"echo 'show parameter optimizer_index_cost_adj;' | sqlplus / as sysdba\"")
    listComandosOracle.append("echo \"Parametro oracle _optimizer_mode:\" && sudo su - oracle -c \"echo 'show parameter optimizer_mode;' | sqlplus / as sysdba\"")
    listComandosOracle.append("echo \"Parametro oracle _pga_aggregate_target:\" && sudo su - oracle -c \"echo 'show parameter pga_aggregate_target;' | sqlplus / as sysdba\"")
    listComandosOracle.append("echo \"Parametro oracle _processes:\" && sudo su - oracle -c \"echo 'show parameter processes;' | sqlplus / as sysdba\"")
    listComandosOracle.append("echo \"Parametro oracle _sga_max_size:\" && sudo su - oracle -c \"echo 'show parameter sga_max_size;' | sqlplus / as sysdba\"")
    listComandosOracle.append("echo \"Parametro oracle _sga_target:\" && sudo su - oracle -c \"echo 'show parameter sga_target;' | sqlplus / as sysdba\"")
    listComandosOracle.append("echo \"Parametro oracle _streams_pool_size:\" && sudo su - oracle -c \"echo 'show parameter streams_pool_size;' | sqlplus / as sysdba\"")

    #### Comandos Base de dados: Versão do Oracle
    listComandosOracle.append("echo \"Versão do Oracle:\" && sudo su - oracle -c \"echo 'BEGIN DBMS_OUTPUT.PUT_LINE(DBMS_DB_VERSION.VERSION || '.' || DBMS_DB_VERSION.RELEASE); END;' | sqlplus / as sysdba\"")

    listaClientesError = []
    file = CsvFile("saas.csv")
    file.create_config_file_local(file.opencsvfile(), "config.txt")

    ambiente_tomcat = AcessClientProxy("aaaa-prd")
    ambiente_tomcat.exec_list_commands(listComandosSOTomcat)

    for clientes in file.opencsvfile().items():
        #tem que passar o mesmo nome da chave do arquivo ./.ssh/config
        #precisa separar por ambientes: oracle ou tomcat
        oracle = clientes[0] + "_oracle"
        tomcat = clientes[0] + "_tomcat"
        print("Cliente: %s" % clientes[0])
        try:
            ambiente_oracle = AcessClientProxy(oracle)
            ambiente_oracle.exec_list_commands(listComandosSOOracle)
            ambiente_oracle.exec_list_commands(listComandosOracle)
            ambiente_tomcat = AcessClientProxy(tomcat)
            ambiente_tomcat.exec_list_commands(listComandosSOTomcat)
        except paramiko.ssh_exception.SSHException as Ex:
            print("Erro na conexão com o cliente: %s" % clientes[0])
            print("Erro: %s" % Ex)
            listaClientesError.append(clientes[0])
    print("Lista de Clientes com problemas de conexão: %s" % listaClientesError)

