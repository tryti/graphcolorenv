"""
TODO:
    documentation
    add fully connected graphs of size 3-6
"""
import networkx as nx
import settings


def min_no_color():
    g = nx.Graph()
    g.add_node(1, color=settings.Color.NOCOLOR)
    g.add_node(2, color=settings.Color.NOCOLOR)
    g.add_node(3, color=settings.Color.NOCOLOR)
    g.add_node(4, color=settings.Color.NOCOLOR)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    return g

def complete_three_no_color():
    g = nx.Graph()
    g.add_node(3, color=settings.Color.NOCOLOR)
    g.add_node(2, color=settings.Color.NOCOLOR)
    g.add_node(1, color=settings.Color.NOCOLOR)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    return g


def complete_four_no_color():
    g = nx.Graph()
    g.add_node(3, color=settings.Color.NOCOLOR)
    g.add_node(2, color=settings.Color.NOCOLOR)
    g.add_node(1, color=settings.Color.NOCOLOR)
    g.add_node(4, color=settings.Color.NOCOLOR)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    return g


def min_with_color_correct():
    g = nx.Graph()
    g.add_node(1, color=settings.Color.RED)
    g.add_node(2, color=settings.Color.BLUE)
    g.add_node(3, color=settings.Color.BLUE)
    g.add_node(4, color=settings.Color.RED)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    return g


def min_with_color_incorrect():
    g = nx.Graph()
    g.add_node(1, color=settings.Color.RED)
    g.add_node(2, color=settings.Color.BLUE)
    g.add_node(3, color=settings.Color.BLUE)
    g.add_node(4, color=settings.Color.BLUE)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    return g

def g6_no_color():
    g = nx.Graph()
    g.add_node(1, color=settings.Color.NOCOLOR)
    g.add_node(2, color=settings.Color.NOCOLOR)
    g.add_node(3, color=settings.Color.NOCOLOR)
    g.add_node(5, color=settings.Color.NOCOLOR)
    g.add_node(6, color=settings.Color.NOCOLOR)
    g.add_node(4, color=settings.Color.NOCOLOR)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(2, 5)
    g.add_edge(4, 5)
    g.add_edge(5, 6)
    return g


def g6_half_color():
    g = nx.Graph()
    g.add_node(1, color=settings.Color.RED)
    g.add_node(2, color=settings.Color.NOCOLOR)
    g.add_node(3, color=settings.Color.NOCOLOR)
    g.add_node(5, color=settings.Color.BLUE)
    g.add_node(6, color=settings.Color.NOCOLOR)
    g.add_node(4, color=settings.Color.NOCOLOR)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(2, 5)
    g.add_edge(4, 5)
    g.add_edge(5, 6)
    return g


def g6_half_color2():
    g = nx.Graph()
    g.add_node(1, color=settings.Color.RED)
    g.add_node(2, color=settings.Color.BLUE)
    g.add_node(3, color=settings.Color.GREEN)
    g.add_node(5, color=settings.Color.NOCOLOR)
    g.add_node(6, color=settings.Color.NOCOLOR)
    g.add_node(4, color=settings.Color.NOCOLOR)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(2, 5)
    g.add_edge(4, 5)
    g.add_edge(5, 6)
    return g
