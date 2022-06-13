print("Choose Module\n1: Circles \n 2: Quadrilaterals \n3: Triangles \n4: Other")
i = int(input("\nInput:"))
l = ["cir","quad","tri","oth"]
m = __import__(l[i-1])