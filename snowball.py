
import global_vars as GLOBALS
from ursina import *

 
class Snowball(Entity):
    
    def __init__(self, position=Vec3(0,0,0), speed=15, direction=Vec3(0,0,0)):
        #super().__init__(model='sphere', color=color.white, scale=0.5, position=position, collider='sphere')
        #self.direction = direction
        #self.speed = speed  # Set the desired speed (adjust as needed)
        return
        
    def update(self):
        #self.position += self.direction * self.speed * time.dt # Move the snowball in its current direction with the specified speed
        #self.direction.y += (-0.3 * time.dt) 

        # Check if snowball is out range of world
        #if self.position.y < 0:
        #    destroy(self)  # Remove the snowball from the scene        
        return
    
    #def destroy_snowball(self):
    #    destroy(self)
    #    return
