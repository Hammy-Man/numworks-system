print("Choose solver\n1: Area Solver\n2: Area Sector Solver\n3: Reverse Area Solver\n4: Reverse Area Sector Solver")
i = int(input("\nInput:"))
l = ["carea","sec","rarea","rsec"]
m = __import__(l[i-1])