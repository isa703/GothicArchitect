import bmesh


def build_base(bm, radius, height=0.25, segments=32):
    """
    Creates the base of the column.
    Returns the top face so the shaft can continue from it.
    """

    result = bmesh.ops.create_cone(
        bm,
        cap_ends=True,
        cap_tris=False,
        segments=segments,
        radius1=radius,
        radius2=radius,
        depth=height,
    )

    return result