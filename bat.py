import global_vars as GLOBALS
from ursina import *
from direct.actor.Actor import Actor
import random
 
class Bat(Entity):

    def __init__(self, position=Vec3(0,0,0), rotation=Vec3(0,0,0)):
        super().__init__(position=position, rotation=rotation)
        self.speed = 3

        self.actor = Actor("models/bat/bat.gltf")
        print(self.actor.getAnimNames())
        self.actor.reparent_to(self) # Attach the actor to this entity
        self.actor.loop('ArmatureAction') #play animation

        #attach Actor
        self.actor.setScale(Vec3(0.02, -0.02, 0.02))
        
        self.sound = Audio('sounds/snowballhit.mp3', loop=False, autoplay=False, volume=1, range=10, parent=self) #makes it so sound is only audible within 10 range of entity
        
        self.avoidance = False
        return
    
    def update(self):
        return
        
    def end_avoidance(self):
        self.avoidance = False
        return
    
    def restorecolor(self):  
        self.actor.setColor(1, 1, 1, 1) 
        return