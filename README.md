# README.md

## Introdução

Este projeto consiste em uma pipeline de processamento de dados utilizando Apache Beam para consumir mensagens de um tópico Kafka contendo transações financeiras simuladas e inseri-las em um banco de dados PostgreSQL. O código está dividido em dois componentes principais: o produtor de mensagens em Python e o consumidor Apache Beam.

## Pré-requisitos

Antes de executar a pipeline, certifique-se de ter os seguintes componentes instalados:

- Python 3.x
- Apache Beam
- Confluent Kafka
- PostgreSQL

Instale as bibliotecas Python necessárias executando o seguinte comando:

```bash
pip install -r requirements.txt
```

## Configuração

### Configuração do Kafka

Certifique-se de ter um servidor Kafka em execução. No código do produtor, o tópico é definido como 'financial_transactions', e o endereço do servidor Kafka é 'localhost:9092'. Certifique-se de ajustar essas configurações conforme necessário.

### Configuração do PostgreSQL

Antes de executar a pipeline, configure um banco de dados PostgreSQL e ajuste as configurações de conexão no código do consumidor. As configurações padrão são as seguintes:

- Host: localhost
- Porta: 5432
- Banco de dados: postgres
- Usuário: postgres
- Senha: postgres

Altere essas configurações no código do consumidor de acordo com a sua configuração do PostgreSQL.

## Execução

1. Execute o produtor de mensagens:

```bash
python producer.py
```

Este script Python produzirá mensagens simuladas contendo transações financeiras e as enviará para o tópico Kafka.

2. Execute a pipeline do Apache Beam:

```bash
python consumer.py
```

Este script Python consumirá as mensagens do tópico Kafka, transformará os dados e os inserirá em um banco de dados PostgreSQL.

Certifique-se de que todas as dependências estão corretamente instaladas e as configurações estão ajustadas antes de executar os scripts.

## Contribuições

Contribuições são bem-vindas! Se encontrar algum problema ou tiver sugestões de melhoria, por favor, abra uma issue neste repositório.
