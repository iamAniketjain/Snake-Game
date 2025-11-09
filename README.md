# 🐍 Classic Snake Game – Python Turtle Edition

## 🎮 Overview
The **Classic Snake Game** is a fun and interactive Python project built using the `turtle` graphics library.  
This game recreates the nostalgic experience of the retro Snake Game, where players control a snake to eat food, grow in size, and avoid collisions.  
It’s a great beginner-to-intermediate level project demonstrating **object-oriented programming (OOP)** concepts in Python.

---

## 🧩 Project Structure
| File Name | Description |
|------------|-------------|
| `main.py` | The main entry point of the game. Initializes the screen, handles game loops, and manages gameplay logic. |
| `snake.py` | Defines the `Snake` class responsible for creating, moving, and controlling the snake. |
| `food.py` | Defines the `Food` class responsible for generating food at random locations. |
| `score.py` | Defines the `ScoreBoard` class for displaying the current score and high score, with persistence using a local file (`data.txt`). |

---

## ⚙️ How It Works
1. The game window is created using the `turtle` module with a 600x650 black background.
2. The snake starts at the center and moves continuously in the current direction.
3. When the snake eats food:
   - The food reappears in a random position.
   - The snake grows in length.
   - The score increases.
4. If the snake hits the wall or itself:
   - The game resets.
   - The high score is updated and saved in `data.txt`.

---

## 🧠 Key Classes & Methods

### 🐍 `Snake` Class (`snake.py`)
- **`create_snake()`** – Initializes the snake body with 3 white squares.  
- **`snake_move()`** – Moves the snake forward continuously.  
- **`extend()`** – Adds a new segment to the snake when it eats food.  
- **`reset()`** – Resets the snake position after a collision.  
- **Directional Methods (`up`, `down`, `left`, `right`)** – Controls the movement via arrow keys.

### 🍎 `Food` Class (`food.py`)
- **Inherits from `Turtle`**.
- Creates a small blue circle that appears at random coordinates using `refresh()`.

### 🧮 `ScoreBoard` Class (`score.py`)
- Displays the **current score** and **high score** at the top of the screen.
- Saves high scores to `data.txt` to persist across sessions.
- Methods:
  - `inc_score()` – Increases the score when food is eaten.
  - `reset()` – Updates and resets scores after a collision.
  - `scoring()` – Handles on-screen score updates.

---

## 🕹️ Controls
| Key | Action |
|------|---------|
| ⬆️ | Move Up |
| ⬇️ | Move Down |
| ⬅️ | Move Left |
| ➡️ | Move Right |

---

## 🚀 How to Run the Game

### 🧰 Requirements
- Python 3.7 or higher  
- No external libraries required (uses built-in `turtle` and `random` modules)

### ▶️ Steps
1. Clone or download the project files.  
2. Make sure all files (`main.py`, `snake.py`, `food.py`, `score.py`, and `data.txt`) are in the same directory.  
3. Run the following command in your terminal or IDE:
   ```bash
   python main.py
🏅 Features

✅ Real-time snake movement using event listeners
✅ Random food placement after each consumption
✅ Persistent high score tracking via data.txt
✅ Smooth animation using Screen.tracer(0) and Screen.update()
✅ OOP-based modular code structure

📸 Sample Output
---------------------------------
|     Score: 3  High Score: 7   |
|                               |
|      🐍  ← Snake Game 🐍       |
---------------------------------

🧰 Technologies Used

Python 3

Turtle Graphics

OOP (Classes & Inheritance)

File Handling (High Score Data)

🧩 Future Enhancements

Add levels or increasing speed over time.

Include sound effects when eating food or hitting walls.

Add a start menu and game-over screen.

Add difficulty modes or color customization.

🏁 Conclusion

This project demonstrates how Python can be used to create engaging interactive games using simple built-in modules.
It’s a great foundation for understanding OOP, event handling, and real-time graphics in Python.
Play, learn, and have fun coding your own version of the classic Snake Game! 🎮
