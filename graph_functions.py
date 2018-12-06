import networkx as nx
import settings
import sys

def chromatic_number(graph):
    """
    Returns the chromatic_number for the graph g, calculated using a brute force
    algorithm. O(k^|V|, g=<V,E>

    Args:
        g (NetworkX.Graph) - network x graph

    Returns:
        cn (int) - chromatic_number for g
    """
    colors = nx.get_node_attributes(graph, settings.COLOR)
    node_ids = [v for v in graph.nodes()] # maps integers 0-|V| to nodes
    root = None
    for i in range(len(node_ids)):
        if colors[node_ids[i]] == settings.Color.NOCOLOR:
            root = i
            break
    solution, min_chrom = __calculate_chrom_rec(graph, root, colors, node_ids)
    print(min_chrom)
    print(solution)
    return solution, min_chrom


def __calculate_chrom_rec(graph, node, colors, node_ids):
    """

    Precondition: nodes with id's 0 to k-1 is colored if node = k
    """
    neighbor_colors = set([colors[v] for v in nx.all_neighbors(graph, node_ids[node])])
    available_colors = list(set(c for c in settings.Color.all_colors() if c not in neighbor_colors))

    next_node = node + 1
    while next_node < len(node_ids):
        if colors[node_ids[next_node]] == settings.Color.NOCOLOR:
            break
        next_node += 1
    if next_node >= len(colors):        # If current node is the last node to color
        solution_colors = colors.copy()
        min_c = -1
        min_chrom = sys.maxint
        for c in available_colors:
            solution_colors[node_ids[node]] = c
            used_colors = set(solution_colors.values())
            if settings.Color.NOCOLOR in used_colors:
                used_colors.remove(settings.Color.NOCOLOR)
            if len(used_colors) < min_chrom:
                min_c = c
                min_chrom = len(used_colors)
        solution_colors[node_ids[node]] = min_c
        return solution_colors, min_chrom
    else:
        best_solution = None
        best_chrom = sys.maxint
        for c in available_colors:
            solution_colors = colors.copy()
            solution_colors[node_ids[node]] = c
            solution_colors, min_chrom = __calculate_chrom_rec(graph, next_node, solution_colors, node_ids)
            if min_chrom < best_chrom:
                best_solution = solution_colors
                best_chrom = min_chrom
        return best_solution, best_chrom


def correct_solution(g, c):
    """
    Checks graph g's coloring solution

    Args:
        g (NetworkX.Graph) - NetworkX Graph object with node attribute "color"
                             containing integer values 1 to c.
        c (int) - c is the max color number for g's color attributes

    Returns:

    """
    used_colors = []
    colors = nx.get_node_attributes(g, settings.COLOR)
    for v in g.nodes():
        if colors[v] not in used_colors:
            used_colors.append(colors[v])
            if len(used_colors) > c:
                return False
        if colors[v] == settings.Color.NOCOLOR:
            return False
        for u in g.neighbors(v):
            if colors[u] == colors[v]:
                return False
        pass
    return True


def remove_colors(g):
    """
    Set all color attributes in graph g to NOCOLOR

    Args:
        g (networkx.Graph) - Graph with color attributes to remove.

    Returns:
         h (NetworkX.Graph) - Copy of g with removed color attributes
    """
    h = g.copy()
    for v in h.nodes:
        h.node[v][settings.COLOR] = settings.Color.NOCOLOR
    return h
