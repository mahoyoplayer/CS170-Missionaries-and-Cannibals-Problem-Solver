# CS170-Missionaries-and-Cannibals-Problem-Solver
Made for CS170 @ UCR. Winter 2026 w/ Eamonn Keogh.

# Run With 
   ```bash
      python main.py
   ```

# Problem
The problem starts with three missionaries and three cannibals on the left side of the river, and the boat also on the left. The number of missionaries can never exceed the number of cannibals at any time or else they will be eaten.

```python
startLeft = Side(3, 3)
startRight = Side(0, 0)
startBoat = "L"  
```

There are four unique solutions to the original version of this problem.

The program can also solve non-original versions of this problem - 
```python
startLeft = Side(5, 3)
startRight = Side(2, 1)
startBoat = "R"  
```
Now, there are 5 missionaries and 3 cannibals on the left side and 2 missionaries and 1 cannibal on the left. The boat starts on the right side rather than the left. 

# Approach
A simple brute-force DFS approach.

# Output for the Original 3,3 Missionary and Cannibal Problem
<img width="875" height="554" alt="image" src="https://github.com/user-attachments/assets/e3af0b64-be61-4239-8ebc-21d5409faa09" />
<img width="531" height="623" alt="image" src="https://github.com/user-attachments/assets/9eceb289-06c3-4b27-879d-6bf1b6a38262" />

