# _____Copyright © 2024 FaroukAshraf_____

# _________Libraries__________
import ttkbootstrap as ttk
from tkinter import PhotoImage


def Reversing():
    # ________Main_Window________

    window1 = ttk.Window()
    window1.title("Reversing Mutation")
    window1.geometry("920x520")
    window1.configure(bg = "#AAD7FF")
    window1.position_center()


    # ________Canvas________
    canvas = ttk.Canvas(
        window1,
        height = 480,
        width = 880
    )
    canvas.place(x = 20, y = 20)
    
    canvas.create_rectangle(
        14,
        19,
        886,
        481,
        fill="#FFFFFF",
        outline="")
    
    # ________Images________
    Photo = PhotoImage(master = window1, file = r"libs\assets\Reversing.png")
    label = ttk.Label(master= window1, image= Photo)
    label.place(x=60 , y=305)


    # ________Text________
    canvas.create_text(
        23,
        40,
        anchor="nw",
        text="How does Reversing Mutation work?",
        fill="#000000",
        font=("K2D Medium", 24 * -1)
    )

    canvas.create_text(
        10,
        65,
        anchor="nw",
        text="""
    Reversing Mutation: A random position is chosen or more and the bits next to that position 
    are reversed and child chromosome is produced.
            """,
        fill="#0063BC",
        font=("K2D Medium", 20 * -1)
    )

    canvas.create_text(
        120,
        240,
        anchor="nw",
        text="Before Mutation",
        fill="#000000",
        font=("K2D Medium", 20 * -1)
    )

    canvas.create_text(
        600,
        240,
        anchor="nw",
        text="After Mutation",
        fill="#000000",
        font=("K2D Medium", 20 * -1)
    )


    window1.mainloop()

if __name__ == "__main__":
    Reversing()