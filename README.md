# Keyboard Piano (v1.0)

A simple **virtual piano** built with **Python** and **Pygame**.  
Play piano notes using your **computer keyboard**.  
It supports notes from **C3** to **C6**, using `.wav` samples for each note.

---

## Features
- Supports **C3 → C6** (three octaves)  
- Press keys to play the notes
- Press **ESC** to quit  

---

## Keyboard → Note Layout

| Octave | White Keys | Black Keys (Sharps `#`) |
|:-------|:------------|:------------------------|
| **C3–B3** | `q w e r t y u` | `2 3 5 6 7` |
| **C4–B4** | `i o p [ ] z x` | `9 0 = a s` |
| **C5–B5** | `c v b n m , .` | `f g j k l` |
| **C6** | `/` |  |

Each key corresponds to a note file in the `sounds/` folder:

## Requirements
- **Pygame**: install via `pip install pygame`

## How to Run

1. Open a terminal or command prompt in the project directory.  
2. Run the program with:

```
python main_simple.py
```
