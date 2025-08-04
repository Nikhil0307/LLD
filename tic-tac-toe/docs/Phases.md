### 🧭 `phases.md`

---

## 🛠️ PHASE 1: Design the Core Classes and Data Structures

**Goal:** Think through what components your game needs.

* What is the minimal set of classes or data structures you need?
* How will you represent the game board?
* How will you store and track the game state?

💡 *Hint: Try drawing a class diagram or writing out responsibilities in plain English.*

---

## 🎯 PHASE 2: Implement the Game Board

**Goal:** Create a basic `Board` class (or similar) that can:

* Store the grid state.
* Print/display the board.
* Update the board with a player move.
* Check if a move is valid.

💡 *Hint: A 2D list can work well for a 3x3 board. Think about how you’ll map positions (1–9 or 0-indexed tuples?).*

---

## 🎮 PHASE 3: Player Move Logic

**Goal:** Accept input from both players in turns.

* Take user input (position on the board).
* Validate it (not out of range or already filled).
* Place the mark (X/O).

💡 *Hint: Use a loop to alternate turns. Keep track of current player.*

---

## 🏁 PHASE 4: Game End Logic

**Goal:** After every move, check if the game is over.

* Check for a win: 3 in a row (horizontal/vertical/diagonal).
* Check for a draw: All cells filled, no winner.

💡 *Hint: Write a separate function to evaluate win conditions using the grid.*

---

## 🔁 PHASE 5: Game Loop & Replay

**Goal:** Wrap all logic into a single loop.

* Start the game.
* Take turns.
* End when there's a win or draw.
* Ask user if they want to play again.

💡 *Hint: Structure this cleanly — don’t let your `main()` become bloated.*

---

## 🧹 PHASE 6 (Optional): Cleanups and Enhancements

**Goal:** Refactor and polish.

* Use OOP principles (create `Game`, `Board`, `Player` classes).
* Make error handling clean.
* Add optional features: replay, reset, stats, etc.

💡 *Hint: Think like a game engine developer — encapsulate logic cleanly.*

---