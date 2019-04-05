# Travelling salesman problem
--------------------
  
  
O problema do caixeiro-viajante está dentre os mais famosos na computação, na área de otimização. A proposta é conseguir estimar qual a menor rota entre uma quantidade n de pontos dados. Em uma breve analogia com o cotidiano, qual seria a rota mais eficiente para um entregador de mercadorias em diferentes cidades?  

Quando o número n de cidades (ou pontos) é pequeno, a resolução é facilmente encontrada através de força bruta. Isto é, testando todas alternativas possíveis. Contudo, o problema torna-se inviável conforme esse valor aumenta. Aqui vale lembrar que as combinações existentes são dadas por meio de n!. Sendo assim, alguns exemplos de combinações possíveis seriam:  

3! = 6  
10! = 3628800  
50! = 3,04×10^64  

Dessa forma, métodos distintos ao da força bruta são necessários para a resolução desse problema. A técnica de algoritmos genéticos tem como proposta aplicar conceitos advindos da biologia evolutiva em computação, afim de simular um ambiente evolutivo.  

O problema aplicado nesse estudo trata-se de uma matriz de distâncias NxN, onde cada índice M[ i ][ j ] representa a distância de transição de uma cidade i para uma cidade j. Tanto o número de cidades quanto sua numeração possuem relação direta com a quantidade N de linhas (ou colunas) da matriz. Dessa forma uma matriz 3x3 possuirá cidades [ 0 , 1 , 2].

O objetivo do algoritmo é encontrar a menor rota que tenha início em uma cidade qualquer e fim na cidade zero (0).

## Algoritmo evolutivo
-----------------
  
    
Utilização da biblioteca geap para criação de uma toolbox que contenha os seguintes itens:  

Indivíduo - Lista de tamanho N que representa uma rotas aleatórias não repetidas entre as cidades.  
  

Exemplo: [3, 1, 2]   
    
|Step | Cidade inicial | Cidade destino |
|-----|-----------|----------------|
| (1) | 3 | 1 |
| (2) | 1 | 2 |
| (3) | 2 | 0 |

População - Conjunto de indivíduos  
  
Fitness - Função que avalia a desempenho. Lembrando que trata-se de um problema de otimização de mínimos. 
  
Função de Avaliação - Avalia o desempenho da rota proposta. É a soma das distâncias das rota proposta.  
  
Seleção - Método de seleção de melhores indivíduos. O modelo utilizado foi o mesmo proposto em sala de aula: Torneio
  
Cruzamento - Método para troca de 'genes' ou rotas entre os melhores indivíduos.
  
Mutação - Método de geração de variabilidade genética que possui como proposta favorecer a saída e mínimos ou máximos locais.  


## Uso
---------------
  
    
1 - git clone https://github.com/g-rm/Travelling-Salesman-Problem.git  
2 - Instale dependências (deap, numpy...)  
3 - Ajuste parâmetros desejados em _main.py_ (qtd cidades, pop, mutpb, ngen)  
4 - Execute _python3 main.py_  
  
  
## Resultados da otimização

![Alt text](../assets/evolution.png?raw=true "TSP")
