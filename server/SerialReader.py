#!/usr/bin/python3.8
import serial
import time
import DbContext as db
from DadosParaPlotarEntity import DadosParaPlotar as Maquina
import datetime



db.DbContext.create_all_tables()
posicao_x = 0
posicao_y = 0
#ser = serial.Serial('COM3')
x = 240
y = 700
#VALUE_SERIAL = 0

id_maquina = input('Digite a identificacao da maquina: ')


#while 1==1:
#    VALUE_SERIAL = ser.readline(29)

#    if b'valorx' in VALUE_SERIAL:
#        x = float(VALUE_SERIAL[21:28].strip())
#        print (" o valor de x é " + str(x))

#    if b'valory' in VALUE_SERIAL :
#        y = float(VALUE_SERIAL[21:28].strip())
#        print (" o valor de y é " + str(y))

maquina = Maquina(periodo = 8, dataEHora = datetime.datetime.now(), posicao_x = x, posicao_y = y,  Id_maquina = id_maquina,)
db.DbContext.add(maquina)
maquina = db.s.query(Maquina).filter(Maquina.Id_maquina == id_maquina).first()
db.s.commit()        
#ser.close()
