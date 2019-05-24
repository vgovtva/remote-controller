#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4 sw=4 tw=100 et ai si

"""This module holds classes which define our GUI."""

import tkinter.ttk as ttk
from collections import OrderedDict
from dependencies.viewidget import Dial, Digit
from modules.VideoStream import VideoStream

class Window:
    """A class that reprensents the window of the application."""

    def __init__(self, top, gui):
        self.window = gui
        self.top_level = top
        self.root = top

    def destroy_window(self):
        # Function which closes the window.
        self.top_level.destroy()
        self.top_level = None

class Toplevel1:
    """This is  the application itself. It holds information about the contents."""

    def update_dials(self, data):
        """Update the values of dials."""

        for key in self.dials:
            if key in data:
                self.dials[key].set_value(data[key])

    def __init__(self, top, cams, tk):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        self.thread_cam1 = None
        self.thread_cam2 = None
        self.thread_cam3 = None

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("2560x1377+166+0")
        top.title("RakkaGuiProto")
        top.configure(background="#d9d9d9")

        self.Labelframe1 = tk.Label(top)
        self.Labelframe1.place(relx=0.004, rely=0.007, relheight=0.657
                , relwidth=0.629)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Camera 1''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(width=1610)

        self.Labelframe2 = tk.Label(top)
        self.Labelframe2.place(relx=0.004, rely=0.668, relheight=0.301
                , relwidth=0.313)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(foreground="black")
        self.Labelframe2.configure(text='''Camera 2''')
        self.Labelframe2.configure(background="#d9d9d9")
        self.Labelframe2.configure(width=800)

        self.Labelframe3 = tk.Label(top)
        self.Labelframe3.place(relx=0.32, rely=0.668, relheight=0.301
                , relwidth=0.313)
        self.Labelframe3.configure(relief='groove')
        self.Labelframe3.configure(foreground="black")
        self.Labelframe3.configure(text='''Camera 3''')
        self.Labelframe3.configure(background="#d9d9d9")
        self.Labelframe3.configure(width=800)

        self.Labelframe4 = tk.LabelFrame(top)
        self.Labelframe4.place(relx=0.637, rely=0.007, relheight=0.962
                , relwidth=0.355)
        self.Labelframe4.configure(relief='groove')
        self.Labelframe4.configure(foreground="black")
        self.Labelframe4.configure(text='''Engine parameters''')
        self.Labelframe4.configure(background="#d9d9d9")
        self.Labelframe4.configure(width=910)

        self.TSeparator1 = ttk.Separator(self.Labelframe4)
        self.TSeparator1.place(relx=-0.011, rely=0.02, relwidth=1
                , bordermode='ignore')

        self.TSeparator2 = ttk.Separator(self.Labelframe4)
        self.TSeparator2.place(relx=0.0, rely=0.306, relwidth=0.989
                , bordermode='ignore')

        self.TSeparator3 = ttk.Separator(self.Labelframe4)
        self.TSeparator3.place(relx=0.363, rely=0.306, relheight=0.242
                , bordermode='ignore')
        self.TSeparator3.configure(orient="vertical")

        self.TSeparator4 = ttk.Separator(self.Labelframe4)
        self.TSeparator4.place(relx=0.0, rely=0.55, relwidth=1
                , bordermode='ignore')

        speed= 0
        self.Custom1 = Dial(self.Labelframe4, size=300, unit='    Km/h', min = 0, max = 60, value=speed)
        self.Custom1.place(relx=0.001, rely=0.31, relheight=0.24, relwidth=0.361
                , bordermode='ignore')

        pitch = 0
        self.Custom2 = Dial(self.Labelframe4, size = 350, unit='    Pitchdeg', min = -60, max = 60, start=180, extent=-180, value=pitch)
        self.Custom2.place(relx=0.001, rely=0.021, relheight=0.284, relwidth=0.41
                , bordermode='ignore')
        roll = 0
        self.Custom3 = Dial(self.Labelframe4, size = 350, unit='    Rolldeg', min = -60, max = 60, start=180, extent=-180, value=roll)
        self.Custom3.place(relx=0.41, rely=0.021, relheight=0.284, relwidth=0.41
                , bordermode='ignore')

        fuel = 0
        self.Custom4 = Dial(self.Labelframe4, size=200, unit='\n\nFuel%', min = 0, max = 100, value=fuel)
        self.Custom4.place(relx=0.37, rely=0.31, relheight=0.16, relwidth=0.23
                , bordermode='ignore')
        voltage = 0
        self.Custom5 = Dial(self.Labelframe4, size=200, unit='V', min = 10, max = 20,  majorscale=1, value=voltage)
        self.Custom5.place(relx=0.6, rely=0.31, relheight=0.16, relwidth=0.23
                , bordermode='ignore')


        oillevel = 0
        self.Custom7 = Dial(self.Labelframe4, size=200, unit='\n\nOil%', min = 0, max = 100, value=fuel)
        self.Custom7.place(relx=0.6, rely=0.47, relheight=0.16, relwidth=0.23
                , bordermode='ignore')

        enginetemp = 0
        self.Custom8 = Dial(self.Labelframe4, size=200, unit='\n\nEngdegC', min = 0, max = 100, value=enginetemp)
        self.Custom8.place(relx=0.37, rely=0.63, relheight=0.16, relwidth=0.23
                , bordermode='ignore')

        engineoilpres = 0
        self.Custom9 = Dial(self.Labelframe4, size=200, unit='\n\nEngOilpres', min = 0, max = 100, value=enginetemp)
        self.Custom9.place(relx=0.6, rely=0.63, relheight=0.16, relwidth=0.23
                , bordermode='ignore')

        self.Custom10 = Digit(self.Labelframe4, size=100, fg = 'white')
        self.Custom10.place(relx=0.001, rely=0.79, relheight=0.075, relwidth=0.1
                , bordermode='ignore')
        self.Custom11 = Digit(self.Labelframe4, size=100, fg = 'white')
        self.Custom11.place(relx=0.07, rely=0.79, relheight=0.075, relwidth=0.1
                , bordermode='ignore')
        self.Custom12 = Digit(self.Labelframe4, size=100, fg = 'white')
        self.Custom12.place(relx=0.14, rely=0.79, relheight=0.075, relwidth=0.1
                , bordermode='ignore')
        self.Custom13 = Digit(self.Labelframe4, size=100, fg='white')
        self.Custom13.place(relx=0.21, rely=0.79, relheight=0.075, relwidth=0.1
                            , bordermode='ignore')
        self.Custom14 = Digit(self.Labelframe4, size=100, fg='white')
        self.Custom14.place(relx=0.28, rely=0.79, relheight=0.075, relwidth=0.1
                            , bordermode='ignore')
        oiltemp = 0
        self.Custom6 = Dial(self.Labelframe4, size=200, unit='degC', min = 20, max = 120, value=oiltemp)
        self.Custom6.place(relx=0.37, rely=0.47, relheight=0.16, relwidth=0.23
                , bordermode='ignore')

        self.Custom15 = Digit(self.Labelframe4, size=100, fg='red', value =1 )
        self.Custom15.place(relx=0.03, rely=0.88, relheight=0.075, relwidth=0.08
                            , bordermode='ignore')

        self.Custom16 = Digit(self.Labelframe4, size=100, fg='blue')
        self.Custom16.place(relx=0.15, rely=0.88, relheight=0.075, relwidth=0.08
                            , bordermode='ignore')

        self.Custom17 = Digit(self.Labelframe4, size=100, fg='green')
        self.Custom17.place(relx=0.27, rely=0.88, relheight=0.075, relwidth=0.08
                            , bordermode='ignore')
        rpm = 0
        self.Custom18 = Dial(self.Labelframe4, size=300, unit='\n\nRPM', min = 0, max = 5000, majorscale=200, semimajorscale=0, minorscale=0, casewidth=7, value=rpm)
        self.Custom18.place(relx=0.001, rely=0.55, relheight=0.24, relwidth=0.361
                , bordermode='ignore')

        self.dials = OrderedDict([("RPM", self.Custom18),
                                  ("oil_pressure", self.Custom9),
                                  ("eng_temp", self.Custom8),
                                  ("fuel", self.Custom4),
                                  ("battary_voltage", self.Custom5),
                                  ("body_roll", self.Custom3),
                                  ("body_pitch", self.Custom2),
                                  ("speed", self.Custom1)],)

        # First we must initialize all the streams, and only after that we can start them, otherwise
        # we encounter a RuntimeError. Tkinter library doesn't like when OpenCV is trying to
        # initalize a capture while a video loop thread is running.
        widths = {self.Labelframe3: 300, self.Labelframe2: 300, self.Labelframe1: 900}
        streams = []
        for frame, url in zip((self.Labelframe1, self.Labelframe2, self.Labelframe3), cams):
            streams.append(VideoStream(frame, url, widths[frame]))

        for stream in streams:
            stream.start()
