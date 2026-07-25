
import bpy


class GA_PT_main_panel(bpy.types.Panel):
    bl_label = "Gothic Architect"
    bl_idname = "GA_PT_main_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Gothic"

    def draw(self, context):
        layout = self.layout
        props = context.scene.ga_props

        layout.prop(props, "height")
        layout.prop(props, "radius")
        layout.prop(props, "base_radius")
        layout.prop(props, "capital_height")
        layout.prop(props, "capital_radius")
        layout.prop(props, "shafts")
        layout.prop(props, "seed")

        layout.operator("ga.add_gothic_column", icon="MESH_CYLINDER")
