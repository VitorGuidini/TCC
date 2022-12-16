# importa bibliotecas
import csv 
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import pandas as pd
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
    barWidth = 0.25

    df = pd.DataFrame({
        'Meses': list_circ_mes,
        "list_circ_total": list_circ_total,
        "list_circ_ipts": list_circ_ipts,
        "list_circ_ppt" : list_circ_ppt,
        "list_circ_fe" : list_circ_fe,
        "list_circ_cobre" : list_circ_cobre,
    })

    x = np.arange(len(list_circ_mes))
    
    fig, left_ax = plt.subplots()
    
    left_ax.bar(df["Meses"], df["list_circ_total"], color="#6A5ACD", width=-barWidth, align="edge")
    left_ax.set_ylabel('Perda (MWh)', color="#6A5ACD")
    left_ax.set_xlabel("Meses") 
    left_ax.set_facecolor("white")

    right_ax = left_ax.twinx()
    right_ax.bar(df["Meses"], df["list_circ_ipts"], color="#6395ED", width=barWidth, align="edge")
    right_ax.set_ylabel("IPTS (%)", color="#6395ED")

    fig2, left_ax2 = plt.subplots()
    
    left_ax2.bar(df["Meses"], df["list_circ_ppt"], color="#6A5ACD", width=-barWidth, align="edge")
    left_ax2.set_ylabel('PPT (%)', color="#6A5ACD")
    left_ax2.set_xlabel("Meses") 
    left_ax2.set_facecolor("white")
    
    fig3, left_ax3 = plt.subplots()
    
    left_ax3.bar(df["Meses"], df["list_circ_fe"], color="#6A5ACD", width=-barWidth, align="edge")
    left_ax3.set_ylabel('Ferro (MWh)', color="#6A5ACD")
    left_ax3.set_xlabel("Meses") 
    left_ax3.set_facecolor("white")

    right_ax3 = left_ax3.twinx()
    right_ax3.bar(df["Meses"], df["list_circ_cobre"], color="#6395ED", width=barWidth, align="edge")
    right_ax3.set_ylabel("Cobre (MWh)", color="#6395ED")
    
    left_ax3.set_title(f"{circ}")
    left_ax2.set_title(f"{circ}")
    left_ax.set_title(f"{circ}")
    fig3.savefig(f'PerdasFerroeCobre/{circ}.png', dpi=100) 
    fig2.savefig(f'perda técnica circui vs Global (%)/{circ}.png', dpi=100)
    fig.savefig(f'TotalePorSegmento/{circ}.png', dpi=100)
   

   