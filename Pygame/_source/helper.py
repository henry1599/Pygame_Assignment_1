from constants import *
import pygame as pg
from components import *

def GetBackgroundScreenScale(_bg_width, _bg_height, _scale_by_width = False):
    background_width_ratio = SCREEN_WIDTH / _bg_width
    background_height_ratio = SCREEN_HEIGHT / _bg_height
    background_ratio = 1.0
    if _scale_by_width:
        background_ratio = background_width_ratio
    else:
        background_ratio = background_height_ratio
    return (background_ratio * _bg_width, background_ratio * _bg_height)


def draw_text(font_path, position, string, size, fcolor, anchor, window):
    font = pg.font.Font(font_path, size)
    text = font.render(string, True, fcolor)
    textbox = text.get_rect()
    if anchor == Anchor.TOP_LEFT:
        textbox.topleft = position
    elif anchor == Anchor.MID_LEFT:
        textbox.midleft = position
    elif anchor == Anchor.BOTTOM_LEFT:
        textbox.bottomleft = position
    elif anchor == Anchor.TOP_CENTER:
        textbox.midtop = position
    elif anchor == Anchor.MID_CENTER:
        textbox.center = position
    elif anchor == Anchor.BOTTOM_CENTER:
        textbox.midbottom = position
    elif anchor == Anchor.TOP_RIGHT:
        textbox.topright = position
    elif anchor == Anchor.MID_RIGHT:
        textbox.midright = position
    elif anchor == Anchor.BOTTOM_RIGHT:
        textbox.bottomright = position
    window.blit(text, textbox)

def draw_text_with_outline(font_path, position, string, size, fcolor, ocolor, border_radius, anchor, window):
    draw_text(font_path, (position[0] + border_radius, position[1] - border_radius) , string, size, ocolor, anchor, window)
    draw_text(font_path, (position[0] + border_radius, position[1] - border_radius) , string, size, ocolor, anchor, window)
    draw_text(font_path, (position[0] - border_radius, position[1] + border_radius) , string, size, ocolor, anchor, window)
    draw_text(font_path, (position[0] - border_radius, position[1] + border_radius) , string, size, ocolor, anchor, window) 
    draw_text(font_path, (position[0] + border_radius, position[1] + border_radius) , string, size, ocolor, anchor, window)
    draw_text(font_path, (position[0] - border_radius, position[1] - border_radius) , string, size, ocolor, anchor, window) 
    draw_text(font_path, (position[0], position[1]), string, size, fcolor, anchor, window)

    