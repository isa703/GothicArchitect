import bpy
import math


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
    # Главен ствол
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=48,
        radius=radius,
        depth=height,
        location=(0, 0, height / 2),
    )

    column = context.active_object
    column.name = "Gothic_Column"

    # Основа
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=48,
        radius=base_radius,
        depth=0.25,
        location=(0, 0, 0.125),
    )

    base = context.active_object
    base.name = "Column_Base"

    # Капител
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=48,
        radius=capital_radius,
        depth=capital_height,
        location=(0, 0, height + capital_height / 2),
    )

    capital = context.active_object
    capital.name = "Column_Capital"

    # Малки колони около главната
    offset = radius * 1.8

    for i in range(shafts):
        angle = math.radians((360 / shafts) * i)

        x = math.cos(angle) * offset
        y = math.sin(angle) * offset

        bpy.ops.mesh.primitive_cylinder_add(
            vertices=24,
            radius=radius * 0.18,
            depth=height,
            location=(x, y, height / 2),
        )

    # Обединяване в един обект
    bpy.ops.object.select_all(action='DESELECT')

    for obj in context.scene.objects:
        if obj.name.startswith(("Gothic_Column", "Column_Base", "Column_Capital", "Cylinder")):
            obj.select_set(True)

    context.view_layer.objects.active = column
    bpy.ops.object.join()

    column.name = "Gothic_Column"
