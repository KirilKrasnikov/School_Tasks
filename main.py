from tkinter import Tk

window = Tk()

width = 500
height = 350

window.geometry(f"{width}x{height}")
window.resizable(False, True)
window.title("WINDOW!!!!!!!")
window["bg"] = "#4c6"

def close(event):
	window.quit()

window.bind("<Escape>", close)

window.mainloop()