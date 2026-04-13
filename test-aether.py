import ast
import json
import os

class Aether:
    def __init__(self):
        self.variables = {}
        self.types = {}
        self.history = []

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_help(self):
        print("\n--- AETHER COMMAND GUIDE ---")
        print(f"{'Command':<14} | {'Action'}")
        print("-" * 50)
        print(f"{'help':<14} | Show this menu")
        print(f"{'clear':<14} | Wipe terminal screen")
        print(f"{'vars':<14} | View memory and types")
        print(f"{'del <name>':<14} | Delete a variable")
        print(f"{'save <file>':<14} | Save memory to JSON")
        print(f"{'load <file>':<14} | Load memory from JSON")
        print(f"{'history':<14} | Show command history")
        print(f"{'echo text <text>':<14} | Print raw text to console")
        print(f"{'echo var <name>':<14} | Print variable value to console")
        print(f"{'exit':<14} | Quit Aether")
        print("-" * 50)
        print("Syntax: x := 10 + 5 (Declare)")
        print("        x = x * 2    (Update)")
        print("        del x        (Delete variable)")
        print("-" * 50 + "\n")

    def list_vars(self):
        if not self.variables:
            print("Memory is empty.")
            return
        print(f"\n{'NAME':<10} | {'TYPE':<8} | {'VALUE'}")
        print("-" * 40)
        for name, val in self.variables.items():
            print(
                f"{name:<10} | "
                f"{self.types.get(name, type(val).__name__):<8} | {val}"
            )
        print()

    def run(self):
        self.clear_screen()
<<<<<<< HEAD
        print("🌌 Aether v0.1.3-alpha | PyGo Hybrid (safe-eval + persistence)")
=======
        print("🌌 Aether v0.1.4a-alpha | PyGo Hybrid (safe-eval + persistence)")
>>>>>>> Update the local code for the programming language
        print("Type 'help' to begin.")

        while True:
            try:
                line = input("æ> ").strip()
                if not line:
                    continue
                self.history.append(line)
                lower = line.lower()
                if lower == 'exit':
                    break
                if lower == 'help':
                    self.show_help()
                    continue
                if lower == 'clear':
                    self.clear_screen()
                    continue
                if lower == 'vars':
                    self.list_vars()
                    continue
                if lower.startswith('del '):
                    _, name = line.split(None, 1)
                    self.delete_var(name.strip())
                    continue
                if lower.startswith('save '):
                    _, fname = line.split(None, 1)
                    self.save_vars(fname.strip())
                    continue
                if lower.startswith('load '):
                    _, fname = line.split(None, 1)
                    self.load_vars(fname.strip())
                    continue
                if lower == 'history':
                    self.print_history()
                    continue

                # Echo variants
                if lower.startswith('echo text'):
                    # preserve original casing and spacing of text
                    if lower == 'echo text':
                        text = ''
                    else:
                        text = line[len('echo text '):]
                    self.echo_text(text)
                    continue

                if lower.startswith('echo var'):
                    parts = line.split(None, 2)
                    if len(parts) < 3 or not parts[2].strip():
                        print("Usage: echo var <name>")
                    else:
                        name = parts[2].strip()
                        self.echo_var(name)
                    continue

                # Backwards-compat: single-word echo prints raw following text
                if lower.startswith('echo '):
                    _, text = line.split(None, 1)
                    self.echo_text(text)
                    continue
                if lower == 'echo':
                    self.echo_text('')
                    continue

                self.evaluate(line)
            except Exception as e:
                print(f"Error: {e}")

    # Persistence helpers
    def save_vars(self, filename):
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.variables, f, default=str, indent=2)
            print(f"Saved memory to '{filename}'")
        except Exception as e:
            print(f"Save Error: {e}")

    def load_vars(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            for k, v in data.items():
                self.variables[k] = v
                self.types[k] = type(v).__name__
            print(f"Loaded memory from '{filename}'")
        except Exception as e:
            print(f"Load Error: {e}")

    def delete_var(self, name):
        if name in self.variables:
            del self.variables[name]
            self.types.pop(name, None)
            print(f"Deleted '{name}'")
        else:
            print(f"Error: '{name}' not found.")

    def print_history(self):
        for i, cmd in enumerate(self.history, 1):
            print(f"{i:3}: {cmd}")

    # Console output commands
    def echo_text(self, text):
        """Print raw text to the console. Usage: echo text Hello world"""
        print(text)

    def echo_var(self, name):
        """Print the value of a stored variable. Usage: echo var myVar"""
        if name in self.variables:
            val = self.variables[name]
            print(val)
        else:
            print(f"Error: variable '{name}' not found.")

    # Safe evaluator using AST
    def safe_eval(self, expr):
        node = ast.parse(expr, mode='eval')
        return self._eval_node(node.body)

    def _eval_node(self, node):
        # Literals
        if isinstance(node, ast.Constant):
            return node.value
<<<<<<< HEAD
        # For older Python versions
        if isinstance(node, ast.Num):
            return node.n
        if isinstance(node, ast.Str):
            return node.s
        if isinstance(node, ast.NameConstant):
=======
        # For new Python versions
        if isinstance(node, ast.Constant):
            return node.value
        if isinstance(node, ast.Constant):
            return node.value
        if isinstance(node, ast.Constant):
>>>>>>> Update the local code for the programming language
            return node.value

        if isinstance(node, ast.List):
            return [self._eval_node(elt) for elt in node.elts]
        if isinstance(node, ast.Tuple):
            return tuple(self._eval_node(elt) for elt in node.elts)
        if isinstance(node, ast.Dict):
            return {
                self._eval_node(k): self._eval_node(v)
                for k, v in zip(node.keys, node.values)
            }

        # Names
        if isinstance(node, ast.Name):
            if node.id in self.variables:
                return self.variables[node.id]
            if node.id in ("True", "False", "None"):
                return {"True": True, "False": False, "None": None}[node.id]
            raise NameError(f"Unknown variable '{node.id}'")

        # Binary operations
        if isinstance(node, ast.BinOp):
            left = self._eval_node(node.left)
            right = self._eval_node(node.right)
            op = node.op
            if isinstance(op, ast.Add):
                return left + right
            if isinstance(op, ast.Sub):
                return left - right
            if isinstance(op, ast.Mult):
                return left * right
            if isinstance(op, ast.Div):
                return left / right
            if isinstance(op, ast.FloorDiv):
                return left // right
            if isinstance(op, ast.Mod):
                return left % right
            if isinstance(op, ast.Pow):
                return left ** right
            raise TypeError(f"Unsupported binary operator {op}")

        # Unary operations
        if isinstance(node, ast.UnaryOp):
            operand = self._eval_node(node.operand)
            if isinstance(node.op, ast.UAdd):
                return +operand
            if isinstance(node.op, ast.USub):
                return -operand
            if isinstance(node.op, ast.Not):
                return not operand
            raise TypeError("Unsupported unary operator")

        # Comparisons
        if isinstance(node, ast.Compare):
            left = self._eval_node(node.left)
            for op, comparator in zip(node.ops, node.comparators):
                right = self._eval_node(comparator)
                if isinstance(op, ast.Eq):
                    ok = left == right
                elif isinstance(op, ast.NotEq):
                    ok = left != right
                elif isinstance(op, ast.Lt):
                    ok = left < right
                elif isinstance(op, ast.LtE):
                    ok = left <= right
                elif isinstance(op, ast.Gt):
                    ok = left > right
                elif isinstance(op, ast.GtE):
                    ok = left >= right
                else:
                    raise TypeError("Unsupported comparison")
                if not ok:
                    return False
                left = right
            return True

        # Boolean ops
        if isinstance(node, ast.BoolOp):
            if isinstance(node.op, ast.And):
                for val in node.values:
                    if not self._eval_node(val):
                        return False
                return True
            if isinstance(node.op, ast.Or):
                for val in node.values:
                    if self._eval_node(val):
                        return True
                return False

        # Subscript (indexing)
        if isinstance(node, ast.Subscript):
            value = self._eval_node(node.value)
            slice_node = node.slice
            # Handle different AST slice representations across Python versions
            if isinstance(slice_node, ast.Index):
                idx = self._eval_node(slice_node.value)
            else:
                # For ast.Constant or direct nodes
                try:
                    idx = self._eval_node(slice_node)
                except Exception:
                    idx = (
                        self._eval_node(slice_node.value)
                        if hasattr(slice_node, 'value')
                        else None
                    )
            return value[idx]

        # Disallow calls, attributes, and other exec-capable nodes
        if isinstance(
            node, (ast.Call, ast.Attribute, ast.Lambda, ast.FunctionDef, ast.ClassDef)
        ):
            raise TypeError("Function calls, attribute access and definitions are not allowed")

        raise TypeError(f"Unsupported expression: {ast.dump(node)}")

    def evaluate(self, line):
        # Declaration
        if ":=" in line:
            parts = line.split(":=", 1)
            name = parts[0].strip()
            if name in self.variables:
                print(f"Error: '{name}' already exists. Use '=' to update.")
                return
            val = self.safe_eval(parts[1].strip())
            self.variables[name] = val
            self.types[name] = type(val).__name__
            print(f"Initialized {name}")
            return

        # Update (single '=' but not '==')
        if "=" in line and "==" not in line:
            parts = line.split("=", 1)
            name = parts[0].strip()
            if name not in self.variables:
                print(f"Error: '{name}' not found. Use ':=' to declare.")
                return
            val = self.safe_eval(parts[1].strip())
            self.variables[name] = val
            self.types[name] = type(val).__name__
            print(f"Updated {name}")
            return

        # Expression / comparison / raw math
        try:
            result = self.safe_eval(line)
            print(result)
        except Exception as e:
            print(f"Logic Error: {e}")

if __name__ == "__main__":
    Aether().run()
