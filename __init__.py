
bl_info = {
    "name": "Gothic Architect",
    "author": "Isa703",
    "version": (0, 3, 0),
    "blender": (5, 1, 0),
    "location": "View3D > Sidebar > Gothic",
    "description": "Procedural Gothic Architecture Generator",
    "category": "Add Mesh",
}

import bpy

from . import properties
from . import ui
from .operators import add_column


classes = (
    properties.GA_ColumnProperties,
    add_column.GA_OT_AddColumn,
    ui.GA_PT_MainPanel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.ga_props = bpy.props.PointerProperty(
        type=properties.GA_ColumnProperties
    )


def unregister():

    del bpy.types.Scene.ga_props

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()

