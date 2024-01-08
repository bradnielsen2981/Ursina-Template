import global_vars as GLOBALS
from ursina import *
from direct.actor.Actor import Actor
import random
 
class Wolf(Entity):

    def __init__(self, position=Vec3(0,0,0), rotation=(0,0,0)):
        super().__init__(position=position, scale=1, rotation=(rotation))
        self.speed = 3

        #attach health bar
        self.max_hp = 100; self.hp = self.max_hp
        self.health_bar = Entity(parent=self, y=1.2, model='cube', color=color.red, scale=(1,0.1,0.1), position=(0,3,0.5))

        self.actor = Actor("models/golem/golem.gltf")
        print(self.actor.getAnimNames())
        self.actor.reparent_to(self) # Attach the actor to this entity
        #self.actor.loop('Defence1') #play animation

        '''#attach Actor
        self.actor.setScale(0.5)
        self.actor.setH(self.actor.getH() + 180)
        '''
        self.sound = Audio('sounds/snowballhit.mp3', loop=False, autoplay=False, volume=1, range=10, parent=self) #makes it so sound is only audible within 10 range of entity
        
        self.avoidance = False
        return


    def update(self):

        self.health_bar.alpha = max(0, self.health_bar.alpha - time.dt)

        #looks for anything it intersects with enemy except ground
        hit_info = self.intersects(ignore=(GLOBALS.GAME.ground,), debug=True)  #use debug=True to see collision box
        if hit_info.hit:
            try:
                if hit_info.entity.name == 'snowball': #if hit by a snowball  hit_info.entity.name 
                    self.color = color.rgba(1.0, 0.0, 0.0, 0.5)
                    invoke(self.restorecolor, delay=0.5) #try to avoid other enemies
                    GLOBALS.GAME.create_explosion(hit_info.entity.position + 2*self.forward)
                    self.sound.play()
                    GLOBALS.GAME.update_score(1)
                    self.update_hp(-30)
                    destroy(hit_info.entity) #destroy the snowball

                else: #if hits anything else with a collision box 
                    if hit_info.entity.name == 'player': #if hit the player
                        hit_info.entity.hit() #tell the player they have been hit

                    self.avoidance = True
                    invoke(self.end_avoidance, delay=3)
                    self.look_at_2d(self.position + hit_info.normal, 'y') #bounce off
                    self.position += self.forward*3
            except:
                print("ENEMY.py - I'm really not sure why this is an issue!!!")
        else:
            if self.avoidance: #avoidance mode is turned on when hitting an obstacle
                self.speed = 3
                self.position += self.forward * time.dt * self.speed
            else:     
                if GLOBALS.PLAYER: #if not avoiding an obstacle move towards the player
                    if GLOBALS.PLAYER.enabled == True:
                        #find the player and move towards the player
                        self.look_at_2d(GLOBALS.PLAYER.position, 'y')
                        dist = distance_xz(GLOBALS.PLAYER.position, self.position) #get the distance to the player
                        if dist < 100 and dist > 2:
                            ray = raycast(self.position, self.forward, distance=100, ignore=(self,), debug=False) #use debug = true if you want to see ray tracing
                            if ray.hit:
                                self.position += self.forward * time.dt * self.speed
        return
        
    def end_avoidance(self):
        self.avoidance = False
        return
    
    def restorecolor(self):  
        self.actor.setColor(1, 1, 1, 1) 
        return

    def update_hp(self, value):
        self.hp += value
        if self.hp <= 0:
            GLOBALS.ENEMYLIST.remove(self)
            destroy(self)
            return

        self.health_bar.world_scale_x = self.hp / self.max_hp * 1.5
        self.health_bar.alpha = 1
        return