from typing import List, Tuple

class Side:
    def __init__(self, m: int, c: int):
        self.m = m
        self.c = c

    def valid(self) -> bool:
        return not (self.m > 0 and self.c > self.m)

    def __hash__(self):
        return hash((self.m, self.c))

    def __eq__(self, other) -> bool:
        if isinstance(other, Side):
            return self.m == other.m and self.c == other.c
        raise RuntimeError(f"Tried to compare Side with obj that was of {type(other)}")

    def empty(self) -> bool:
        return self.m == 0 and self.c == 0

class Scene:
    def __init__(self, left: Side, right: Side, boat: str, history: List[Tuple[int, int]]):
        self.left = left
        self.right = right
        self.boat = boat
        self.history = history

    def __str__(self):
        s = (f"Left: M={self.left.m}, C={self.left.c}" + (", Boat" if self.boat == "L" else ""))
        s +=(f" || Right: M={self.right.m}, C={self.right.c}" + (", Boat" if self.boat == "R" else ""))
        return s

    def valid(self):
        return self.left.valid() and self.right.valid()

    def __hash__(self):
        return hash((self.left, self.right, self.boat))

    def isSolution(self) -> bool:
        # If left is empty, we have moved everyone to the right.
        return self.left.empty()

    def depth(self) -> int:
        return len(self.history)

    def printHistory(self, startLeft, startRight, startBoat: str):
        boat = startBoat
        l_m, l_c, r_m, r_c = startLeft.m, startRight.c, startRight.m, startRight.c

        def helperPlural(t, count):
            if t == "m":
                return "missionary" if count == 1 else "missionaries"
            else:
                return "cannibal" if count == 1 else "cannibals"


        for i, (deltaM, deltaC) in enumerate(self.history):
            print(f"{i+1}. " , end = "")
            crossText = "from the right to left side" if boat == "R" else "from the left to right side"
            if deltaM == 0 and deltaC != 0:
                print(f"{deltaC} {helperPlural("c", deltaC)} crossed {crossText}.")
            elif deltaM != 0 and deltaC != 0:
                print(f"{deltaM} {helperPlural("m", deltaM)} and {deltaC} {helperPlural("c", deltaC)} crossed {crossText}.")
            else:
                print(f"{deltaM} {helperPlural("m", deltaM)} crossed {crossText}.")
            boat = "R" if boat == "L" else "L"
            
startLeft = Side(3,3)
startRight = Side(0, 0)
startBoat = "L" # "L" to start on left, "R" to start on right

totalM = startLeft.m + startRight.m
totalC = startLeft.c + startRight.c

visited = set()
solutions = []
operators = ( (0,1), (0, 2), (1, 1), (1, 0), (2, 0) )


def dfs(scene):
    # Indent
    print(scene.depth() * "   ", end = "")
    
    if scene.isSolution():
        print(f"SOLUTION FOUND - " + str(scene) + " at depth = " + str(scene.depth()))
        solutions.append(scene)
        return

    elif hash(scene) in visited:
        print("REPEAT - " + str(scene))
        return

    
    if not scene.valid():
        print("INVALID - " + str(scene))
    else:
        # Scene is valid.
        visited.add(hash(scene))
        print("VISITING -", scene)

        for deltaM, deltaC in operators:
            m = scene.left.m if scene.boat == "L" else scene.right.m
            c = scene.left.c if scene.boat == "L" else scene.right.c
            m -= deltaM
            c-= deltaC
            if m < 0 or c < 0: continue

            left = Side(m, c) if scene.boat == "L" else Side(totalM - m, totalC - c)
            right = Side(m, c) if scene.boat == "R" else Side(totalM - m, totalC - c)
            history = scene.history + [(deltaM, deltaC)]

            newScene = Scene(left, right, "L" if scene.boat == "R" else "R", history)
            dfs(newScene)        
        visited.remove(hash(scene))

dfs(Scene(startLeft, startRight, startBoat, []))

print("\n\nAnalysis:")
if solutions:
    solutions.sort(key=lambda scene: scene.depth())
    print("Total Unique Solution Count =", len(solutions), "at depths", [scene.depth() for scene in solutions]) 
    print("Lowest Depth of Solution -", min([scene.depth() for scene in solutions]))
    print("\n\n")

    for i, sol in enumerate(solutions):
        print(f"Solution #{i+1}, Cost = {sol.depth()}")
        sol.printHistory(startLeft, startRight, startBoat)
        print("\n\n")
else:
    print("0 solutions found.")

