import bpy
import bmesh
from math import pi
from mathutils import Matrix


def build_column(
        context,
        height=5,
        radius=0.35,
        base_radius=0.8,
        capital_height=0.7,
        capital_radius=0.75,
        shafts=4,
        seed=0,
):

    mesh = bpy.data.meshes.new("GothicColumn")

    obj = bpy.data.objects.new("GothicColumn", mesh)

    context.collection.objects.link(obj)

    bm = bmesh.new()

    # ------------------------
    # BASE
    # ------------------------

    bmesh.ops.create_cone(
        bm,
        cap_ends=True,
        cap_tris=False,
        segments=64,
        radius1=base_radius,
        radius2=base_radius * 0.9,
        depth=0.40
    )

    # ------------------------
    # SHAFT
    # ------------------------

    result = bmesh.ops.create_cone(
        bm,
        cap_ends=True,
        cap_tris=False,
        segments=48,
        radius1=radius,
        radius2=radius,
        depth=height
    )

    shaft = result["verts"]

    mat = Matrix.Translation((0, 0, height / 2 + 0.2))

    bmesh.ops.transform(
        bm,
        verts=shaft,
        matrix=mat
    )

    bm.to_mesh(mesh)
    bm.free()

    obj.location = (0, 0, 0)

    return obj
