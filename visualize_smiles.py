import pandas as pd
import matplotlib.pyplot as plt
import math
from rdkit import Chem
from rdkit.Chem import Draw



def visualize_smiles(input_file: str) -> None:
    """
    Takes a csv file of SMILES and outputs a png of the structures.
    CSV file should have two columns: the first column containing a label for the molecule, the second containing the SMILES string
    """
    ligands = pd.read_csv(input)
    
    names = ligands.iloc[:,0]
    smiles = ligands.iloc[:,1]
    
    num_imgs = len(smiles)
    num_rows = math.ceil(num_imgs/3)
    
    fig, axes = plt.subplots(num_rows, 3, layout="constrained", figsize=(4,8))
    
    if num_imgs == 1:
        axes = [axes]
    else:
        axes = axes.flatten()
    
    for i, ligand in enumerate(smiles):
        mol = Chem.MolFromSmiles(ligand)
        img = Draw.MolToImage(mol, size=(600,600))
    
        axes[i].imshow(img)
        axes[i].set_title(names[i], fontsize=4)
        axes[i].axis('off')
        
    for j in range(num_imgs, len(axes)):
        axes[j].axis('off')
    
    plt.tight_layout()
    plt.savefig('ligands.png', dpi=600)
    plt.show()

