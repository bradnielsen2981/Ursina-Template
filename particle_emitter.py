from ursina import *
from direct.particles.Particles import Particles
from direct.particles.ParticleEffect import ParticleEffect
from panda3d.core import Filename
from direct.particles.ForceGroup import ForceGroup
import time
 
class ParticleEmitter(Entity):
    
    def __init__(self, position=Vec3(0,0,0), file='particles/snowsplash.ptf', life=1, deathtime=2, parent=None):
        super().__init__(position=position)
        self.stoptime = time.time() + life 
        self.effect = ParticleEffect() 
        self.effect.loadConfig(file)
        self.life = life
        self.deathtime = deathtime
        if parent == None:
            self.effect.start(parent=self)
        else:
            self.effect.start(parent=parent)
        return
        
    def update(self):
        if time.time() > self.stoptime:
            self.effect.soft_stop()
            invoke(self.die, delay=self.deathtime)     
        return
    
    def die(self):
        destroy(self)
        return

