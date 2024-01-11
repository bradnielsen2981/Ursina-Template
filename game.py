import sys, time, math
from ursina import *    
from ursina.shaders import lit_with_shadows_shader
#from snowman import Snowman
from bat import Bat
from player import Player
from particle_emitter import ParticleEmitter
import global_vars as GLOBALS

sys.tracebacklimit = 1 # Set the level of error 

#This is an invisible Entity that controls everything in the game
class Game(Entity):

    # Initialise the Game
    def __init__(self):
        super().__init__(position=Vec3(0,0,0), ignore_paused=True)
        self.state = "ready"
        self.loaded = False

        #texts
        self.start_text = Text(text="Press Space to start!", origin=Vec2(0, 0), scale=3, color=color.black)
        self.end_text = Text(text="You are dead!", origin=Vec2(0, 0), scale=3, color=color.red); self.end_text.enabled = False
        self.score_text = Text(text="0", y=0.4, x=-0.6, origin=Vec2(0,0),scale=3, color=color.black); self.score_text.enabled=True; self.score = 0
        self.load_text = Text(text="Loading", origin=Vec2(0, 0), scale=3, color=color.violet); self.load_text.enabled = False

        #camera
        self.editor_camera = EditorCamera(enabled=False, ignore_paused=True)

        self.sun = DirectionalLight()
        self.sun.look_at(Vec3(1,-1,-1))
        #self.sky = Sky(texture='sky_default') #self.sky = Sky(texture='sky_sunset')
        self.sky = Sky(texture='textures/skies/snowmountains/snowmountains.jpg') #to get a sky background, you need to download a SKYBOX texture and you may need to flip
        self.ground = Entity(model='plane', collider='box', scale=128, texture='grass_tintable', texture_scale=(8,8))
        return
    
    # Menu
    def menu(self):
        print("MENU"); self.state = "menu"
        self.end_text.enabled = False
        self.start_text.enabled = True 
        return
    
    # Load the game assets and level 
    def loading(self):
        print("LOADING"); self.state = "loading"
        #if not self.loaded:
            #self.music = Audio("sounds/sinister.mp3", loop = True, autoplay = False, volume = 0.2, parent=self)
            #wall = Entity(model='cube', collider="box", origin=(-0.5, -0.5, 0), scale=(8,8,2), position=(-64,0,64), texture="textures/stonewall/stonewall.png", texture_scale=(1, 1, 2))
        invoke(self.start_game, delay=2) 
        return
    
    # Start the game
    def start_game(self):
        print("START GAME"); self.state = "game"
        self.load_text.enabled = False
        #self.music.play()
        GLOBALS.PLAYER = Player(position=(0,1,0)) #Create the GLOBALS.PLAYER - Player is a First Person Controller
        return
    
    # End the game
    def end_game(self):
        print("END GAME"); self.state = "end"
        destroy(GLOBALS.PLAYER)
        #self.music.stop()
        self.end_text.enabled = True
        invoke(self.menu, delay=2) #return to menu in two seconds
        return
    
    
    # Handle input when it occurs
    def input(self, key):

        if key == 'tab':    # press tab to toggle edit/play mode
            self.editor_camera.enabled = not self.editor_camera.enabled
            GLOBALS.PLAYER.visible_self = self.editor_camera.enabled
            GLOBALS.PLAYER.cursor.enabled = not self.editor_camera.enabled
            mouse.locked = not self.editor_camera.enabled
            self.editor_camera.position = GLOBALS.PLAYER.position
            application.paused = self.editor_camera.enabled
        elif key == 'escape':
            self.exit_application()

        if self.state == "menu":
            if key == 'space':
                self.start_text.enabled = False
                self.load_text.enabled = True
                invoke(self.loading, delay=2)
        return
    
    # Update function called every frame - dont see any need for it at present
    def update(self):
        return
      
    # Exit application
    def exit_application(self):
        app.userExit()
        return
    
# CREATE THE URSINA APPLICATION
app = Ursina()
Entity.default_shader = lit_with_shadows_shader #set the type of shading
GLOBALS.GAME = Game() #CREATE THE GAME CONTROLLER ENTITY
GLOBALS.GAME.menu()
app.enableParticles()
app.run()

























