__version__= '1.0.0'
__author__= 'Ara Buenaventura'

import cv2
import numpy as np

def apply_invert(frame):
  return cv2.bitwise_not(frame)

def apply_sepia(frame, intensity=0.5):
  blue, green, red = 100, 70, 15
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
  frame_height, frame_width, frame_channel = frame.shape
  sepia_bgra = (blue, green, red, 1)

  overlay = np.full((frame_height, frame_width, 4), sepia_bgra, dtype='uint8')

  frame = cv2.addWeighted(overlay, intensity, frame, 1.0, 0)
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
  return frame

def apply_filter2(frame, intensity=0.5):
  blue, green, red = 50, 70, 15
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
  frame_height, frame_width, frame_channel = frame.shape
  filter2_bgra = (blue, green, red, 1)

  overlay = np.full((frame_height, frame_width, 4), filter2_bgra, dtype='uint8')

  frame = cv2.addWeighted(overlay, intensity, frame, 1.0, 0)
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
  return frame

def apply_filter3(frame, intensity=0.5):
  blue, green, red = 50, 40, 90
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
  frame_height, frame_width, frame_channel = frame.shape
  filter3_bgra = (blue, green, red, 1)

  overlay = np.full((frame_height, frame_width, 4), filter3_bgra, dtype='uint8')

  frame = cv2.addWeighted(overlay, intensity, frame, 1.0, 0)
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
  return frame

def apply_filter4(frame, intensity=0.5):
  blue, green, red = 20, 90,40
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
  frame_height, frame_width, frame_channel = frame.shape
  filter4_bgra = (blue, green, red, 1)

  overlay = np.full((frame_height, frame_width, 4), filter4_bgra, dtype='uint8')

  frame = cv2.addWeighted(overlay, intensity, frame, 1.0, 0)
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
  return frame

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    
    invert = apply_invert(frame)
    sepia = apply_sepia(frame)
    filter2 = apply_filter2(frame)
    filter3 = apply_filter3(frame)
    filter4 = apply_filter4(frame)

    cv2.imshow('frame', frame)
    cv2.imshow('invert', invert)
    cv2.imshow('sepia', sepia)
    cv2.imshow('filter2', filter2)
    cv2.imshow('filter3', filter3)
    cv2.imshow('filter4', filter4)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break 
 
