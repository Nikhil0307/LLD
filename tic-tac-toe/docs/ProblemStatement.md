### 📄 `problemstatement.md`

---

## 🧩 Problem Statement: Build a Console-Based Tic-Tac-Toe Engine

Design and implement a **2-player Tic-Tac-Toe game** that runs in a console (text-based interface). The goal is to simulate a clean, modular, and object-oriented implementation of the game engine. This is **not about building a UI**, but instead **focusing on logic, correctness, and clarity** of the design.

### Functional Requirements:

* The game must allow **two players** to take turns placing their respective marks (`X` or `O`) on a **3x3 grid**.
* After each move, the game must:

  * Validate the move.
  * Update the game board.
  * Display the current board state.
  * Check for win/draw conditions.
* The game should end when:

  * One player wins.
  * All cells are filled without a winner (draw).

---

## 🧠 Constraints and Scope:

* Input/output will be done via the console.
* The game state must be persistent throughout play.
* No GUI, AI, or multiplayer over network.
* The code should be modular and readable.
* Prefer OOP-style design (optional functional composition where necessary).

---

## ✨ Bonus (Optional):

* Allow replaying a new game after one ends.
* Support a reset command during the game.
* Keep track of game stats like wins/losses if multiple games are played.

---
