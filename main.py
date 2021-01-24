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
    
class Player(Entity):
    def __init__(self):
        player = FirstPersonController(model="capsule.obj", y=0, origin_y=-.5)
        playerspeed = 10
        player.speed = playerspeed
        #Would import the model for the "gun" from the .blend file but the support apparently is broken :(
        gun = Entity(parent=camera, model='gun.obj', x=0.7, z=1, y=-0.2, scale=Vec3(0.4,0.4,0.4), rotation=Vec3(0,-92,0),shader=lit_with_shadows_shader)
        player.gun = gun
    #This isnt working for some reason IDK Why Ill fix it later
    '''
    def input(self, key):
        if key == 'escape':
            sys.exit()
        elif key == 'left mouse down' and player.gun:
            gun.blink(color.red)
        elif key == 'right mouse down' and player.gun:
            gun.position(0,0,0)
    '''
    '''
    def update(self):
        #test will eventually put stuff here
        pass
    '''
worldclass = World()
playerclass = Player()

app.run()