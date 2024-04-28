# Video Game Data Analysis

This repository contains Python code for analyzing a dataset of video games from Steam. The dataset is provided in a CSV format (`asn_games.csv`), containing information such as game names, Metacritic scores, recommendation counts, and prices.

## Dataset Overview

The dataset (`asn_games.csv`) consists of comma-separated values (CSV) with the following columns:

- **Game Name**: The name of the video game.
- **Metacritic Score**: The Metacritic score of the game, ranging from 0 to 100.
- **Recommendation Count**: The number of recommendations the game has received on Steam.
- **Price**: The cost of the game. If the game is free, the price is listed as "free"; otherwise, it's a float representing the price.

## Python Functions

The Python code in this repository provides solutions to several questions related to analyzing the dataset:

1. Calculating the number of lines and the number of games in the dataset.
2. Parsing each line of the CSV file to extract game information.
3. Finding and printing games with the highest Metacritic scores, the most recommendations, and the highest prices.
4. Calculating the average Metacritic score, the average number of recommendations, and the average price of the games.
5. Analyzing duplicate game names and occurrences.
6. Drawing a histogram of Metacritic scores.

## Instructions

To run the Python code, ensure that you have Python installed on your system. Use the provided Python script (`a5.py`) to execute the functions and analyze the dataset.

```bash
python a5.py
