import tkinter

'''
Adjust GUI by changing width and height in window.minsize().
Changing column and row in item.grid() will move the positions of respective box, button or label.
If prior column or row isn't occupied, the first item can not be directly placed past these positions.
i.e. no item at (column=0, row=0), first item -!-> (column=1, row=1)
'''

# Create a GUI window.
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)

# Create an entry box to get user_input.
entry_box = tkinter.Entry(width=13)
# Place the box at desired location.
entry_box.grid(column=2, row=1)

# Create labels at appropriate locations.
# Place an empty label at the top of mid row so that entry box can be placed right under.
empty_label = tkinter.Label(text=" ")
empty_label.grid(column=1, row=0)
# Change desired font style.
mile_label = tkinter.Label(text="Miles", font=("Telugu MN", 22))
mile_label.grid(column=3, row=1)
equal_to_label = tkinter.Label(text="is equal to", font=("Telugu MN", 22))
equal_to_label.grid(column=0, row=2)
output_label = tkinter.Label(text=" ", font=("Telugu MN", 22))
output_label.grid(column=2, row=2)
km_label = tkinter.Label(text="Km", font=("Telugu MN", 22))
km_label.grid(column=3, row=2)


# When clicked, convert mile_input to km_output.
def button_clicked():
    # Get user_input for calculation.
    user_input = int(entry_box.get())
    distance_in_km = user_input * 1.609344
    # Change the text of output_label.
    output_label.config(text=f"{round(distance_in_km, 3)}")


# Create a "Calculate" button.
button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)

# To keep the window stay on.
window.mainloop()