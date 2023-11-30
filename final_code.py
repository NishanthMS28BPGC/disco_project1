import networkx as nx
import random

G=nx.DiGraph()

from networkx.algorithms.flow import shortest_augmenting_path
G.add_node("S")
G.add_node("T")
with open("input_1.txt",'r') as rf:
    courses=rf.readline().split()
    cdc=[];el=[];hde=[]
    for i in courses:
        if "cdc" in i.lower():
            cdc.append(i)
            
        elif "hde" in i.lower():
            hde.append(i)
           
        else: el.append(i)  
    courses=cdc + hde+el
    for i in courses:
        G.add_node(i)
        G.add_edge("S", i, capacity=2)

    prof=rf.readline().split()
    while len(prof)>0:
        G.add_node(prof[0])
        # G.add_edges_from("S",prof[0],{"capacity":int(float(prof[1])*2)})
        G.add_edge(prof[0],"T", capacity=int(float(prof[1])*2))
        for j in prof[2:]:
            G.add_edge( j,prof[0], capacity=2)


        prof=rf.readline().split()
flow_value,flow_dict=nx.maximum_flow(G,"S","T",flow_func=shortest_augmenting_path)


# flow_dict = {'S': {'Professor_1': 1, 'Professor_2': 2, 'Professor_3': 3}, 'T': {}, 'cdc11': {'T': 2}, 'cdc12': {'T': 2}, 'cdc21': {'T': 2}, 'Professor_1': {'cdc11': 1, 'cdc12': 0}, 'Professor_2': {'cdc12': 2, 'cdc21': 0, 'cdc22': 0}, 'cdc22': {}, 'Professor_3': {'cdc11': 1, 'cdc21': 2}}
a=[]

for keys in flow_dict['S'].keys():
        if flow_dict['S'][keys]!=2 :
             flow_dict['S'][keys]=0
             a.append(keys)

for professor, connections in flow_dict.items():
    if professor.startswith('cdc') or professor.startswith('HD') or professor.startswith("el"):
        # for i,j in connections.items():
        #     if j<2:
        #         flow_dict[professor][i]=0
        #         a.append(professor)
        if professor not in a:
            for course, flow in connections.items():
                if  flow> 0 :
                    print(f"{professor}: assigned to {course}: {flow}/2")

print("\n This is 2nd solution")

G.clear()
G.add_node("S")
G.add_node("T")
with open("input_1.txt",'r') as rf:
    courses=rf.readline().split()
    cdc=[];el=[];hde=[]
    for i in courses:
        if "cdc" in i.lower():
            cdc.append(i)
            
        elif "hde" in i.lower():
            hde.append(i)
           
        else: el.append(i)  
    random.shuffle(cdc)
    random.shuffle(hde)  
    random.shuffle(el)
    courses=cdc + hde+el
    for i in courses:
        G.add_node(i)
        G.add_edge("S", i, capacity=2)

    prof=rf.readline().split()
    fixed_part=prof[:2]
    remaining_part=prof[2:]
    random.shuffle(remaining_part)
    prof=fixed_part+remaining_part
    while len(prof)>0:
        G.add_node(prof[0])
        G.add_edge(prof[0],"T", capacity=int(float(prof[1])*2))
        for j in prof[2:]:
            G.add_edge( j,prof[0], capacity=2)


        prof=rf.readline().split()
flow_value,flow_dict=nx.maximum_flow(G,"S","T",flow_func=shortest_augmenting_path)

# print (flow_dict)
# flow_dict = {'S': {'Professor_1': 1, 'Professor_2': 2, 'Professor_3': 3}, 'T': {}, 'cdc11': {'T': 2}, 'cdc12': {'T': 2}, 'cdc21': {'T': 2}, 'Professor_1': {'cdc11': 1, 'cdc12': 0}, 'Professor_2': {'cdc12': 2, 'cdc21': 0, 'cdc22': 0}, 'cdc22': {}, 'Professor_3': {'cdc11': 1, 'cdc21': 2}}

a=[]

for keys in flow_dict['S'].keys():
        if flow_dict['S'][keys]!=2 :
             flow_dict['S'][keys]=0
             a.append(keys)

for professor, connections in flow_dict.items():
    if professor.startswith('cdc') or professor.startswith('HD') or professor.startswith("el"):
        # for i,j in connections.items():
        #     if j<2:
        #         flow_dict[professor][i]=0
        #         a.append(professor)
        if professor not in a:
            for course, flow in connections.items():
                if  flow> 0 :
                    print(f"{professor}: assigned to {course}: {flow}/2")

print("\n This is 3rd solution")

G.clear()
G.add_node("S")
G.add_node("T")
with open("input_1.txt",'r') as rf:
    courses=rf.readline().split()
    cdc=[];el=[];hde=[]
    for i in courses:
        if "cdc" in i.lower():
            cdc.append(i)
            
        elif "hde" in i.lower():
            hde.append(i)
           
        else: el.append(i)  
    random.shuffle(cdc)
    random.shuffle(hde)  
    random.shuffle(el)
    courses=cdc + hde+el
    for i in courses:
        G.add_node(i)
        G.add_edge("S", i, capacity=2)

    prof=rf.readline().split()
    
    while len(prof)>0:
        G.add_node(prof[0])
        G.add_edge(prof[0],"T", capacity=int(float(prof[1])*2))
        for j in prof[2:]:
            G.add_edge( j,prof[0], capacity=2)


        prof=rf.readline().split()
flow_value,flow_dict=nx.maximum_flow(G,"S","T",flow_func=shortest_augmenting_path)

# print (flow_dict)
# flow_dict = {'S': {'Professor_1': 1, 'Professor_2': 2, 'Professor_3': 3}, 'T': {}, 'cdc11': {'T': 2}, 'cdc12': {'T': 2}, 'cdc21': {'T': 2}, 'Professor_1': {'cdc11': 1, 'cdc12': 0}, 'Professor_2': {'cdc12': 2, 'cdc21': 0, 'cdc22': 0}, 'cdc22': {}, 'Professor_3': {'cdc11': 1, 'cdc21': 2}}

a=[]

for keys in flow_dict['S'].keys():
        if flow_dict['S'][keys]!=2 :
             flow_dict['S'][keys]=0
             a.append(keys)

for professor, connections in flow_dict.items():
    if professor.startswith('cdc') or professor.startswith('HD') or professor.startswith("el"):
        # for i,j in connections.items():
        #     if j<2:
        #         flow_dict[professor][i]=0
        #         a.append(professor)
        if professor not in a:
            for course, flow in connections.items():
                if  flow> 0 :
                    print(f"{professor}: assigned to {course}: {flow}/2")


    