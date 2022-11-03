# importa bibliotecas
import csv 
import matplotlib.pyplot as plt
from numpy import double
import matplotlib
matplotlib.style.use('ggplot')

circuitos = ['AAA  0100','AAA  0101','AAA  0102','AAA  0103','AAA  0104','AAA  0105','AAA  0106','AAA  0107',
'AAA  0108','AAA  0109','AAA  0110','AAA  0111','AAA  0112','AAA  0113','AAA  0114','AAA  0115'] # circuitos a serem analisados

for circ in circuitos: #cria listas vazias para as variáveis dos circuitos
    list_circ_mes = []
    list_circ_total = []
    list_circ_ipts = []  
    list_circ_fe = []
    list_circ_cobre = []
    list_circ_ppt = []

    with open('RedeEstudoTCC.csv', encoding='utf-8-sig') as arq: #carrega o arquivo csv a ser lido
        reader = csv.reader(arq, delimiter=';') #separa as informações do arquivo com ";"
        for line in reader: 
            tipo = line[0] #adiciona a coluna meses à variável tipo
            if tipo == 'Meses': 
                continue
            
            if circ == line[1]: #confere se os circuitos são iguais ao código do csv  
                list_circ_mes.append(line[0])  # alimennta as listas vazias com as informações da coluna 1
                list_circ_total.append(float(line[2].replace(',', '.'))) # alimennta as listas vazias com as informações da coluna 3
                list_circ_ipts.append(float(line[3].replace(',', '.')))    # alimennta as listas vazias com as informações da coluna 4                                              
                list_circ_fe.append(float(line[6].replace(',', '.')))  # alimennta as listas vazias com as informações da coluna 7
                list_circ_cobre.append(float(line[5].replace(',', '.')))  # alimennta as listas vazias com as informações da coluna 6
                list_circ_ppt.append(float(line[4].replace(',', '.'))) 
                
    plt.rcParams["figure.figsize"] = [14.00, 7.00]  # determina altura e largura da imagem a ser gerada 
    fig, ax = plt.subplots() # função para gerar gráficos
    
    #gráfico perdas totais e %IPTS

    ax.set_title(circ) # título do gráfico será o circuito
    ax.plot(list_circ_mes, list_circ_total, color='red', marker='x') #gera um gráfico de mês por energia total 
    ax.set_xlabel('Meses', fontsize=14)    
    ax.set_ylabel('Total (MWh)', color='red', fontsize=14) 
    ax2 = ax.twinx() #cria uma segunda escala em um mesmo gráfico 
    ax2.plot(list_circ_mes, list_circ_ipts, color="blue",marker="x") #gera um gráfico de mês por energia índice de perdas técnicas por segmento 
    ax2.set_ylabel("IPTS (%)", color="blue", fontsize=14) 
    ax.grid() 
    fig.savefig(f'TotalePorSegmento/{circ}.png', dpi=100)  #salva as imagens em uma pasta no computador

    #gráfico perdas próprias    

    fig1, ax3 = plt.subplots() 
    ax3.set_title(circ) # título do gráfico será o circuito
    ax3.set_xlabel('Meses', fontsize=14)
    ax3.plot(list_circ_mes, list_circ_ppt, color="blue",marker="x") #gera um gráfico de mês por perda própria
    ax3.set_ylabel("perda própria (%)", color="blue", fontsize=14) 
    ax3.grid() 
    fig1.savefig(f'PerdasProprias/{circ}.png', dpi=100)   #salva as imagens em uma pasta no computador 

    #gráfico perdas no ferro e cobre de transformadores 

    fig2, ax4 = plt.subplots() 
    ax4.set_title(circ) # título do gráfico será o circuito
    ax4.plot(list_circ_mes, list_circ_fe, color='red', marker='x')  #gera um gráfico de mês por energia injetada
    ax4.set_xlabel('Meses', fontsize=14)
    ax4.set_ylabel('ferro', color='red', fontsize=14)
    ax5 = ax4.twinx()
    ax5.plot(list_circ_mes, list_circ_cobre, color="blue",marker="x") #gera um gráfico de mês por perda própria
    ax5.set_ylabel("cobre", color="blue", fontsize=14) 
    ax5.grid() 
    fig2.savefig(f'PerdasFerroeCobre/{circ}.png', dpi=100)   #salva as imagens em uma pasta no computador 