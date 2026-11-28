from tkinter import *

window = Tk()
window.title("My Profile Card")
window.geometry("400x380")

title = Label(window, text="My Profile Card", bg="light blue", fg="black", width=40)
title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

name_label = Label(window, text="Name:", bg="light blue", fg="black")
name_label.grid(row=1, column=0, padx=10, pady=5)

name_entry = Entry(window, fg="black", bg="pink", width=25)
name_entry.grid(row=1, column=1, padx=10, pady=5)

hobby_label = Label(window, text="Hobby:", bg="light blue", fg="black")
hobby_label.grid(row=2, column=0, padx=10, pady=5)

hobby_entry = Entry(window, fg="black", bg="pink", width=25)
hobby_entry.grid(row=2, column=1, padx=10, pady=5)

country_label = Label(window, text="Country:", bg="light blue", fg="black")
country_label.grid(row=3, column=0, padx=10, pady=5)

country_entry = Entry(window, fg="black", bg="pink", width=25)
country_entry.grid(row=3, column=1, padx=10, pady=5)

food_label = Label(window, text="Favorite Food:", bg="light blue", fg="black")
food_label.grid(row=4, column=0, padx=10, pady=5)

food_entry = Entry(window, fg="black", bg="pink", width=25)
food_entry.grid(row=4, column=1, padx=10, pady=5)

futureprofession_label = Label(window, text="Future Profession:", bg="light blue", fg="black")
futureprofession_label.grid(row=5, column=0, padx=10, pady=5)

futureprofession_entry = Entry(window, fg="black", bg="pink", width=25)
futureprofession_entry.grid(row=5, column=1, padx=10, pady=5)

birthdate_label = Label(window, text="Birthdate:", bg="light blue", fg="black")
birthdate_label.grid(row=6, column=0, padx=10, pady=5)

birthdate_entry = Entry(window, fg="black", bg="pink", width=25)
birthdate_entry.grid(row=6, column=1, padx=10, pady=5)

zodiacsign_label = Label(window, text="Zodiac Sign:", bg="light blue", fg="black")
zodiacsign_label.grid(row=7, column=0, padx=10, pady=5)

zodiacsign_entry = Entry(window, fg="black", bg="pink", width=25)
zodiacsign_entry.grid(row=7, column=1, padx=10, pady=5)

about_frame = Frame(window, relief=RAISED, borderwidth=1)
about_frame.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

about_label = Label(about_frame, text="About Me:")
about_label.pack()

about_text = Text(about_frame, height=5, width=30)
about_text.pack()

submit = Button(window, text="Show My card", bg="grey", fg="black", width=10)
submit.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()