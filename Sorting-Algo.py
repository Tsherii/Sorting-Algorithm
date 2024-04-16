import tkinter as tk
import tkinter.scrolledtext as scrolledtext
from functools import partial

# Set the color scheme
BACKGROUND_COLOR = "#FFFFFF"  # White
TEXT_COLOR = "#000000"  # Black
BUTTON_COLOR = "#CCCCCC"  # Light Gray

# Set the font
FONT_FAMILY = "Helvetica"
FONT_SIZE = 12


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        yield arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr

def perform_sorting(sort_algorithm, elements, output_text):
    arr = list(map(int, elements.get().split()))
    output_text.delete('1.0', tk.END)
    output_text.update()

    if sort_algorithm.get() == "Bubble Sort":
        sort_generator = bubble_sort(arr)
    elif sort_algorithm.get() == "Insertion Sort":
        sort_generator = insertion_sort(arr)
    elif sort_algorithm.get() == "Selection Sort":
        sort_generator = selection_sort(arr)
    else:
        return

    for step, intermediate_arr in enumerate(sort_generator, start=1):
        output_text.insert(tk.END, f"Step {step}: {intermediate_arr}\n")
        output_text.update()

window = tk.Tk()
window.title("Sorting Algorithm by: Rodillon, Nerio, and Tilan  IT1R14")
window.geometry("500x400")  # Set the window size
window.configure(background=BACKGROUND_COLOR)


elements_label = tk.Label(window, text="Elements:", bg=BACKGROUND_COLOR, fg=TEXT_COLOR, font=(FONT_FAMILY, FONT_SIZE))
elements_label.pack()

elements_entry = tk.Entry(window, font=(FONT_FAMILY, FONT_SIZE))
elements_entry.pack()

algorithm_label = tk.Label(window, text="Algorithm:", bg=BACKGROUND_COLOR, fg=TEXT_COLOR, font=(FONT_FAMILY, FONT_SIZE))
algorithm_label.pack()

# Sort algorithm dropdown menu
sort_algorithm = tk.StringVar()
sort_algorithm.set("Bubble Sort")

algorithm_option_menu = tk.OptionMenu(window, sort_algorithm, "Bubble Sort", "Insertion Sort", "Selection Sort")
algorithm_option_menu.config(bg=BACKGROUND_COLOR, font=(FONT_FAMILY, FONT_SIZE), width=15)
algorithm_option_menu.pack()


# Output text area
output_text = scrolledtext.ScrolledText(window, width=40, height=10, font=(FONT_FAMILY, FONT_SIZE))
output_text.pack()


# Sort button
sort_button = tk.Button(window, text="Sort", command=partial(perform_sorting, sort_algorithm, elements_entry, output_text))
sort_button.config(bg=BUTTON_COLOR, font=(FONT_FAMILY, FONT_SIZE), width=15)
sort_button.pack(pady=10)  # Add padding below the button

window.mainloop()