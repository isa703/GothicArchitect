def build_shaft(builder, props):

    bottom = builder.create_circle(
        radius=props.radius,
        z=0.0,
        segments=props.segments
    )

    top = builder.create_circle(
        radius=props.radius,
        z=props.height,
        segments=props.segments
    )

    builder.bridge(bottom, top)