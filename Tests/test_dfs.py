import pytest
from hw7.dfs import Graph


class TestGraph:
    def test_empty_graph(self):
        g = Graph()
        assert g.dfs(0) == []
        assert list(g) == []

    def test_single_vertex(self):
        g = Graph()
        g.add_edge(1, 1)
        assert g.dfs(1) == [1]
        assert list(g) == [1]

    def test_two_vertices(self):
        g = Graph()
        g.add_edge(1, 2)
        assert g.dfs(1) == [1, 2]
        assert list(g) == [1, 2]

    def test_linear_graph(self):
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 4)
        assert g.dfs(1) == [1, 2, 3, 4]
        assert list(g) == [1, 2, 3, 4]

    def test_star_graph(self):
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(0, 3)
        result = g.dfs(0)
        assert set(result) == {0, 1, 2, 3}
        assert result[0] == 0
        assert len(result) == 4

    def test_cycle_graph(self):
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 1)
        result = g.dfs(1)
        assert set(result) == {1, 2, 3}
        assert result[0] == 1

    def test_different_start_vertex(self):
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 4)
        assert g.dfs(3) == [3, 2, 1, 4]

    def test_complex_graph(self):
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 3)
        result = g.dfs(0)
        assert set(result) == {0, 1, 2, 3}
        assert result[0] == 0
