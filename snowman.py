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

        #self.max_hp = 100; self.hp = self.max_hp
        #self.health_bar = Entity(parent=self, y=1.2, model='cube', color=color.red, scale=Vec3(1,0.1,0.1), position=Vec3(0,4,0.5))
        
        self.sound = Audio('sounds/snowballhit.mp3', loop=False, autoplay=False, volume=1, range=10, parent=self) #makes it so sound is only audible within 10 range of entity
        self.avoidance = False
        return

    def update(self):

        #self.health_bar.alpha = max(0, self.health_bar.alpha - time.dt)

        #looks for anything it intersects with enemy except ground
        try:
            hit_info = self.intersects(ignore=(GLOBALS.GAME.ground,), debug=True)  #use debug=True to see collision box
            if hit_info.hit:
                if hit_info.entity.name == 'snowball': #if hit by a snowball  hit_info.entity.name 
                    self.color = color.rgba(1.0, 0.0, 0.0, 0.5)
                    invoke(self.restorecolor, delay=0.5) #try to avoid other enemies
                    GLOBALS.GAME.create_explosion(hit_info.entity.position + 2*self.forward)
                    self.sound.play()
                    
                    #GLOBALS.GAME.update_score(1)
                    #self.update_hp(-30)

                    destroy(hit_info.entity) #destroy the snowball

                else: #if hits anything else with a collision box 
                    if hit_info.entity.name == 'player': #if hit the player
                        hit_info.entity.hit() #tell the player they have been hit

                    self.avoidance = True
                    invoke(self.end_avoidance, delay=3)
                    self.look_at_2d(self.position + hit_info.normal, 'y') #bounce off
                    self.position += self.forward*3
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
                                ray = raycast(self.position + Vec3(0,1,0), self.forward, distance=100, ignore=(self,), debug=False) #use debug = true if you want to see ray tracing
                                if ray.hit:
                                    self.position += self.forward * time.dt * self.speed
        except:
            pass #sometimes a collision will reference an object that no longer exists e.g a snowball
        return
        
    def end_avoidance(self):
        self.avoidance = False
        return
    
    def restorecolor(self):  
        self.color = color.white 
        return

    def update_hp(self, value):
    #    self.hp += value
    #    if self.hp <= 0:
    #        try:
    #            GLOBALS.ENEMYLIST.remove(self)
    #            destroy(self)
    #        except:
    #            pass #there is a change the snowman will no longer exist
    #        return

    #    self.health_bar.world_scale_x = self.hp / self.max_hp * 1.5
    #    self.health_bar.alpha = 1
        return