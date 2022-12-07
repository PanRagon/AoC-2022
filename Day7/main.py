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

def testing():
    root = Dir()
    a_folder = Dir("a")
    root.add_child(a_folder)
    a_folder.add_child(Dir("c"))
    a_folder.add_child(File("d", 25))
    root.add_child(Dir("b"))
    
    print(a_folder)

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
                curr = all[2]
        elif(all[0] == "dir"):
            locals()[all[1]] = Dir(all[1])
            eval(curr).add_child(locals()[all[1]])
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


total = 0

def check_folder_size(node, max_size):
    global total
    size = node.size
    print(size)
    for child in node.children:
        if(isinstance(child, Dir)):
            check_folder_size(child, max_size)
    if(size < max_size):
        print('is small boy', size)
        total += size
        print(total)
    return size


parse_input()
add_folder_sizes(root)
check_folder_size(root, 100000)
print(total)