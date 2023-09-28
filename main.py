from tkinter import *

def update():
  global label
  global text
  a = text.get('1.0', END).strip().lower()
  if a == 'mo':
    label.pack_forget()
    canvas.pack()
    canvas.itemconfig(contain, image=new_image1)
  elif a == 'katie':
    label.pack_forget()
    canvas.pack()
    canvas.itemconfig(contain, image=new_image2)
  elif a == 'gerald':
    label.pack_forget()
    canvas.pack()
    canvas.itemconfig(contain, image=new_image3)
  elif a == 'charlotte':
    label.pack_forget()
    canvas.pack()
    canvas.itemconfig(contain, image=new_image4)
  else:
    canvas.pack_forget()
    label.pack()
    pass
  
  
window = Tk()
window.geometry('450x450')
window.title('Guess Who')

text = Text(window, height=2, width=20)
text.pack()

button = Button(window, text='Find', command=lambda:update())
button.pack()

canvas = Canvas(window, height=200, width=200)

label = Label(window, text='Unable to find Image')

photo = PhotoImage(file='')
photo = photo.subsample(3)
  
new_image1 = PhotoImage(file='.tutorial/Guess Who/mo.png')
new_image1 = new_image1.subsample(3)
new_image2 = PhotoImage(file='.tutorial/Guess Who/katie.png')
new_image2 = new_image2.subsample(3)
new_image3 = PhotoImage(file='.tutorial/Guess Who/gerald.png')
new_image3 = new_image3.subsample(3)
new_image4 = PhotoImage(file='.tutorial/Guess Who/charlotte.png')
new_image4 = new_image4.subsample(3)

contain = canvas.create_image(100, 100, image=photo)
  
window.mainloop()