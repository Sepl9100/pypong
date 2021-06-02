from GLOBAL import *


class Collider:
    def __init__(self, rect):
        self.rect = pg.Rect(rect)
        COLLIDERS.append(self)
        self.last_collider = ""

    def collide_test(self):
        for object in COLLIDERS:
            if not object.rect == self.rect:
                if pg.Rect.colliderect(self.rect, object):
                    self.last_collider = object
                    return False
        return True
