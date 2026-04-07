# categoria-de-atletas.py
## Classificador de Categoria de Atletas

Este script em Python automatiza a classificação de atletas em categorias esportivas com base no ano de nascimento, utilizando cálculo de idade dinâmico.

## Funcionalidades
- **Cálculo de Idade Real:** Utiliza a biblioteca `datetime` para obter o ano atual do sistema.
- **Lógica de Categorização:** - **Mirim:** Até 7 anos.
  - **Júnior:** Menor de 18 anos.
  - **Sênior:** 18 anos ou mais.

## Conceitos Aplicados
* **Importação de Módulos:** Uso de `from datetime import date`.
* **Casting:** Conversão de entrada para `int`.
* **Estruturas Condicionais Encadeadas:** Uso estratégico de `if`, `elif` e `else`.
* **F-Strings:** Saída de dados dinâmica e personalizada.

##  Exemplo de Uso
```text
Ano de nascimento: 2015
O atleta tem 11 anos.
O atleta é considerado júnior.
