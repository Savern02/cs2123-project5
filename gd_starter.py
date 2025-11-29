# Project 5: starter code
# Edit distance between gene sequences

#### define the data structures to store the steps to turn the source into the target
#### use these lists in your edit_dist() function, do NOT change them here
# source symbol involved in each step
sourceSymbols = []
# target symbol involved in each step
targetSymbols = []
# four possible actions to take in each step i
# actions[i] = 0: step i is keep
# actions[i] = 1: step i is substitution
# actions[i] = 2: step i is insertion
# actions[i] = 3: step i is deletion
actions = []

# Function to print the results of edit distance algorithm
# Do NOT change this function
# The results must be displayed using this function !!!
def display_results(dist):
    print("The edit distance is ", dist)
    print("The number of steps to turn the source into the target gene:", len(actions))
    print("These steps are: ")
    for a, (sc, tc) in zip(actions, zip(sourceSymbols, targetSymbols)):
        if a==0: #match, keeping operation
            print("Keep "+sc+" unchanged")
        elif a==1: #no match, substitute
            print("Modify "+str(sc)+" to "+tc)
        elif a==2: #insertion
            print("Insert "+tc)
        elif a==3: #deletion
            print("Delete "+sc)
    print("Done")    

# Complete this function
# Output: the edit distance between the src and the tgt
# Please also record your edit steps in the three pre-defined lists: sourceSymbols, targetSymbols and actions
def gene_dist(src, tgt):          
    return 0

# Follow each part in the main script to test your functions
# Don't change any statements in the main script! 
if __name__ == "__main__":
    seq1 = "AGTC"
    seq2 = "GCCA"
    seq3 = "AGCTATTC"
    seq4 = "GTTCAACG"

    sourceSymbols.clear()
    targetSymbols.clear()
    actions.clear()
    dist12 = gene_dist(seq1, seq2)
    display_results(dist12)

    print()

    sourceSymbols.clear()
    targetSymbols.clear()
    actions.clear()
    dist34 = gene_dist(seq3, seq4)
    display_results(dist34)

    print()

    # Switch the source and target, and observe the resulting distance and edits
    # Notice any similarities/differences compared with the original order? 
    # Explain the observed similarities and differences
    sourceSymbols.clear()
    targetSymbols.clear()
    actions.clear() 
    dist21= gene_dist(seq2, seq1)
    display_results(dist21)

    print()

    sourceSymbols.clear()
    targetSymbols.clear()
    actions.clear()
    dist43= gene_dist(seq4, seq3)
    display_results(dist43)

