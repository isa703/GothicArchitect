from ..geometry.column import build_column

class GA_OT_add_gothic_column(bpy.types.Operator):

    bl_idname = "ga.add_gothic_column"
    bl_label = "Add Gothic Column"

    def execute(self, context):

        props = context.scene.ga_props

        build_column(
            context,
            props.height,
            props.radius,
            props.base_radius,
            props.capital_height,
            props.capital_radius,
            props.shafts,
            props.seed,
        )

        return {'FINISHED'}
