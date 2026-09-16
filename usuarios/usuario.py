from dataclasses import dataclass

@dataclass
class Usuario:
    __username: str
    __clave: str

    def registrar_usuario(self, nuevo_usuario, nueva_clave):
        pass

    @property
    def username(self): return self.__username
    
    @property
    def clave(self): return self.__clave
