import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    parent_id = set(tree['p_id'].dropna())

    tree['type'] = tree['p_id'].case_when([
        (tree['p_id'].isna(), 'Root'),
        (tree['id'].isin(parent_id), 'Inner'),
        (pd.Series(True, index=tree.index),'Leaf')
   ])

    return tree[['id', 'type']]
    