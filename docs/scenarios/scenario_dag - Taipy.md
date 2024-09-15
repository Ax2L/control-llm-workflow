Displays the DAG of a scenario.

## Properties[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_dag/#properties "Permanent link")

<sup id="dv">(★)</sup>[`scenario`](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_dag/#p-scenario "Jump to the default property documentation.") is the default property for this visual element.

## Details[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_dag/#details "Permanent link")

When the [_scenario_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_dag/#p-scenario) property is set to an instance of [`Scenario`](https://docs.taipy.io/en/release-3.0/manuals/reference/taipy.core.Scenario), the control displays a graphical representation of its DAG.

Here is what the control looks like when connected to a scenario instance:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_dag-init-d.png)

The DAG of a scenario

The visual representation of the Data Nodes and Tasks is the same as the one used in the [Taipy Studio extension](https://docs.taipy.io/en/release-3.0/manuals/studio/config/graphview/).

The toolbar, which can be removed by setting the [_show\_toolbar_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_dag/#p-show_toolbar) property to False, contains a button that adapts the rendering area zoom factor to the graph representation.