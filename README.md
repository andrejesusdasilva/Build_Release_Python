# Build_Release_Python
Um modelo de script em python responsável por realizar o processo de release de sistemas que estão no Stash.

#Processo

No arquivo passo a passo, esta disponível os passos realizados por tipo de Build, são elas: builds em branche de release, branche develop ou branches de features.

#Configuração

É necessário editar o arquivo produtos_core.xml, com as informações pertinentes ao repositório, diretório temporário etc ...

O caminho para o arquivo .xml esta hardcoded (precisa melhorar), então é necessário editar o arquivo "LeituraXml.py" na variável "__arquivoxml" com o caminho do mesmo.

O clone do repositório será realizado no diretório configurado na tag "temp_dir" do .xml.


#Pré-requisito

Ter o cliente do git instalado na máquina e acesso ao repositório.


#Modo de usar


Acesse o diretório do script e execute o seguinte: 


```sh

nomeapp 3.04.26 develop 3.04.27

```


O tipo release aceita somente 3 parametros.


```sh

nomeapp 5.07.05 release 

```


```sh

nomeapp 5.07.05 feature/branche_feature 5.07.06

```