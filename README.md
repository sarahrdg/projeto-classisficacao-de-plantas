# Identificador da flora de Guaramiranga
> **Projeto Final de Programação Orientada a Objetos (POO) - UFC**

Este projeto foi desenvolvido como parte da disciplina de Programação Orientada a Objetos (POO). O objetivo é fornecer uma ferramenta de software para uma ONG ambiental em Guaramiranga, Ceará, auxiliando na identificação e classificação de espécies vegetais da região.

## Funcionalidade
O sistema oferece dois caminhos para a identificação:

**Por meio de Perguntas:** Guia o usuário através de características biológicas para identificar o grupo da planta (Briófitas, Pteridófitas, Gimnospermas ou Angiospermas).

**Busca Direta:** Permite pesquisar uma planta pelo seu nome popular para obter informações científicas completas.

**Ficha Técnica:** Exibe grupo, espécie, nome popular, características e uma curiosidade biológica baseada no polimorfismo.

## Tecnologias utilizadas
**Linguagem:** ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

**Biblioteca:** Pandas (para manipulação da base de dados CSV)


## Implementação dos Pilares de POO
O projeto foi estruturado para demonstrar o domínio dos quatro pilares da POO:

**Abstração:** Criação da classe base `Plantas`.

**Encapsulamento:** Uso de atributos privados (`__`) e métodos de acesso Getters.

**Herança:** Implementação de subclasses específicas (`Angiosperma, Gimnosperma, Pteridofita e Briofita`) que herdam da classe mãe Plantas.

**Polimorfismo:** Uso do método `curiosidade()` que retorna informações distintas dependendo da classe específica do objeto instanciado.

## Estrutura do Projeto
`main.py`: Ponto de entrada do programa e interface do menu.

`plantas.py`: Definição das classes e subclasses.

`identificador.py`: Lógica de busca e carregamento de dados.

`plantas_guaramiranga.csv`: Base de dados contendo até então 80 espécies cadastradas.

## UML

<img width="621" height="671" alt="image" src="https://github.com/user-attachments/assets/938b4463-37c7-4dae-8135-f0729e52a2d6" />

## Evidência dos resultados obtidos
>  Guia o usuário através de características biológicas para identificar o grupo da planta
<img width="788" height="443" alt="image" src="https://github.com/user-attachments/assets/323dd783-9897-4ba8-9775-7b3f1a51d8c0" />

> Permite pesquisar uma planta pelo seu nome popular para obter informações
<img width="737" height="451" alt="image" src="https://github.com/user-attachments/assets/cf23762c-2313-4410-bea1-65e5b482ad98" />


## Como Executar
1. Certifique-se de ter o Python e a biblioteca Pandas instalados:


```pip install pandas```

2. Clone o repositório ou baixe os arquivos.

```git clone https://github.com/seu-usuario/seu-repositorio.git```

3. Execute o arquivo principal:

```python main.py```
