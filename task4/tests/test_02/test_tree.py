import tree_utils_02.node as node
import tree_utils_02.tree as tree
import tempfile
from pytest import raises
import os


def test_tree():
    exemp = tree.Tree()
    with raises(AttributeError):
        exemp.get("...", True)

    with tempfile.TemporaryDirectory('./') as tmp_dir:
        with open(os.path.join(tmp_dir, 'text.txt'), "w") as file:
            file.write("Python")
        with raises(AttributeError):
            exemp.get(file.name, True, False)

        c = node.FileNode(name=file.name.split('/')[-1], is_dir=False, children=[])
        a = exemp.get(file.name, False)
        assert a == c

        assert exemp.get(file.name, True, True) == None

        c = node.FileNode(name=file.name.split('/')[-1], is_dir=False,
                        children=[])
        a = exemp.get(file.name, False, True) 
        assert a == c

        c = node.FileNode(name=tmp_dir.split('/')[-1], is_dir=True, children=[node.FileNode(name='text.txt', is_dir=False, children=[])])
        a = exemp.get(f'{tmp_dir}', False, False)
        assert a == c

        c = node.FileNode(name=tmp_dir.split('/')[-1], is_dir=True, children=[node.FileNode(name='text.txt', is_dir=False, children=[])])
        assert exemp.filter_empty_nodes(c) == None

        c = node.FileNode(name=tmp_dir.split('/')[-1], is_dir=True, children=[])
        exemp.filter_empty_nodes(c, f'{tmp_dir}')
