from typing import Literal

import narwhals as nw
import reflex as rx
from narwhals.typing import IntoDataFrame


def plot(
    df: IntoDataFrame,
    kind: Literal["line", "area", "bar"],
    x: str,
    y: str,
    xlabel: str | None = None,
    ylabel: str | None = None,
    grid: bool = False,
    tool_tip: bool = False,
    heigth: int = 300,
    width: str = "100%",
    margin: dict[str, int] = dict(left=60, bottom=60),
) -> rx.Component:
    df = nw.from_native(df)
    data = df.rows(named=True)
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
        data=data,
        width=width,
        height=heigth,
        margin=margin,
    )
