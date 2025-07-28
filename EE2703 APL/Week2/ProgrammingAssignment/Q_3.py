import io
def countfruits(msg):
    sfp = io.StringIO(msg)
    d = {}
    s = sfp.readlines()
    # print(s)
    for sentence in s:
        words = sentence.rstrip().split()
        if len(words) < 2:
            continue
        if words[0] not in d.keys():
            d[words[0]] = int(words[1])
        else:
            d[words[0]] += int(words[1])
    return d

msg = """
Apple 3
Orange 5
Banana 4
Apple 7
Apple 2
Banana 3
"""

print(countfruits(msg))