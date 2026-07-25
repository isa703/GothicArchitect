
import bpy


class GA_ColumnProperties(bpy.types.PropertyGroup):
    height: bpy.props.FloatProperty(
        name="Height",
        default=5.0,
        min=0.1,
        max=100.0
    )

    radius: bpy.props.FloatProperty(
        name="Radius",
        default=0.5,
        min=0.01,
        max=20.0
    )

    base_radius: bpy.props.FloatProperty(
        name="Base Radius",
        default=1.0,
        min=0.01,
        max=20.0
    )

    capital_height: bpy.props.FloatProperty(
        name="Capital Height",
        default=0.8,
        min=0.01,
        max=10.0
    )

    capital_radius: bpy.props.FloatProperty(
        name="Capital Radius",
        default=0.9,
        min=0.01,
        max=20.0
    )

    shafts: bpy.props.IntProperty(
        name="Columns",
        default=4,
        min=1,
        max=12
    )

    seed: bpy.props.IntProperty(
        name="Seed",
        default=0,
        min=0,
        max=999999
    )
