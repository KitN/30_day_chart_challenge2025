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

#Convert the outline file to Newick format
def outline_to_newick(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    def parse_outline(lines, level=0):
        tree = []
        while lines:
            line = lines[0]
            current_level = len(line) - len(line.lstrip(' '))
            if current_level < level:
                break
            lines.pop(0)
            name = line.strip()
            if lines and (len(lines[0]) - len(lines[0].lstrip(' '))) > current_level:
                children = parse_outline(lines, current_level + 1)
                tree.append(f"({','.join(children)}){name}")
            else:
                tree.append(name)
        return tree

    newick_tree = parse_outline(lines)
    return f"{','.join(newick_tree)};"

# Example usage
file_path = 'outline_too.txt'
newick_format = outline_to_newick(file_path)
print(newick_format)