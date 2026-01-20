import pandas as pd
from plantas import Plantas

class Identificador:
    def __init__(self):
        self.lista_plantas = []

    def ler_planilha(self, caminho_arquivo):
        df = pd.read_csv(caminho_arquivo, encoding='utf-8').fillna('')

        for index, linha in df.iterrows():
            # 3. Cria um objeto Planta com os dados daquela linha
            nova_planta = Plantas(
                grupo=linha['GRUPO'],
                especie=linha['ESPÉCIE'],
                nome_popular=linha['NOME POPULAR'],
                caracteristica=linha['CARACTERÍSTICAS']
            )
            # 4. Adiciona esse objeto na nossa lista (isso é 'popular' a lista!)
            self.lista_plantas.append(nova_planta)
        
        print(f"Sucesso! {len(self.lista_plantas)} plantas de Irauçuba carregadas.")

    def buscar_por_nome(self, nome_digitado):
        # Lógica simples de busca:
        print(f"\n--- Resultados para: {nome_digitado} ---")
        encontrou = False
        for p in self.lista_plantas:
            nome_popular_texto = str(p.get_nome_popular()).lower()
            if nome_digitado.lower() in nome_popular_texto:
                print(p)
                print(f"[CURIOSIDADE]: {p.curiosidade()}")
                print("-" * 40)
                encontrou = True
        
        if not encontrou:
            print("Nenhuma planta encontrada com esse nome.")

    def filtrar_por_grupo(self, nome_grupo):
        resultado = []
        for p in self.lista_plantas:
            grupo_da_planta = str(p.get_grupo()).lower()
            
            if grupo_da_planta == nome_grupo.lower():
                resultado.append(p)
                
        return resultado