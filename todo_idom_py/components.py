import json
from uuid import uuid4

from idom import component, html

from .datastructure import TodoList


def event_dbg(event):
    print(json.dumps(event, indent=2))


@component
def Button(label, color=None):

    return html.button(
        {
            "class": "btn",
            "onClick": event_dbg,
            "style": {
                "backgroundColor": color,
                "borderRadius": "8px",
            },
        },
        label,
        key=uuid4().hex,
    )


@component
def Item(i: dict):

    return html.li(
        {"style": {"margin": "0.5em"}},
        html.input({"onChange": event_dbg, "type": "checkbox"}, key=uuid4().hex),
        html.label({"style": {"margin": "0.5em"}}, i["text"]),
        Button("✏️", color="blue"),
        Button("🗑️", color="red"),
        key=i["id"],
    )


new_task_form = html.form(
    html.input({"onChange": event_dbg, "style": {"margin": "0.5em"}}),
    Button("➕", color="green"),
)


@component
def DataList(items, filter_by_priority=None, sort_by_priority=False):
    if filter_by_priority:
        items = [i for i in items if i["priority"] <= filter_by_priority]
    if sort_by_priority:
        items = list(sorted(items, key=lambda x: x["priority"]))
    list_item_elements = [Item(i) for i in items]
    return html.ul(
        {
            "style": {"listStyleType": "none"},
        },
        new_task_form,
        list_item_elements,
    )


@component
def TodoApp():
    t = TodoList()

    return html.section(
        html.h1("My Todo List"),
        DataList(t.tasks, filter_by_priority=1, sort_by_priority=True),
    )
