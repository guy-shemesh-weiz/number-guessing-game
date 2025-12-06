# 🎯 Mastermind

*Mastermind* is a classic code-breaking logic game originally invented in Israel, inspired by the earlier pen-and-paper game **Bulls & Cows**.

Your mission: **decode the secret pattern in as few guesses as possible.**  
Clear rules, minimal setup, infinite fun.

---

## 📌 How It Works

The computer secretly generates a sequence of digits.  
You submit guesses — and receive hints:

| Symbol | Meaning |
|--------|---------|
| `*`    | Correct digit **in the correct position** |
| `+`    | Correct digit **but in the wrong position** |

**Example**

Secret: `4271`  
Guess: `1234`  
Feedback: `*++`  
- `1` is in the right spot  
- `2` & `4` are correct but misplaced

---

## ▶️ How to Play

Run the game from the terminal:

```bash
python mastermind.py
```


