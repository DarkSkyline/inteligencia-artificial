from queue import Queue, PriorityQueue


def ucs_weight(from_node, to_node, weights):
    '''
        Devolve o peso entre os dois nós adjacentes
        :param from_node: o no de partida
        :param to_node: O nó de chegada
        :param weights: Dicionário completo de pesos entre dois nós
        return devolve o peso do nó from para to

    '''
    return weights.get((from_node, to_node)) if weights else 1


def ucs(graph, start, end, weights1, weights2):
    '''
        Função que premite determinar as iterações da procura sofrega
        :param graph: grafo com as adjacências
        :param start: no de começo
        :param end: nó de chegada
        :param weights: Dicionário completo de pesos entre dois nós     
    '''
    frontier = PriorityQueue()
    frontier.put((0, start))  # retira o primeiro elemento da priority queue e o seu custo
    print('iteração 0')
    print(start)
    pos=1
    controlo = False
    while True:
        if frontier.empty():
            raise Exception("No way Exception")
        ucs_w, current_node = frontier.get()
        if controlo:
            ucs_w = ucs_w - ucs_weight(current_node,'Faro',weights2)

        if current_node == end:
            print('#'*100)
            print('Nó escolhido '+end)
            print('chegámos ao fim')
            return

        print('-' * 100)
        print('iteração ' + str(pos))
        for node in graph[current_node]:
            frontier.put((
                ucs_w + ucs_weight(current_node, node, weights1)+ucs_weight(node, 'Faro', weights2),node))
        print(sorted(frontier.queue))
        if frontier.queue[0][1] is not end:
            print('Nó escolhido para abrir '+str(frontier.queue[0][1])+'.') 
        pos = pos + 1
        controlo=True

tabela_2 = {
    ('Faro', 'Aveiro'): 366,
    ('Faro', 'Braga'): 454,
    ('Faro', 'Braganca'): 487,
    ('Faro', 'Beja'): 99,
    ('Faro', 'Castelo Branco'): 280,
    ('Faro', 'Coimbra'): 319,
    ('Faro', 'Evora'): 157,
    ('Faro', 'Faro'): 0,
    ('Faro', 'Guarda'): 352,
    ('Faro', 'Leiria'): 278,
    ('Faro', 'Lisboa'): 195,
    ('Faro', 'Portalegre'): 228,
    ('Faro', 'Porto'): 418,
    ('Faro', 'Santarem'): 231,
    ('Faro', 'Setubal'): 168,
    ('Faro', 'Viana'): 473,
    ('Faro', 'Vila Real'): 429,
    ('Faro', 'Viseu'): 363,
    ('Aveiro', 'Faro'): 366,
    ('Braga', 'Faro'): 454,
    ('Braganca', 'Faro'): 487,
    ('Beja', 'Faro'): 99,
    ('Castelo Branco', 'Faro'): 280,
    ('Coimbra', 'Faro'): 319,
    ('Evora', 'Faro'): 157,
    ('Faro', 'Faro'): 0,
    ('Guarda', 'Faro'): 352,
    ('Leiria', 'Faro'): 278,
    ('Lisboa', 'Faro'): 195,
    ('Portalegre', 'Faro'): 228,
    ('Porto', 'Faro'): 418,
    ('Santarem', 'Faro'): 231,
    ('Setubal', 'Faro'): 168,
    ('Viana do Castelo', 'Faro'): 473,
    ('Vila Real', 'Faro'): 429,
    ('Viseu', 'Faro'): 363,
}

tabela1 = {
    ('Aveiro', 'Porto'): 68,
    ('Aveiro', 'Viseu'): 95,
    ('Aveiro', 'Coimbra'): 68,
    ('Aveiro', 'Leiria'): 115,

    ('Braga', 'Viana do Castelo'): 48,
    ('Braga', 'Vila Real'): 106,
    ('Braga', 'Porto'): 53,

    ('Braganca', 'Vila Real'): 137,
    ('Braganca', 'Guarda'): 202,

    ('Beja', 'Evora'): 78,
    ('Beja', 'Faro'): 152,
    ('Beja', 'Setubal'): 142,

    ('Castelo Branco', 'Coimbra'): 159,
    ('Castelo Branco', 'Guarda'): 106,
    ('Castelo Branco', 'Portalegre'): 80,
    ('Castelo Branco', 'Evora'): 203,

    ('Coimbra', 'Viseu'): 96,
    ('Coimbra', 'Leiria'): 67,
    ('Coimbra', 'Aveiro'): 68,
    ('Coimbra', 'Castelo Branco'): 159,

    ('Evora','Lisboa'): 150,
    ('Evora','Santarem'): 117,
    ('Evora','Portalegre'): 131,
    ('Evora','Setubal'): 103,
    ('Evora','Beja'): 78,
    ('Evora','Castelo Branco'): 203,

    ('Faro', 'Setubal'): 249,
    ('Faro', 'Lisboa'): 299,
    ('Faro', 'Beja'): 152,

    ('Guarda', 'Vila Real'): 157,
    ('Guarda', 'Viseu'): 85,
    ('Guarda', 'Braganca'): 202,
    ('Guarda', 'Castelo Branco'): 106,

    ('Leiria', 'Lisboa'): 129,
    ('Leiria', 'Santarem'): 70,
    ('Leiria', 'Aveiro'): 115,
    ('Leiria', 'Coimbra'): 67,

    ('Lisboa', 'Santarem'): 78,
    ('Lisboa', 'Setubal'): 50,
    ('Lisboa', 'Evora'): 150,
    ('Lisboa', 'Faro'): 299,
    ('Lisboa', 'Leiria'): 129,

    ('Porto', 'Viana do Castelo'): 71,
    ('Porto', 'Vila Real'): 116,
    ('Porto', 'Viseu'): 133,
    ('Porto', 'Aveiro'): 68,
    ('Porto', 'Braga'): 53,

    ('Vila Real', 'Viseu'): 110,
    ('Vila Real', 'Braga'): 106,
    ('Vila Real', 'Braganca'): 137,
    ('Vila Real', 'Guarda'): 157,
    ('Vila Real', 'Porto'): 116,

    ('Viseu', 'Aveiro'): 95,
    ('Viseu', 'Coimbra'): 96,
    ('Viseu', 'Guarda'): 85,
    ('Viseu', 'Porto'): 133,
    ('Viseu', 'Vila Real'): 110,
    
    ('Setubal', 'Beja'): 142,
    ('Setubal', 'Evora'): 103,
    ('Setubal', 'Faro'): 249,
    ('Setubal', 'Lisboa'): 50,

    ('Santarem', 'Evora'): 117,
    ('Santarem', 'Leiria'): 70,
    ('Santarem', 'Lisboa'): 78,

    ('Viana do Castelo', 'Braga'): 48,
    ('Viana do Castelo', 'Porto'): 71,
    
    ('Portalegre', 'Castelo Branco'): 80,
    ('Portalegre', 'Evora'): 131,
}

graphCities = {
    'Aveiro': set(['Porto', 'Viseu', 'Coimbra', 'Leiria']),
    'Braga': set(['Viana do Castelo', 'Vila Real', 'Porto']),
    'Braganca': set(['Vila Real', 'Guarda']),
    'Beja': set(['Evora', 'Faro', 'Setubal']),
    'Castelo Branco': set(['Coimbra', 'Guarda', 'Portalegre', 'Evora']),
    'Coimbra': set(['Viseu', 'Leiria', 'Aveiro', 'Castelo Branco']),
    'Evora': set(['Lisboa', 'Santarem', 'Portalegre', 'Setubal', 'Beja', 'Castelo Branco']),
    'Faro': set(['Setubal', 'Lisboa', 'Beja']),
    'Guarda': set(['Vila Real', 'Viseu', 'Braganca', 'Castelo Branco']),
    'Leiria': set(['Lisboa', 'Santarem', 'Aveiro', 'Coimbra']),
    'Lisboa': set(['Santarem', 'Setubal', 'Evora', 'Faro', 'Leiria']),
    'Porto': set(['Viana do Castelo', 'Vila Real', 'Viseu', 'Aveiro', 'Braga']),
    'Vila Real': set(['Viseu', 'Braga', 'Braganca', 'Guarda', 'Porto']),
    'Viseu': set(['Aveiro', 'Guarda', 'Porto', 'Vila Real', 'Coimbra']),
    'Setubal': set(['Beja', 'Evora', 'Faro', 'Lisboa']),
    'Viana do Castelo': set(['Braga', 'Porto']),
    'Santarem': set(['Evora', 'Leiria', 'Lisboa']),
    'Portalegre': set(['Castelo Branco', 'Evora'])
}

ucs(graphCities, 'Coimbra', 'Faro', tabela1, tabela_2)
