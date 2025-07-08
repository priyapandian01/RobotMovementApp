# main.py

from simulator import MovementEngine

def run_simulation():
    engine = MovementEngine()

    engine.register_bot("Bot1")
    engine.register_bot("Bot2")

    engine.send_instruction("Bot1", "E3")
    print(f"Bot1: {engine.locate_bot('Bot1')}")

    engine.send_instruction("Bot2", "E5")
    print(f"Bot2: {engine.locate_bot('Bot2')}")

    engine.send_instruction("Bot1", "N2")
    print(f"Bot1: {engine.locate_bot('Bot1')}")

    engine.send_instruction("Bot2", "E1")
    print(f"Bot2: {engine.locate_bot('Bot2')}")

if __name__ == "__main__":
    run_simulation()
