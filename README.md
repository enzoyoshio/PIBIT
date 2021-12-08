# PIBIT

Atualmente o script busca os standings em um contest de um grupo e transforma os dados dos standings em um arquivo csv.

## Comando para instalar as bibliotecas necessárias para o projeto

Caso o programa esteja quebrando por falta de alguma biblioteca, digite no terminal:

**pip install -r requirements.txt**

## Como pegar as chaves privadas (Key e secret)

Entre em sua conta no codeforces, no lado direito clique em "settings":

![Alt text](/images/alt.png)

Após isso, clique em "API":

![Alt text](/images/second.png)

Então clique em "Add API Key":

![Alt text](/images/third.png)

Ele pedirá que você dê um nome para a chave e insira sua senha, logo ele te dará as duas chaves necessárias para usar esse script.

## Como usar

Use a linha de comando:

**python3 standings.py**

Informe as chaves privadas e o Id do contest desejado e ele irá colocar as informações no arquivo parsed.csv
