import unittest
import networkx as nx
import graph_functions as gf
import test_utils_graphs as utils
import settings


class GraphFunctionTests(unittest.TestCase):
    def test_correct_solution(self):
        g1 = utils.min_with_color_correct()
        g2 = utils.min_with_color_incorrect()
        g3 = utils.min_no_color()

        assert gf.correct_solution(g1, 2)
        assert not gf.correct_solution(g1, 1)
        assert not gf.correct_solution(g2, 2)
        assert not gf.correct_solution(g3, 2)

    def test_chromatic_number(self):
        g1 = utils.min_no_color()
        g2 = utils.complete_three_no_color()
        g3 = utils.complete_four_no_color()
        g4 = utils.g6_no_color()
        g5 = utils.g6_half_color()
        g6 = utils.g6_half_color2()

        sol1, c1 = gf.chromatic_number(g1)
        assert c1 == 2
        sol2, c2 = gf.chromatic_number(g2)
        assert c2 == 3
        sol3, c3 = gf.chromatic_number(g3)
        assert c3 == 4
        sol4, c4 = gf.chromatic_number(g4)
        assert c4 == 3
        sol5, c5 = gf.chromatic_number(g5)
        assert c5 == 3
        sol6, c6 = gf.chromatic_number(g6)
        assert c6 == 3

    def test_remove_color(self):
        g1 = utils.min_with_color_incorrect()
        g2 = gf.remove_colors(g1)
        for n in g1.nodes(data=True):
            assert not n[1][settings.COLOR] == settings.Color.NOCOLOR
        for n in g2.nodes(data=True):
            assert n[1][settings.COLOR] == settings.Color.NOCOLOR


if __name__ == '__main__':
    unittest.main()
