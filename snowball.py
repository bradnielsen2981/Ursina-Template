
import global_vars as GLOBALS
from ursina import *

 
class Snowball(Entity):
    
    def __init__(self, position=Vec3(0,0,0), speed=15, direction=Vec3(0,0,0)):
        super().__init__(model='sphere', color=color.white, scale=0.5, position=position)
        self.direction = direction
        self.speed = speed  # Set the desired speed (adjust as needed)
        self.collider = SphereCollider(self, center=Vec3(0,0,0), radius=0.5) 
        return
        
    def update(self):
        self.position += self.direction * self.speed * time.dt # Move the snowball in its current direction with the specified speed
        self.direction.y += (-0.3 * time.dt) 

        # Check if snowball is out of range of the world
        dist = distance(Vec3(0,0,0),self.position)
        if dist > 64:
            destroy(self)  # Remove the snowball from the scene

        #if hits ground, destroy or leave??
        hit_info = self.intersects()
        if hit_info.entity == GLOBALS.GAME.ground:
            self.collision = False
            self.speed = 0
            self.ignore = True
            self.Y = 0
            invoke(self.destroy_snowball, delay=5)
        return
    
    def destroy_snowball(self):
        destroy(self)
        return
