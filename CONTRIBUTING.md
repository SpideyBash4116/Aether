# Contributing to Aether

Thank you for your interest in contributing to Aether (Æther). This document explains how to contribute, the project's coding and documentation preferences, and the canonical wiki sidebar structure used by the project.

Please read this document carefully before opening issues or pull requests. Small, focused contributions are preferred.

---
## Quick start
- Fork the repository and create a branch from `main`:
  - Feature branches: `feat/<short-description>`
  - Fix branches: `fix/<short-description>`
  - Docs: `docs/<short-description>`
- Keep each pull request focused on a single change or logical set of changes.
- Add tests for new functionality and ensure all tests pass locally.

---
## Code style & formatting
- This project follows the rules in the repository's `.editorconfig`. Always obey `.editorconfig` where present (indentation, line endings, encoding, naming conventions).
- For Python code, follow PEP 8 where it does not conflict with `.editorconfig`.
- Use 4 spaces for indentation unless `.editorconfig` specifies otherwise.
- File encoding: UTF-8 without BOM.
- Limit lines to 88 characters where reasonable.
- Use descriptive names for functions, classes, and variables. Public APIs should include docstrings.

Recommended tools
- Use `black` for formatting, `flake8` for linting, and `isort` for sorting imports where practical.

---
## Tests
- Add unit tests for new features or bug fixes under the `tests/` directory.
- Use `pytest` for tests. Keep tests small and deterministic.
- Run tests locally before submitting a PR: `pytest -q`.

---
## Commit messages
- Use imperative, present-tense style (e.g., "Add safe AST evaluator").
- Keep the subject line short (<=72 chars) and add a body when necessary describing the "why".
- Reference issues using `Fixes #123` or `Closes #123` when appropriate.

---
## Pull request process
1. Open an issue first for non-trivial features or design changes.
2. Create a branch from `main` and implement your changes.
3. Ensure unit tests pass and add tests for the new behavior.
4. Update `README.md`, wiki pages, or other documentation as needed.
5. Open a pull request with a clear title and description. Include screenshots or examples when relevant.
6. A maintainer will review your PR. Address review comments and push follow-up commits to the same branch.
7. Once approved, a maintainer will merge the PR. Squash merging may be used.

Checklist for PRs (what reviewers will look for)
- [ ] Tests added or updated
- [ ] Documentation updated if behavior or API changed
- [ ] Code follows `.editorconfig` and PEP 8
- [ ] No debug or commented-out code left behind
- [ ] Clear, descriptive commit history

---
## Branching & releases
- `main` contains the release-ready code.
- Use semantic versioning for releases (e.g., `v0.1.2-alpha`).
- Create release branches/tags when preparing a new release.

---
## Documentation
- Keep documentation in `README.md` for the top-level overview and create detailed pages in the project wiki for in-depth topics.
- Update the README for changes that affect getting started or core behavior.
- Include runnable examples in docs where possible.

---
## Wiki Sidebar (canonical)
To keep the project documentation consistent, use this exact wiki sidebar structure and page titles. Place the most-used pages near the top.

1. Home — Overview, links to core docs and quick start.
2. Getting Started — Installation, running the REPL, minimal examples.
3. Language Guide
   - Syntax & Expressions — declarations, assignment, operators
   - Types & Values — primitives, lists, dicts
   - Control Flow (future) — if/else, loops, indentation rules
4. REPL Commands — `help`, `vars`, `save`, `load`, `del`, `history`, `exit`
5. Examples & Recipes — short, focused programs and patterns
6. Architecture & Internals
   - High-level overview
   - Lexer & Parser
   - AST Nodes (detailed reference)
   - Visitor/Interpreter implementation
7. Security & Sandbox — safe-eval design, limitations, best practices
8. Persistence & File Formats — save/load behavior and JSON format notes
9. Roadmap & Releases — milestones, release notes, changelog
10. API Reference (if applicable) — exported functions/modules
11. Contributing — contribution guide and coding standards
12. Tests & CI — how tests are organized and how to run them
13. FAQ & Troubleshooting — common issues and fixes
14. Community & Contact — repo, issue tracker, communication channels

Notes:
- Keep page slugs stable; avoid renaming pages without updating links and the sidebar.
- Use concise page titles and organize subpages under their parent topic.

---
## Security & reporting vulnerabilities
- Do not disclose security vulnerabilities publicly. Open a private issue if the repository settings allow, or contact a maintainer directly.
- If you discover a vulnerability, include reproduction steps and a suggested mitigation strategy.

---
## License & Code of Conduct
- Include a `LICENSE` file at the repository root (recommended: MIT).
- Consider adding `CODE_OF_CONDUCT.md` to set community expectations. If present, abide by it when interacting in issues and PRs.

---
## Support & Contacts
- Open issues for bugs and feature requests.
- For questions about contributing, open an issue labelled `help wanted` or `discussion`.
- Maintainers will monitor issues and PRs on `main`.

---
Thank you for helping improve Aether. We appreciate clear, focused contributions and constructive feedback.
