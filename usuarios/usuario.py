from dataclasses import dataclass

@dataclass
class Usuario:
    __username: str
    __clave: str

    @property
    def username(self): return self.__username
    
    @property
    def clave(self): return self.__clave
