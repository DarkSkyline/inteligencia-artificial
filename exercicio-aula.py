# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

5//2*3
22%8/4
22%(8/4)
34/8*3
44%4+3
(44*3+1)==44*3+1
3*5//2

'Carro'+'Casa'
3*'Euros'
'Euros'+3 //nao da
5+5.0
5.0*'Polónia' //nao da
'Euros'*3
'Santa'+3*'Ana'
'Ana'+3+'Santa' //nao da
'Terra'+'1'+'Mar'
1=='1' //false

4-Desenvolva um programa em python que peça ao utilizador o nome, o ano de nascimento, a rua e o código postal.
O programa deve saudar o utilizador e devolver a sua idade.
Deve também apresentar a morada completa(rua e código postal) bem como indicar o número de caracteres usados.

'Diz me o teu nome'
name=input();
'Olá, ' + name


/***********************************************/
name='Filipe'
password='root'
if name== 'Filipe':
    print('Hello Filipe')
    if password == 'root':
        print('Access granted')
    else:
        print('Wrong password')
        
/***********************************************/
name='Alice'
if name== 'Alice':
    print('Hi, Alice')
    
/***********************************************/
name='Alice'
age=5
if name== 'Alice':
    print('Hi, Alice')
else:
    if age < 12:
        print('You are not Alice, Kiddo')
        
/***********************************************/
verificar se o nome foi o inserido 


/**********************************************/
for i in range(5):
    print('Bom dia');

/********************************************/
for i in range(5):
    if (i==2):
        continue
    print('Bomdia', i);

/*******************************************/
for i in range(5):
    if (i==2):
        break
    print('Bomdia', i);
    
i=0
while(i<5):
    print('Bom dia!', i)
    i=i+1
    
/********************************************/
for i in range (0,10,2):
    print(i)
    
/*******************************************/
import webbrowser

while True:
    webbrowser.open('https://www.youtube.com/watch?v=88-Z4MVmSJE&t=19s') 

/******************************************/
True and not True
False or not False
(7<8)and(98>=98)
False or not (27+5<78-7)
not not not True
False or False or not True
False or (False or not True)
True or not False
not 77<3==27>2
True and True and True and True or not False

/******************************************/
for i in range (0,100,2):
    print(i)
 
i=0
while(i<100):
    print(i)
    i=i+1
    
/*********************************************/
def spam() :
    print(eggs)

eggs=42
spam()
print(eggs)

/*********************************************/
def spam():
    eggs = 'spam local'
    print(eggs)

def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)

eggs='global'
bacon()
print(eggs)

/******************************************************/
def spam():
    global eggs
    eggs = 'spam'
    
eggs= ' global'
spam()
print(eggs)

/********************************************************/
def spam ():
    global eggs
    eggs = 'spam'
    
def bacon():
    eggs = 'bacon'
def ham():
    print(eggs)
    
eggs= 42
spam()
print(eggs)

/************************************************************/
def spam():
    print(eggs)
    eggs ='spam local'

eggs ='global'
spam()

/**********************************************************/
def division(divideBy):
    try:
        return 10 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
        

print(division(10))
print(division(5))
print(division(0))

/**************************************************************/
def sequence():
    for x in range (1,11,1):
        print(x)

/*************************************************************/
def val(valmin, valmax):
    for i in range(valmin, valmax+1):
        print(i)

val(2,6)

/**************************************************************/
def val (val):
    if val>0:
        print(val)
    elif val<0:
        val=-1*val
        print(val)
    return(val)
    val(3)
/*************************************************************/
spam = ["cat", "bat", "rat", "elephant"]

spam[0]
/*************************************************************/
lista2 = ['macaco', 'elefante', 'baleia', 'puma']
    print(lista2[0])
    print(lista2[1])
    print(lista2[2])
    print(lista2[3])
    print(lista2[4])
    
print('O '+lista2[0]+'foge do' + lista2[1]) 

/************************************************************/
listaMultipla = [['sapo', 'rã', 'ovelha'], [1,2,3,4,5]]
print(listaMultipla)
print(listaMultipla[0])
print(listaMultipla[1])
print(listaMultipla[0][1])
print(listaMultipla[0][2])
print(listaMultipla[1][3])
print(listaMultipla[0][-1])
/*************************************************************/

listaAnimal = ['macaco', 'elefante', 'baleia', 'puma']
print(listaAnimal[1])
print(listaAnimal[0:3])
print(listaAnimal[0:4])
print(listaAnimal[1:3])
print(listaAnimal[0:-1])
print(listaAnimal[:4])
print(listaAnimal[2:])
print(listaAnimal[:])

/**************************************************************/
listaNova=['maria', 'manuela', 'marta', 'paula']
print(len(listaNova))

listaNova=[['maria', 'manuela', 'marta', 'paula'], [1,2]]
print(len(listaNova))
print(len(listaNova[0]))

/*************************************************************/
listaMultipla = ['sapo', 'rã', 'ovelha']
listaMultipla[1]='cavalo'
print(listaMultipla)

listaMultipla = ['sapo', 'rã', 'ovelha']
listaMultipla[-1]='sapo'
print(listaMultipla)

listaMultipla = ['sapo', 'rã', 'ovelha']
listaMultipla[1]=listaMultipla[2]
print(listaMultipla)

/************************************************************/
print(['Sara', 'Rita', 'Constança']+['Beatriz','Teresa','Sandra'])
print(['Sara', 'Rita', 'Constança']*3)

/***********************************************************/
listaPrimos = []
while True:
    name = input('Qual o nome do teu primo: ')
    
    if name=="sair":
        break
    listaPrimos=listaPrimos+[name]

print (listaPrimos)
/**********************************************************/
material = ['canetas','agrafadores','lápis','capas']

for i in range(len(material)):
    print('Index ' + str(i) + ' da lista de compras: ' + material[i])

/**********************************************************/
nomes = ['Maria', 'Manuela', 'Teresa', 'Ana']
nomes.append('Joana')
print (nomes)

nomes = ['Maria', 'Manuela', 'Teresa', 'Ana']
nomes.insert(1, 'Telma')
print (nomes)
    
nomes = ['Maria', 'Manuela', 'Teresa', 'Ana']
nomes.remove('Maria')
print (nomes)

/********************************************************/
numeros=[1,4,2,99,-12,12]
numeros.sort()
print(numeros)
numeros.sort(reverse=True)
print(numeros)

nomes=['Maria', 'Manuela', 'Teresa', 'Ana', 'Maria', '1', '2', '3']
nomes.sort()
nomes.sort(reverse=True)
print(nomes)

/*************************DICIONARIOS************************************/
meuGato={'nome':'Ben', 'cor':'cinza', 'idade':3, 'feitio':'melga'}
print(meuGato)
print(meuGato['nome'])
print('O meu gato chama-se '+meuGato['nome']+' e tem '+str(meuGato['idade'])+' anos.... Está velho!')

/****************************************************/
cc={'nome':'Filipe', 'idade':21}
cc['nif']=123456
print(cc)

cc['idade']=22

/***********DICIONARIOS VS LISTAS*****************************/
listaGatos1=['ben','mel','miss']
listaGatos2=['ben','mel','miss']
listaGatos3=['ben','miss','mel']
print(listaGatos1==listaGatos2)
print(listaGatos3==listaGatos2)

/*************************************************************/
meuGato={'nome':'Ben', 'cor':'cinza', 'idade':3, 'feitio':'melga'}
for gatoKeys in meuGato.keys():
    print(gatoKeys)
    
for gatoKeys in meuGato.values():
    print(gatoKeys) 
    
for gatoKeys in meuGato.items():
    print(gatoKeys)

for gato in meuGato:
    print(gato)

/***********************************************************/
dicCC={'nome':'Filipe', 'nascimento':'09-09-2000'}
print('nome' in dicCC.Keys())
/***********************************************************/

list = {}
sair = False
while(not sair):
    nome=input()
    if(nome=='sair'):
        sair=True
    elif(nome not in list.keys()):
        data=input()
        list[nome]=data
    else:
        print(nome, '-', list[nome])

/**************************************************************/
spam={'nome':'Filipe','age':44}
for k, v in spam.items():
    print('Key: ' + k + 'Value: ' + str(v))
/***************************************************************/
picnicItems={'ovos':20,'frangos':3,'tinto':3}
print('Vou levar '+str(picnicItems.get('ovos',0)) + ' ovos')
print('Vou levar '+str(picnicItems.get('viriatos',0)) + ' viriatos')
/***************************************************************/

dicCC={'nome':'Filipe', 'nascimento':'09-09-2000'}
if 'nif' not in dicCC.keys():
    dicCC['nif']=111222333
    print(dicCC)
    
/***************************************************************/
s = "o curso de python já vai a meio"
words = s.split()
letter_count_per_word = {w:len(w) for w in words}
print(len(letter_count_per_word))


