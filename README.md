# Flappy Bird with Genetic Algorithm and Neural Network

## Overview

This project is an implementation of the Flappy Bird game where birds are controlled by an artificial intelligence (AI) trained with genetic algorithms and neural networks. The birds evolve over generations, learning to navigate through pipes.

## Main Components

### `app.py`
The main script that initiates the game loop using Pygame. It manages game initialization, the main loop, and game exit.

### `attrib.py`
Defines game attributes, bird behavior, and pipe mechanics. Here, you'll find the `Game` class that initializes the game, the `Bird` class that defines bird behavior, and the `Pipe` class that manages pipes.

### `genetic.py`
Implements genetic algorithms for the evolution of the bird population. The `Population` class manages the bird population, evaluates fitness, selects parents, performs crossovers and mutations, evolving the population over time.

### `neural.py`
Defines the neural network structure and functions. The `NeuralNetwork` class has methods for activation, feed-forward, and error calculation.

## Features

- Birds evolve and improve their scores over successive generations.
- The AI adapts to optimize bird behavior, avoiding pipes and increasing survival chances.

## How It Works

1. Birds are represented as individuals with neural networks controlling their actions.
2. Genetic algorithms drive evolution, selecting the fittest birds for the next generation.
3. Neural networks are fine-tuned through crossover and mutation, improving performance.

## How to Run

1. Clone the repository.
2. Ensure you have Python and Pygame installed.
3. Run the `app.py` script to start the game.

## Contributions

Feel free to explore the code, provide feedback, or contribute to the project. Issues and pull requests are welcome!

## Acknowledgments

Special thanks to the Pygame community and contributors for making game development in Python so accessible!

---

Have fun exploring the world of AI in Flappy Bird! 🐦🎮
