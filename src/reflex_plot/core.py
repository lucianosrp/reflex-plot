from typing import Literal, TypeAlias

import narwhals as nw
import reflex as rx
from narwhals.typing import IntoDataFrame

LineStyle: TypeAlias = Literal["-", "--", "..."]
Grid: TypeAlias = Literal["x", "y", "both"]


def _get_grid_linestyle(
    linestyle: LineStyle | None, linewidth: int = 3
) -> dict:
    match linestyle:
        case "-":
            return {}
        case "--":
            return dict(stroke_dasharray=f"{linewidth} {linewidth}")
        case _:
            return {}


def _get_grid(grid: Grid) -> dict:
    match grid:
        case "both":
            return {}
        case "y":
            return dict(horizontal=True, vertical=False)
        case "x":
            return dict(vertical=True, horizontal=False)


def plot(
    df: IntoDataFrame,
    kind: Literal["line", "area", "bar"],
    x: str,
    y: str,
    xlabel: str | None = None,
    ylabel: str | None = None,
    grid: Grid | None = "x",
    grid_linestyle: LineStyle | None = "-",
    grid_linewidth: int = 3,
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

    if grid is not None:
        components.append(
            rx.recharts.cartesian_grid(
                **(
                    _get_grid(grid)
                    | _get_grid_linestyle(grid_linestyle, grid_linewidth)
                ),
            ),
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
