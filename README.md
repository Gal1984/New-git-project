# Tic-Tac-Toe (`tiktakto.py`)

A two-player command-line tic-tac-toe game. Players take turns placing **X** and **O** on a 3×3 board. The interface and prompts are in Hebrew.

## Requirements

- Python 3

## How to run

From this folder:

```bash
python tiktakto.py
```

On some systems you may need `python3` instead of `python`.

## How to play

1. Player **X** starts.
2. On each turn, enter a **row** and **column** as two numbers separated by a space.
3. Both numbers are **1-based**: `1 1` is the top-left cell, `3 3` is the bottom-right.

Example:

```
הכנס מספר שורה ומספר עמודה (לדוג' 1 2): 2 3
```

That places a mark in row 2, column 3.

The game ends when a player gets three in a row (horizontal, vertical, or diagonal), or when the board is full (draw).

Invalid input is handled: out-of-range cells, occupied cells, and non-numeric input ask you to try again.

## Board layout

```
---------
|   |   |   |
---------
|   |   |   |
---------
|   |   |   |
---------
```

Rows and columns are numbered 1, 2, 3 from top to bottom and left to right.
