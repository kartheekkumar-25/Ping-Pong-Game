# Ping-Pong-Game
🏓 Ping Pong Game (Python Turtle)  A two-player Ping Pong (Pong) game built using Python’s turtle module. The game features paddle movement, ball physics, real-time scoring, increasing difficulty, and a win condition based on points.  This project demonstrates object-oriented programming, collision detection, and keyboard event handling in Python.

## 📁 Project Structure

```
ping-pong-game/
│
├── main.py          # Game loop and screen setup
├── paddle.py        # Paddle movement and controls
├── ball.py          # Ball movement and collision logic
├── scoreboard.py   # Score display and win messages
└── README.md
```

---

## 🎮 How the Game Works

* Two paddles are controlled by players on the left and right.
* The ball starts with a random direction.
* The ball:

  * Bounces off the top and bottom walls
  * Bounces off paddles on contact
* Ball speed gradually increases as the game progresses.
* When a player misses the ball:

  * The opponent scores a point
  * The ball and paddles reset to the center
* The first player to score **3 points** wins the game.

---

## ⌨️ Controls

### Left Player

* **W** – Move Up
* **S** – Move Down

### Right Player

* **↑ Arrow** – Move Up
* **↓ Arrow** – Move Down

## ▶️ How to Run

1. Make sure Python 3.x is installed
2. Clone the repository
3. Run the main file:

```bash
python main.py
```

---

## 🏆 Win Condition

* **Left Player wins** when left score reaches 3
* **Right Player wins** when right score reaches 3
* A win message is displayed at the center of the screen

🖼️ Image 1 – Game Start Screen

This image shows the initial state of the Ping Pong game.
Both paddles are positioned at the center on the left and right sides, the ball is placed near the center, and the score at the top is 0 : 0. This represents the starting condition before any player scores.

<img width="1252" height="911" alt="start" src="https://github.com/user-attachments/assets/ea26afce-14b5-4ebd-9a7f-cd1e8ba291de" />


🖼️ Image 2 – Game Over Screen

This image shows the end state of the Ping Pong game.
The score displayed at the top is 1 : 3, indicating that the Right Player has reached the winning score. A centered message “R Player WON” appears on the screen, confirming the winner. The paddles and ball are visible in their final positions, and the game has stopped accepting input.

<img width="1250" height="916" alt="gameover" src="https://github.com/user-attachments/assets/b0208ba6-b6ca-4ffd-93d3-791b4f3ba5b0" />


---

