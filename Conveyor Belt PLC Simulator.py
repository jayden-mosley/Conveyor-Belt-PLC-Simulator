#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 16:13:05 2025

@author: JaydenAndrew
"""

import tkinter as tk
import random

running = False
items_on_belt = []
objects_passed = 0
time_remaining = 24

def start_conveyor():
    global running, items_on_belt, objects_passed, time_remaining
    running = True
    items_on_belt = []
    objects_passed = 0
    time_remaining = 24
    status_label.config(text="Conveyor Running...")
    update_timer()
    update_belt()

def stop_conveyor():
    global running
    running = False
    status_label.config(text=f"Status: Stopped. Total Passed: {objects_passed}")

def scan_item():
    if not running:
        return
    
    item = random.choice(["OK", "REMOVE", "OK", "OK", "REMOVE"])
    items_on_belt.append(item)
    status_label.config(text=f"Scanned: {item}")
    
    if item == "REMOVE":
        items_on_belt.remove(item)
        status_label.config(text="Item Removed!")
    
    update_belt()

def update_belt():
    global objects_passed
    if running:
        belt_canvas.delete("all")
        belt_canvas.create_rectangle(20, 40, 380, 80, fill="grey")
        x_pos = 30
        for item in items_on_belt:
            color = "green" if item == "OK" else "red"
            belt_canvas.create_oval(x_pos, 50, x_pos+20, 70, fill=color)
            x_pos += 40
        
        if len(items_on_belt) > 5:  # If item reaches the end
            objects_passed += 1
            status_label.config(text=f"Object Passed! Next Object. Total Passed: {objects_passed}")
            items_on_belt.pop(0)
        
        root.after(1000, scan_item)  # Auto-scan every second

def update_timer():
    global time_remaining
    if time_remaining > 0 and running:
        time_remaining -= 1
        timer_label.config(text=f"Time Remaining: {time_remaining}s")
        root.after(1000, update_timer)
    elif time_remaining == 0:
        stop_conveyor()
        status_label.config(text=f"Time's up! Total Passed: {objects_passed}")

def reset_counter():
    global objects_passed, time_remaining
    objects_passed = 0
    time_remaining = 24
    status_label.config(text="Counter Reset. Ready for new items.")
    timer_label.config(text=f"Time Remaining: {time_remaining}s")



# GUI Setup
root = tk.Tk()
root.title("Conveyor Belt PLC Simulation")

belt_canvas = tk.Canvas(root, width=400, height=100, bg="white")
belt_canvas.pack()

timer_label = tk.Label(root, text=f"Time Remaining: {time_remaining}s", font=("Arial", 12))
timer_label.pack()

status_label = tk.Label(root, text="Status: Stopped", font=("Arial", 12))
status_label.pack()

start_button = tk.Button(root, text="Start", command=start_conveyor)
start_button.pack(side=tk.LEFT, padx=5, pady=10)

scan_button = tk.Button(root, text="Scan Item", command=scan_item)
scan_button.pack(side=tk.LEFT, padx=5, pady=10)

stop_button = tk.Button(root, text="Emergency Stop", command=stop_conveyor, bg="red")
stop_button.pack(side=tk.LEFT, padx=5, pady=10)

reset_button = tk.Button(root, text="Reset Counter", command=reset_counter)
reset_button.pack(side=tk.LEFT, padx=5, pady=10)

root.mainloop()