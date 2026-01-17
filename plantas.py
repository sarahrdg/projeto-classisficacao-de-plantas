class Plantas:
    def __init__(self, especie, nome_popular, grupo, caracteristica):
        self.__especie = especie
        self.__nome_popular = nome_popular
        self.__grupo = grupo
        self.__caracteristica = caracteristica

    def __str__(self):
        return (f"----------------------------------------\n"
                f"Grupo: {self.__grupo}\n"
                f"Espécie: {self.__especie}\n"
                f"Nome Popular: {self.__nome_popular}\n"
                f"Características: {self.__caracteristica}"
                )
    
    def get_grupo(self):
        return self.__grupo

    def get_nome_popular(self):
        return self.__nome_popular
    
    def curiosidade(self):  #polimorfismo
        return "Esta é uma planta nativa da serra."
#herança 
class Angiosperma(Plantas):
    def __init__(self, especie, nome_popular, grupo, caracteristica):
        super().__init__(especie, nome_popular, grupo, caracteristica)
    
    def curiosidade(self):  #polimorfismo
        return "Possui flores e frutos verdadeiros."
    
class Gimnosperma(Plantas):
    def __init__(self, especie, nome_popular, grupo, caracteristica):
        super().__init__(especie, nome_popular, grupo, caracteristica)

    def curiosidade(self):
        return "As sementes são 'nuas', não ficam protegidas dentro de frutos."


class Pteridofita(Plantas):
    def __init__(self, especie, nome_popular, grupo, caracteristica):
        super().__init__(especie, nome_popular, grupo, caracteristica)

    def curiosidade(self):
        return "São plantas que não produzem sementes, mas têm vasos condutores."
    
class Briofita(Plantas):
    def __init__(self, especie, nome_popular, grupo, caracteristica):
        super().__init__(especie, nome_popular, grupo, caracteristica)

    def curiosidade(self):  #polimorfismo
        return "Não possui vasos condutores de seiva (são bem pequenas)."
