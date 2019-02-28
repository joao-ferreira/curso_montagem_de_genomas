import os

fs = os.listdir('.')

pref = 'carlos_abyss'
suf = '-stats.tab'

data = {}

for f in fs:
    if f.startswith(pref) and f.endswith(suf):
        linhas = open(f, 'r').readlines()
        num_scaffs = linhas[3].split('\t')[0]
        n50 = linhas[3].split('\t')[5]
        l50 = linhas[3].split('\t')[2]
        knum = f.split(pref)[1].split(suf)[0]
        data[knum] = {}
        data[knum]['scaffs'] = num_scaffs
        data[knum]['n50'] = n50
        data[knum]['l50'] = l50

#print(data)

categories = ""
n50_data = 'n50\t'
l50_data = 'l50\t'
scaf_data = 'scaffolds\t'

for x in range(52, 90):
    ind = str(x)
    categories += ind + '\t'
    n50_data += data[ind]['n50'] + '\t'
    l50_data += data[ind]['l50'] + '\t'
    scaf_data += data[ind]['scaffs'] + '\t'

saida = open('montagens', 'w')
saida.write(categories + '\n' + n50_data + '\n' + l50_data + '\n' + scaf_data + '\n')
