from abc import ABC, abstractmethod

class Caminhoes(ABC):
    def __init__(self, capacidade, custo, porte): 
        self.porte = porte
        if self.porte not in ('pequeno','medio','grande'):
            raise Exception('Porte inválido')

        self.capacidade = capacidade
        self.custo = custo

    def calcular_rota(self, distancia):
        return self.custo * distancia
        
    def __str__(self):
        return f'Caminhão de {self.porte} porte'
    
class GrandePorte(Caminhoes):
    def __init__(self): 
        super().__init__(capacidade = 10000.0, custo = 27.44, porte='grande')

class MedioPorte(Caminhoes):
    def __init__(self):
        super().__init__(capacidade = 4000.0, custo = 11.92, porte='medio')

class PequenoPorte(Caminhoes):
    def __init__(self):
        super().__init__(capacidade = 1000.0, custo = 4.87, porte='pequeno')

        