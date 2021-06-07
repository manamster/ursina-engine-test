#World Gen Stuff

from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina.prefabs.first_person_controller import *
from noise import *

class World(object):
    def __init__(self):
        def worldGen(self):
            heightMap = 0
        ground = Entity(model='plane', scale=(100,1,100), color=color.yellow.tint(-.2), texture='white cube', texture_scale=(100,100), collider='box', shader=lit_with_shadows_shader)
        monkey = Entity(model='monkey.obj', color=color.light_gray, shader=lit_with_shadows_shader, collider='box', y=1, x=-2)
        pivot=Entity()
        lightEntity = DirectionalLight(parent=pivot,y=2,z=3,shadowns=True)
    