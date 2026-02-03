# ⚡ Neon Runner - Rhythmic Survival Sim

A high-speed, text-based reaction game where the player must dodge obstacles in a futuristic neon corridor. Unlike traditional turn-based games, Neon Runner tracks your physical reaction time. As your score increases, the "reaction window" shrinks, requiring faster and more precise inputs to survive.

This project focuses on teaching:
* **Temporal Logic:** Measuring user response time using the `time` module.
* **Difficulty Scaling:** Using the modulo operator (`%`) to trigger speed increases at specific intervals.
* **Stream Processing:** Handling rapid-fire inputs and providing immediate feedback.
* **Dynamic Thresholds:** Comparing an elapsed time variable against a decreasing "survival" variable.

---

## ✨ Features

* **Real-Time Speed Tracking:** See exactly how many milliseconds it took you to react to an obstacle.
* **Three Action Types:** Specific commands (`jump`, `slide`, `dodge`) mapped to unique obstacles.
* **Scaling Difficulty:** The game starts at a 1.0s window and reduces by 20% every 5 points.
* **Precision Formatting:** Uses f-string formatting to display reaction times to two decimal places.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You need **Python 3** installed.

### 2. Setup and Execution
1.  **Save the Code:** Save the script as `neon_runner.py`.
2.  **Open Terminal:** Navigate to your project folder.
3.  **Run the Script:**
    ```bash
    python neon_runner.py
    ```

### 3. Gameplay Instructions
1.  **Read the Hazard:** The scanner will detect an approaching obstacle.
2.  **Input the Action:** Type the corresponding command and hit **Enter** immediately.
    * **LOW BAR** ➔ `jump`
    * **HIGH WALL** ➔ `slide`
    * **SIDE PANEL** ➔ `dodge`
3.  **Beat the Clock:** If you take longer than the current speed window, you crash!



---

## 🧠 Code Structure Highlights

### Measuring Performance
The core "Engine" of Neon Runner is the delta between two timestamps. This is how the game determines if you were "Fast Enough."

```python
start_time = time.time()
user_input = input("ACTION: ")
end_time = time.time()

elapsed = end_time - start_time

