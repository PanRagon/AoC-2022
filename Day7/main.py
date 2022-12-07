from input import input


class Dir:
    def __init__(self, name="Root", children=None):
        self.name = name
        self.children = []
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

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    def __repr__(self):
        return self.name

def testing():
    root = Dir()
    a_folder = Dir("a")
    root.add_child(a_folder)
    a_folder.add_child(Dir("c"))
    root.add_child(Dir("b"))
    
    print(a_folder)
testing()

def parse_input():
    #TODO
    file_system = {}
    steps = input.split('\n')
    curr = ''
    return file_system

def check_folder_sizes(file_system):
    #TODO
    return file_system 

parse_input()