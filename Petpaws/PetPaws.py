
# file and window manager import
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
# widget import
from kivy_garden.mapview import MapView
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
# screen stuff
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, NoTransition
from kivy.properties import StringProperty, ObjectProperty
from kivy.lang import Builder
# socket and stream processing stuff import
from kivy.clock import Clock
from kivy.clock import CyClockBaseFree
import socket
import cv2
import pickle
import struct
import imutils
import numpy as np
import base64
import sys
import time

# app establishing import
from kivy.app import App

class Loading_pg(Screen):
	def __init__(self,  **kwargs):
		super(Loading_pg, self).__init__(**kwargs)
		Clock.schedule_once(self.waiting, 2)
	def waiting(self, dt):
		time.sleep(1)
		self.manager.current = 'logging'
	
class Logging_pg(Screen):
	def __init__(self,  **kwargs):
		super(Logging_pg, self).__init__(**kwargs)

class Register_pg(Screen):
	def __init__(self,  **kwargs):
		super(Register_pg, self).__init__(**kwargs)

	"""
class (Screen):
	pass
	"""
class ScreenManager(ScreenManager):
	pass

class PetPaws(App):
	def build(self):
		Window.size = (321, 694.5)
		pass


if __name__ == "__main__":
	PetPaws().run()

