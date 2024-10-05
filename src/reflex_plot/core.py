from typing import Literal, Optional, Dict

import pandas as pd
import reflex as rx


def plot(
    df: pd.DataFrame,
    kind: Literal["line", "area", "bar"],
    x: str,
    y: str,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    grid: bool = False,
    tool_tip: bool = False,
    heigth: int = 300,
    width: str = "100%",
    margin: Dict[str,int] = dict(left=60, bottom=60)
) -> rx.Component:
    components = [
        getattr(rx.recharts, kind)(data_key=y),
        rx.recharts.x_axis(x or xlabel, label=dict(value=x, position="bottom")),
        rx.recharts.y_axis(
            y or ylabel, label=dict(value=y, position="left", angle=-90)
        ),
    ]

    if grid:
        components.append(
            rx.recharts.cartesian_grid(stroke_dasharray="4 4"),
        )

    if tool_tip:
        components.append(rx.recharts.graphing_tooltip())

    return getattr(rx.recharts, f"{kind}_chart")(
        *components,
        data=df.to_dict("records"),
        width=width,
        height=heigth,
        margin=margin,
    )
