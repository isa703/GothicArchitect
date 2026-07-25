import bpy
from bpy.props import (
    FloatProperty,
    IntProperty,
)


class GA_ColumnProperties(bpy.types.PropertyGroup):

    height: FloatProperty(
        name="Height",
        default=4.0,
        min=1.0,
        max=30.0,
    )

    radius: FloatProperty(
        name="Radius",
        default=0.30,
        min=0.05,
        max=5.0,
    )

    base_radius: FloatProperty(
        name="Base Radius",
        default=0.45,
        min=0.05,
        max=5.0,
    )

    capital_height: FloatProperty(
        name="Capital Height",
        default=0.50,
        min=0.05,
        max=5.0,
    )

    capital_radius: FloatProperty(
        name="Capital Radius",
        default=0.50,
        min=0.05,
        max=5.0,
    )

    shafts: IntProperty(
        name="Bundle Shafts",
        default=8,
        min=1,
        max=16,
    )

    seed: IntProperty(
        name="Seed",
        default=0,
        min=0,
        max=999999,
    )
