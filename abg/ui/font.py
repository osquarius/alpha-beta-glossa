import pygame

import settings
from abg.ui import colors

_font_cache = {}

def get_font(size):
    if not size in _font_cache:
        _font_cache[size] = pygame.font.Font(settings.FONT, size)
    return _font_cache[size]

def text_fits(text, font_size, max_text_width, max_text_height):
    width, height = get_font(font_size).size(text)
    return width <= max_text_width and height <= max_text_height

def optimal_font_size(text, max_text_width, max_text_height, max_font_size=200):
    left = 1
    right = max_font_size + 1
    while right - left > 1:
        middle = (left + right) // 2
        if text_fits(text, middle, max_text_width, max_text_height):
            left = middle
        else:
            right = middle
    return left

def best_fit_text_surface(text, max_width, max_height, color=colors.BLACK):
    size = optimal_font_size(text, max_width, max_height)
    surface = get_font(size).render(text, True, color)
    return surface
