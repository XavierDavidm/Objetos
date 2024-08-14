# .1 matriz 4x6

#main

M=[]

#primeira linha
linha1=[]
for i in range(0,6):
    elemento=int(input('digite um número inteiro: '))
    linha1.append(elemento)
M.append(linha1)

#segunda linha
linha2=linha1[::-1]
M.append(linha2)

#terceira linha
linha3=[]
for i in range(0,6):
    a=linha1[i]
    b=linha2[i]
    c=a+b
    linha3.append(c)
M.append(linha3)

#quarta linha
linha4=[]
impar=[]
for i in range(0,6):
    e=linha1[i]
    if e%2==0:
        linha4.append(e)
    else:
        impar.append(e)
for i in range(len(impar)):
    e=impar[i]
    linha4.append(e)
M.append(linha4)

#leitor
print('Matriz normal')
for x in range(len(M)):
    for y in range(len(M[0])):
        print(M[x][y], end="\t")
    print()

print('Matriz transposta')
MI=[]
for x in range(len(M[0])):
    novalinha=[]
    for y in range(len(M)):
        novalinha.append(M[y][x])
    MI.append(novalinha)

#leitor final
for x in range(len(MI)):
    for y in range(len(MI[0])):
        print(MI[x][y], end="\t")
    print()

