
import global_vars as GLOBALS
from ursina import *

 
class Snowball(Entity):
    
    def __init__(self, position=Vec3(0,0,0), speed=15, direction=Vec3(0,0,0)):
        super().__init__(model='sphere', color=color.white, scale=0.5, position=position, collider='sphere')
        self.direction = direction
        self.speed = speed  # Set the desired speed (adjust as needed)
        return
        
    def update(self):
        self.position += self.direction * self.speed * time.dt # Move the snowball in its current direction with the specified speed
        self.direction.y += (-0.3 * time.dt) 

        # Check if snowball is out range of world
        if self.position.y < 0:
            destroy(self)  # Remove the snowball from the scene

        #if hits ground, destroy or leave??
        #try:
        #    hit_info = self.intersects()
        #    if hit_info.entity == GLOBALS.GAME.ground:
        #        self.collision = False
        #        self.speed = 0
        #        self.ignore = True
        #        self.y = 0.2
        #        invoke(self.destroy_snowball, delay=5)

        #    elif hit_info.entity.name != 'snowman':
        #        destroy(self)
        #except:
        #    pass #sometimes an entity no longer exists
        
        return
    
    def destroy_snowball(self):
        destroy(self)
        return
