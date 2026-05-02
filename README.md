“start” is used as the starting point in the graph. “\_” is used as a signal to the program that the user has reached an ending point. The program first tries to open the file. If it fails, it reports what happened and terminates. It then proceeds to iterate over every row in the file and construct the dictionary that will be used to represent the graph information. If it fails while constructing the graph, it tells the user what happened. It then recursively calls the clean\_up() function to ensure that if the user starts from “start,” there are no cycles that the user encounters, no situations where two rows have the exact same first column values and the exact same second column values, there is a valid starting point, and there are no dead ends that can be reached if the user starts at “start.” It then proceeds to ask the user what is going on at each step.

I recognize that my code could result in a user forgetting to connect a section of the graph to the “start” graph and the section therefore being unreachable from “start,” but I wish to make the user able to easily remove a section of the graph from the “start” graph without deleting many rows if they decide that it is what they wish to do. 

<img width="866" height="296" alt="Screenshot 2026-05-01 172138" src="https://github.com/user-attachments/assets/507ce81e-3199-4f34-803b-fc931f5ee6df" />

<img width="865" height="80" alt="Screenshot 2026-05-01 171323" src="https://github.com/user-attachments/assets/3247bcc7-9747-489d-8abb-464a7d31161e" />

<img width="857" height="206" alt="Screenshot 2026-05-01 165948" src="https://github.com/user-attachments/assets/087807c3-8b4c-4994-ad9c-8cb430010821" />


