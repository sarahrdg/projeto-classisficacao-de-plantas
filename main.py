#menu
from identificador import Identificador
from plantas import Plantas

meu_buscador = Identificador()
meu_buscador.ler_planilha('plantas Guaramiranga - Planilha de Plantas Nativas de Guaramiranga.csv')

print("\n=== BEM-VINDO AO IDENTIFICADOR DA FLORA DE GUARAMIRANGA ===")

while True:
    print("\nResponda as perguntas para identificarmos a planta:")
    print("1. A planta possui FLORES e FRUTOS? (Ex: Ipê, Bromélia)")
    print("2. A planta possui SEMENTES, mas NÃO tem flores? (Ex: Pinheiros)")
    print("3. A planta é uma SAMAMBAIA ou AVENCA?")
    print("4. A planta é um MUSGO pequeno que vive no úmido?")
    print("5. Já sei o nome popular e quero buscar por informações")
    print("0. Sair do sistema")
    
    opcao = input("\nEscolha uma opção: ")

    if opcao == "0":
        print("Saindo... Até a próxima trilha em Guaramiranga!")
        break
    grupo_escolhido = ""
    if opcao == "1": grupo_escolhido = "Angiosperma"
    elif opcao == "2": grupo_escolhido = "Gimnosperma"
    elif opcao == "3": grupo_escolhido = "Pteridófita"
    elif opcao == "4": grupo_escolhido = "Briófita"
    elif opcao == "5":
        nome_busca = input("\nDigite o nome popular da planta: ")
        meu_buscador.buscar_por_nome(nome_busca)
        input("\nPressione ENTER para voltar ao menu...")
        continue

    if grupo_escolhido:
        plantas_filtradas = meu_buscador.filtrar_por_grupo(grupo_escolhido)
        
        print(f"\nEncontrei {len(plantas_filtradas)} plantas desse grupo em Guaramiranga.")
        print("Aqui estão elas para você identificar:")
        
        for p in plantas_filtradas:
            print(p) 
            
        input("\nPressione ENTER para fazer uma nova busca...")
    else:
        print("Opção inválida! Tente novamente.")