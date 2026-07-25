import bpy

from ..geometry.column import build_column


class GA_OT_AddColumn(bpy.types.Operator):
    """Create a procedural Gothic column"""

    bl_idname = "ga.add_column"
    bl_label = "Create Gothic Column"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        props = context.scene.ga_props

        build_column(
            context=context,
            height=props.height,
            radius=props.radius,
            base_radius=props.base_radius,
            capital_height=props.capital_height,
            capital_radius=props.capital_radius,
            shafts=props.shafts,
            seed=props.seed,
        )

        self.report({'INFO'}, "Gothic column created.")

        return {'FINISHED'}
