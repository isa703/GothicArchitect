import bpy


class GA_OT_add_gothic_column(bpy.types.Operator):
    bl_idname = "ga.add_gothic_column"
    bl_label = "Add Gothic Column"
    bl_description = "Create a procedural Gothic column"

    def execute(self, context):
        self.report({'INFO'}, "Gothic Column: next step will generate the mesh")
        return {'FINISHED'}
