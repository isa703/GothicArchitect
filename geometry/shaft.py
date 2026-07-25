import bmesh


def build_shaft(bm, radius, height, segments=32):
    """
    Creates the main shaft of the column.
    Temporary implementation.
    """

    result = bmesh.ops.create_cone(
        bm,
        cap_ends=False,
        cap_tris=False,
        segments=segments,
        radius1=radius,
        radius2=radius,
        depth=height,
    )

    return result