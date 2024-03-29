#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4 sw=4 tw=100 et ai si

import cv2
import imutils
import threading
from PIL import Image, ImageTk

class VideoStream:
    """This class handles obtainig video stream from the ip camera."""

    def video_loop(self):
        """
        Loop which displays the video. Do not call without using Threading. Otherwise the programm
        will softlock.
        """

        _, img = self.vs.read()
        img = imutils.resize(img, width=self.width)
        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        self.frame.configure(image=image)
        self.frame.photo = image

        self.top.after(self.fps, self.video_loop)

    def start(self):
        """Start asyncronous video stream."""

        self.top.after(15, self.video_loop)

    def __init__(self, top, frame, url, width):
        """
        Init method for video stream.
        frame - Tkinter Frame which will display the video stream.
        url - link to the video camera. This can also be a file.
        """

        self.fps = int(1000/60)
        self.top = top
        self.frame = frame
        self.width = width
        self.vs = cv2.VideoCapture(url)
        self.vs.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        

