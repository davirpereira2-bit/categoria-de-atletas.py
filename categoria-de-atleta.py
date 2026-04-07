from datetime import date
ano = date.today().year
nasc = int(input('Ano de nascimento:'))
idade = ano - nasc

if idade <= 7:
    print(f'O atleta tem, {idade} anos.')
    print('O atleta é considerado mirim')
elif idade < 18:
    print(f'O atleta tem, {idade} anos')
    print('O atleta é considerado júnior')
else :
    print(f"O atleta tem, {idade} anos ")
    print('o atleta é considerado Sênior')
