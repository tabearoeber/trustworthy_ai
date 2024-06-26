import graphviz
import numpy as np

def display_tree(tree, n, feature_names=None):
    dot = graphviz.Digraph(filename='fsdt')
    add_nodes(dot, tree, n, feature_names)
    dot.view()
    return dot

def add_nodes(dot, tree, n, feature_names=None,):
    dot.attr('node', shape='box')
    dot.attr(size='10')
    if 'feat' in tree:
        feat = tree['feat']
        left = tree['left']
        right = tree['right']
        if feature_names is None: 
            dot.node(str(id(tree)), label=f'{feat}')
        else:
            dot.node(str(id(tree)), label=f'{feature_names[feat]}')
        add_nodes(dot, left, n, feature_names)
        add_nodes(dot, right, n, feature_names)
        dot.edge(str(id(tree)), str(id(left)), label='True')
        dot.edge(str(id(tree)), str(id(right)), label='False')
    else:
        value = tree['value']
        error = tree['error']/n
        dot.node(str(id(tree)), label=f'Class {value}\nError: {error:.3f}')

def get_num_leaves(tree):
    if 'value' in tree:
        return 1
    else:
        left_leaves = get_num_leaves(tree['left'])
        right_leaves = get_num_leaves(tree['right'])
        return left_leaves + right_leaves


def get_avg_rule_length(tree):
    path_lengths = []

    def traverse(node, path_len):
        if 'left' not in node and 'right' not in node:
            path_lengths.append(path_len)
        if 'left' in node:
            traverse(node['left'], path_len + 1)
        if 'right' in node:
            traverse(node['right'], path_len + 1)

    traverse(tree, 0)
    avg_rule_length = sum(path_lengths) / get_num_leaves(tree)

    return avg_rule_length


def get_avg_rule_length_per_sample(tree, X):
    def record_decision_path_length(tree, X):
        """
        Records the length of the decision path for every sample in X.

        Parameters:
        tree (dict): A decision tree represented as a nested dictionary.
        X (numpy array): An array of samples to record the decision path length for.

        Returns:
        A numpy array of integers representing the length of the decision path for each sample in X.
        """
        path_lengths = []
        for sample in X:
            node = tree
            path_length = 0
            while 'value' not in node:
                feature = node['feat']
                if sample[feature] == 1:
                    node = node['left']
                else:
                    node = node['right']
                path_length += 1
            path_lengths.append(path_length)
        return np.array(path_lengths)

    path_lengths = record_decision_path_length(tree, X)
    return np.mean(path_lengths)