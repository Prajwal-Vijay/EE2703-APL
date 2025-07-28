import io
from collections import defaultdict

def def_value():
    return 0
    
def circuit_count(msg):
    sfp = io.StringIO(msg)
    s = sfp.readlines()
    d = defaultdict(def_value)
    seen = False
    for sentence in s:
        words = sentence.rstrip().split()
        if len(words) == 0:
            continue
        
        if seen:
            if words[0][0] == '.':
                continue
            if words[0][0] not in d.keys():
                d[words[0][0]] = 1
            else:
                d[words[0][0]] += 1
        
        if words[0] == '.circuit':
            seen = True
        if words[0] == '.end':
            seen = False
    return d

msg = """
This is a test circuit with some junk in front.
.circuit
Vsource n1 GND 10
Isource n3 GND 1
R1 n1 n2 2
R2 n2 n3 5
L3 n2 GND 3
.end
"""

print(circuit_count(msg))