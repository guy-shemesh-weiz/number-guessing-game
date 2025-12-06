# 🎯 Mastermind

_Mastermind_ is a small, terminal-based number-guessing game (Bulls & Cows style).

Your mission: decode the secret number in as few guesses as possible.

Key files

- `logic.py` — core logic: `calc_response(secret, guess, number_of_digits)` (integer-based, returns `*` then `+`).
- `master_mind.py` — single-player CLI (computer picks a secret) with leaderboard integration.
- `scoreboard.py` — persistent leaderboard: loads/saves scores to `leaderboard.json`, tracks high scores.
- `two_player_mode.py` — two-player CLI (players set secrets for each other).
- `test_master_mind_logic.py` — pytest test coverage for `calc_response`.
- `test_logic_extra.py` — additional unit tests (leading zeros, repeated digits, variable widths).

How it works (short)

- `*` means exact digit+position match.
- `+` means correct digit but wrong position.

Example: secret `4271`, guess `1234` → feedback `*++` (`1` exact, `2` and `4` misplaced).

## ▶️ How to run

Single-player (computer sets secret):

```bash
python3 master_mind.py
```

Menu options available in the main CLI:

- `s` — start single-player game (vs computer)
- `p` — play two-player mode
- `l` — show leaderboard (top 10 scores)
- `i` — print instructions
- `h` — print help
- `q` — quit

**Leaderboard**

- After each successful game, you'll be prompted to enter your name.
- Your score (number of guesses) is saved to `leaderboard.json`.
- Leaderboard is persistent across runs: fewer guesses = better score.
- "New high score" message appears when you beat the previous best.

Two-player (local, shared console)

```bash
python3 two_player_mode.py
```

- Players enter names, then take turns setting a secret and trying to crack the other player's secret.
- Each guessing turn continues until the guesser cracks the secret (or quits).
- Scores are tracked as total guesses across rounds (fewer is better).
- The match is infinite: after each round players are prompted to continue or stop.

## Tests

Run the unit tests for core logic using pytest:

```bash
python3 -m pytest -q
```

Or run specific test files:

```bash
python3 -m pytest -q test_master_mind_logic.py
python3 -m pytest -q test_logic_extra.py
```

## Notes for contributors / AI agents

- `calc_response(secret, guess, number_of_digits)` is integer-based (uses `%` and `//`). Tests and other code expect exact ordering of `*` before `+`.
- Formatting uses fixed-width zero-padded numbers (e.g. `{{guess:04}}`) — preserve when changing printouts.
- `NUMBER_0F_DIGITS` (note the digit `0`) is used in `master_mind.py`.
- When editing two-player flow, `two_player_mode.py` uses `clear_screen()` to avoid leaving secrets visible in the console.
- Leaderboard data is stored in `leaderboard.json` (auto-created). See `scoreboard.py` for the data schema.
