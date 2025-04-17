### 🧠 Monty Hall Problem Simulation

This project simulates the **Monty Hall Problem**—a famous probability puzzle—to demonstrate whether switching doors increases your chances of winning.

---

### 📊 Problem Summary

- You're on a game show with **3 doors**.
- Behind one door is a **car**, behind the other two are **goats**.
- You choose a door.
- The host, who knows what's behind each door, opens another door, revealing a goat.
- You're then given a choice: **Stick with your original door or switch** to the remaining unopened one.

**Should you switch? This simulation explores that!**

---

### 🚀 How It Works

- The program randomly hides the car behind one of the doors.
- The player randomly picks one door.
- The host opens one of the two remaining doors that has a goat.
- The simulation tracks:
  - Wins when the player **stays**
  - Wins when the player **switches**

---

### ✅ Results (after 10,000 trials)

```
No switch Wins = 3384 | 33.84%
Switch Wins    = 6616 | 66.16%
```

> You should see switching wins ~2/3rd of the time, while staying wins ~1/3rd.
---

### 🛠️ Technologies Used
- Python 3
- `random` module

---

### 📁 Files

- `monty_hall_simulation.py`: Main simulation script

---

### 🧠 Learn More
- [Monty Hall Problem – Wikipedia](https://en.wikipedia.org/wiki/Monty_Hall_problem)

---
