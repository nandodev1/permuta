#constantes para a comfiguração da clase Cadeira
SEG = 1
TER = 2
QUA = 3
QUI = 4
SEX = 5
SAB = 6

horario_A = '18:30'
horario_B = '20:10'
horario_C = '8:00'
horario_D = '10:00'


class Cadeira:
    def __init__(self,codigo,nome,periodo,pre_requisitos,tupla_horario_dia):
        self.nome = nome
        self.periodo = periodo
        self.codigo = codigo
        self.pre_requisitos = pre_requisitos
        self.horarios = tupla_horario_dia #Formato hora1 dia1 hora2 dia2

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

def formata_str(str):
    str_saida = ''
    for i in range(str.__len__()-1):
        str_saida += str[i]
    return str_saida

#retira o '#' do inicio da string
def retira_comentario(str):
    str_descomentada = ''
    for i in range(1,str.__len__()):
        str_descomentada += str[i]
    return str_descomentada

#recebe um arquivo contendo as cadeiras e devolve uma tupla de cadeiras
def load_cadeira(cadeiras):
    cadeiras_tmp = []
    cadeiras = open(cadeiras)
    for i in cadeiras:
        i = formata_str(i)
        primeiro_caracter = i[0]
        if primeiro_caracter != '#':
            dados_cadeiras = i.split(' ')
            cadeiras_tmp.append(Cadeira(dados_cadeiras[0],dados_cadeiras[1],dados_cadeiras[2],
                                    dados_cadeiras[3],(dados_cadeiras[4],dados_cadeiras[5],
                                    dados_cadeiras[6],dados_cadeiras[7])))
    return cadeiras_tmp

def ha_choque_horarios(cadeira_1,cadeira_2):
    if cadeira_1.horarios[0] == cadeira_2.horarios[0]:
        if cadeira_1.horarios[1] == cadeira_2.horarios[1]:
            return True
    else:
        if cadeira_1.horarios[0] == cadeira_2.horarios[2]:
            if cadeira_1.horarios[1] == cadeira_2.horarios[3]:
                return True
    if cadeira_1.horarios[2] == cadeira_2.horarios[0]:
        if cadeira_1.horarios[3] == cadeira_2.horarios[1]:
            return True
    else:
        if cadeira_1.horarios[2] == cadeira_2.horarios[2]:
            if cadeira_1.horarios[3] == cadeira_2.horarios[3]:
                return True
    return False

def int_para_dia(dia_int):
    dia_int = int(dia_int)
    if dia_int == SEG:
        return 'SEG'
    if dia_int == TER:
        return 'TER'
    if dia_int == QUA:
        return 'QUA'
    if dia_int == QUI:
        return 'QUI'
    if dia_int == SEX:
        return 'SEX'
    if dia_int == SAB:
        return 'SAB'

def filtra_dias_ocupados_cadeira(cadeira):
    dias_ocupados = []
    dia_1 = int_para_dia(cadeira.horarios[1])
    dia_2 = int_para_dia(cadeira.horarios[3])
    if not dias_ocupados.__contains__(dia_1):
        dias_ocupados.append(dia_1)
    if not dias_ocupados.__contains__(dia_2):
        dias_ocupados.append(dia_2)
    return dias_ocupados


def filtra_dias_ocupados_arranjos(arranjos):
    dias_ocupados = []
    for i in arranjos:
        dias_cadeira = filtra_dias_ocupados_cadeira(i)
        for d_c in dias_cadeira:
            if not dias_ocupados.__contains__(d_c):
                dias_ocupados.append(d_c)
    return dias_ocupados

def imprime_cadeiras(cadeiras, exibi_horarios_dias = False):
    print('+==============================================================================================')
    for i in cadeiras:
        for j in i:
            if exibi_horarios_dias:
                dia_1 = int_para_dia(j.horarios[1])
                horario_1 = (j.horarios[0],dia_1)
                dia_2 = int_para_dia(j.horarios[3])
                horario_2 = (j.horarios[2],dia_2)
                print('| '+ j.nome, '-- Periodo:', j.periodo + 'º -- Horários: ',horario_1, horario_2)
            else:
                print(j.nome,' Periodo:', j.periodo + 'º')
        filtro = filtra_dias_ocupados_arranjos(i)
        print('| Dias: ', filtro,' Quant. dias: ',len(filtro))
        imprime_arranjo_semana(i)
        print('+==============================================================================================')

def filtra_arranjo_por_horario(arranjo):
    for indice_cadeira in range(arranjo.__len__()):
        for indice_cadeira_tmp in range(indice_cadeira + 1,arranjo.__len__()):
            if ha_choque_horarios(arranjo[indice_cadeira],arranjo[indice_cadeira_tmp]):
                return None
    return arranjo

def filtra_permutacoes_por_horario(permutacoes):
    filtradas = []
    for indice_cadeira in range(permutacoes.__len__()):
        arranjo_teste = filtra_arranjo_por_horario(permutacoes[indice_cadeira])
        if arranjo_teste != None:
            filtradas.append(arranjo_teste)
    return filtradas

def filtra_arranjo_por_dia(arranjo,dia,incluir = False):
    for cadeira in arranjo:
        if cadeira.horarios[1] == str(dia) or \
                cadeira.horarios[3] == str(dia):
                if not incluir:
                    return None
                else:
                    return arranjo
    if not incluir:
        return arranjo
    else:
        return None

def filtra_permutacoes_por_dia(permutacoes,dia, incluir = False ):
    filtradas = []
    for indice_cadeira in range(permutacoes.__len__()):
        arranjo_teste = filtra_arranjo_por_dia(permutacoes[indice_cadeira],dia,incluir)
        if arranjo_teste != None:
            filtradas.append(arranjo_teste)
    return filtradas

def filtra_arranjo_por_codigo(arranjo, codigo, incluir = False):
    for cadeira in arranjo:
        if cadeira.codigo == str(codigo):
                if not incluir:
                    return None
                else:
                    return arranjo
    if not incluir:
        return arranjo
    else:
        return None

def filtra_permutacoes_por_codigo(permutacoes, codigo, incluir = False):
    filtradas = []
    for indice_cadeira in range(permutacoes.__len__()):
        arranjo_teste = filtra_arranjo_por_codigo(permutacoes[indice_cadeira], codigo, incluir)
        if arranjo_teste != None:
            filtradas.append(arranjo_teste)
    return filtradas



def preenche_calendario(calendario,cadeira):
    #convenções
    # se 0 esta live o dia
    # se 1 apenas primeiro horário ocupado
    # se 2 apenas segundo horário ocupado
    # se 3 primeiro e segundo horário ocupado

    horario_amostra = cadeira.horarios
    dia_1 = horario_amostra[1]
    dia_2 = horario_amostra[3]

    calendario_dia_1 = calendario[dia_1]
    calendario_dia_2 = calendario[dia_2]

def cadeiras_calendario(arranjo):
    calendario = []
    for cadeira in arranjo:
        print(cadeira.nome)
    return calendario
    
def filtra_permutacoes_por_horario_ate(curso,ate_quant_cadeiras):
    import permuta
    cadeiras = []
    if ate_quant_cadeiras >= 7 and not cadeiras.__len__() :
        cadeiras = permuta.permutar_7_cadeiras(curso)
        cadeiras = filtra_permutacoes_por_horario(cadeiras)
    if ate_quant_cadeiras >= 6 and not cadeiras.__len__() :
        cadeiras = permuta.permutar_6_cadeiras(curso)
        cadeiras = filtra_permutacoes_por_horario(cadeiras)
    if ate_quant_cadeiras >= 5 and not cadeiras.__len__() :
        cadeiras = permuta.permutar_5_cadeiras(curso)
        cadeiras = filtra_permutacoes_por_horario(cadeiras)
    if ate_quant_cadeiras >= 4 and not cadeiras.__len__() :
        cadeiras = permuta.permutar_4_cadeiras(curso)
        cadeiras = filtra_permutacoes_por_horario(cadeiras)
    if  ate_quant_cadeiras >= 3 and not cadeiras.__len__():
        cadeiras = permuta.permutar_3_cadeiras(curso)
        cadeiras = filtra_permutacoes_por_horario(cadeiras)
    if  ate_quant_cadeiras >= 2 and not cadeiras.__len__():
        cadeiras = permuta.permutar_2_cadeiras(curso)
        cadeiras = filtra_permutacoes_por_horario(cadeiras)
    return cadeiras