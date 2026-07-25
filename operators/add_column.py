from ..geometry.column.generator import ColumnGenerator


def execute(self, context):

    props = context.scene.ga_column

    ColumnGenerator(
        context,
        props
    ).build()

    return {'FINISHED'}