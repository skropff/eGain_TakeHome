import csv

try:   
    file = input("Please enter the troubleshooting file name: ")
    fd = open(file, mode='r')
except FileNotFoundError:
    sys.exit("The file does not exist in your current directory.")

reader = csv.reader(fd)

#Each row will have the state, the current event, the new state given the old state and the current event, and possibly an optional closing message

row_count = 0
graph = {}

start_detected = False

for row in reader:

    if len(row) != 4 and len(row) != 3:
        sys.exit("Row " + str(row_count) + " has " + str(len(row)) + " columns instead of 4 or 3.")
        
    stripped_first_element = "".join((row[0]).split())
        
    graph[(stripped_first_element, row[1])] = tuple(row[i] for i in range(2, (len(row)))) #(row[2], row[3])
    
    stripped_third_element = "".join((row[2]).split())
    
    if len(row) == 4 and stripped_third_element != "_":
        sys.exit("There are four elements in row " + str(row_count) + ", yet the third element is not _.")
    
    row_count = row_count + 1
    
    """
    if stripped_first_element == "start" and start_detected == False:
        start_detected = True
    elif stripped_first_element == "start" and start_detected == True:
        sys.exit("Two start elements detected in the table.")
    """

#Ensure that the graph is complete and that there are no issues with the graph

def clean_up(current_state):
    if current_state == "_":
        return
    
    path_found = False
    
    for (first, second) in graph:
        if first == current_state:
            path_found = True
            clean_up(graph[(first, second)][0])
    
    if path_found = False:
        sys.exit("No path was found here.")

clean_up("start")

state = "start"

while True:
    print("Which of these events are happening: ")
    
    keys_list = graph.keys()
    
    filtered_list = [t[1] for t in keys_list if t[0] == state]
    
    
    for i in range(len(filtered_list)):
        print(f"{i}: {filtered_list[i]}")
    
    raw_input = input("")
    converted_input = int("".join(raw_input.split()))
    
    next1 = graph[(state, filtered_list[converted_input])]
    
    if next1[0] == "_":
        sys.exit(next1[1])
    
    state = next1[0]
    
    