import pygame as py
from constantes import *


ANCHO = 500
ALTO = 500
COLOR_ROJO = (255,0,0)
COLOR_VERDE = (0,255,0)
COLOR_AZUL = (0,0,255)
COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)
VENTANA = py.display.set_mode((ANCHO, ALTO))

top_10_puntajes = {
    "Usuario1": 1500,
    "Usuario2": 1400,
    "Usuario3": 1300,
    "Usuario4": 1200,
    "Usuario5": 1100,
    "Usuario6": 1000,
    "Usuario7": 900,
    "Usuario8": 800,
    "Usuario9": 700,
    "Usuario10": 600,
}

def iniciar_ventana_puntaje():
    py.display.set_caption("Pygame")
    superficie_fondo = py.Surface((ANCHO, ALTO))
    VENTANA.blit(superficie_fondo, (0, 0))
    fuente = py.font.SysFont("jokerman",40)
    titulo = fuente.render("TOP 10",False,COLOR_BLANCO)
    VENTANA.blit(titulo,(190,30)) 
    cargar_top(top_10_puntajes,fuente)
    cargar_boton()

def cargar_top(top_diez:dict,fuente):
    ubicacion_x = 100
    ubicacion_y = 120
    fuente = py.font.SysFont("Arial",25)
    for usuario, puntaje in top_10_puntajes.items():
        usuario_puntaje = f"Usuario: {usuario}, Puntaje: {puntaje}"
        nombre = fuente.render(usuario_puntaje,True,COLOR_BLANCO)
        VENTANA.blit(nombre,(ubicacion_x,ubicacion_y))
        ubicacion_y += 30


def cargar_boton(): 
    boton_atras = py.image.load("./imagenes/boton_atrass.png")
    boton = py.transform.scale(boton_atras, (50,50))
    VENTANA.blit(boton,(450, 450))

def iniciar_ventana_menu():
    py.display.set_caption("Pygame")
    superficie_fondo = py.Surface((ANCHO, ALTO))
    VENTANA.blit(superficie_fondo, (0, 0))
    fuente = py.font.SysFont("jokerman",40)
    titulo = fuente.render("INICIAR JUEGO ",False,COLOR_BLANCO)
    VENTANA.blit(titulo,(190,30)) 
    

    
        




