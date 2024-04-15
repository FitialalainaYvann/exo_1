prop = []
i = 0
n = int(input("entrer le nombre de votre proposition (entre 1 a 3svp!):"))
if n<=3:
    while i<n:
        var=input("entrer votre {}è proposition(a,b,c): ".format(i))  
        prop.append(var)
        i=i+1
else:print("1 a 3svp! T-T")

print("vos propositions sont {}".format(prop))    
#je vous prie de m'éxcuser pour la suite (c'est le désordre totale mr T-T)
if n == 1:    
    a = prop[0]
    print("prop1 | 7prop1")
    for a in (0,1):
        print(f"{a}     | {not a}")
elif n == 2:
    a = prop[0]
    b = prop[1]
    print("{ a } | {b }   |  {a and b }   |   {a or b }   |   {not a}|   {not b}|")
    for a in (0,1):
        for b in (0,1):
            print(f"{ a }     | {b }      | {a and b }             | {a or b }             | {int(not a)}        | {int(not b)}        |")
elif n == 3:
    a = prop[0]
    b = prop[1]
    c = prop[2]
    print("{ a } |  {b}  |  {c}   |  {a and b or c}   |   {a or b or c}   |   {not a}|   {not b}|   {not c}|")
    for a in (0,1):
        for b in (0,1):
            for c in (0,1):
                print(f"{ a }     | {b }     | {c}      |  {int(a and b or c)}                |   {int(a or b or c)}               |   {int(not a)}      |   {int(not b)}      |   {int(not c)}      |")
    




