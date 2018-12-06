import Tkinter as tk
import cv2

class MyVideoCapture:
     def __init__(self, video_source=0):
         # Open the video source
         self.vid = cv2.VideoCapture(video_source)
         if not self.vid.isOpened():
             raise ValueError("Unable to open video source", video_source)

         # Get video source width and height
         self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
         self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

     # Release the video source when the object is destroyed
     def __del__(self):
         if self.vid.isOpened():
            self.vid.release()
         self.window.mainloop()

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        #super().__init__()
        tk.Tk.__init__(self)

        self.title("This is the MainWindow")
        self._is_hidden = False


    def toggle_hide(self):
        if self._is_hidden:
            self.iconify()
            self.deiconify()
        else:
            self.withdraw()

        self._is_hidden = not self._is_hidden

class OtherWindow(tk.Toplevel):
    def __init__(self, master, *args, **kwargs):
        #super().__init__(master)
        tk.Toplevel.__init__(self, master)

        if 'title' in kwargs:
            self.title(kwargs['title'])

        self.hide_main_button = tk.Button(self, text="Hide/Show MainWindow")
        self.hide_main_button['command'] = self.master.toggle_hide
        self.hide_main_button.pack()

if __name__ == '__main__':
    root = MainWindow()
    root.mainloop()
