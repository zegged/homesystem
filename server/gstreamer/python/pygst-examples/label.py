#!/usr/bin/env python3
#https://zetcode.com/python/gtk/

import gi
gi.require_version("Gst", "1.0")
gi.require_version('Gtk', '3.0')
from gi.repository import Gst, GObject, Gtk
from gstPipeline import GTK_Main

lyrics = """Meet you downstairs in the bar and heard
your rolled up sleeves and your skull t-shirt
You say why did you do it with him today?
and sniff me out like I was Tanqueray

cause you're my fella, my guy
hand me your stella and fly
by the time I'm out the door
you tear men down like Roger Moore

I cheated myself
like I knew I would
I told ya, I was trouble
you know that I'm no good"""

class MyWindow(Gtk.Window):

    def __init__(self):
        super(MyWindow, self).__init__()

        self.init_ui()

    def init_ui(self):    
        
        self.set_border_width(15)
        vbox = Gtk.VBox()
        self.add(vbox)
        label = Gtk.Label(lyrics)
        vbox.add(label)
        player = Gst.Pipeline.new("player")

        self.set_title("You know I'm no Good")
        self.set_size_request(250, 180)
        
        self.connect("destroy", Gtk.main_quit)
        

win = MyWindow()
win.show_all()
Gtk.main()
