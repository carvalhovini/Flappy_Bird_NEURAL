Flappy Bird with Genetic Algorithm and Neural Network
Este projeto é uma implementação do jogo Flappy Bird, onde os pássaros são controlados por uma inteligência artificial (IA) treinada com algoritmos genéticos e redes neurais. Os pássaros evoluem ao longo de gerações, aprendendo a navegar através de tubos.

Componentes Principais
app.py
Este é o script principal que inicia o loop do jogo usando Pygame. Ele gerencia a inicialização do jogo, o loop principal e a saída do jogo.

attrib.py
Define os atributos do jogo, o comportamento do pássaro e a mecânica dos tubos. Aqui, você encontrará a classe Game que inicializa o jogo, a classe Bird que define o comportamento do pássaro, e a classe Pipe que gerencia os tubos.

genetic.py
Implementa algoritmos genéticos para evolução da população de pássaros. A classe Population gerencia a população de pássaros, avalia a aptidão, seleciona os pais, realiza cruzamentos e mutações, evoluindo a população ao longo do tempo.

neural.py
Define a estrutura da rede neural e suas funções. A classe NeuralNetwork possui métodos para ativação, alimentação para frente e cálculo de erro.

Recursos
Os pássaros evoluem e melhoram suas pontuações ao longo de gerações sucessivas.
A IA adapta-se para otimizar o comportamento do pássaro, evitando tubos e aumentando as chances de sobrevivência.
Como Funciona
Os pássaros são representados como indivíduos com redes neurais controlando suas ações.
Algoritmos genéticos impulsionam a evolução, selecionando os pássaros mais aptos para a próxima geração.
Redes neurais são aprimoradas por meio de cruzamento e mutação, melhorando o desempenho.
Como Executar
Clone o repositório.
Certifique-se de ter o Python e o Pygame instalados.
Execute o script app.py para iniciar o jogo.
Contribuições
Sinta-se à vontade para explorar o código, fornecer feedback ou contribuir para o projeto. Issues e pull requests são bem-vindos!

Agradecimentos
Um agradecimento especial à comunidade e aos colaboradores do Pygame por tornarem o desenvolvimento de jogos em Python tão acessível!