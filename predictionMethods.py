'''
Network based function prediction of candidate genes

This program predicts the functions of unknown proteins in PPI networks.

Author: Ganeshiny Sridharan
Date:4/25/2023
'''


import networkx as nx
import matplotlib.pyplot as plt


'''

Method for making graph objects out of STRING interactions file

Input : Interactions file in a ".tsv" format

Output: Graph object
'''
def createGraphObject(input_file):
    G = nx.Graph()
    with open (input_file, "r") as ppi_file:
        for line in ppi_file:
            if "#" not in line:
                G.add_edge(line.split()[0], line.split()[1])
    return G


'''
Function for outputting the graph details: proteins (nodes) and interations (edges)

'''
def outputGraphData(graph):
    return f"number of proteins = {len(graph.nodes())}", f"number of interactions = {len(graph.edges())}"

    
'''
To read functional annotation files

Input: The ".tsv" file for functional annotations of proteins obtained from STRING

Output: dictionary with keys being the protein and the value being the function

'''
def readSeedList(functional_annot_file):
    protein_functional_annot = {}
    with open (functional_annot_file, "r") as seed_list_file:

        for line in seed_list_file:
            if "#" not in line:
                protein_functional_annot[line.strip("\n").split("\t")[0]] = (line.strip("\n").split("\t")[4])

    return protein_functional_annot


'''
Input: 

Graph G representing the protein-protein interaction network
Seed proteins S with known functions
One function

Output: Candidate genes

Method: Majority Voting Algo

'''

def candidateFunctionSingleMVA(function, graph, functional_annot, threshhold = 6):

    #Create a dictionary for the candidate genes that pass the threshold 
    candidate_genes = {}

    #These are the proteins that are currently annotated for the function
    known_proteins = [k for k, v in functional_annot.items() if v == function]

    #Initialize node voting count
    node_vote = 0

    #Loop through each node in graph
    for node in graph:
        print("Enter1")

    #Check if the node is unknown 
        if node not in known_proteins:
    
    #For each neighbor n of the node 
            for n in graph.neighbors(node):
    
    #Count the neighbors who are known for the function as the vote
                if n in known_proteins:
                    node_vote +=1
    #Apply threshold
            if node_vote >= threshhold:
    
    #Add to dictionary
                candidate_genes[node] = node_vote
    
    #Reset Value
            node_vote = 0
    print(candidate_genes)
    return candidate_genes

'''
Input: 

Graph G representing the protein-protein interaction network
Seed proteins S with known functions
Many functions

Output: Candidate genes

Method: Majority Voting Algo

'''
def candidateFunctionMultipleMVA(function_list, graph, functional_annot, threshhold = 6):
    #Create a dictionary for the candidate genes that pass the threshold 
    candidate_genes = {}

    #These are the proteins that are currently annotated for the function
    known_proteins_multiple = {}

    #Create a dictionary of known
    for func in function_list:
        known_proteins_multiple[func] = [k for k, v in functional_annot.items() if v == func]

    # print(known_proteins_multiple)

    #Intialize dictionary to store all the genes
    all_dict = {}

    #Initialize node voting count
    node_vote = 0

    #Loop through each node in graph
    for node in graph:
    #For each function iteratively
        for func in known_proteins_multiple:

    #Check if the node is unknown
            if node not in known_proteins_multiple[func]:
    
    #For each neighbor n of the node 
                for n in graph.neighbors(node):
    
    #Count the neighbors who are known for the function as the vote
                    if n in known_proteins_multiple[func]:
                        node_vote +=1
    #Populate the all dictionary
                all_dict[f"{node}, {func}"] = node_vote
    #Reset the node value
            node_vote = 0

    # Choose the keys that are above threshold
    # for key in all_dict:
    #     if all_dict[key]>threshhold:
    #         candidate_genes[key] + all_dict[key]
    # print(candidate_genes)        
    return all_dict


# print(candidateFunctionMultipleMVA(sample_graph, dict1, 5, 'POLO box domain superfamily','Domain of unknown function DUF5595', 'Kinesin motor, catalytic domain. ATPase.'))


'''
Input: 

Graph G representing the protein-protein interaction network
Seed proteins S with known functions
One functions

Output: Candidate genes

Method: Hishigaki Method

'''
def candidateFunctionSingleHishigaki(function, graph, functional_annot, threshhold = 1):
    print(type(graph))
    #Create a dictionary for the candidate genes that pass the threshold 

    candidate_genes = {}

    #number of proteins with given function in then-neighborhood
    func_nneighbor_count = 0

    #These are the proteins that are currently annotated for the function
    known_proteins = [k for k, v in functional_annot.items() if v == function]

    #Loop through each node in graph 
    for node in graph:

     #Check if the node is unknown 
        if node not in known_proteins:

    #Calculate expected frequency of the function
            expected_frequency = (len(known_proteins)/len(graph.nodes()))* len([n_count for n_count in graph.neighbors(node)])
            
    #For each neighbor n of the node         
            for n in graph.neighbors(node):
                # print(len([n_count for n_count in graph.neighbors(node)]))
                
    #Count the neighbors who are known for the function as the vote      
                if n in known_proteins:
                    func_nneighbor_count += 1
    #Calculate the prediction score 
            prediction_score_chisq = ((func_nneighbor_count - expected_frequency)**2)/expected_frequency
            func_nneighbor_count = 0

    #Choose the ones above threshhold
            if prediction_score_chisq > threshhold:
                candidate_genes[node] = prediction_score_chisq
        prediction_score_chisq = 0
    return candidate_genes



# print(candidateFunctionSingleHishigaki("Kinesin motor, catalytic domain. ATPase.", sample_graph, dict1))



'''
Input: 

Graph G representing the protein-protein interaction network
Seed proteins S with known functions
Many functions

Output: Candidate genes

Method: Hishigaki Method

'''
def candidateFunctionMultipleHishigaki(functions, graph, functional_annot, threshhold = 1):
    print(type(graph))
    #Create a dictionary for the candidate genes that pass the threshold 
    candidate_genes = {}

    #These are the proteins that are currently annotated for the function
    known_proteins_multiple = {}
    
    #number of proteins with given function in then-neighborhood 
    func_nneighbor_count = 0

    #Loop thorugh the fucntions from the list
    for func in functions:
        known_proteins_multiple[func] = [k for k, v in functional_annot.items() if v == func]
    
    #Loop through each node in graph 
    for node in graph:

    #For each function 
        for func in known_proteins_multiple:
            # print(func)
    
    #Check if the node is unknown 
            if node not in known_proteins_multiple[func]:
    
    #Calculate expected frequency of the function
                expected_frequency = (len(known_proteins_multiple[func])/len(graph.nodes()))* len([n_count for n_count in graph.neighbors(node)])
                
    #For each neighbor n of the node    
                for n in graph.neighbors(node):
                    # print(len([n_count for n_count in graph.neighbors(node)]))
                    
    #Count the neighbors who are known for the function as the vote      
                    if n in known_proteins_multiple[func]:
                        func_nneighbor_count += 1

    #Calculate the prediction score 
                prediction_score_chisq = ((func_nneighbor_count - expected_frequency)**2)/expected_frequency
                # all_dict[f"{node},{func}"] = prediction_score_chisq
                
    #Reset values and adding the vales above threshhold to output
                func_nneighbor_count = 0
                if prediction_score_chisq > threshhold:
                    candidate_genes[f"{node},{func}"] = prediction_score_chisq
            prediction_score_chisq = 0
    return candidate_genes


sample_graph = createGraphObject("string_interactions.tsv")
dict1 = readSeedList("string_functional_annotations.tsv")
# print(candidateFunctionMultipleMVA(['POLO box domain superfamily','Domain of unknown function DUF5595', 'Kinesin motor, catalytic domain. ATPase.'],sample_graph, dict1, 1))