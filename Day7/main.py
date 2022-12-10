from input import input


class Dir:
    def __init__(self, name="Root", children=None, size=0):
        self.name = name
        self.children = []
        self.size = size
        if children is not None:
            for child in children:
                self.add_dir(child)
    def __repr__(self):
        string = self.name + ":\n"
        for child in self.children:
            string += "\t" + str(child)
        return string
    def add_child(self, child):
        self.children.append(child)
    def add_size(self, size):
        self.size += size

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    def __repr__(self):
        return self.name + ", size:" + str(self.size)



root = Dir("root")
def parse_input():
    #TODO
    steps = input.split('\n')
    curr = "root"
    del steps[0]
    for step in steps:
        all = step.split()
        if(all[0] == "$"):
            if(all[1] == "cd"):
                if(all[2] == ".."):
                    curr = curr[:curr.rfind('_')]
                else:
                    curr = curr + '_' + all[2]
        elif(all[0] == "dir"):
            #Should be done with a traversal / tree walk, not by storing the name as a variable
            path = curr + '_' + all[1]
            locals()[path] = Dir(all[1])
            eval(curr).add_child(locals()[path])
        else:
            eval(curr).add_child(File(all[1], all[0]))

def add_folder_sizes(node):
    size = 0
    for child in node.children:
        if(isinstance(child, Dir)):
            size += add_folder_sizes(child)
        else:
            size += int(child.size)
    #TODO
    node.add_size(size)
    return size 

#Shouldn't be handled with global variable
total = 0

def check_folder_size(node, max_size):
    global total
    size = node.size
    for child in node.children:
        if(isinstance(child, Dir)):
            check_folder_size(child, max_size)
    if(size < max_size):
        total += size
    return size


parse_input()
add_folder_sizes(root)
check_folder_size(root, 100000)
#Part 1 Solution
print(total)


#Part 2

needed_space = root.size - (70000000 - 30000000)
print(needed_space)

match = 70000000

#Shouldn't be handled with global variable
def find_smallest_fit(node, needed_space):
    global match
    size = node.size
    if(size >= needed_space and size < match):
        match = size
    for child in node.children:
        if(isinstance(child, Dir)):
            if(child.size >= needed_space):
                return find_smallest_fit(child, needed_space)
    return node

#Part 2 Solution
find_smallest_fit(root, needed_space)
print(match)