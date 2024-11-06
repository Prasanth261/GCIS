def tuple_equaity(a_tuple,b_tuple):
    print(a_tuple is b_tuple)
    print(a_tuple == b_tuple)

def main():
    list_a=['a',3,3.0]
    list_b=['a',3,3]

    tupleA=tuple(list_a)
    tupleB=tuple(list_b)

    tuple_equaity(tupleA,tupleB)



main()