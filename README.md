# 🤖 Robot Movement App 

This is a Python project that simulates robot movement on a 10x10 grid using a simple GUI (Tkinter).  
You can add multiple robots and issue directional commands like `E3`, `N2` to move them.

---

## 📁 Project Files

| File Name          | Purpose                          |
|--------------------|----------------------------------|
| `main.py`          | Console-based simulation         |
| `simulator.py`     | Robot logic and movement engine  |
| `robot_grid_ui.py` | Tkinter GUI for robot control    |
| `test_robot.py`    | Unit tests using `unittest`      |
| `README.md`        | Project overview and instructions|

---

## 🚀 How to Run 

```bash
python robot_grid_ui.py


Step 2: Inside the App
➕ Enter robot name (e.g., R1), click Add Robot

🎮 Enter command (e.g., E3), click Send Command

🧱 Robot will stop if another robot blocks the path


Example Commands
Command	Action
N2	Move 2 steps up
S1	Move 1 step down
E3	Move 3 steps right
W2	Move 2 steps left

