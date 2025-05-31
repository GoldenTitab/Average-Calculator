import tkinter as tk


def calculate_average():
    numbers = entry.get().split(" ")
    if numbers:
        total = 0
        count = 0
        for number in numbers:
            num = int(number)
            total += num
            count += 1
        average = total / count
        result_label.config(text=f"Average: {average}")


def clear_entries():
    entry.delete(0, tk.END)
    result_label.config(text="")


root = tk.Tk()
root.title("Average Calculator")

frame = tk.Frame(root)
frame.pack(pady=10)

entry_label = tk.Label(frame, text="Enter numbers separated by Space:")
entry_label.grid(row=0, column=0)

entry = tk.Entry(frame)
entry.grid(row=0, column=1)

calculate_button = tk.Button(frame, text="Calculate", command=calculate_average)
calculate_button.grid(row=1, column=0, pady=10)

clear_button = tk.Button(frame, text="Clear", command=clear_entries)
clear_button.grid(row=1, column=1, pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
