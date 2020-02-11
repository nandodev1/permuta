
def imprime_semana(vetor_semana):
    h1 = [' ',' ',' ',' ',' ',' ',' ']
    h2 = [' ',' ',' ',' ',' ',' ',' ']
    for i in range(len(vetor_semana)):
        if vetor_semana[i] == 1:
            h1[i] = '*'
        if vetor_semana[i] == 2:
            h2[i] = '*'
        if vetor_semana[i] == 3:
            h1[i] = '*'
            h2[i] = '*'
    print('+---------------------------+\n' +
              '| d | s | t | q | q | s | s |\n' +
              '|  ' + str(h1[0]) + '| '+ str(h1[1]) + ' | ' +str(h1[2]) + ' | ' +str(h1[3]) + ' | ' +str(h1[4]) + ' | ' +str(h1[5]) + ' | ' +str(h1[6]) +' |\n' +
              '|  ' + str(h2[0]) + '| '+ str(h2[1]) + ' | ' +str(h2[2]) + ' | ' +str(h2[3]) + ' | ' +str(h2[4]) + ' | ' +str(h2[5]) + ' | ' +str(h2[6]) +' |\n' +
              '+---------------------------+')

def preenche_semana(arranjo):
    semana = [0,0,0,0,0,0,0]
    hora_tmp = ''
    for cadeira in arranjo:
        for horario in cadeira.horarios:
            try:
                dia = int(horario)
                if hora_tmp == '18:30':
                    if semana[dia] == 0:
                        semana[dia] = 1
                    if semana[dia] == 2:
                        semana[dia] = 3
                if hora_tmp == '20:10':
                    if semana[dia] == 0:
                        semana[dia] = 2
                    if semana[dia] == 1:
                        semana[dia] = 3
                if hora_tmp == '08:00':
                    if semana[dia] == 0:
                        semana[dia] = 1
                    if semana[dia] == 2:
                        semana[dia] = 3
                if hora_tmp == '10:00':
                    if semana[dia] == 0:
                        semana[dia] = 2
                    if semana[dia] == 1:
                        semana[dia] = 3
            except:
                hora_tmp = horario
    return semana
 def imprime_arranjo_semana(arranjo):
    imprime_semana(preenche_semana(arranjo))

