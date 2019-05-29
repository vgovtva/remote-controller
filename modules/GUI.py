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

        top.title('remote-controller')
        top.geometry('1680x1050')
        top.configure(background="#d9d9d9")


        top.frame = tk.Frame(top, relief='ridge', borderwidth=2)
        top.frame.pack(fill='both', expand=1)
        
        #   camera 1
        top.Labelframe1 = tk.Label(top)
        top.Labelframe1.place(relx=0.004, rely=0.007, relheight=0.657
                , relwidth=0.629)
        top.Labelframe1.configure(relief='groove')
        top.Labelframe1.configure(foreground="black")
        top.Labelframe1.configure(text='''Camera 1''')
        top.Labelframe1.configure(background="#d9d9d9")
        top.Labelframe1.configure(width=1610)

        #   camera 2
        top.Labelframe2 = tk.Label(top.frame)
        top.Labelframe2.place(relx=0.004, rely=0.668, relheight=0.301
                , relwidth=0.313)
        top.Labelframe2.configure(relief='groove')
        top.Labelframe2.configure(foreground="black")
        top.Labelframe2.configure(text='''Camera 2''')
        top.Labelframe2.configure(background="#d9d9d9")
        top.Labelframe2.configure(width=800)

        #   Camera 3
        top.Labelframe3 = tk.Label(top.frame)
        top.Labelframe3.place(relx=0.32, rely=0.668, relheight=0.301
                , relwidth=0.313)
        top.Labelframe3.configure(relief='groove')
        top.Labelframe3.configure(foreground="black")
        top.Labelframe3.configure(text='''Camera 3''')
        top.Labelframe3.configure(background="#d9d9d9")
        top.Labelframe3.configure(width=800)

        #   Engine parameters
        top.Labelframe4 = tk.Label(top.frame)
        top.Labelframe4.place(relx=0.637, rely=0.007, relheight=0.962
                , relwidth=0.355)
        top.Labelframe4.configure(relief='groove')
        top.Labelframe4.configure(foreground="black")
        top.Labelframe4.configure(text='''Engine parameters''')
        top.Labelframe4.configure(background="#d9d9d9")
        top.Labelframe4.configure(width=910)

        top.TSeparator1 = ttk.Separator(top.Labelframe4)
        top.TSeparator1.place(relx=-0.011, rely=0.02, relwidth=1,
                              bordermode='ignore')

        #
        #   Dials
        #
        speed= 0
        top.Speed = Dial(top.Labelframe4, size=200, unit='    Km/h', min = 0, max = 10, majorscale=1,casewidth=10, value=speed)
        top.Speed.place(relx=0.001, rely=0.24, relheight=0.24, relwidth=0.382
                , bordermode='ignore')
        top.Speed.itemconfig('face', fill='#d9d9d9')
        top.Speed.itemconfig('needle', fill='red')
        top.speedlabel = tk.Label(top.Labelframe4)
        top.speedlabel.configure(text='''Speed''',font="-family {Arial} -size 11 -weight bold")
        top.speedlabel.place(relx=0.0001, rely=0.21, relheight=0.02, relwidth=0.34)

        rpm = 0
        top.RPM = Dial(top.Labelframe4, size=200, unit='\n\nRPM', min = 0, max = 3000, majorscale=200, semimajorscale=0, minorscale=0, casewidth=10, value=rpm)
        top.RPM.place(relx=0.001, rely=0.473, relheight=0.24, relwidth=0.382
                , bordermode='ignore')
        top.RPM.itemconfig('face', fill='#d9d9d9')
        top.RPM.itemconfig('needle', fill='red')
        top.rpmlabel = tk.Label(top.Labelframe4)
        top.rpmlabel.configure(text='''RPM''',font="-family {Arial} -size 11 -weight bold")
        top.rpmlabel.place(relx=0.0001, rely=0.45, relheight=0.02, relwidth=0.34)

        pitch = 0
        top.Pitch = Dial(top.Labelframe4, size = 180, unit='    Pitchdeg', min = -40, max = 40, start=180, extent=-180,casewidth=10, value=pitch)
        top.Pitch.place(relx=0.001, rely=0.036, relheight=0.19, relwidth=0.34
                , bordermode='ignore')
        top.pitchlabel = tk.Label(top.Labelframe4)
        top.pitchlabel.configure(text='''Pitch''',font="-family {Arial} -size 11 -weight bold")
        top.pitchlabel.place(relx=0.0001, rely=0.004, relheight=0.02, relwidth=0.33)

        roll = 0
        top.Roll = Dial(top.Labelframe4, size = 180, unit='    Rolldeg', min = -40, max = 40, start=180, extent=-180,casewidth=10, value=roll)
        top.Roll.place(relx=0.32, rely=0.036, relheight=0.19, relwidth=0.34
                , bordermode='ignore')
        top.rolllabel = tk.Label(top.Labelframe4)
        top.rolllabel.configure(text='''Roll''',font="-family {Arial} -size 11 -weight bold")
        top.rolllabel.place(relx=0.32, rely=0.004, relheight=0.02, relwidth=0.35)

        angle = 0
        top.Angle = Dial(top.Labelframe4, size = 180, unit='    Angledeg', min = -40, max = 40, start=180, extent=-180,casewidth=10, value=angle)
        top.Angle.place(relx=0.64, rely=0.036, relheight=0.19, relwidth=0.351
                , bordermode='ignore')
        top.anglelabel = tk.Label(top.Labelframe4)
        top.anglelabel.configure(text='''Steering angle''',font="-family {Arial} -size 11 -weight bold")
        top.anglelabel.place(relx=0.64, rely=0.004, relheight=0.02, relwidth=0.355)

        fuel = 0
        top.Fuel = Dial(top.Labelframe4, size=170, unit='\n\nFuel%', min = 0, max = 100,casewidth=10, value=fuel)
        top.Fuel.place(relx=0.384, rely=0.24, relheight=0.18, relwidth=0.3
                , bordermode='ignore')
        top.fuellabel = tk.Label(top.Labelframe4)
        top.fuellabel.configure(text='''Fuel level''',font="-family {Arial} -size 11 -weight bold")
        top.fuellabel.place(relx=0.34, rely=0.21, relheight=0.02, relwidth=0.39)

        voltage = 0
        top.Voltage = Dial(top.Labelframe4, size=170, unit='V', min = 10, max = 20,  majorscale=1,casewidth=10, value=voltage)
        top.Voltage.place(relx=0.684, rely=0.24, relheight=0.18, relwidth=0.307
                , bordermode='ignore')
        top.batterylabel = tk.Label(top.Labelframe4)
        top.batterylabel.configure(text='''Battery voltage''',font="-family {Arial} -size 11 -weight bold")
        top.batterylabel.place(relx=0.64, rely=0.21, relheight=0.02, relwidth=0.355)

        oiltemp = 0
        top.Oiltemp = Dial(top.Labelframe4, size=170, unit='degC', min = 20, max = 120, casewidth=10, value=oiltemp)
        top.Oiltemp.place(relx=0.384, rely=0.432, relheight=0.18, relwidth=0.3
                , bordermode='ignore')
        top.oiltemplabel = tk.Label(top.Labelframe4)
        top.oiltemplabel.configure(text='''Oil temp.''',font="-family {Arial} -size 11 -weight bold")
        top.oiltemplabel.place(relx=0.34, rely=0.407, relheight=0.02, relwidth=0.39)

        oillevel = 0
        top.Oillevel = Dial(top.Labelframe4, size=170, unit='\n\nOil%', min = 0, max = 100,casewidth=10, value=fuel)
        top.Oillevel.place(relx=0.684, rely=0.432, relheight=0.18, relwidth=0.307
                , bordermode='ignore')
        top.oillevellabel = tk.Label(top.Labelframe4)
        top.oillevellabel.configure(text='''Oil level''',font="-family {Arial} -size 11 -weight bold")
        top.oillevellabel.place(relx=0.64, rely=0.407, relheight=0.02, relwidth=0.355)

        enginetemp = 0
        top.Enginetemp = Dial(top.Labelframe4, size=170, unit='\n\nEngdegC', min = 0, max = 100,casewidth=10, value=enginetemp)
        top.Enginetemp.place(relx=0.384, rely=0.625, relheight=0.18, relwidth=0.3
                , bordermode='ignore')
        top.enginetemplabel = tk.Label(top.Labelframe4)
        top.enginetemplabel.configure(text='''Engine temp.''',font="-family {Arial} -size 11 -weight bold")
        top.enginetemplabel.place(relx=0.34, rely=0.605, relheight=0.02, relwidth=0.39)

        engineoilpres = 0
        top.Engineoilpres = Dial(top.Labelframe4, size=170, unit='\n\nEngPres', min = 0, max = 100,casewidth=10, value=engineoilpres)
        top.Engineoilpres.place(relx=0.684, rely=0.625, relheight=0.18, relwidth=0.307
                , bordermode='ignore')

        top.engineoilpreslabel = tk.Label(top.Labelframe4)
        top.engineoilpreslabel.configure(text='''Engine oil press.''',font="-family {Arial} -size 11 -weight bold")
        top.engineoilpreslabel.place(relx=0.64, rely=0.605, relheight=0.02, relwidth=0.355)

        # Distance, warnings/errors and mode
        distance = 0
        top.distance = tk.Text(top.Labelframe4)
        top.distance.configure(background="#d9d9d9")
        top.distance.insert(tk.INSERT, distance)
        top.distance.config(state="disabled")
        top.distance.place(relx=0.002, rely=0.724, relheight=0.02, relwidth=0.382
                , bordermode='ignore')

        top.distancelabel = tk.Label(top.Labelframe4)
        top.distancelabel.configure(text='''Distance traveled''', font="-family {Arial} -size 11 -weight bold")
        top.distancelabel.place(relx=0.0001, rely=0.7, relheight=0.02, relwidth=0.382)

        top.warninglabel = tk.Label(top.Labelframe4)
        top.warninglabel.configure(text='''Warnings''', font="-family {Arial} -size 11 -weight bold")
        top.warninglabel.place(relx=0.0001, rely=0.74, relheight=0.02, relwidth=0.382)

        error =" "
        top.error = tk.Text(top.Labelframe4)
        top.error.configure(background="#d9d9d9")
        top.error.insert(tk.INSERT, error)
        top.error.config(state="disabled")
        top.error.place(relx=0.002, rely=0.764, relheight=0.04, relwidth=0.382
                , bordermode='ignore')

        top.canvas = tk.Canvas(top.Labelframe4)
        top.canvas.place(relx=0.0001, rely=0.805, relheight=0.195, relwidth=1
                , bordermode='ignore')
        top.canvas.configure(background="#F0F0F0")
        top.canvas.configure(borderwidth="2")
        top.canvas.configure(insertbackground="black")
        top.canvas.configure(relief="ridge")
        top.canvas.configure(selectbackground="#c4c4c4")
        top.canvas.configure(selectforeground="black")
        top.canvas.configure(width=125)

        top.modelabel = tk.Label(top.Labelframe4)
        top.modelabel.configure(text='''Mode''',font="-family {Arial} -size 11 -weight bold",relief="ridge")
        top.modelabel.place(relx=0.32, rely=0.81, relheight=0.02, relwidth=0.35)

        top.drivelabel = tk.Label(top.Labelframe4)
        top.drivelabel.configure(text='''Drive''',font="-family {Arial} -size 11 -weight bold")
        top.drivelabel.place(relx=0.003, rely=0.83, relheight=0.02, relwidth=0.32)

        top.excalabel = tk.Label(top.Labelframe4)
        top.excalabel.configure(text='''Excavator''',font="-family {Arial} -size 11 -weight bold")
        top.excalabel.place(relx=0.32, rely=0.83, relheight=0.02, relwidth=0.32)

        top.tiltlabel = tk.Label(top.Labelframe4)
        top.tiltlabel.configure(text='''Flotation''',font="-family {Arial} -size 11 -weight bold")
        top.tiltlabel.place(relx=0.65, rely=0.83, relheight=0.02, relwidth=0.32)

        #
        # Modes
        #
        off = "red"
        on = "green"

        # if mode = drive top.drive(fill = on), top.exca(fill=off) etc.
        top.drive = top.canvas.create_oval(50, 60, 150, 160, fill=off)
        top.exca = top.canvas.create_oval(240, 60, 340, 160, fill=off)
        top.tilt = top.canvas.create_oval(430, 60, 530, 160, fill=off)

        self.dials = OrderedDict([("RPM", top.RPM),
                                  ("oil_pressure", top.Engineoilpres),
                                  ("eng_temp", top.Enginetemp),
                                  ("fuel", top.Fuel),
                                  ("battary_voltage", top.Voltage),
                                  ("body_roll", top.Roll),
                                  ("body_pitch", top.Pitch),
                                  ("speed", top.Speed)],)

        # First we must initialize all the streams, and only after that we can start them, otherwise
        # we encounter a RuntimeError. Tkinter library doesn't like when OpenCV is trying to
        # initalize a capture while a video loop thread is running.
        widths = {top.Labelframe3: 300, top.Labelframe2: 300, top.Labelframe1: 900}
        streams = []
        for frame, url in zip((top.Labelframe1, top.Labelframe2, top.Labelframe3), cams):
            streams.append(VideoStream(top, frame, url, widths[frame]))

        for stream in streams:
            stream.start()
