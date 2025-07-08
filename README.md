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

| Task Requirement                                                   | Implementation ✅                                                                  |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| **a) Create multiple robots**                                      | `add_robot("R1")`, `add_robot("R2")`                                              |
| **b) Associate each robot with a unique number**                   | Unique robot IDs like `"R1"`, `"R2"`                                              |
| **c) Move a selected robot based on input like N4, E3, etc.**      | `issue_command("R1", "E3")`                                                       |
| **d) Stop movement if a robot is already at the destination cell** | Movement stops before occupied cell — collision prevention logic implemented      |
| **e) Display the current location of the selected robot**          | `get_robot_current_position("R1")` returns current (x, y) position                |
| **f) Terrain is a grid and robots start at cell (0, 0)**           | Each robot starts from `(0, 0)` and moves on grid coordinates                     |
| **g) Terrain need not be visually shown**                          | Terminal output shows positions (GUI included optionally)                         |
| **h) Include unit test cases**                                     | `test_robot.py` includes test cases for movement, collision, and input validation |



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

