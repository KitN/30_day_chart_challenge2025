from Bio import Phylo
from Bio.Phylo import PhyloXML
from Bio.Phylo.PhyloXML import Phyloxml, Clade

"""- **Liliopsida** (Monocots)
  - **Order: Asparagales**
    - **Family: Orchidaceae**
      - **Genus: Vanilla**
        - *Vanilla planifolia* (Vanilla)
    - **Family: Amaryllidaceae**
      - **Genus: Allium**
        - *Allium cepa* (Onions)"""
# Convert the outline file to an PhlyoXML file
def parse_outline_to_phyloxml(input_file, output_file):

    with open(input_file, 'r') as f:
        lines = f.readlines()

    def parse_line(line):
        indent_level = len(line) - len(line.lstrip(' '))  # Determine the hierarchy level based on indentation
        name = line.strip()
        return indent_level, name

    root = None
    current_nodes = {}

    for line in lines:
        if not line.strip():
            continue  # Skip empty lines
        level, name = parse_line(line)
        clade = Clade(name=name)
        if level == 0:
            root = clade
            current_nodes[level] = clade
        else:
            parent = current_nodes[level - 1]
            parent.clades.append(clade)
            current_nodes[level] = clade

    phyloxml_tree = Phyloxml()
    phyloxml_tree.add_clade(root)

    with open(output_file, 'w') as f:
        Phylo.write([phyloxml_tree], f, 'phyloxml')


# Input and output file paths
input_file = 'outlined_too.txt'
output_file = 'output.xml'

# Convert the outline to PhyloXML
parse_outline_to_phyloxml(input_file, output_file)
