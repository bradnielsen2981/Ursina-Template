import global_vars as GLOBALS
from ursina import *
import random
 
#class Snowman(Entity):

#    def __init__(self, position, rotation):
#        super().__init__(position=position, rotation=rotation, model='models/snowman/snowman.gltf')
#        self.speed = 3

#        self.collider = BoxCollider(self, center=Vec3(0,1.6,0.5), size=Vec3(2.2,3.4,3.5))      
        #self.colliderbox = Entity(parent=self, model="cube", color=color.red, alpha=0.5, scale=Vec3(2.5,3.4,3.5), position=Vec3(0,1.6,0.5)) #visual the collision box

#        self.model.setScale((1,1,-1))

#        self.sound = Audio('sounds/snowballhit.mp3', loop=False, autoplay=False, volume=1, range=10, parent=self) #makes it so sound is only audible within 10 range of entity
#        self.avoidance = False
#        return

#    def update(self):
 
#        if GLOBALS.PLAYER: #if not avoiding an obstacle move towards the player
#            if GLOBALS.PLAYER.enabled == True:
                #find the player and move towards the player
#                self.look_at_2d(GLOBALS.PLAYER.position, 'y')
#                dist = distance_xz(GLOBALS.PLAYER.position, self.position) #get the distance to the player
#                if dist < 100 and dist > 2:
#                    ray = raycast(self.position + Vec3(0,1,0), self.forward, distance=100, ignore=(self,), debug=False) #use debug = true if you want to see ray tracing
#                    if ray.hit:
#                        self.position += self.forward * time.dt * self.speed
    
