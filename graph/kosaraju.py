from collections import deque

"""
   Выделение компонент сильной связанности
   ориентированного графа
"""


def reverse_graph(graph):
    """
       Обращение ориентации всех ребер графа.
       Возвращает обращенный граф
    """
    r_graph = {v: set() for v in graph}
    for vertex in graph:
        for value in graph[vertex]:
            r_graph[value].add(vertex)
    return r_graph


def get_stack(graph):
    """
       Возвращает заполненный стек при прямом проходе графа
    """
    stack = deque()
    for vertex in graph:
        if vertex not in stack:
            dfs_stack(graph, vertex, stack)
    return stack

def dfs_stack(graph, vertex, stack):
    stack.appendleft(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in stack:
            dfs_stack(graph, neighbour, stack)


def get_strong_components(graph, stack):
    """
       Выполняет обратный проход по графу с сформированным стеком
       Возвращает список вершин компонент сильной связанности
    """
    strong_components = []
    used = set()
    rG = reverse_graph(graph)
    while stack:
        v = stack.popleft()
        if v not in used:
            component = get_strong_component(rG,v,used)
            strong_components.append(component)
    return strong_components

def get_strong_component(graph, vertex, used, component = None):
    used.add(vertex)
    component = component or set()
    component.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in used:
            get_strong_component(graph, neighbour, used, component)
    return component



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
    G = {'A': {'B'}, 'B': {'D', 'C'}, 'C': {'A'}, 'D': {'E'}, 'E': {'F'}, 'F': {'D'}, 'H': {'I'}, 'I': {'J'}, 'J': {'G'}, 'G': {'F', 'H'}, 'K': {'J'}}
    rG = {'A': {'C'}, 'B': {'A'}, 'C': {'B'}, 'D': {'F', 'B'}, 'E': {'D'}, 'F': {'G', 'E'}, 'H': {'G'}, 'I': {'H'}, 'J': {'K', 'I'}, 'G': {'J'}, 'K': set()}
    assert rG == reverse_graph(G), "Reverse graph test failed"


def test_stack():
    G = {'A': {'B'}, 'B': {'D', 'C'}, 'C': {'A'}, 'D': {'E'}, 'E': {'F'}, 'F': {'D'}, 'H': {'I'}, 'I': {'J'}, 'J': {'G'}, 'G': {'F', 'H'}, 'K': {'J'}}
    assert deque(['K', 'G', 'J', 'I', 'H', 'F', 'E', 'D', 'C', 'B', 'A']) == get_stack(G), "Stack test failed"

rG = reverse_graph(G)
print(rG)
