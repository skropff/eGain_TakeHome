import csv
import sys

try:   
    file = input("Welcome to this troubleshooting chatbot! Each row in your file will be referred to by this chatabot based on the amount of lines preceding it. (i.e. the first line will be referred by this chatbot as line 0. Please enter the troubleshooting file name: ")
    file = file.strip()
    fd = open(file, mode='r')
except FileNotFoundError:
    sys.exit("The file does not exist in your current directory.")
except PermissionError:
    sys.exit("This program does not have permission to read this file. ")

reader = csv.reader(fd)

#Each row will have the state, the current event, the new state given the old state and the current event, and possibly an optional closing message

row_count = 0
graph = {}

start_detected = False

for row in reader:

    if len(row) == 0 or len(row) == 1:
        row_count = row_count + 1
        continue
    elif len(row) != 4 and len(row) != 3:
        sys.exit("Row " + str(row_count) + " has " + str(len(row)) + " columns instead of 4 or 3. Either make this row empty or increase the column count to 3 or 4. ")
        
    stripped_first_element = "".join((row[0]).split())
    
    stripped_third_element = "".join((row[2]).split())
    
    row[2] = stripped_third_element
        
    graph[(stripped_first_element, row[1])] = tuple(row[i] for i in range(2, (len(row)))) #(row[2], row[3])
    
    """
    if len(row) == 4 and stripped_third_element != "_":
        sys.exit("There are four elements in row " + str(row_count) + ", yet the third element is not _.")
    """
    
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
        #print(f"{first}, {current_state}, {first == current_state}")
    
    if path_found == False:
        sys.exit(f"No path was found here for current_state {current_state}. ")

clean_up("start")

state = "start"

while True:
    print("Which of these events are happening: ")
    
    keys_list = graph.keys()
    
    filtered_list = [t[1] for t in keys_list if t[0] == state]
    
    
    for i in range(len(filtered_list)):
        print(f"{i}: {filtered_list[i]}")
    
    
    while True:
        try:    
            raw_input = input("")
            converted_input = int("".join(raw_input.split()))
            if converted_input < 0:
                raise ValueError
            next1 = graph[(state, filtered_list[converted_input])]
            break
        except ValueError:
            print("You did not enter a valid non-negative integer. Please enter a valid input. ")
        except IndexError:
            print("You did not pick one of the valid options. Please enter a valid input. ")
    
    
    if next1[0] == "_":
        sys.exit(next1[1])
    
    state = next1[0]
    
    