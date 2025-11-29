# cs2123-project5
Topic: this project will use edit distance to compare gene sequences. ACGT represents
four types of bases found in a DNA molecule: adenine (A), cytosine (C), guanine (G) and
thymine (T). A DNA molecule consists of two intertwined strands, with each strand held
together by bonds between the bases. Adenine pairs with thymine, and cytosine pairs
with guanine. The sequence of bases in a portion of a DNA molecule, called a gene,
carries the instructions needed to assemble a protein [1].

#Goal:
gene_dist(src, tgt): the iterative function to compute the edit distance between the
source gene s and the target gene t. This function must traceback on the dictionary (or
2D array) of edit distances to identify the specific steps to turn the source string into
target string.
