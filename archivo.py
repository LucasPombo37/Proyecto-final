import pygame as py
from modulo import *

py.init()

corriendo = True
ventana = 3

while(corriendo):
    lista_eventos = py.event.get()
    match ventana:
        case 1:
            iniciar_ventana_menu()           
            pass        
        case 2:
            #iniciar_ventana_juego()
            pass
        case 3:    
            iniciar_ventana_puntaje()        
            for evento in lista_eventos:      #Itera a través de los eventos en lista_eventos 
                if evento.type == py.QUIT:    #y evalua los que van sucediendo            
                    corriendo = False
                elif evento.type == py.MOUSEBUTTONDOWN:
                    if evento.button == 1:
                        if evento.pos[0] > 450 and evento.pos[0] < 500:
                            if evento.pos[1] > 450 and evento.pos[1] < 500:                               
                                ventana = 1
    py.display.update()



