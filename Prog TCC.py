import csv
import matplotlib.pyplot as plt
from numpy import double

equipamentos = ['EMB  0100','EMB  0101','EMB  0102','EMB  0103','EMB  0104','EMB  0105','EMB  0106','EMB  0107',
'EMB  0108','EMB  0109','EMB  0110','EMB  0111','EMB  0112','EMB  0113','EMB  0114','EMB  0115','MAZ  0100',
'MAZ  0101','MAZ  0102','MAZ  0103','MAZ  0104','MAZ  0105','MAZ  0106','MAZ  0107','MAZ  0108','MAZ  0109',
'MAZ  0110','MAZ  0111','MAZ  0112','MAZ  0113','MAZ  0114','MAZ  0115']

for equip in equipamentos:
    list_equip_mes = []
    list_equip_total = []
    list_equip_ipts = []  
    list_equip_ei = []
    list_equip_pp = []

    with open('Data.csv', encoding='utf-8-sig') as arq:
        reader = csv.reader(arq, delimiter=';')
        for line in reader:
            tipo = line[0]
            if tipo == 'Posicao':
                continue
            
            if equip == line[1]:
                list_equip_mes.append(line[0])
                list_equip_total.append(float(line[2].replace(',', '.')))
                list_equip_ipts.append(float(line[3].replace(',', '.')))  
                list_equip_ei.append(line[4])
                list_equip_pp.append(line[5])                                  
              #  list_equip_ei.append(float(line[4].replace(',', '.')))
              #  list_equip_pp.append(float(line[5].replace(',', '.'))) 

    plt.rcParams["figure.figsize"] = [14.00, 7.00]
  
    fig, ax = plt.subplots()
    
    #gráfico perdas totais e %IPTS
    ax.set_title(equip)
    ax.plot(list_equip_mes, list_equip_total, color='red', marker='x')
    ax.set_xlabel('Meses', fontsize=14)    
    ax.set_ylabel('Total', color='red', fontsize=14)
    ax2 = ax.twinx()
    ax2.plot(list_equip_mes, list_equip_ipts, color="blue",marker="x")
    ax2.set_ylabel("IPTS (%)", color="blue", fontsize=14)
    ax.grid()
  #  ax.annotate("x", (list_equip_mes, list_equip_ipts))
    fig.savefig(f'images/{equip}.png', dpi=100)  

    #gráfico ei e perdas próprias
    fig1, ax3 = plt.subplots()
    ax3.set_title(equip)
    ax3.plot(list_equip_mes, list_equip_ei, color='green', marker='o')
    ax3.set_xlabel('Meses', fontsize=14)
    ax3.set_ylabel('energia injetada', color='green', fontsize=14)
    ax4 = ax3.twinx()
    ax4.plot(list_equip_mes, list_equip_pp, color="blue",marker="o")
    ax4.set_ylabel("perda própria", color="blue", fontsize=14)
    ax3.grid()
  #  ax.annotate("x", (list_equip_mes, list_equip_ipts))
    fig1.savefig(f'energiacircuito/{equip}.png', dpi=100)    