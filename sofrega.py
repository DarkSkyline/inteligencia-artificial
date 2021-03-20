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


def ucs(graph, start, end, weights):
    '''
    	Função que premite determinar as iterações da procura sofrega
    	:param graph: grafo com as adjacências
    	:param start: no de começo
    	:param end: nó de chegada
    	:param weights: Dicionário completo de pesos entre dois nós   	
    '''
    frontier = PriorityQueue()
    frontier.put((ucs_weight(start, 'Faro', weights), start))  # põe no inicio da lista o nó de partida com custo 0
    print('iteração 0')
    print(start+', '+str(ucs_weight(start, 'Faro', weights)))
    pos = 1
    while True:
        ucs_w, current_node = frontier.get() # retira o primeiro elemento da priority queue e o seu custo
        if current_node == end:   	
        	print('#'*100)
        	print('Nó escolhido '+end)
        	print('chegámos ao fim')
        	return
        print('-' * 100)
        print('iteração ' + str(pos))
        #percorrer todos os nós que tem como adjacência o current_node
        for node in graph[current_node]:
            frontier.put((ucs_weight(node, 'Faro', weights), node))
            #Adiciona á iteração os adjacentes do current node e a sua distância a faro
        print(sorted(frontier.queue))              
        print('Nó escolhido '+str(frontier.queue[0][1])+' '+str(frontier.queue[0][0])+'.')
        pos = pos + 1



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

ucs(graphCities, 'Coimbra', 'Faro', tabela_2)
