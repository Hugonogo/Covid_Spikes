import sys
import re

def lerSequence(arquivo):
    arq = open(arquivo, "r") 
    linha = arq.read()
    linha = list(linha.rstrip())
    linha.insert(0, '-')
    return(linha)
def lerMutations(arquivo):
    arq = open(arquivo, "r")
    linha = arq.read()
    linha = linha.rstrip()
    mut = linha.split(', ')
    
    return(mut)
def subistituir(lista, amino1, pos, amino2 ):
    if (lista[pos] != amino1):
        print(f"A posição {pos} não conten aminoácido {amino1}")
    else:
        lista[pos] = amino2

def substituicao(lista, mut):
    for i in mut:
        if (i[0:3] != "del" and i[0:3] != "ins"):
            amino1 = i[0]
            amino2 = i[-1]
            pos = int(i[1:-1])
            subistituir(lista, amino1, pos, amino2)   

def delecao(lista, mut):
        for i in mut:
            if (i[0:3] == "del"):
                i = i.lstrip("del")
                temp = i.split("-")
                pos1 = int(temp[0])
                pos2 = int(temp[0])
                if(len(temp)> 1):
                    pos2 = int(temp[1])
                for p in range(pos1, pos2):
                    lista.pop(p)

def inserir(lista, mut):
    for i in range(len(mut)-1, -1, -1):
        if (mut[i][0:3] == "ins"):
            m = mut[i].lstrip("ins")
            pos = re.search("[\d]+", m)
            pos = int(pos.group())
            seq = re.search("[A-Z]+", m)
            seq = list(seq.group())
            seq.reverse()
            for a in seq:
                lista.insert(pos, a)
            
if len(sys.argv) != 3:
    print("USAGE: python3 file.py <sequancias> <mutacoes>")
    exit()
sequencia = lerSequence(sys.argv[1])
mutacao = lerMutations(sys.argv[2])
sequencia_mut = sequencia.copy()

substituicao(sequencia_mut, mutacao)
delecao(sequencia_mut, mutacao)
inserir(sequencia_mut, mutacao)
print("Sequência Original: ")
for i in range(0, len(sequencia)):
    print(f" [{i}: {sequencia[i]}]", end="")

print("\nSequência Mutada: ")
for j in range(0, len(sequencia_mut)):
    print(f" [{j}: {sequencia_mut[j]}]", end="")



