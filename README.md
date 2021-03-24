# Florence

É um script de automação feito em Python. Ele acessa a página do meu modem de internet e coleta dados sobre o sinal. Os dados são formatados em dicionários e depois convertidos em um JSON, que é retornado como a saída do programa.

----

## Solução

Desenvolvi este script por que gostaria de monitorar os sinais TX e RX da minha conexão, disponíveis no painel de gerenciamento do meu modem. Utilizando o `selenium` , o programa acessa a página do modem e coleta estes dados que estão contidos em uma tabela HTML. Em tempo de execução, os dados são armazenados em dicionários que posteriormente serão convertidos em um JSON e retornados para a saída do programa. 

O programa é executado por um shell script agendado na `crontab`. Este shell, executa o programa e salva seu output em uma variável de ambiente que posteriormente é enviada para o Zabbix através do deamon `zabbix_sender`.

---

## Contato
- Email: rafasc0404@gmail.com
- Linkedin: https://www.linkedin.com/in/r-camargo/