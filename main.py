import util
import permuta

curso = util.load_cadeira('cadeiras.txt')
cadeiras = util.filtra_permutacoes_por_horario_ate(curso,4)
arranjos = cadeiras

#Para adicionar um fitro descomentar a linha desejada

#arranjos = util.filtra_permutacoes_por_dia(cadeiras,util.SEG)
#arranjos = util.filtra_permutacoes_por_dia(cadeiras,util.SEG,True)
#arranjos = util.filtra_permutacoes_por_dia(arranjos,util.TER)
#arranjos = util.filtra_permutacoes_por_dia(arranjos,util.TER,True)
arranjos = util.filtra_permutacoes_por_dia(cadeiras,util.QUA)
#arranjos = util.filtra_permutacoes_por_dia(cadeiras,util.QUA,True)
#arranjos = util.filtra_permutacoes_por_dia(arranjos,util.QUI)
#arranjos = util.filtra_permutacoes_por_dia(arranjos,util.QUI,True)
#arranjos = util.filtra_permutacoes_por_dia(cadeiras,util.SEX)
#arranjos = util.filtra_permutacoes_por_dia(cadeiras,util.SEX,True)
#arranjos = util.filtra_permutacoes_por_dia(arranjos,util.SAB)
arranjos = util.filtra_permutacoes_por_dia(arranjos,util.SAB,True)

#arranjos = util.filtra_permutacoes_por_codigo(arranjos,'14112')#metodologia aplicada
#arranjos = util.filtra_permutacoes_por_codigo(arranjos,'14112',True)#metodologia aplicada
#arranjos = util.filtra_permutacoes_por_codigo(arranjos,'04341')
#arranjos = util.filtra_permutacoes_por_codigo(arranjos,'28009')#Pratica_ensino_2
#arranjos = util.filtra_permutacoes_por_codigo(arranjos,'28009',True)#Pratica_ensino_2
#arranjos = util.filtra_permutacoes_por_codigo(arranjos,'28008')#Pratica_ensino_1
#arranjos = util.filtra_permutacoes_por_codigo(arranjos,'28008',True)#Pratica_ensino_1
#arranjos = util.filtra_permutacoes_por_codigo(arranjos,'04304')#produção de texto
#arranjos = util.filtra_permutacoes_por_codigo(arranjos,'06506')#algebra linear
#arranjos = util.filtra_permutacoes_por_codigo(arranjos,'06243')#estatistica exploratória
#arranjos = util.filtra_permutacoes_por_codigo(arranjos,'14324',True)#interacao homen maquina
#arranjos = util.filtra_permutacoes_por_codigo(arranjos,'06226')#engenharia de software
#arranjos = util.filtra_permutacoes_por_codigo(arranjos,'06215')#banco de dados //obrigatória
arranjos = util.filtra_permutacoes_por_codigo(arranjos,'05498',True)#Educação brasileira funcionamento
#arranjos = util.filtra_permutacoes_por_codigo(arranjos,'14063',True)
#arranjos = util.filtra_permutacoes_por_codigo(arranjos,'14063',True)#Circuitos_digitais

util.imprime_cadeiras(arranjos,True)
print('Total de possibilidades: ',arranjos.__len__())
