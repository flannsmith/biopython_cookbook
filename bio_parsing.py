from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

#read in data from fasta file
# for seq_record in SeqIO.parse('ls_orchid.fasta.rtf', "fasta"):
#     print(seq_record.id)
#     print(repr(seq_record.seq))
#     print(len(seq_record))

my_seq = Seq("AGTACACTGGT", IUPAC.unambiguous_dna)
print(my_seq.alphabet)

my_prot = Seq("AGTACACTGGT", IUPAC.protein)
print(my_prot)

# for index, letter in enumerate(my_seq):
#     print("%i %s" % (index,letter))

#print(len(my_seq))
print((my_seq[0]))

#count occurrence of letters AA in sequence
print(Seq("AAAA").count("AA"))

print(my_seq.count("G"))

#calculate GC percentage
100 * float(my_seq.count("G") + my_seq.count("C")) / len(my_seq)

from Bio.SeqUtils import GC
my_seq_2 = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC", IUPAC.unambiguous_dna)
print(GC(my_seq_2))


print(my_seq_2[0::3])

#nucleotide sequences and reverse complements
my_seq3 = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC", IUPAC.unambiguous_dna)
#print(my_seq3.complement())
#print(my_seq3.reverse_complement())

#What is the difference between complement and reverse complement?

#To reverse a Seq object or string: slice it with- 1
print(my_seq3[::-1])

protein_seq = Seq("EVRNAK", IUPAC.protein)

#protein_seq.complement()
#print(protein_seq)
#Error: proteins do not have complements! 

#Transcription



