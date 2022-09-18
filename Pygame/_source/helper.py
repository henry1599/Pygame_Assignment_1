from constants import *
import pygame as pg

def GetBackgroundScreenScale(_bg_width, _bg_height, _scale_by_width = False):
    background_width_ratio = SCREEN_WIDTH / _bg_width
    background_height_ratio = SCREEN_HEIGHT / _bg_height
    background_ratio = 1.0
    if _scale_by_width:
        background_ratio = background_width_ratio
    else:
        background_ratio = background_height_ratio
    return (background_ratio * _bg_width, background_ratio * _bg_height)