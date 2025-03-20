# Conveyor Belt PLC Simulation

## Overview
This project is a **Conveyor Belt PLC Simulation** built in Python and designed to mimic real-world industrial automation. It includes a **Graphical User Interface (GUI)** for control and a **Ladder Logic Diagram** that was made in https://app.plcsimulator.online/.

## Features
✅ **Start Button** – Begins belt movement and auto-scans objects.

✅ **Object Scanning** – Detects items and determines if they should pass or be removed. 

✅ **Decision Logic** – Items flagged as 'REMOVE' are discarded from the belt and not in final count. 

✅ **Object Pass Counter** – Keeps track of how many items successfully pass.  

✅ **24-Second Timer** – Simulates a full day (1 sec = 1 hour), stopping all functions after 24s.  

✅ **Emergency Stop** – Instantly halts operations.  

✅ **Ladder Logic Diagram** – Can be used in an online PLC simulator.  

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/jayden-mosley/Conveyor-Belt-PLC.git
   cd Conveyor-Belt-PLC
   ```
2. Install dependencies (if required):
   ```bash
   pip install tkinter
   ```
3. Run the simulation:
   ```bash
   python conveyor_belt.py
   ```

## How It Works
- The **GUI** displays the conveyor belt and allows user interaction (the scan button can be a bit dramtic so don't press it too much).  
- Items move along the belt and are either kept or removed based on scanning logic which is mostly random  
- After **24 seconds**, the simulation automatically stops and displays the total count of passed items.  

## Ladder Logic Implementation
image

## Future Improvements
- implement animated visualisation of the conveyor belt movement  
- Improve randomness in object detection and fix the scan button 
- Expand Ladder Logic with more PLC features like speed control

## Author
**Jayden Mosley**  
[GitHub](https://github.com/jayden-mosley)  
[LinkedIn](https://linkedin.com/in/jayden-mosley)  

---
*Built for industrial automation & PLC control simulation*
