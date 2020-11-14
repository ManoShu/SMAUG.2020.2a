from typing import List

import pygame as pg


class SpriteSheet:
    @staticmethod
    def generate(file_path, columns, rows) -> List[pg.Surface]:
        base_image = pg.image.load(file_path).convert_alpha()

        images = []

        width = base_image.get_width()
        height = base_image.get_height()

        tile_width = width / columns
        tile_height = height / rows

        for y in range(rows):
            for x in range(columns):
                r_x = x * tile_width
                r_y = y * tile_height
                r = pg.Rect((r_x, r_y), (tile_width, tile_height))
                sub_image = base_image.subsurface(r)
                images.append(sub_image)

        return images
