import cidades
import os
from queue import Queue, PriorityQueue
clear = lambda: os.system('cls')
clear()


def __init__(self):
    print('entrei aqui')

#recuperar os dados da class
mapa = cidades.Cidades()

#recuperar os dados de cada grafo
cidadesLigadas = mapa.Ligadas()
cidadeReta = mapa.Reta()
cidadeRetaFaro  = mapa.DistanciaReta()
pesos = mapa.Pesos()

#função pesquisa em profundidade
def pesquisa_profundidade(grafo, inicio, fim):
    fronteira = []
    ant = []
    fronteira.append(inicio)
    visitados = []
    
    i = 1
    print('Nó inicial escolhido: '+ inicio)

    while True:
        print('Iteração - ', i)
        no_atual = fronteira.pop(0) #remove o primeiro da lista
        

        visitados.append(no_atual) #adiciona aos visitados
        print('Nó atual: ' + no_atual) # printa o no atual
        if(fronteira is not fronteira):
            ant.append(fronteira) #guarda todos aqueles que ainda nao foram explorados
        

        if no_atual == fim:
            print('*'*100)
            print('Chegamos a ' + fim)
            print('Locais Explorados: ')
            print(visitados)
            print('Total iterações: ', i)
            return
        else:
            print('Nó escolhido para abrir ' + no_atual)
        
        f = 0
        for no in grafo[no_atual]:
            if no not in visitados:
                fronteira.insert(f,no)
                f = f + 1
        
        print('-'*100)
        print('Na lista para visitar --> ', fronteira)  
        i = i+1
# fim pesquisa em profundidade


def retorna_peso(no_inicio, no_para, tamanho):
    return tamanho.get((no_inicio, no_para)) if tamanho else 1

#custo_uniforme
def custo_uniforme(graph, inicio, fim, peso):
    fronteira = PriorityQueue()
    fronteira.put((0,inicio))
    print('iteração 0')
    print(inicio)
    pos = 1
    while True:
        ucs_w, no_atual = fronteira.get()

        if no_atual == fim:
            print('-'*100)
            print('No escolhido ' + fim)
            print('Chegamos ao fim')
            return
        print('-'*100)
        print('Iteração '+str(pos))
        for no in graph[no_atual]:
            fronteira.put((ucs_w + retorna_peso(no_atual, no, peso), no))
        print(sorted(fronteira.queue))
        if fronteira.queue[0][1] is not fim:
            print('Para abrir ---> ' + str(fronteira.queue[0][1] + '.'))
        pos = pos+1



def procura_sofrega(graph, inicio, fim,reta):
    fronteira = PriorityQueue()
    fronteira.put((0,inicio))
    print('iteração 0')
    print(inicio)
    pos = 1
    valor = False
    while True:
        
        ucs_w, no_atual = fronteira.get()
        if valor:
            ucs_w = retorna_peso(no_atual, fim, reta)

        if no_atual == fim:
            print('-'*100)
            print('No escolhido ' + fim)
            print('Chegamos ao fim')
            return

        print('-'*100)
        print('Iteração '+str(pos))
        for no in graph[no_atual]:
            fronteira.put((retorna_peso(no, fim, reta), no))
        print(sorted(fronteira.queue))
        if fronteira.queue[0][1] is not fim:
            print('Para abrir ---> ' + str(fronteira.queue[0][1] + '.'))
        pos = pos+1
        valor = True


#junção do custo uniforme com pesquisa sofrega, gera uma lista dos possiveis proximos passos e com priority queue escolhe o mais proximo em distância e repete o processo até atingir o destino ou não houver mais caminhos
def a_star(graph, inicio, fim, peso, reta):
    fronteira = PriorityQueue()
    fronteira.put((0,inicio))
    print('iteração 0')
    print(inicio)
    pos = 1
    valor = False
    while True:
        
        ucs_w, no_atual = fronteira.get()
        if valor:
            ucs_w = ucs_w - retorna_peso(no_atual, fim, reta)

        if no_atual == fim:
            print('-'*100)
            print('No escolhido ' + fim)
            print('Chegamos ao fim')
            return

        print('-'*100)
        print('Iteração '+str(pos))
        for no in graph[no_atual]:
            fronteira.put((ucs_w + retorna_peso(no_atual, no, peso)+retorna_peso(no, fim, reta), no))
        print(sorted(fronteira.queue))
        if fronteira.queue[0][1] is not fim:
            print('Para abrir ---> ' + str(fronteira.queue[0][1] + '.'))
        pos = pos+1
        valor = True

      
#menu

def menu(nome):
    sair = True
    while sair:
        Inicio = None
        Fim = None
        
        print(20*'*' + ' Opções ' + '*'*20)
        print('Opção 1: Pesquisa em profundidade')
        print('Opcao 2: Procura Custo Uniforme')
        print('Opção 3: Procura sôfrega (Faro)')
        print('Opção 4: A* (FARO)')
        print('Opcao: exit')
        opcao = input(nome + ' escolha uma opção: ')
        
        if opcao == "1":
            clear()
            print('Algoritmo - Pesquisa em Profundidade Primeiro')
            Inicio = input('Escolha o local de inicio: ')
            Fim = input('Escolha o destino: ')
            print(cidadesLigadas)
            pesquisa_profundidade(cidadesLigadas, Inicio, Fim)
            
        elif opcao == "2":
            clear()
            print('Algoritmo - Custo uniforme ')
            Inicio = input('Escolha o local de inicio: ')
            Fim = input('Escolha o local de fim: ')
            custo_uniforme(cidadeReta,Inicio, Fim,pesos)
        elif opcao == "3":
            clear()
            print('Algoritmo - Procura Sofrega ')
            Inicio = input('Escolha o local de inicio: ')
            print('Destino predefenido [Faro] ')
            Fim = 'Faro'
            procura_sofrega(cidadeReta,Inicio, Fim,cidadeRetaFaro)
        elif opcao == "4":
            clear()
            print('Algoritmo - A* ')
            Inicio = input('Escolha o local de inicio: ')
            print('Destino predefenido [Faro] ')
            Fim = 'Faro'
            a_star(cidadesLigadas,Inicio, Fim, pesos,cidadeRetaFaro)
            
        elif opcao == "exit":
            clear()

            sair = False
        else:
            clear()
            print('Opcao errada escreva um numero de 1 a 4 ')
            print('Você escreveu: [' + opcao + ']')
        


nome = input('Diga-nos o seu nome: ')
print('Bem vindo '+  nome)
clear()
menu(nome)

print('Adeus e até uma proxima ' + nome)