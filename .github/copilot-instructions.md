## Repo snapshot

- Small Python project implementing a Mastermind-style number guessing game.
- Key files: `logic.py` (pure logic: calc_response), `master_mind.py` (CLI game loop),
  `two_player_mode.py` (two-player mode with alternating roles and round tracking),
  `test_master_mind_logic.py` (pytest-style unit tests).

## What to know up-front

- calc_response(secret, guess, number_of_digits) in `logic.py` works on integer values (uses % and //)
  and returns a string with all exact matches (`*`) first then value-but-wrong-place matches (`+`).
- Tests assume this ordering and the signature. Keep output formatting and ordering unchanged when changing logic.
- `master_mind.py` imports `calc_response` and drives the interactive CLI. It validates numeric ranges using
  NUMBER_0F_DIGITS (note the 0 character used in the constant name).

## Typical developer tasks & commands

- Run the game (interactive):
  - python3 master_mind.py — main menu with options for single-player (vs computer) or two-player mode.
  - Note: `readme.md` references `mastermind.py` which does not exist; use `master_mind.py`.
- Run tests (pytest):
  - python3 -m pytest -q
  - Single file: python3 -m pytest -q test_master_mind_logic.py
- Two-player mode can also be run directly:
  - python3 two_player_mode.py — infinite match where each player gets one guess per round, with option to continue or stop.

## Project-specific patterns and gotchas (for an AI agent)

- Integers not strings: digits are processed numerically. Don't refactor calc_response to use string operations
  unless you preserve exact behavior (padding, ordering of `*` and `+`, and handling of leading zeros in formatting).
- The code uses a fixed digit width formatting in `master_mind.py` (e.g. `{{guess:04}}`). Maintain that when changing printouts.
- Variable naming quirks: `NUMBER_0F_DIGITS` uses the digit `0` instead of the letter `O`. Search for that exact symbol when editing.
- Tests iterate over ranges like `range(10**dig_num)` — avoid slowdowns in new tests by keeping them focused and small.
- Two-player mode (`two_player_mode.py`) uses `clear_screen()` to hide the secret code after entry. Each player keeps guessing until they crack the code. Scoring tracks total guesses across rounds — fewer is better. Game is infinite with y/n continue prompt at round end.

## Where to change behavior safely

- Pure logic: `logic.py` — safe to refactor as long as the public contract (inputs/outputs) is preserved.
- CLI & UX: `master_mind.py` — change prompts, help text, or add options here. Keep input validation for numeric range intact.
- Two-player mode: `two_player_mode.py` — add rounds, change scoring, or adjust player flow. Uses `clear_screen()` to hide codes.
- Tests: `test_master_mind_logic.py` — update tests only if you intentionally change calc_response contract; otherwise update code to satisfy tests.

## Examples to reference when writing or fixing code

- Exact-match behavior: `test_exact_match()` asserts calc_response(i, i, 4) == "\*\*\*\*"
- Partial-match example: calc_response(1268, 6218, 4) == "\*\*++" (see `test_partial_match`)

## Suggested priorities for changes

1. Preserve `calc_response` signature and output ordering.
2. When modifying CLI, keep existing commands: s (start), i (instructions), h (help), q (quit), and game-level q/h.
3. Keep tests fast — avoid adding exhaustive loops unless necessary.

## If you need to run or extend tests

- Use pytest; keep edits minimal and run `python3 -m pytest -q` locally.
- If you refactor `calc_response`, run tests and update `test_master_mind_logic.py` to match new contract.

---

If anything here is unclear or you'd like the instructions to be shorter/longer or to include examples of common edits (e.g., adding a new validation or refactoring to string-based digits), tell me which sections to change and I'll update the file.
