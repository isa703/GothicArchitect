import bpy

from ...core.mesh_builder import MeshBuilder

from .shaft import build_shaft
from .base import build_base
from .bundle import build_bundle
from .capital import build_capital


class ColumnGenerator:

    def __init__(self, context, props):
        self.context = context
        self.props = props

    def build(self):

        builder = MeshBuilder()

        build_base(builder, self.props)
        build_shaft(builder, self.props)
        build_bundle(builder, self.props)
        build_capital(builder, self.props)

        mesh = bpy.data.meshes.new("GA_Column")

        builder.mesh.to_mesh(mesh)
        builder.mesh.free()

        obj = bpy.data.objects.new("GA_Column", mesh)

        self.context.collection.objects.link(obj)

        obj.select_set(True)
        self.context.view_layer.objects.active = obj

        return obj