# simulator.py

class Bot:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0

    def current_location(self):
        return (self.x, self.y)

    def move(self, direction, distance, blocked_positions):
        dx, dy = 0, 0

        if direction == 'N':
            dy = 1
        elif direction == 'S':
            dy = -1
        elif direction == 'E':
            dx = 1
        elif direction == 'W':
            dx = -1
        else:
            raise ValueError(f"Unknown direction: {direction}")

        for _ in range(distance):
            next_x = self.x + dx
            next_y = self.y + dy

            if (next_x, next_y) in blocked_positions:
                break

            self.x = next_x
            self.y = next_y


class MovementEngine:
    def __init__(self):
        self.bot_map = {}

    def register_bot(self, bot_name):
        if bot_name in self.bot_map:
            raise ValueError(f"Bot '{bot_name}' is already registered.")
        self.bot_map[bot_name] = Bot(bot_name)

    def locate_bot(self, bot_name):
        self._ensure_bot_exists(bot_name)
        return self.bot_map[bot_name].current_location()

    def send_instruction(self, bot_name, instruction):
        self._ensure_bot_exists(bot_name)

        if len(instruction) < 2:
            raise ValueError("Instruction format is invalid")

        direction = instruction[0].upper()
        try:
            steps = int(instruction[1:])
        except ValueError:
            raise ValueError("Instruction must end with a numeric value")

        occupied = {
            b.current_location()
            for key, b in self.bot_map.items()
            if key != bot_name
        }

        self.bot_map[bot_name].move(direction, steps, occupied)

    def _ensure_bot_exists(self, bot_name):
        if bot_name not in self.bot_map:
            raise ValueError(f"No bot found with ID: {bot_name}")
