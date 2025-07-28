import numpy as np

class Resistor:
    def __init__(self, node_i, node_e, value):
        self.node_i = node_i
        self.node_e = node_e
        self.value = value
    

class VoltageSource:
    def __init__(self, node_i, node_e, value):
        self.node_i = node_i
        self.node_e = node_e
        self.value = value
        
nodes = [0,0,0,0]

V1 = VoltageSource(nodes[0], nodes[1], 10)
R1 = Resistor(nodes[1], nodes[2], 2)
R2 = Resistor(nodes[0], nodes[2], 3)
R3 = Resistor(nodes[2], nodes[3], 5)
RL = Resistor(nodes[0], nodes[3], 1)


    