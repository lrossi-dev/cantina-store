# cantina-store
A sua cantina com café coado :coffee:

## Instalando dependências

É preciso que você tenha instalado em sua máquina:
* [python >= 3.6](https://python-guide-pt-br.readthedocs.io/pt_BR/latest/starting/install3/linux.html)
* [pip](https://pip.pypa.io/en/stable/installation/)


```
$ pip install -r requirements.txt
```

## Banco de dados

A aplicação assume que você tem uma instância do MySQL ouvindo a porta 3306. Além disso, alguns parâmetros que a app utiliza para se conectar são:

* User: `root`
* Senha: `root`
* DB: `Cantina`

A única tabela que é consultada pela applicação chama-se `Lanches`, e segue a estrutura abaixo:

Nome da coluna | Tipo | Constraints
--- | --- | ---
Id | INT | NOT NULL, PRIMARY KEY
Nome | VARCHAR(255) | NOT NULL
Valor | DECIMAL(4,2) |

## Executando a aplicação

Da raiz do projeto, execute:

```
$ python app/main.py
```

A aplicação deverá ser disponibilizada em: [http://localhost:8080](http://localhost:8080).

## Executando os testes

Você poderá testar a aplicação utilizando pytest ou, preferivelmente, o `tox`. 

```
$ pip install -U tox
$ tox
```

## Dúvidas e sujestões

Levante uma issue!
