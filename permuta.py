
def permutar_7_cadeiras(curso):
    permutacoes = []
    quant_curso = len(curso)
    for i in range(quant_curso):
        for j in range(i,quant_curso):
            if curso[i].codigo != curso[j].codigo:
                for k in range(j,quant_curso):
                    if j != k:
                        for l in range(k,quant_curso):
                            if curso[l].codigo != curso[k].codigo:
                                for m in range(l,quant_curso):
                                    if curso[m].codigo != curso[l].codigo:
                                        for n in range(m,quant_curso):
                                            if curso[n].codigo != curso[m].codigo:
                                                for o in range(n,quant_curso):
                                                    if curso[o].codigo != curso[n].codigo:
                                                        sequencia = (curso[i], curso[j], curso[k], curso[l], curso[m], curso[n], curso[o])
                                                        if not permutacoes.__contains__(sequencia):
                                                            permutacoes.append(sequencia)
    return permutacoes

def permutar_6_cadeiras(curso):
    permutacoes = []
    quant_curso = len(curso)
    for i in range(quant_curso):
        for j in range(i,quant_curso):
            if curso[i].codigo != curso[j].codigo:
                for k in range(j,quant_curso):
                    if j != k:
                        for l in range(k,quant_curso):
                            if curso[l].codigo != curso[k].codigo:
                                for m in range(l,quant_curso):
                                    if curso[m].codigo != curso[l].codigo:
                                        for n in range(m,quant_curso):
                                            if curso[n].codigo != curso[m].codigo:
                                                    sequencia = (curso[i], curso[j], curso[k], curso[l], curso[m], curso[n])
                                                    if not permutacoes.__contains__(sequencia):
                                                        permutacoes.append(sequencia)
    return permutacoes

def permutar_5_cadeiras(curso):
    permutacoes = []
    quant_curso = len(curso)
    for i in range(quant_curso):
        for j in range(i,quant_curso):
            if curso[i].codigo != curso[j].codigo:
                for k in range(j,quant_curso):
                    if j != k:
                        for l in range(k,quant_curso):
                            if curso[l].codigo != curso[k].codigo:
                                for m in range(l,quant_curso):
                                    if curso[m].codigo != curso[l].codigo:
                                        sequencia = (curso[i], curso[j], curso[k], curso[l], curso[m])
                                        if not permutacoes.__contains__(sequencia):
                                            permutacoes.append(sequencia)
    return permutacoes

def enche(i):
    if i < 0:
        return 0
    enche(i -1)
   # print(curso[i])
    return 1

def main(curso):
    enche(curso.__len__()-1)
    return 0

def permutar_4_cadeiras(curso):
    permutacoes = []
    quant_curso = len(curso)
    for i in range(quant_curso):
        for j in range(i,quant_curso):
            if curso[i].codigo != curso[j].codigo:
                for k in range(j,quant_curso):
                    if j != k:
                        for l in range(k,quant_curso):
                            if curso[l].codigo != curso[k].codigo:
                                sequencia = (curso[i],curso[j],curso[k],curso[l])
                                if not permutacoes.__contains__(sequencia):
                                    permutacoes.append(sequencia)
    return permutacoes

def permutar_3_cadeiras(curso):
    permutacoes = []
    quant_curso = len(curso)
    for i in range(quant_curso):
        for j in range(i,quant_curso):
            if curso[i].codigo != curso[j].codigo:
                for k in range(j,quant_curso):
                    if j != k:
                        sequencia = (curso[i],curso[j],curso[k])
                        if not permutacoes.__contains__(sequencia):
                            permutacoes.append(sequencia)
    return permutacoes

def permutar_2_cadeiras(curso):
    permutacoes = []
    quant_curso = len(curso)
    for i in range(quant_curso):
        for j in range(i,quant_curso):
            if curso[i].codigo != curso[j].codigo:
                    sequencia = (curso[i], curso[j])
                    if not permutacoes.__contains__(sequencia):
                        permutacoes.append(sequencia)
    return permutacoes
