class Vehiculo: # Clase que representa a un vehículo
    def __init__(self, marca, modelo, tarifa_diaria):
        self.marca = marca
        self.modelo = modelo
        self.__tarifa_diaria = tarifa_diaria
    
    @property
    def tarifa_diaria(self):
        return self.__tarifa_diaria
    
    def calcular_alquiler(self, dias):
        return self.__tarifa_diaria * dias
    
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Tarifa Diaria: {self.__tarifa_diaria}"
    
class Auto(Vehiculo): # Clase que representa a un auto, hereda de Vehiculo
    def __init__(self, marca, modelo, tarifa_diaria, puertas):
        super().__init__(marca, modelo, tarifa_diaria)
        self.puertas = puertas
    
    def __str__(self):
        return super().__str__() +f", Puertas: {self.puertas}"

class Camioneta(Vehiculo): # Clase que representa a una camioneta, hereda de Vehiculo
    def calcular_alquiler(self, dias):
        return self.tarifa_diaria * dias + 10
    
def main():
    auto = Auto("Toyota", "Corolla", 100, 4) # Creamos un auto
    camioneta = Camioneta("Ford", "Mustang", 1500) # Creamos una camioneta
    
    # Imprimimos los datos de los vehículos y el costo de alquiler por 5 días
    print("="*22 + " VEHÍCULOS DISPONIBLES " + "="*22)
    print("-"*30 + " AUTO " + "-"*31)
    print(auto)
    print(f"Alquiler de {auto.marca} {auto.modelo}: ${auto.calcular_alquiler(5)} por 5 días")
    print("-"*28 + " CAMIONETA " + "-"*28)
    print(camioneta)
    print(f"Alquiler de {camioneta.marca} {camioneta.modelo}: ${camioneta.calcular_alquiler(5)} por 5 días")

main()