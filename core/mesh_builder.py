import bmesh
from math import cos, sin, tau


class MeshBuilder:

    def __init__(self):
        self.bm = bmesh.new()

    @property
    def mesh(self):
        return self.bm

    def create_circle(self, radius, z, segments=32):
        verts = []

        for i in range(segments):
            angle = tau * i / segments

            verts.append(
                self.bm.verts.new(
                    (
                        cos(angle) * radius,
                        sin(angle) * radius,
                        z
                    )
                )
            )

        self.bm.verts.ensure_lookup_table()

        return verts

    def bridge(self, ring1, ring2):

        count = len(ring1)

        for i in range(count):

            v1 = ring1[i]
            v2 = ring1[(i + 1) % count]

            v3 = ring2[(i + 1) % count]
            v4 = ring2[i]

            self.bm.faces.new((v1, v2, v3, v4))