
bl_info = {
    "name": "Gothic Architect",
    "author": "OpenAI",
    "version": (1, 0, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > Gothic Architect",
    "description": "Procedural Gothic architecture generator",
    "category": "Add Mesh",
}

import bpy

from . import properties
from . import ui
from .operators import add_column


classes = (
    properties.GA_ColumnProperties,
    add_column.GA_OT_add_gothic_column,
    ui.GA_PT_main_panel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.ga_props = bpy.props.PointerProperty(type=properties.GA_ColumnProperties)


def unregister():
    del bpy.types.Scene.ga_props

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
