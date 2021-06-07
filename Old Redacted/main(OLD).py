#Ursina Engine Test

from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina.prefabs.first_person_controller import *
from noise import *
import sys
#import worldGen

app=Ursina()
window.exit_button.enabled = False

class World(object):
    def __init__(self):
        ground = Entity(model='plane', scale=(100,1,100), color=color.yellow.tint(-.2), texture='white cube', texture_scale=(100,100), collider='box', shader=lit_with_shadows_shader)
        monkey = Entity(model='monkey.obj', color=color.light_gray, shader=lit_with_shadows_shader, collider='box', y=1, x=-2)
        pivot=Entity()
        lightEntity = DirectionalLight(parent=pivot,y=2,z=3,shadowns=True)

class Player(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__()
        self.position=(2,1,0)
        playerspeed=10
        self.speed=playerspeed
        #Would import the model for the "gun" from the .blend file but the support apparently is broken :(
        gun = Entity(parent=camera, model='gun.obj', x=0.7, z=1, y=-0.2, scale=Vec3(0.4,0.4,0.4), rotation=Vec3(0,-92,0),shader=lit_with_shadows_shader)
        self.gun = gun
        for key, value in kwargs.items():
            setattr(self, key, value)

    def input(self, key):
        if key == 'escape':
            sys.exit()

    def update(self):
        pass

worldclass = World()
playerclass = Player()

app.run()