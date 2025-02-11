from typing import Any, Dict, Literal, Optional

import narwhals as nw
import reflex as rx
from narwhals.typing import IntoDataFrame


def key_value_to_dicts(data_dict: dict[str, list[Any]]) -> list[dict[str, Any]]:
    """Convert dictionary form {key1:[v1,v2], key2:[v3,v4]} into [{key1:v1,key2:v3},{key1:v2,key2:v4}]."""
    result = []
    max_length = max(len(values) for values in data_dict.values())

    for i in range(max_length):
        entry = {}
        for key, values in data_dict.items():
            if i < len(values):
                entry[key] = values[i]
        result.append(entry)

    return result


def plot(
    df: IntoDataFrame,
    kind: Literal["line", "area", "bar"],
    x: str,
    y: str,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    grid: bool = False,
    tool_tip: bool = False,
    heigth: int = 300,
    width: str = "100%",
    margin: Dict[str, int] = dict(left=60, bottom=60),
) -> rx.Component:
    df = nw.from_native(df)
    data = key_value_to_dicts(df.to_dict(as_series=False))
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
