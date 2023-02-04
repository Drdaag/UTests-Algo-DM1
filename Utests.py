# Special Python function to load module with its file name
from importlib.machinery import SourceFileLoader

# My handout
myfile = "NAME OF THE FILE.py"
# Load module. Same result as "import mycode"
mycode = SourceFileLoader('mycode', myfile).load_module()

print("---Anti-bug---")


# Constructeur :
test = ("[OK]" if "[None]" == str(mycode.Heap()) else "-----------NO")
print(f"Constructeur : {test}")
if(test == "-----------NO"):
    print("[None] =",mycode.Heap())
    print()

print("\n---------heappush---------")

#heappush_vide
H2 = mycode.Heap()
mycode.heappush(H2, "newelt", 42)

tru_val = "[None, (42, 'newelt')]"
test = ("[OK]" if tru_val == str(H2) else "-----------NO")
print(f"heappush_vide : {test}")
if(test == "-----------NO"):
    print(tru_val," = ", H2, sep="")
    print()


#heappush_non_vide
H = [None, (2, 'A'), (12, 'C'), (10, 'B'), (24, 'I'), (16, 'E'), (14, 'D'), (18, 'F'), (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H')]
mycode.heappush(H, 'N', 5)

tru_val = "[None, (2, 'A'), (12, 'C'), (5, 'N'), (24, 'I'), (16, 'E'), (14, 'D'), (10, 'B'), (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H'), (18, 'F')]"
test = ("[OK]" if str(H) == tru_val else "-----------NO")
print(f"heappush_non_vide : {test}")
if(test == "-----------NO"):
    print(tru_val ," =\n", H, sep="")
    print()

print("\n---------heappop---------")

#heappop_non_vide
tmp = mycode.heappop(H)
tru_val = "(2, 'A')"
test = ("[OK]" if tru_val == str(tmp) else "-----------NO")
print(f"heappop_non_vide_return : {test}")
if(test == "-----------NO"):
    print(tru_val, " = ",tmp, sep="")
    print() 

tru_val = "[None, (5, 'N'), (12, 'C'), (10, 'B'), (24, 'I'), (16, 'E'), (14, 'D'), (18, 'F'), (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H')]" 
test = ("[OK]" if tru_val == str(H) else "-----------NO")
print(f"heappop_non_vide_liste : {test}")
if(test == "-----------NO"):
    print(tru_val," = \n", H, sep="")
    print() 


#heappop_vide
H2 = mycode.Heap()
try:
    mycode.heappop(H2)
except Exception:
    print("heappop_vide : [OK]")
except :
    print("heappop_vide : -----------NO")
    print()

print("\n---------isheap---------")

#isheap
tmp = mycode.isheap(H)
tru_val = True
test = ("[OK]" if tru_val == tmp else "-----------NO")
print(f"isheap_non_vide : {test}")
if(test == "-----------NO"):
    print(tru_val, " = ",tmp, sep="")
    print()

#isheap_vide   
tmp = mycode.isheap([None])
tru_val = True
test = ("[OK]" if tru_val == tmp else "-----------NO")
print(f"isheap_vide : {test}")
if(test == "-----------NO"):
    print(tru_val, " = ",tmp, sep="")
    print()
    
#isheap_False   
tmp = mycode.isheap([None, (3, 'A'), (2, 'B'), (1, 'C')])
tru_val = False
test = ("[OK]" if tru_val == tmp else "-----------NO")
print(f"isheap_False : {test}")
if(test == "-----------NO"):
    print(tru_val, " = ",tmp, sep="")
    print()
    
print("\n---------heapsort---------")   
    
#heapsort_sort
L = [('A', 20), ('B', 5), ('C', 10), ('D', 12), ('E', 15), ('F', 8), ('G', 2), ('H', 6), ('I', 2), ('J', 9)]
tmp = mycode.heapsort(L)
tru_val = "[('I', 2), ('G', 2), ('B', 5), ('H', 6), ('F', 8), ('J', 9), ('C', 10), ('D', 12), ('E', 15), ('A', 20)]"
tru_val2 = "[('G', 2), ('I', 2), ('B', 5), ('H', 6), ('F', 8), ('J', 9), ('C', 10), ('D', 12), ('E', 15), ('A', 20)]"
test = ("[OK]" if (tru_val == str(tmp) or tru_val2 == str(tmp)) else "-----------NO")
print(f"heapsort_sort : {test} but is the place matter for the same value ?")
if(test == "-----------NO"):
    print(tru_val, " = \n",tmp, sep="")
    print("[OR]")
    print(tru_val2, " = \n",tmp, sep="")
    print()


# heapsort_nochange
tru_val = "[('A', 20), ('B', 5), ('C', 10), ('D', 12), ('E', 15), ('F', 8), ('G', 2), ('H', 6), ('I', 2), ('J', 9)]"
test = ("[OK]" if (tru_val == str(L)) else "-----------NO")
print(f"heapsort_nochange : {test}")
if(test == "-----------NO"):
    print(tru_val, " = \n",L, sep="")
    print()
    
#heapsort_vide
L = []
tmp = mycode.heapsort(L)
tru_val = "[]"
test = ("[OK]" if (tru_val == str(tmp)) else "-----------NO")
print(f"heapsort_vide : {test}")
if(test == "-----------NO"):
    print(tru_val, " = \n",tmp, sep="")
    print()
