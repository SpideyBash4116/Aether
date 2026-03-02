import re
import os

class Aether:
    def __init__(self):
        self.variables = {}
        self.types = {}

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_help(self):
        print("\n--- AETHER COMMAND GUIDE ---")
        print(f"{'Command':<10} | {'Action'}")
        print("-" * 35)
        print(f"{'help':<10} | Show this menu")
        print(f"{'clear':<10} | Wipe terminal screen")
        print(f"{'vars':<10} | View memory and types")
        print(f"{'exit':<10} | Quit Aether")
        print("-" * 35)
        print("Syntax: x := 10 + 5 (Declare)")
        print("        x = x * 2    (Update)")
        print("-" * 35 + "\n")

    def list_vars(self):
        if not self.variables:
            print("Memory is empty.")
            return
        print(f"\n{'NAME':<10} | {'TYPE':<8} | {'VALUE'}")
        print("-" * 30)
        for name, val in self.variables.items():
            print(f"{name:<10} | {self.types[name]:<8} | {val}")
        print()

    def run(self):
        self.clear_screen()
        print("🌌 Aether v1.2 | PyGo Hybrid")
        print("Type 'help' to begin.")
        
        while True:
            try:
                line = input("ae> ").strip()
                if not line: continue
                if line.lower() == 'exit': break
                if line.lower() == 'help': self.show_help(); continue
                if line.lower() == 'clear': self.clear_screen(); continue
                if line.lower() == 'vars': self.list_vars(); continue
                
                self.evaluate(line)
            except Exception as e:
                print(f"Error: {e}")

    def evaluate(self, line):
        # A simple regex-based evaluator for our hybrid syntax
        # Handles: var := expression OR var = expression
        if ":=" in line:
            parts = line.split(":=")
            name = parts[0].strip()
            if name in self.variables:
                print(f"Error: '{name}' already exists. Use '=' to update.")
                return
            val = eval(parts[1], {}, self.variables)
            self.variables[name] = val
            self.types[name] = type(val).__name__
            print(f"Initialized {name}")
            
        elif "=" in line:
            parts = line.split("=")
            name = parts[0].strip()
            if name not in self.variables:
                print(f"Error: '{name}' not found. Use ':=' to declare.")
                return
            val = eval(parts[1], {}, self.variables)
            self.variables[name] = val
            self.types[name] = type(val).__name__
            print(f"Updated {name}")
        else:
            # Just evaluate raw math/variables
            print(eval(line, {}, self.variables))

if __name__ == "__main__":
    Aether().run()
