import bpy


def build_column(
    context,
    height,
    radius,
    base_radius,
    capital_height,
    capital_radius,
    shafts,
    seed,
):

    bpy.ops.mesh.primitive_cylinder_add(
        vertices=32,
        radius=radius,
        depth=height,
        location=(0, 0, height / 2),
    )

    obj = context.active_object
    obj.name = "Gothic_Column"
