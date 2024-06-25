import requests
import json
from Restaurantes import Restaurante
from Data import get_json_from_url
from Data import obtener_datos
from Estadios import Estadio
from Equipos import Equipo
from Partido import Partido



class Euro_App:
    def __init__(self):
        self.partido = []
        self.estadio = []
        self.equipo = []
        self.restaurante = []
        self.cliente = []
        
        
        