import tkinter
import tkinter.ttk
from PIL import Image, ImageTk

window = tkinter.Tk()
window.title('BMI calculator')
window.geometry('470x580+700+200')
window.resizable(False, False)


logo_img = tkinter.PhotoImage(file='bin/icon.png')
window.iconphoto(False, logo_img)


#top

top_img = tkinter.PhotoImage(file='bin/top.png')
top = tkinter.Label(master=window, image=top_img)
top.place(x=-10, y=0)

# bottom
bottom = tkinter.Label(master=window, bg='lightblue', width=72, height=18)
bottom.place(x=0, y=305)

# 2 boxes
box_img = tkinter.PhotoImage(file='bin/box.png')
box_1 = tkinter.Label(master=window, image=box_img)
box_1.place(x=20, y=100)
             
box_2 = tkinter.Label(master=window, image=box_img)
box_2.place(x=240, y=100)


# 2 entries

height_var = tkinter.StringVar()
height_var.set('0')

height_entry = tkinter.Entry(
    master=window,
    textvariable=height_var,
    width=5,
    font=('arial', 50),
    bd=0,
    bg='lightblue',
    #fg='white',
    justify='center',
)
height_entry.place(x=35, y=160)


weight_var = tkinter.StringVar()
weight_var.set('0')

weight_entry = tkinter.Entry(
    master=window,
    textvariable=weight_var,
    width=5,
    font=('arial', 50),
    bd=0,
    bg='lightblue',
    #fg='white',
    justify='center',
)
weight_entry.place(x=255, y=160)


# 2 SLIDER

def height_slider_changed(event):
    event = float(event)
    height_var.set(f'{event:.0f}')

    weight = int(weight_var.get())

    avatar_img_pil = Image.open('bin/man.png')

    avatar_img_pil = avatar_img_pil.resize([100 + int(weight * 0.5), 50 + int(event * 0.94)])
    



    avatar_img_tk = ImageTk.PhotoImage(avatar_img_pil)
    avatar['image'] = avatar_img_tk
    avatar.image = avatar_img_tk
    avatar.place(x=100 + int(event * 0.01), y=525 - int(event * 0.94))

style = tkinter.ttk.Style()
style.configure('TScale', background='white')


height_slider = tkinter.ttk.Scale(
    master=window,
    #orient='horizontal'
    command=height_slider_changed,
    from_=0,
    to=220
)
height_slider.place(x=80, y=250)

def weight_slider_changed(event):
    event = float(event)
    weight_var.set(f'{event:.0f}')
    
    height = int(height_var.get())
    
    avatar_img_pil = Image.open('bin/man.png')

    avatar_img_pil = avatar_img_pil.resize([100 + int(event * 0.5), 50 + int(height * 0.94)])
    

    avatar_img_tk = ImageTk.PhotoImage(avatar_img_pil)
    avatar['image'] = avatar_img_tk
    avatar.image = avatar_img_tk
    avatar.place(x=100 + int(event * 0.01), y=525 - int(height * 0.94))


weight_slider = tkinter.ttk.Scale(
    master=window,
    #orient='horizontal',
    command=weight_slider_changed,
    from_=0,
    to=220
)
weight_slider.place(x=300, y=250)

#Scale

scale_img = tkinter.PhotoImage(file='bin/scale.png')
tkinter.Label(master=window, image=scale_img, bg='lightblue' ).place(x=0, y=320)

# Result button


def bmi_value():
    h = int(height_var.get()) / 100
    w = int(weight_var.get())

    bmi = w / (h**2)
    print(bmi)
    output_label['text'] = f'{bmi:.1f}'

result_button = tkinter.Button(
    master=window,
    font=('arial', 10, 'bold'),
    text='View Result',
    bg='grey5',
    fg='lightblue',
    command=bmi_value
)
result_button.place(x=380, y=300)

# Output Label

output_label = tkinter.Label(
    master=window,
    text='0',
    bg='lightblue',
    fg='grey100',
    font=('arial', 25)
)    
output_label.place(x=380, y=350)


# Person avatar
avatar = tkinter.Label(
    master=window,
    bg='lightblue'
    
)
avatar.place(x=100, y=360)

    




window.mainloop()
















