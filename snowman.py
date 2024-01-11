import global_vars as GLOBALS
from ursina import *
import random
 
class Snowman(Entity):

    def __init__(self, position, rotation):
        super().__init__(position=position, rotation=rotation, model='models/snowman/snowman.gltf')
        self.speed = 3

        self.collider = BoxCollider(self, center=Vec3(0,1.6,0.5), size=Vec3(2.2,3.4,3.5))      
        #self.colliderbox = Entity(parent=self, model="cube", color=color.red, alpha=0.5, scale=Vec3(2.5,3.4,3.5), position=Vec3(0,1.6,0.5)) #visual the collision box

        self.model.setScale((1,1,-1))

        self.sound = Audio('sounds/snowballhit.mp3', loop=False, autoplay=False, volume=1, range=10, parent=self) #makes it so sound is only audible within 10 range of entity
        self.avoidance = False
        return

    def update(self):

        #looks for anything it intersects with enemy except ground
        #try:
        #    hit_info = self.intersects(ignore=(GLOBALS.GAME.ground,), debug=True)  #use debug=True to see collision box
        #    if hit_info.hit:
        #        if hit_info.entity.name == 'snowball': #if hit by a snowball  hit_info.entity.name 
        #            self.color = color.rgba(1.0, 0.0, 0.0, 0.5)
        #            invoke(self.restorecolor, delay=0.5) #try to avoid other enemies

        #            self.sound.play()

        #            destroy(hit_info.entity) #destroy the snowball

        #        else: #if hits anything else with a collision box 
        #            self.avoidance = True
        #            invoke(self.end_avoidance, delay=3)
        #            self.look_at_2d(self.position + hit_info.normal, 'y') #bounce off
        #            self.position += self.forward*3
        #    else:
        #        if self.avoidance: #avoidance mode is turned on when hitting an obstacle
        #            self.speed = 3
        #            self.position += self.forward * time.dt * self.speed
        #        else:     
        if GLOBALS.PLAYER: #if not avoiding an obstacle move towards the player
            if GLOBALS.PLAYER.enabled == True:
                #find the player and move towards the player
                self.look_at_2d(GLOBALS.PLAYER.position, 'y')
                self.position += self.forward * time.dt * self.speed
                        
        #except:
        #    pass #sometimes a collision will reference an object that no longer exists e.g a snowball
        #return
        
    #def end_avoidance(self):
    #    self.avoidance = False
    #    return
    
    def restorecolor(self):  
        self.color = color.white 
        return
