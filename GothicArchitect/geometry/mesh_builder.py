import bpy
import bmesh


def new_mesh(name="GothicMesh"):
    mesh = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(name, mesh)

    bpy.context.collection.objects.link(obj)

    bm = bmesh.new()

    return obj, mesh, bm


def finish_mesh(obj, mesh, bm):

    bm.to_mesh(mesh)
    bm.free()

    mesh.update()

    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)

    return obj