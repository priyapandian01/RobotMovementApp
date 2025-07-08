import tkinter as tk
from simulator import MovementEngine

GRID_SIZE = 10  # 10x10 grid
CELL_SIZE = 40  # pixels

class RobotGridUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Robot Grid Simulator")
        self.root.geometry(f"{GRID_SIZE * CELL_SIZE + 200}x{GRID_SIZE * CELL_SIZE + 100}")

        self.engine = MovementEngine()

        self.canvas = tk.Canvas(root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE, bg='white')
        self.canvas.pack(side=tk.LEFT, padx=10, pady=10)

        # Draw the grid
        for i in range(GRID_SIZE + 1):
            self.canvas.create_line(i * CELL_SIZE, 0, i * CELL_SIZE, GRID_SIZE * CELL_SIZE)
            self.canvas.create_line(0, i * CELL_SIZE, GRID_SIZE * CELL_SIZE, i * CELL_SIZE)

        # Right panel
        control_frame = tk.Frame(root)
        control_frame.pack(side=tk.RIGHT, padx=10)

        tk.Label(control_frame, text="Robot Name:").pack()
        self.name_entry = tk.Entry(control_frame)
        self.name_entry.pack()

        tk.Label(control_frame, text="Command (e.g., N2):").pack()
        self.command_entry = tk.Entry(control_frame)
        self.command_entry.pack()

        tk.Button(control_frame, text="Add Robot", command=self.add_robot).pack(pady=5)
        tk.Button(control_frame, text="Send Command", command=self.send_command).pack(pady=5)

        self.status_label = tk.Label(control_frame, text="", fg="green")
        self.status_label.pack(pady=5)

        self.robot_tags = {}

    def add_robot(self):
        name = self.name_entry.get().strip()
        if name:
            try:
                self.engine.register_bot(name)
                self.status_label.config(text=f"Robot '{name}' added.")
                self.draw_robot(name)
            except ValueError as e:
                self.status_label.config(text=str(e), fg='red')

    def send_command(self):
        name = self.name_entry.get().strip()
        cmd = self.command_entry.get().strip().upper()

        if name and cmd:
            try:
                self.engine.send_instruction(name, cmd)
                self.status_label.config(text=f"{name} moved to {self.engine.locate_bot(name)}", fg="green")
                self.draw_all_robots()
            except ValueError as e:
                self.status_label.config(text=str(e), fg='red')

    def draw_robot(self, name):
        pos = self.engine.locate_bot(name)
        x, y = pos
        x1 = x * CELL_SIZE
        y1 = (GRID_SIZE - 1 - y) * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE

        # Remove old if exists
        if name in self.robot_tags:
            self.canvas.delete(self.robot_tags[name])

        tag = self.canvas.create_rectangle(x1, y1, x2, y2, fill="orange")
        text = self.canvas.create_text(x1 + CELL_SIZE // 2, y1 + CELL_SIZE // 2, text=name, fill="white")
        self.robot_tags[name] = tag
        self.robot_tags[name + "_text"] = text

    def draw_all_robots(self):
        for name in self.engine.bot_map:
            self.draw_robot(name)


if __name__ == "__main__":
    root = tk.Tk()
    app = RobotGridUI(root)
    root.mainloop()
