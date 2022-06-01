#! python

#python_scrappery - Encontra todos os numeros de telefone e emails em uma pagina web ou documento .


import pyperclip, re


phoneregex = re.compile(r'''(

    (\(\d\d\)|\d\d)?     # código de área

    (\s)?   # espaço

    (\d{4,5})   # primeiros 4 ou 5 digitos 

    (\s|-|)?   # separador esáço traço

    (\d{4})   #ultimos 4 digitos

    )''', re.VERBOSE)

# TO DO: CRIANDO O EMAIL REGEX.


emailregex = re.compile (r'''(

[a-zA-Z0-9._%+-]+    #username pode ter letras e numeros, maiusculas e minusculas

@   # @ simbolo

[a-zA-Z0-9._%+-]+    # dominio pode ter letras maiusculas e minusculas

(\.[a-zA-Z]{2,4})   # . alguma coisa (.com . edu)

)''', re.VERBOSE)

# TO DO: PROCURANDO OS MATCHS.

#Usando o metodo pyperclip pegamos todo o texto que foi copiado da pagina ou documento
text = str(pyperclip.paste())

matches = []

for groups in phoneregex.findall(text):
    #Group 1: codigo de area 3,5 Primeiros e ultimos digitos
    phoneNum = ' '.join([groups[1], groups[3], groups[5]]) # juntando os grupos para mostrar o numero completo
    matches.append(phoneNum) #Adicionando na lista

for groups in emailregex.findall(text):
    matches.append(groups[0])

# TO DO: Mostrando todos os calores encontrados ao usuario

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print ('Copied matches to clipboard:')
    print('\n'.join(matches))
else:
    print ('No phone numbers and email addresses found.')

#EXEMPLO https://www.ibiunainvest.com.br/

#APOS ENTRAR NO SITE PRESSIONE CNTRL A DEPOIS CNTRL C E RODE O PROGRAMA, ELE VAI RETORNAR OS CONTATOS DE TELEFONE E EMAIL DO IBIUNA