from test import test_input


#Data structure
class Valve:
    def __init__(self, name, flow, tunnels):
        self.name = name
        self.flow = flow
        self.tunnels = tunnels

    def __str__(self):
        return self.name + ' has a flow rate of: ' + self.flow


#Parse
valves = test_input.split('\n')

for idx, valve in enumerate(valves):
    valve = valve.split(';')
    name = valve[0].split(' ')[1]
    flow = valve[0].split('=')[-1]
    tunnels = valve[1].replace('valves', 'valve').split('valve')[-1].split(',')

    valves[idx] = Valve(name, flow, tunnels)

