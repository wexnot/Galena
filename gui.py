import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle

class ImageLabel(tk.Label):
    """
    A Label that displays images, and plays them if they are gifs

    :im: A PIL Image instance or a string filename
    """
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)

switch = True

def change():
    global switch
    if switch == False:
        lbl.unload()
        lbl.load("myGalena.gif")
        switch = True
    else:
        lbl.unload()
        lbl.load("newGalena.gif")
        switch = False

root = tk.Tk()
lbl = ImageLabel(root)
lbl.pack()
btn = tk.Button(root, text="Happy", command=change)
btn.pack()
lbl.load('myGalena.gif')
root.mainloop()
