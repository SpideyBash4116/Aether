# 🌌 Aether Programming Language
## (Also called Æther)
**Current Status:** `v0.1.2-alpha`  
**Aether** is a **high-level, hybrid programming language** designed to combine the explicit declaration and performance-oriented "bones" of *Go* with the clean syntax and "batteries-included" heart of *Python.*

## ✨ Key Features
Explicit Declaration: Uses the `:=` operator for type-inferred variable creation, preventing accidental global overwrites.

- **Indentation-Based Logic:** Adopts Python’s clean `:` and whitespace-aware blocks for better readability.
- **Math-First Parser:** Built-in support for operator precedence (PEMDAS/BODMAS).
- **Type Tracking:** Real-time monitoring of `var` types (`int`, `float`, `str`) within the execution environment.
- **Lightweight Interpreter:** Written in Python, making it highly portable and easy to extend.
- **Explicit Declaration:** Employs the `:=` operator for type-inferred variable creation, stopping accidental global overwrites.

## 🚀 Quick Start
**Installation**  
Ensure you have **Python 3.10+** installed. Clone the repository and ignite the engine:

*Bash (or Powershell)*  
`git clone https://github.com/SpideyBash4116/aether.git`  
`cd aether`  
`python aether.py`

**Basic Syntax**  
Aether bridges the gap between its parent languages:

>**Python**

`// Go-style declaration
mana := 100
// Python-style operation
power := mana * 2 + 5
// Re-assignment (error if var doesn't exist)
mana = 150`


### Persistence Example
Save and load interpreter memory:
`æ> mana := 100 æ> save session.json æ> load session.json`


### 🛠 Architecture
Aether follows the **classic Interpreter Design Pattern**:

**Lexer:** Tokenizes raw input strings using Regular Expressions.

**Parser:** A Recursive Descent Parser that builds an **Abstract Syntax Tree (AST)**.

**Visitor Engine:** Walks the AST to execute logic in a persistent global environment.

### 💻 REPL Commands
|Command|Action|
|`help`|View the interactive syntax guide|
|`vars`|Display all current variables, their types, and values|
|`clear`|Wipe the terminal screen|
|`save <file>`|Save memory to a JSON file|
|`load <file>`|Load memory from a JSON file|
|`del <name>`|Delete a variable from memory|
|`history`|Show session command history|
|`exit`|Safely close the interpreter|

## v0.1.2-alpha — Safe Eval & Persistence
**Status:** `v0.1.2-alpha` (patch release)

This release focuses on security and usability improvements:

- Replaced unsafe use of `eval()` with a safe, restricted AST-based evaluator to prevent arbitrary code execution and to control supported expressions.
- Added JSON persistence: `save <file>` and `load <file>` to export/import interpreter memory.
- Added variable management and session utilities: `del <name>` to remove a variable, and `history` to view the current session's command history.
- Minor UX: updated help text and the version string shown in the REPL.

### Security note
The interpreter now evaluates expressions using a whitelisted AST walker; function calls, attribute access, and other execution-capable AST nodes are disallowed. This reduces the risk of arbitrary code execution when running untrusted input.

### Roadmap (progress)
- [x] Basic Arithmetic & Variables
- [x] Go-style `:=` Implementation
- [x] Meta-command System (`help`, `clear`, `vars`)
- [x] Replace unsafe `eval()` with safe AST-based evaluator
- [x] Persistence (`save`/`load`) and variable management (`del`, `history`)
- [ ] Boolean Logic & Comparisons (`==`, `>`, `<`) — partial support via AST
- [ ] Pythonic `if`/`else` Indentation Blocks
- [ ] Lightweight "Aether-routines" (Concurrency)

### 🤝 Contributing
We welcome "Alchemists" to help refine the Aether. Feel free to open an issue or submit a pull request if you want to add new Nodes to our AST.
