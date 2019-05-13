import bpy
from mathutils import Vector, Matrix

def  GetVerticesCenter():

    numberOfVertices = 0
    verticesCenter = Vector()

    for obj in bpy.data.objects:
        
        mesh = obj.data
        mat_world = obj.matrix_world

        for vert in mesh.vertices:
            numberOfVertices += 1
            verticesCenter += mat_world * vert.co
            
    return verticesCenter / numberOfVertices
        
def TranslateVertices(translationVector):     
      
    translationMatrix = Matrix.Translation(translationVector)
        
    for obj in bpy.data.objects:
        
        mesh = obj.data
        mat_world = obj.matrix_world
        mat_edit = mat_world.inverted() * translationMatrix * mat_world

        for vert in mesh.vertices:
            vert.co = mat_edit * vert.co            

translationVector = GetVerticesCenter()
TranslateVertices(-translationVector)
