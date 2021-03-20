class Node(object):
    """This class represents a node in a graph."""

    def __init__(self, label: str = None):
        """
        Initialize a new node.

        Args:
            label: the string identifier for the node
        """
        self.label = label
        self.children = []

    def __lt__(self, other):
        """
        Perform the less than operation (self < other).

        Args:
            other: the other Node to compare to
        """
        return (self.label < other.label)

    def __gt__(self, other):
        """
        Perform the greater than operation (self > other).

        Args:
            other: the other Node to compare to
        """
        return (self.label > other.label)

    def __repr__(self):
        """Return a string form of this node."""
        return '{} -> {}'.format(self.label, self.children)

    def add_child(self, node, cost=1):
        """
        Add a child node to this node.

        Args:
            node: the node to add to the children
            cost: the cost of the edge (default 1)
        """
        if type(node) is list:
            [self.add_child(sub_node) for sub_node in node]
            return
        edge = Edge(self, node, cost)
        self.children.append(edge)


class Edge(object):
    """This class represents an edge in a graph."""

    def __init__(self, source: Node, destination: Node, cost: int = 1, bidirectional: bool = False):
        """
        Initialize a new edge.

        Args:
            source: the source of the edge
            destination: the destination of the edge
            cost: the cost of the edge (default 1)
            bidirectional: whether source is accessible (default False)
        """
        self.source = source
        self.destination = destination
        self.cost = cost
        self.bidirectional = bidirectional

    def __repr__(self):
        """Return a string form of this edge."""
        return '{}: {}'.format(self.cost, self.destination.label)

Aveiro = Node('Aveiro')
Braga = Node('Braga')
Braganca = Node('Braganca')
Beja = Node('Beja')
Castelo_branco = Node('Castelo Branco')
Coimbra = Node('Coimbra')
Evora = Node('Evora')
Faro = Node('Faro')
Guarda =Node('Guarda')
Leiria = Node('Leiria')
Lisboa = Node('Lisboa')
Portalegre = Node('Portalegre')
Setubal = Node('Setubal')
Viana_do_castelo = Node('Viana do Castelo')
Viseu = Node ('Viseu')
Porto = Node ('Porto')
Santarem=Node('Santarem')
Vila_Real= Node('Vila Real')

Aveiro.add_child([Porto, Viseu, Coimbra,Leiria])
Braga.add_child([Viana_do_castelo, Vila_Real, Porto])
Braganca.add_child([Vila_Real, Guarda])
Beja.add_child([Evora,Faro,Setubal])
Castelo_branco.add_child([Coimbra,Guarda,Portalegre,Evora])
Coimbra.add_child([Viseu,Leiria,Aveiro,Castelo_branco])
Evora.add_child([Lisboa,Santarem,Portalegre,Setubal,Beja,Castelo_branco])
Faro.add_child([Setubal,Lisboa,Beja])
Guarda.add_child([Vila_Real,Viseu,Braganca,Castelo_branco])
Leiria.add_child([Lisboa,Setubal,Aveiro,Coimbra])
Lisboa.add_child([Santarem,Setubal,Leiria,Evora])
Portalegre.add_child([Castelo_branco,Evora])
Porto.add_child([Viana_do_castelo,Vila_Real,Viseu,Aveiro,Braga])
Santarem.add_child([Evora,Leiria,Lisboa])
Setubal.add_child([Evora,Faro,Lisboa,Beja])
Viana_do_castelo.add_child([Braga,Porto])
Vila_Real.add_child([Viseu,Braga,Braganca,Guarda,Porto])
Viseu.add_child([Aveiro,Coimbra,Guarda,Porto,Vila_Real])




def ProfundidadeLimitada(root: Node, goal: str, maximum_depth):
    """
    Retorna o caminho desde a raiz ate o no final

    Args:
        root: nó de inicio
        goal: nó de chegada
        maximum_depth: Limite de profundidade

    Returns:  lista de nós desde o inicio á chegada

   """
    for depth in range(0, maximum_depth):
        result = _dls([root], goal, depth)
        if result is None:
            continue
        return result

    print('Nó final não se encontra no grafo com profundidade {}'.format(maximum_depth))


def _dls(path: list, goal: str, depth: int):
    """
    Retorna o caminho de profundidade limitada de um sub-caminho ate o no de chegada.

    Args:
        path: lista de caminhos que estao a ser utilizados
        goal: Nó de chegada
        depth: Nivel de limite de pesquisa do grafo

    Returns: O caminho se exister, ou None se nao existir.
    """
    current = path[-1]
    if current.label == goal:
        return path
    if depth <= 0:
        return None
    for edge in current.children:
        new_path = list(path)
        print("Escolhido:", new_path)
        new_path.append(edge.destination)
        print("a ir para:", edge.destination)
        #result = _dls(new_path, goal, depth - 1)
       # if result is not None:
         #   return result



def menu():
    ans = True
    while ans:
        print("""
        ---Procura Cega:
        1.Profundidade Primeiro
        2.Profundidade Limitada
        ---Procura Heuristica:
        3.Procura Sofrega
        4.Procura A*
        5.Sair
        """)
        ans = input("Qual a opcao? ")
        if ans == "1":
            print("\n Profundidade Primeiro")

        elif ans == "2":
            print("\n Profundidade Limitada\n")
            ProfundidadeLimitada(Coimbra, 'Castelo Branco', 2)
        elif ans == "3":
            print("\n Procura Sofrega")
        elif ans == "4":
            print("\n Procura A*")
        elif ans == "5":
            return
        elif ans != "":
            print("\n Not Valid Choice Try again")


menu()


