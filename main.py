import bpy
from math import radians

#create cube
bpy.ops.mesh.primitive_cube_add()
so = bpy.context.active_object

#rotate object
so.rotation_euler[0] += radians(45)

#create modifier
mod_subsurf = so.modifiers.new("My Modifier", 'SUBSURF')

#change modifier value
mod_subsurf.levels = 3

#smooth objects
mesh = so.data
for face in mesh.polygons:
    face.use_smooth = True
