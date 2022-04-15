from tree_utils_02.size_node import FileSizeNode
from tree_utils_02.size_tree import SizeTree
import tempfile
import os

def test_size_tree():
    with tempfile.TemporaryDirectory(dir='./') as tmp_dir:
        with open(os.path.join(tmp_dir, 'text'), "w") as file:
            file.write("Python")
        
        cla = SizeTree()

        c = cla.get(tmp_dir, False, True)
        a = FileSizeNode(name='text', is_dir=False, children=[], size=6)
        exp = FileSizeNode(name=tmp_dir.split('/')[-1], is_dir=True, children=[a], size=4102)
        assert c == exp