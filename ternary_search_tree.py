import csv

def fileitems(filename, condition, conditionvalue, tree, conditionsdict):
    with open(filename, 'r') as f:      #opens file
        csvreader = csv.reader(f)
        lines = []
        header = next(csvreader)
        for rawline in csvreader:
            lines.append(rawline)
        check = False
        for line in lines:      #accesses each line and checks if condition matches, accordingly inserts in tree using insert_to_tree function
            if condition == 'all':
                check = True
                name = line[0]
                name = name.strip()
                namelst = name.split(' ')
                insert_to_tree(tree, namelst, line)
            else:
                if line[conditionsdict[condition]] == conditionvalue:
                    check = True
                    name = line[0]
                    name = name.strip()
                    namelst = name.split(' ')
                    insert_to_tree(tree, namelst, line)
        return check

def insert_to_tree(tree, name, data):
    t = {'Root': None, 'Left': None, 'Middle': None, 'Right': None, 'Value': None, 'Data': None}        #initialising an empty tree
    if len(name)>1:     #recursive base case when length of the name of the movie comes down to just one word (last word to be inserted in tree)
        if tree['Root'] == None:        #no value at root, can insert here, will move to middle next
            tree['Root'] = name[0]
            tree['Value'] = 0
            tree['Middle'] = t
            insert_to_tree(tree['Middle'], name[1:len(name)], data)
        else:
            if tree['Middle'] == None:      #no value at middle, can insert here by adding an empty dict here
                t['Root'] = name[0]
                tree['Middle'] = t
                tree['Value'] = 0
                insert_to_tree(tree['Middle'], name[1:len(name)], data)
            elif name[0] == tree['Root']:       #if word matches we move to the next node and compare again
                insert_to_tree(tree['Middle'], name[1:len(name)], data)
            elif name[0] < tree['Root']:
                if tree['Left'] == None:
                    t['Root'] = name[0]
                    tree['Left'] = t
                    tree['Value'] = 0
                    insert_to_tree(tree['Left'], name[1:len(name)], data)
                else:
                    insert_to_tree(tree['Left'], name[0:len(name)], data)
            else:
                if tree['Right'] == None:
                    t['Root'] = name[0]
                    tree['Right'] = t
                    tree['Value'] = 0
                    insert_to_tree(tree['Right'], name[1:len(name)], data)
                else:
                    insert_to_tree(tree['Right'], name[0:len(name)], data)
    else:
        if tree['Root'] == None:
            tree['Root'] = name[0]
            tree['Value'] = 1
            tree['Data'] = data
        else:
            if tree['Middle'] == None:
                t['Root'] = name[0]
                t['Value'] = 1
                t['Data'] = data
                tree['Middle'] = t
                tree['Value'] = 0
            elif name[0] < tree['Root']:
                if tree['Left'] == None:
                    t['Root'] = name[0]
                    t['Value'] = 1
                    t['Data'] = data
                    tree['Left'] = t
                    tree['Value'] = 0
                else:
                    insert_to_tree(tree['Left'], name[0:len(name)], data)
            else:
                if tree['Right'] == None:
                    t['Root'] = name[0]
                    t['Value'] = 1
                    t['Data'] = data
                    tree['Right'] = t
                    tree['Value'] = 0
                else:
                    insert_to_tree(tree['Right'], name[0:len(name)], data)
        return

def search_recursive_dictfinder(tree, fword):   #finds the subtree from where the movies of the input word starts
    if tree == None:
        return None
    if tree['Root'] == fword:
        return tree['Middle']
    else:
        if fword < tree['Root']:
            return search_recursive_dictfinder(tree['Left'], fword)
        else:
            return search_recursive_dictfinder(tree['Right'], fword)

def search_recursive_names(fword, treedict, retlst):        #traverses the entire tree that is sent as a paramter
    if treedict['Value'] == 1:
        if treedict['Data'] not in retlst:
            retlst.append(treedict['Data'])
    else:
        if treedict['Left'] != None:
            search_recursive_names(fword, treedict['Left'], retlst)
        if treedict['Right'] != None:
            search_recursive_names(fword, treedict['Right'], retlst)
        if treedict['Root'] != None:
            search_recursive_names(fword, treedict['Middle'], retlst)

def search(tree, fword):
    treedict = search_recursive_dictfinder(tree, fword)     #finding the subtree from where the movies of the input word starts
    if treedict == None:    #checking if the word exists in the ternary search tree
        return "Does not exist"
    retlst = []
    print(treedict)
    search_recursive_names(fword, treedict, retlst)     #traverses the subtree to get all the movies from the input word
    return retlst

# tree = {'Root': None, 'Left': None, 'Middle': None, 'Right': None, 'Value': None. 'Data': None}
# conditionsdict = {'year': 1, 'femalelead': 2, 'malelead': 3, 'genre': 4, 'rating': 5}

# fileitems(r"D:\Salman\University\Semester 2\Data Structures & Algorithms\Project\movielist.csv", 'genre', 'Romance', tree, conditionsdict)
# print(tree)
# print()
# search(tree, 'Kabhi')