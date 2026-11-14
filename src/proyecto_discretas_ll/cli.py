import argparse

from .loader import load_graph
from .properties import has_cycle, is_connected, is_forest, is_tree


def main():
    parser = argparse.ArgumentParser(description="Check graph properties")
    parser.add_argument("path", help="CSV file with lines source,target,weight")
    parser.add_argument(
        "--directed", action="store_true", help="load the graph as directed"
    )
    args = parser.parse_args()

    graph = load_graph(args.path, directed=args.directed)
    is_connected(graph)
    has_cycle(graph)
    is_tree(graph)
    is_forest(graph)