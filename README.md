# 🌌 Aether Programming Language
**Current Version:** https://img.shields.io/badge/v0.1.0--alpha-8A2BE2
**Aether** is a **high-level, hybrid programming language** designed to combine the explicit declaration and performance-oriented "bones" of *Go* with the clean syntax and "batteries-included" heart of *Python.*

## ✨ Key Features
Explicit Declaration: Uses the *:=* operator for type-inferred variable creation, preventing accidental global overwrites.

**Indentation-Based Logic:** Adopts Python’s clean *:* and whitespace-aware blocks for better readability.

**Math-First Parser:** Built-in support for operator precedence (PEMDAS/BODMAS).

**Lightweight Interpreter:** Written in Python, making it highly portable and easy to extend.

## 🚀 Quick Start
**Installation**
Ensure you have **Python 3.10+** installed. Clone the repository and run the interpreter:

>*Bash (or Powershell)*

git clone https://github.com/SpideyBash4116/aether.git
cd aether
python aether.py
**Basic Syntax**
Aether feels familiar if you've used either "parent" language:

>**Python**

**Go-style declaration**
*mana := 100*

**Python-style operation**
*power := mana * 2 + 5*

**Re-assignment** (error if variable doesn't exist)
*mana = 150*
### 🛠 Architecture
Aether follows the **classic Interpreter Design Pattern**:

**Lexer:** Tokenizes raw input strings using Regular Expressions.

**Parser:** A Recursive Descent Parser that builds an Abstract Syntax Tree (AST).

**Visitor Engine:** Walks the AST to execute logic in a persistent global environment.

### 🗺 Roadmap
- Basic Arithmetic & Variables

- Go-style := Implementation

- Pythonic if/else Indentation Blocks

- Lightweight "Aether-routines" (Concurrency)

- Standard Library (File I/O, Networking)

### 🤝 Contributing
We welcome "Alchemists" to help refine the Aether. Feel free to open an issue or submit a pull request if you want to add new Nodes to our AST.
