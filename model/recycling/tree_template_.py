def choose_tree_template(version):
    tree_template = None
    if version == "2.2.2":
        tree_template = [[0], [1], [2], [3], [4], [5], [6], [7],
                        [0,0], [0,1], [0,2], [0,3], [0,4], [0,5], [0,6], [0,7], [1,0], [1,1], [1,2], [1,3], [2,0], [2,1], [2,2], [3,0], [3,1], [4,0], [5,0], [6,0], [7,0],
                        [0,0,0], [0,0,1], [0,0,2], [0,0,3], [0,0,4], [0,0,5], [0,0,6], [0,0,7], [0,1,0], [0,1,1], [0,1,2], [0,2,0], [0,2,1], [0,3,0], [0,4,0], [0,5,0], [0,6,0], [0,7,0], [1,0,0], [1,0,1], [1,1,0], [2,0,0], [3,0,0], [4,0,0], [5,0,0],
                        [0,0,0,0], [0,0,0,1], [0,0,0,2], [0,0,0,3], [0,0,0,4], [0,0,1,0], [0,0,1,1], [0,0,2,0], [0,0,3,0], [0,0,4,0], [0,1,0,0], [0,2,0,0], [1,0,0,0], [2,0,0,0], [3,0,0,0],
                        [0,0,0,0,0], [0,0,0,0,1], [0,0,0,0,2], [0,0,0,1,0], [0,0,0,2,0], [0,0,1,0,0], [0,1,0,0,0], [1,0,0,0,0],
                        [0,0,0,0,0,0], [0,0,0,0,0,1], [0,0,0,1,0,0],
                        ]

    if tree_template is None:
        raise ValueError("Invalid version")
    return tree_template