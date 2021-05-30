from GLOBAL import *


class Collider:
    def __init__(self, rect):
        self.rect = pg.Rect(rect)
        COLLIDERS.append(self)

    def collide_test(self):
        for object in COLLIDERS:
            if not object.rect == self.rect:
                if pg.Rect.colliderect(self.rect, object):
                    return False
                else:
                    return True
