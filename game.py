import sys, time, math
from ursina import *    
from ursina.shaders import lit_with_shadows_shader
from enemy import Enemy
from wolf import Wolf
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

        self.start_text = Text(text="Press Space to start!", origin=Vec2(0, 0), scale=3)
        self.end_text = Text(text="You are dead!", origin=Vec2(0, 0), scale=3); self.end_text.enabled = False
        self.score_text = Text(text="0", y=0.4, x=-0.6, origin=Vec2(0,0),scale=3); self.score_text.enabled=True; self.score = 0
        self.load_text = Text(text="Loading", origin=Vec2(0, 0), scale=3); self.load_text.enabled = False

        self.editor_camera = EditorCamera(enabled=False, ignore_paused=True)
        self.ground = Entity(model='plane', collider='box', scale=128, texture='grass_tintable', texture_scale=(8,8))# self.ground = Entity(model=Terrain('loddefjord_height_map', skip=8), collider='mesh', texture='loddefjord_color', scale=100, scale_y=50) #self.ground.model.save('loddefjord_terrain')
        self.music = Audio("sounds/sinister.mp3", loop = True, autoplay = False, volume = 0.25, parent=self)
        self.sun = DirectionalLight()
        self.sun.look_at(Vec3(1,-1,-1))
        self.sky = Sky()

        self.spawntime = 2 #number of seconds to spawn enemy
        return
    
    # Menu
    def menu(self):
        print("MENU"); self.state = "menu"
        self.end_text.enabled = False
        self.start_text.enabled = True 
        return
    
    # Start the game
    def start_game(self):
        print("START GAME"); self.state = "game"
        self.load_text.enabled = False
        self.music.play()
        self.score = 0
        GLOBALS.PLAYER = Player(position=(0,1,0)) #Create the GLOBALS.PLAYER - Player is a First Person Controller
        self.spawn_enemy()
        return
    
    # End the game
    def end_game(self):
        print("END GAME"); self.state = "end"
        for enemy in GLOBALS.ENEMYLIST: # Destroy all enemies (!!I can't clear the scene because the Game is an Entity)
            destroy(enemy)
        GLOBALS.ENEMYLIST = []
        destroy(GLOBALS.PLAYER)
        self.music.stop(destroy=True)
        self.end_text.enabled = True
        invoke(self.menu, delay=2) #return to menu in two seconds
        return
    
    # Load the game assets and level
    def loading(self):
        print("LOADING"); self.state = "loading"
        if not self.loaded:
            wall = Entity(model='cube', collider="box", scale=(10,10,2), position=(0,0,5), texture="stonewall.png", texture_scale=(1, 1, 2))
            tree = Entity(model='models/tree/tree.gltf', position=(0,8,5), scale=0.5);
            hut = Entity(model='models/hut/hut.gltf', position=(0,0,20), scale=(2));
            wolf = Wolf(position=(20,0,20))
            #use duplicate(original_entity) to make more as opposed to loading the entity again

            invoke(self.start_game, delay=2) 
            self.loaded = True
        return
    
    # Update the score
    def update_score(self, add):
        self.score += add
        self.score_text.text = str(self.score)
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

        if self.state == "menu":
            if key == 'space':
                self.start_text.enabled = False
                self.load_text.enabled = True
                invoke(self.loading, delay=2)
        return
    
    # Update function called every frame - dont see any need for it at present
    def update(self):
        return
    
    # Create an explosion
    def create_explosion(self, position):
        p = ParticleEmitter(position)
        return
    
    # Spawn an enemy every second
    def spawn_enemy(self):
        if self.state != 'game':
            return
        if len(GLOBALS.ENEMYLIST) < 12:
            position = Vec3(random.randint(-64,64),0,random.randint(-64,64))
            while distance_xz(GLOBALS.PLAYER.position, position) < 10: #make sure positions arent too close to the player
                position = Vec3(random.randint(0,127),0,random.randint(0,127)) 
            e = Enemy(position, (0,0,0))            
            GLOBALS.ENEMYLIST.append(e)

        invoke(self.spawn_enemy, delay=2)
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

























