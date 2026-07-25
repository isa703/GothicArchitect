import bpy


class GA_PT_MainPanel(bpy.types.Panel):
    bl_label = "Gothic Architect"
    bl_idname = "GA_PT_main_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Gothic"

    def draw(self, context):
        layout = self.layout
        props = context.scene.ga_props

        box = layout.box()
        box.label(text="Gothic Column")

        box.prop(props, "height")
        box.prop(props, "radius")
        box.prop(props, "base_radius")
        box.prop(props, "capital_height")
        box.prop(props, "capital_radius")
        box.prop(props, "shafts")
        box.prop(props, "seed")

        layout.separator()

        layout.operator(
            "ga.add_column",
            text="Create Gothic Column",
            icon="MESH_CYLINDER",
        )
