
def reverse_graph(graph):
    r_graph = {v: set() for v in graph}
    for vertex in graph:
        for value in graph[vertex]:
            r_graph[value].add(vertex)
    return r_graph

G = {
    'A' : {'B'},
    'B' : {'C','D'},
    'C' : {'A'},
    'D' : {'E'},
    'E' : {'F'},
    'F' : {'D'},
    'H' : {'I'},
    'I' : {'J'},
    'J' : {'G'},
    'G' : {'F', 'H'} ,
    'K' : {'J'},
    }


def test_reverse():
    rG = {'A': {'C'}, 'B': {'A'}, 'C': {'B'}, 'D': {'F', 'B'}, 'E': {'D'}, 'F': {'G', 'E'}, 'H': {'G'}, 'I': {'H'}, 'J': {'K', 'I'}, 'G': {'J'}, 'K': set()}
    assert rG == reverse_graph(G), "Reverse graph test failed"


rG = reverse_graph(G)
print(rG)
