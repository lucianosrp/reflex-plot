import pandas as pd
from inline_snapshot import snapshot

from reflex_plot.core import plot


def test_bar_plot():
    df = pd.DataFrame({"a": [1, 2], "b": [10, 0]})
    chart = plot(
        df,
        kind="bar",
        x="a",
        y="b",
        grid=True,
        tool_tip=True,
    ).render()

    assert chart == snapshot(
        {
            "name": "RechartsResponsiveContainer",
            "props": ["height={300}", "width={`100%`}",
            ],
            "contents": "",
            "args": None,
            "special_props": set(),
            "children": [{
    "name": "RechartsBarChart",
    "props": [
        "barCategoryGap={`10%`}",
        "barGap={4}",
        'data={[{"a": 1, "b": 10}, {"a": 2, "b": 0}]}',
        "height={`100%`}",
        'margin={{"left": 60, "bottom": 60}}',
        "width={`100%`}",
    ],
    "contents": "",
    "args": None,
    "special_props": set(),
    "children": [
        {
            "name": "RechartsBar",
            "props": ["dataKey={`b`}", "fill={`var(--accent-9)`}"],
            "contents": "",
            "args": None,
            "special_props": set(),
            "children": [],
            "autofocus": False,
        },
        {
            "name": "RechartsXAxis",
            "props": [
                "includeHidden={false}",
                'label={{"value": "a", "position": "bottom"}}',
                "stroke={`var(--gray-9)`}",
                "tickLine={false}",
            ],
            "contents": "",
            "args": None,
            "special_props": set(),
            "children": [
                {
                    "name": "",
                    "props": [],
                    "contents": "{`a`}",
                    "args": None,
                    "special_props": set(),
                    "children": [],
                    "autofocus": False,
                }
            ],
            "autofocus": False,
        },
        {
            "name": "RechartsYAxis",
            "props": [
                'label={{"value": "b", "position": "left", "angle": -90}}',
                "stroke={`var(--gray-9)`}",
                "tickLine={false}",
            ],
            "contents": "",
            "args": None,
            "special_props": set(),
            "children": [
                {
                    "name": "",
                    "props": [],
                    "contents": "{`b`}",
                    "args": None,
                    "special_props": set(),
                    "children": [],
                    "autofocus": False,
                }
            ],
            "autofocus": False,
        },
        {
            "name": "RechartsCartesianGrid",
            "props": ["stroke={`var(--gray-7)`}", "strokeDasharray={`4 4`}"],
            "contents": "",
            "args": None,
            "special_props": set(),
            "children": [],
            "autofocus": False,
        },
        {
            "name": "RechartsTooltip",
            "props": [
                'allowEscapeViewBox={{"x": false, "y": false}}',
                'contentStyle={{"background": "var(--gray-1)", "borderColor": "var(--gray-4)", "borderRadius": "8px"}}',
                'cursor={{"strokeWidth": 1, "fill": "var(--gray-3)"}}',
                'itemStyle={{"color": "var(--gray-12)"}}',
                'labelStyle={{"color": "var(--gray-11)"}}',
            ],
            "contents": "",
            "args": None,
            "special_props": set(),
            "children": [],
            "autofocus": False,
        },
    ],
    "autofocus": False,
}],
            "autofocus": False,
        }
    )


def test_line_plot():
    df = pd.DataFrame({"a": [1, 2], "b": [10, 0]})
    chart = plot(df, kind="line", x="a", y="b").render()

    assert chart == snapshot(
        {
            "name": "RechartsResponsiveContainer",
            "props": ["height={300}", "width={`100%`}",
            ],
            "contents": "",
            "args": None,
            "special_props": set(),
            "children": [{
    "name": "RechartsLineChart",
    "props": [
        'data={[{"a": 1, "b": 10}, {"a": 2, "b": 0}]}',
        "height={`100%`}",
        'margin={{"left": 60, "bottom": 60}}',
        "width={`100%`}",
    ],
    "contents": "",
    "args": None,
    "special_props": set(),
    "children": [
        {
            "name": "RechartsLine",
            "props": [
                'activeDot={{"stroke": "var(--accent-2)", "fill": "var(--accent-10)"}}',
                "dataKey={`b`}",
                'dot={{"stroke": "var(--accent-10)", "fill": "var(--accent-4)"}}',
                "stroke={`var(--accent-9)`}",
            ],
            "contents": "",
            "args": None,
            "special_props": set(),
            "children": [],
            "autofocus": False,
        },
        {
            "name": "RechartsXAxis",
            "props": [
                "includeHidden={false}",
                'label={{"value": "a", "position": "bottom"}}',
                "stroke={`var(--gray-9)`}",
                "tickLine={false}",
            ],
            "contents": "",
            "args": None,
            "special_props": set(),
            "children": [
                {
                    "name": "",
                    "props": [],
                    "contents": "{`a`}",
                    "args": None,
                    "special_props": set(),
                    "children": [],
                    "autofocus": False,
                }
            ],
            "autofocus": False,
        },
        {
            "name": "RechartsYAxis",
            "props": [
                'label={{"value": "b", "position": "left", "angle": -90}}',
                "stroke={`var(--gray-9)`}",
                "tickLine={false}",
            ],
            "contents": "",
            "args": None,
            "special_props": set(),
            "children": [
                {
                    "name": "",
                    "props": [],
                    "contents": "{`b`}",
                    "args": None,
                    "special_props": set(),
                    "children": [],
                    "autofocus": False,
                }
            ],
            "autofocus": False,
        },
    ],
    "autofocus": False,
}],
            "autofocus": False,
        }
    )


def test_area_plot():
    df = pd.DataFrame({"a": [1, 2], "b": [10, 0]})
    chart = plot(df, kind="area", x="a", y="b").render()

    assert chart == snapshot(
        {
            "name": "RechartsResponsiveContainer",
            "props": ["height={300}", "width={`100%`}",
            ],
            "contents": "",
            "args": None,
            "special_props": set(),
            "children": [{
    "name": "RechartsAreaChart",
    "props": [
        'data={[{"a": 1, "b": 10}, {"a": 2, "b": 0}]}',
        "height={`100%`}",
        'margin={{"left": 60, "bottom": 60}}',
        "width={`100%`}",
    ],
    "contents": "",
    "args": None,
    "special_props": set(),
    "children": [
        {
            "name": "RechartsArea",
            "props": [
                'activeDot={{"stroke": "var(--accent-2)", "fill": "var(--accent-10)"}}',
                "dataKey={`b`}",
                "fill={`var(--accent-5)`}",
                "stroke={`var(--accent-9)`}",
                "strokeWidth={1}",
                "type={`monotone`}",
            ],
            "contents": "",
            "args": None,
            "special_props": set(),
            "children": [],
            "autofocus": False,
        },
        {
            "name": "RechartsXAxis",
            "props": [
                "includeHidden={false}",
                'label={{"value": "a", "position": "bottom"}}',
                "stroke={`var(--gray-9)`}",
                "tickLine={false}",
            ],
            "contents": "",
            "args": None,
            "special_props": set(),
            "children": [
                {
                    "name": "",
                    "props": [],
                    "contents": "{`a`}",
                    "args": None,
                    "special_props": set(),
                    "children": [],
                    "autofocus": False,
                }
            ],
            "autofocus": False,
        },
        {
            "name": "RechartsYAxis",
            "props": [
                'label={{"value": "b", "position": "left", "angle": -90}}',
                "stroke={`var(--gray-9)`}",
                "tickLine={false}",
            ],
            "contents": "",
            "args": None,
            "special_props": set(),
            "children": [
                {
                    "name": "",
                    "props": [],
                    "contents": "{`b`}",
                    "args": None,
                    "special_props": set(),
                    "children": [],
                    "autofocus": False,
                }
            ],
            "autofocus": False,
        },
    ],
    "autofocus": False,
}],
            "autofocus": False,
        }
    )
