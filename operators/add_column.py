import bpy

from ..geometry.column import build_column


class GA_OT_add_gothic_column(bpy.types.Operator):
    bl_idname = "ga.add_gothic_column"
    bl_label = "Add Gothic Column"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        props = context.scene.ga_props

        build_column(
            context,
            height=props.height,
            radius=props.radius,
            base_radius=props.base_radius,
            capital_height=props.capital_height,
            capital_radius=props.capital_radius,
            shafts=props.shafts,
            seed=props.seed,
        )

        self.report({'INFO'}, "Column created!")

        return {'FINISHED'}


        for ox, oy in offsets:

    result = bmesh.ops.create_cone(
        bm,
        cap_ends=True,
        cap_tris=False,
        segments=24,
        radius1=small_r,
        radius2=small_r,
        depth=height * 0.98,
    )

    verts = result["verts"]

    bmesh.ops.transform(
        bm,
        verts=verts,
        matrix=Matrix.Translation((ox, oy, small_z)),
    )