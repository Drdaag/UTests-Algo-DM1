# Special Python function to load module with its file name
from importlib.machinery import SourceFileLoader
from heapq import *
import random
random.seed()

# My handout
myfile = "NAME OF FILE.py"
# Load module. Same result as "import mycode"
mycode = SourceFileLoader('mycode', myfile).load_module()

def simple_check(name, tru, val):
    test = ("[OK]" if tru == val else "-----------NO")
    print(f"{name} : {test}")
    if(test == "-----------NO"):
        print(f"{tru} =\n{val}")
        print()

print("---Anti-bug---")


# Constructeur :

simple_check("Constructeur", [None], mycode.Heap())

# test = ("[OK]" if "[None]" == str(mycode.Heap()) else "-----------NO")
# print(f"Constructeur : {test}")
# if(test == "-----------NO"):
#     print("[None] =",mycode.Heap())
#     print()

print("\n---------heappush---------")

#heappush_vide
H2 = mycode.Heap()
mycode.heappush(H2, "newelt", 42)

simple_check("heappush_vide", [None, (42, 'newelt')], H2)


#heappush_non_vide
H = [None, (2, 'A'), (12, 'C'), (10, 'B'), (24, 'I'), (16, 'E'), (14, 'D'), (18, 'F'), (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H')]
mycode.heappush(H, 'N', 5)

tru_val = [None, (2, 'A'), (12, 'C'), (5, 'N'), (24, 'I'), (16, 'E'), (14, 'D'), (10, 'B'), (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H'), (18, 'F')]
simple_check("heappush_non_vide", tru_val, H)


#heappush_multiple_simple
H2 = mycode.Heap()
val = [None, (5, 'N'), (12, 'C'), (10, 'B'), (24, 'I'), (16, 'E'), (14, 'D'), (18, 'F'), (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H')]
leng = len(val)
for i in range(1, leng):
    mycode.heappush(H2, val[i][1], val[i][0])

tru_val = [None, (5, 'N'), (12, 'C'), (10, 'B'), (24, 'I'), (16, 'E'), (14, 'D'), (18, 'F'), (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H')]
simple_check("heappush_multiple_simple", tru_val, H2)

    
#heappush_multiple_complexe
H2 = mycode.Heap()
val = [(2, 'A'), (22, 'H'), (22, 'F'), (3, 'B'), (22, 'J'), (5, 'C'), (10, 'G'), (18, 'D'), (33, 'I'), (15, 'E')]
leng = len(val)
for i in range(leng):
    mycode.heappush(H2, val[i][1], val[i][0])

tru_val = [None, (2, 'A'), (3, 'B'), (5, 'C'), (18, 'D'), (15, 'E'), (22, 'F'), (10, 'G'), (22, 'H'), (33, 'I'), (22, 'J')]
simple_check("heappush_multiple_complexe", tru_val, H2)

print("\n---------heappop---------")

#heappop_non_vide
H = [None, (2, 'A'), (12, 'C'), (5, 'N'), (24, 'I'), (16, 'E'), (14, 'D'), (10, 'B'), (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H'), (18, 'F')]
tmp = mycode.heappop(H)
tru_val = (2, 'A')
simple_check("heappop_non_vide_return", tru_val, tmp)

tru_val = [None, (5, 'N'), (12, 'C'), (10, 'B'), (24, 'I'), (16, 'E'), (14, 'D'), (18, 'F'), (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H')]
simple_check("heappop_non_vide_list", tru_val, H)

#heappop_until_empty
H3 = [None, (2, 'A'), (12, 'C'), (10, 'B'), (24, 'I'), (16, 'E'), (14, 'D'), (18, 'F'), (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H')]
H3_res = [None, (2, 'A'), (12, 'C'), (10, 'B'), (24, 'I'), (16, 'E'), (14, 'D'), (18, 'F'), (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H')]
test = ""
indice = 0
while (len(H3) > 1 and test != "-----------NO"):
    H3_res.pop(0)
    tru_val = H3[1]
    tmp = mycode.heappop(H3)
    heappop(H3_res)
    # tmp3 = list(H3)
    # tmp3.pop(0)
    H3_res.insert(0, None) 
    test = ("[OK]" if tru_val == tmp and H3 == H3_res else "-----------NO")
    # print(H3,"\n" ,H3_res, sep="")
    indice += 1
print(f"heappop_until_empty_return : {test}")
if(test == "-----------NO"):
    print(tru_val, " = ",tmp, sep="")
    print(f"On the {indice}th heappop")
    if(tru_val == tmp):
        print("BUT IS NOT HEAP ANYMORE, YOU MIGHT CHECK YOUR ISHEAP")
        print(H3_res,"\n" ,H3, sep="")
    print() 

H3 = [None, (2, 'A'), (12, 'C'), (10, 'B'), (24, 'I'), (16, 'E'), (14, 'D'), (18, 'F'), (30, 'L'), (26, 'J'), (20, 'G'), (32, 'M'), (28, 'K'), (22, 'H')]
while (len(H3) > 1):
    tru_val = H3[1]
    tmp = mycode.heappop(H3)
tru_val = "[None]" 
test = ("[OK]" if tru_val == str(H3) else "-----------NO")
print(f"heappop_until_empty_liste : {test}")
if(test == "-----------NO"):
    print(tru_val," = \n", H3, sep="")
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
simple_check("isheap_non_vide", tru_val, tmp)

#isheap_vide   
tmp = mycode.isheap([None])
tru_val = True
simple_check("isheap_vide", tru_val, tmp)
    
#isheap_False   
tmp = mycode.isheap([None, (3, 'A'), (2, 'B'), (1, 'C')])
tru_val = False
simple_check("isheap_False", tru_val, tmp)
    
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


# heapsort_nochange_ori
tru_val = [('A', 20), ('B', 5), ('C', 10), ('D', 12), ('E', 15), ('F', 8), ('G', 2), ('H', 6), ('I', 2), ('J', 9)]
simple_check("heapsort_nochange_ori", tru_val, L)
    
#heapsort_vide
L = []
tmp = mycode.heapsort(L)
tru_val = []
simple_check("heapsort_vide", tru_val, tmp)
    
    
# RANDOM TESTS (may be unstable)
print("\n+---------RANDOM TESTS---------+")
print("|    May be unstable, don't    |")
print("|  consider them if the others |")
print("|         are not [OK]         |")
print("+------------------------------+\n")


H = mycode.Heap()
for i in range(10):
    mycode.heappush(H, 'e_'+str(i), random.randint(0, 50))

#isheap_heappush_random
tmp = mycode.isheap(L)
tru_val = True
test = ("[OK]" if (tru_val == tmp) else "-----------NO")
print(f"isheap_heappush_random : {test}")
if(test == "-----------NO"):
    print(tru_val, " = \n",tmp, sep="")
    print(H)
    print()
    
H = mycode.Heap()
for i in range(10):
    mycode.heappush(H, 'e_'+str(i), random.randint(0, 50))

#isheap_heappush_random_long
H = mycode.Heap()
for i in range(50):
    mycode.heappush(H, 'e_'+str(i), random.randint(0, 50))

tmp = mycode.isheap(L)
tru_val = True
test = ("[OK]" if (tru_val == tmp) else "-----------NO")
print(f"isheap_heappush_random_long : {test}")
if(test == "-----------NO"):
    print(tru_val, " = \n",tmp, sep="")
    print(H)
    print()
    
#heappop_random_until_empty
H3 = mycode.Heap()
for i in range(10):
    mycode.heappush(H3, 'e_'+str(i), random.randint(0, 50))
    
H3_res = list(H3)
    
test = ""
indice = 0
while (len(H3) > 1 and test != "-----------NO"):
    H3_res.pop(0)
    tru_val = H3[1]
    tmp = mycode.heappop(H3)
    heappop(H3_res)
    H3_res.insert(0, None)
    test = ("[OK]" if tru_val == tmp and H3_res == H3 else "-----------NO")
    # print(H3,"\n" ,H3_res, sep="")
    indice += 1
print(f"heappop_random_until_empty_return : {test}")
if(test == "-----------NO"):
    print(tru_val, " = ",tmp, sep="")
    print(f"On the {indice}th heappop")
    if(tru_val == tmp):
        print("BUT IS NOT HEAP ANYMORE, YOU MIGHT CHECK YOUR ISHEAP, OR YOUR HEAPPUSH")
        print(H3_res,"\n" ,H3, sep="")
    print() 


H3 = mycode.Heap()
for i in range(10):
    mycode.heappush(H3, 'e_'+str(i), random.randint(0, 50))
    
test = ""
while (len(H3) > 1):
    tru_val = H3[1]
    tmp = mycode.heappop(H3)
tru_val = "[None]" 
test = ("[OK]" if tru_val == str(H3) else "-----------NO")
print(f"heappop_random_until_empty_liste : {test}")
if(test == "-----------NO"):
    print(tru_val," = \n", H3, sep="")
    print() 
