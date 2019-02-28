import os

for x in range(52, 90):
    cl = "abyss-pe k=%d v=-v name=carlos_abyss%d lib='pea' mp='mpa' pea='paired.R1.fastq paired.R2.fastq' mpa='matepair10kb.R1.fastq matepair10kb.R2.fastq'" % (x,x)
    print(cl)
    os.system(cl)
