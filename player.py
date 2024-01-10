from ursina import *
from direct.actor.Actor import Actor
from ursina.prefabs.first_person_controller import FirstPersonController
from snowball import Snowball
import global_vars as GLOBALS

class Player(FirstPersonController):

    def __init__(self, position: Vec3):
        super().__init__(position=position, jump_height=2.5, jump_duration=0.4, origin_y=-0.5, collider="box")
        self.speed=7

        #create the actor model for animation
        self.actor = Actor("models/ralph/ralph",{"run":"models/ralph/ralph-run", "walk":"models/ralph/ralph-walk"})
        self.actor.setScale(Vec3(0.5,0.5,-0.5))
        self.actor.loop('run') #play animation
        self.actor.reparent_to(self) # Attach the actor to the cube entity

        #create a collision box
        self.collider = BoxCollider(self, center=Vec3(0,1.25,0), size=Vec3(1,2.5,1.25))   # add BoxCollider at custom positions and size.      

        #move the player camera
        self.camera_pivot.z = -3.5  # Move the camera behind the player model
        self.camera_pivot.y = 3.2   # Move the camera a little higher  

        #create a healthbar 
        #self.healthbar_bg = Entity(parent=camera.ui,model="quad",color=color.rgb(255, 0, 0), position=(0, 0.45), scale=(0.8, 0.04))
        #self.healthbar = Entity(parent=camera.ui,model="quad",color=color.rgb(0, 255, 0), position=(0, 0.45), scale=(0.8, 0.04))
        #self.health = 100
        return

    #players update function called every frame
    def update(self):
        super().update()
        return

    #player inputs function called every frame WASD are already inputs for the FirstPersonController
    def input(self, key):
        if key == 'left mouse down':
            snowball_direction = camera.forward + Vec3(0,0.2,0) #makes it above the vector
            snowball_position = self.position + self.forward + Vec3(0,2,0)
            try:
                hit_info = raycast(camera.world_position, camera.forward, distance=100, ignore=(GLOBALS.PLAYER, GLOBALS.GAME.ground), debug=False) #if there is a camera target
                if hit_info.hit:
                    if hit_info.entity.name == "enemy":
                        snowball_direction = ((hit_info.entity).position + Vec3(0,2,0) - self.position).normalized() #find the difference vector between the player and enemy (DIRECTION)
                snowball = Snowball(position=snowball_position, speed=15, direction=snowball_direction)
            except:
                pass #there is a change the hit info will return an object that no longer exists
        super().input(key) #The player controller needs input
        return

    #The player is hit
    def hit(self):
        #if self.health > 0:
        #    self.health -= 20
        #    if self.health <= 0:
        #        self.enabled = False
        #        self.healthbar.scale_x = 0.01
        #        GLOBALS.GAME.end_game()
        #    else:
        #        self.healthbar.scale_x = self.health/100 * self.healthbar_bg.scale_x
         #   self.healthbar.x = self.healthbar_bg.x - (self.healthbar_bg.scale_x - self.healthbar.scale_x)/2
        return

    #Dont edit the collisions of the player controller as collisions have already been set up 
