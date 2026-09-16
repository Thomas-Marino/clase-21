from dataclasses import dataclass

@dataclass
class Usuario:
    __username: str
    __clave: str

    def saludar(self): 
        print(f"Hola, me llamo {self.__usuario}")

    @property
    def username(self): return self.__username
    
    @property
    def clave(self): return self.__clave
