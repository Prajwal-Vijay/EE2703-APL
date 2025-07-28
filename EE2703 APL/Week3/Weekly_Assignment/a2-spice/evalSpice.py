###
# Author: Prajwal Vijay
# Roll No.: EE23B057
# Course: APL (EE2703)
# Assignment No.: 2
###

import numpy as np 

def component_search_by_name(components, name): # Here given the name of the component, we search for it in the list of all components.
    for component in components:
        if component['name'] == name:
            return [component]
    return [{}]

def component_search_by_node(components, node): # Given the node, it returns all the components that are attached to the node.
    filtered_components = []
    # This way of appending empty dictionary is a nice way to show that given list, came from this function only.
    filtered_components.append({'name':'dummy', 'type':None, 'node_1':None, 'node_2':None, 'voltage':0}) 
    for component in components:
        if component['node_1'] == node or component['node_2'] == node: 
            filtered_components.append(component)
    return filtered_components

def evalSpice(filename):
    with open(filename, 'r') as file: # Opens up a file with the given name
        lines = file.readlines()
    parse_begin = False
    components = []
    nodes = []
    voltage_sources = []
    circuit_found = False # They are used to determine if the .circuit and .end were found in the file or not.
    end_found = False 
    for line in lines:
        line = line.strip()
        
        if '.circuit' in line:
            circuit_found = True
            parse_begin = True # if .circuit was found, then begin parsing the file for components.
            
        if '.end' in line:
            end_found = True
            parse_begin = False # if .end was found then stop the parsing
        
        if parse_begin:
            words = line.split()
            # Ground Node is assigned a 0
            if words[0][0] == 'V': # Finds a voltage source and adds it to the component list
                c_type = 'V_src'
                c_node_1 = 0 if words[1] == "GND" else words[1]
                c_node_2 = 0 if words[2] == "GND" else words[2]
                voltage_val = float(words[4])
                
                if c_node_1 not in nodes:
                    nodes.append(c_node_1)
                if c_node_2 not in nodes:
                    nodes.append(c_node_2)
                voltage_sources.append(words[0])
                components.append({'name': words[0], 'type':c_type, 'node_1':c_node_1, 'node_2': c_node_2, 'voltage': voltage_val})
            
            elif words[0][0] == 'I': # Finds a current source and adds it to the component list
                c_type = 'I_src'
                c_node_1 = 0 if words[1] == "GND" else words[1]
                c_node_2 = 0 if words[2] == "GND" else words[2]
                current_val = float(words[4])
                
                if c_node_1 not in nodes:
                    nodes.append(c_node_1)
                if c_node_2 not in nodes:
                    nodes.append(c_node_2)
                    
                components.append({'name': words[0], 'type':c_type, 'node_1':c_node_1, 'node_2':c_node_2, 'current': current_val})
            
            elif words[0][0] == 'R': # Finds a resistor and adds it to the component list
                c_type = 'Resistor'
                c_node_1 = 0 if words[1] == "GND" else words[1]
                c_node_2 = 0 if words[2] == "GND" else words[2]
                resistance = float(words[3])
                
                if c_node_1 not in nodes:
                    nodes.append(c_node_1)
                if c_node_2 not in nodes:
                    nodes.append(c_node_2)
                    
                components.append({'name':words[0], 'type':c_type, 'node_1':c_node_1, 'node_2':c_node_2, 'resistance': resistance})
            
            elif words[0][0] != '.': # A check, for any other invalid circuit elements present
                raise ValueError("Invalid Circuit Elements Used")
        
        
        if 0 in nodes: 
            nodes.remove(0)
            nodes.insert(0, 0)
    
    if not circuit_found or not end_found: # Raises the error when the format of the .ckt file is wrong.
        raise ValueError("Invalid Format of .ckt file")
    
    voltages = dict.fromkeys(nodes) # From all the nodes we create a dictionary, that corresponds to the voltage value.
    voltages['GND'] = 0
    voltages.pop(0)
    currents = dict.fromkeys(voltage_sources)
    variables = nodes+voltage_sources
    coeff_matrix = [] # Defining the coeff matrix
    current_source_matrix = [] # Defining the current source matrix
    for i in range(len(variables)-1):
        coeff_matrix.append([])
        if i < len(nodes) - 1: 
            connected_components = component_search_by_node(components, nodes[i+1])
        elif i >= len(nodes) - 1:
            connected_components = component_search_by_name(components, voltage_sources[i+1-len(nodes)])
        
        ### 
        # The logic followed is that:
        # When i == j, then put sum of conductances connected to that node.
        # When i != j, then fill with negative of the conductance between the two nodes
        # It is to be noted, that current from positive to negative terminal of a voltage source is assumed positive
        ###
        
        for j in range(len(variables)-1):
            if i == j and j < len(nodes) - 1:
                conductance = 0 
                for component in connected_components:
                    if component['type'] == 'Resistor':
                        conductance += 1/component['resistance']
                coeff_matrix[i].append(conductance)
            
            elif i < j and j < len(nodes) - 1:
                conductance = 0
                for component in connected_components:
                    if (component['node_1'] == nodes[j+1] or component['node_2'] == nodes[j+1]) and component['type'] == 'Resistor':
                        conductance -= 1/component['resistance']
                coeff_matrix[i].append(conductance)
            
            # The part that deals with currents through voltage sources
            elif i < j and j >= (len(nodes) - 1): # Beyond this point, j is not really referring to a node in the circuit.
                conductance = 0
                for component in connected_components:
                    if component['type'] == 'V_src' and variables.index(component['name']) == j+1:
                        if component['node_1'] == nodes[i+1]:
                            conductance = 1
                        elif component['node_2'] == nodes[i+1]:
                            conductance = -1
                coeff_matrix[i].append(conductance)
            else:
                coeff_matrix[i].append(0)
        current = 0
        current_source_matrix.append([])
        
        # This creates the solution matrix, which have currents from postive to negative terminal of voltage source as +ve
        # For current sources, we assume the current to point from the first node to the last node
        
        # Current sources VERIFIED
        for component in connected_components:
            if component['type'] == 'I_src':
                if i < len(nodes)-1 and component['node_1'] == nodes[i+1]: # If a current source was connected in series to a voltage source, that would mean a new node, so it would still be included in the nodes
                    current -= component['current']
                elif i < len(nodes)-1 and component['node_2'] == nodes[i+1]:
                    current += component['current']
            
            # Voltage Sources VERIFIED        
            # Sign of the voltage source is being taken care in the coeff matrix, here just add the voltage value directly
            if component['type'] == 'V_src' and len(connected_components) == 1:
                current += component['voltage']
        
        current_source_matrix[i].append(current)
        
    current_source_matrix = np.array(current_source_matrix, dtype=float)
    coeff_matrix = np.array(coeff_matrix, dtype=float)
    
    # Creating a symmetric matrix from the initial matrix
    # For all the examples I had taken, I observed a symmetric coefficient matrix always, this has to do with the reciprocity property!
    for i in range(len(coeff_matrix)):
        for j in range(i+1,len(coeff_matrix)):
            coeff_matrix[j, i] = coeff_matrix[i, j]

    # solves the equations
    try:
        solutions = np.linalg.solve(coeff_matrix, current_source_matrix)
    # There is an exception, when input circuit does NOT have a unique solution
    except np.linalg.LinAlgError:
        raise ValueError("Input circuit does NOT have a unique solution")
    
    # Adding all the solutions to list of voltages and currents through these voltages.
    for i in range(len(variables)):
        if i == 0:
            voltages['GND'] = 0
        elif i < len(nodes):
            voltages[variables[i]] = round(solutions[i-1][0],4)
        else:
            currents[variables[i]] = round(solutions[i-1][0],4)

    return (voltages, currents)

voltages, currents = evalSpice('c:\\Users\\prajv\\OneDrive\\Documents\\Prajwal_Learns\\College\\EE2703 APL\\Week3\\Weekly_Assignment\\a2-spice\\testdata\\test_custom.ckt')
