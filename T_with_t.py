from tkinter import *
from PIL import Image, ImageTk
from playsound import playsound

if __name__ == '__main__':

    main_menu = Tk()    #main menu window
    menu_canvas = Canvas(main_menu, height = 580, width = 600)  #Canvas
    menu_canvas.pack()

    #Main Menu Background
    bg_img = ImageTk.PhotoImage(Image.open("Images\MainMenu.jpg"))  #Making .jpg format compatible with tkinter
    bg_img_label = Label(menu_canvas, image = bg_img)               #Using background image as label
    bg_img_label.place(relheight = 1, relwidth = 1)                 #placeing background image


    playsound('Sounds\MainMenu.mp3',False)



    #Main Menu Buttons

    #Play Button
    play_button = Button(menu_canvas, text = 'Play', bg = '#E3CBB9', relief = 'groove', padx = 1, pady = 1)
    play_button.place(relx = 0.7, rely = 0.5, relheight = 0.08, relwidth = 0.25)

    #Options Button
    options_button = Button(menu_canvas, text = 'Options', bg = '#E3CBB9', relief = 'groove', padx = 1, pady = 1)
    options_button.place(relx = 0.7, rely = 0.6, relheight = 0.08, relwidth = 0.25)

    #Exit Button
    exit_button = Button(menu_canvas, text = 'Exit', bg = '#E3CBB9', relief = 'groove', padx = 1, pady = 1)
    exit_button.place(relx = 0.7, rely = 0.7, relheight = 0.08, relwidth = 0.25)



    main_menu.mainloop()
