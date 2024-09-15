Displays a list of the Data Node entities that can be selected.

## Properties[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node_selector/#properties "Permanent link")

<sup id="dv">(★)</sup>[`value`](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node_selector/#p-value "Jump to the default property documentation.") is the default property for this visual element.

## Details[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node_selector/#details "Permanent link")

The control displays a tree selector where all data node entities are listed.  
If [_display\_cycles_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node_selector/#p-display_cycles) is set to False, the cycles are not represented.

In an application that would have created a few data nodes, some of them being scoped at the scenario level, here is what the data node selector would look like:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node_selector-init-d.png)

The list of selectable data nodes

Data nodes are organized in their owning scenario and cycle, when relevant.

When the user selects a data node, the [_on\_change_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node_selector/#p-on_change) callback is invoked so that the application can use the selected value. The value is set to the [_value_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node_selector/#p-value) property.

## Pins

When there are many data nodes in your application, the user can filter out a set of data nodes by _pinning_ them and then set the _Pinned only_ switch (that is active only if some data nodes are pinned): only pinned data nodes will then appear in the list.

Assuming we are in the following situation:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node_selector-pin1-d.png)

Crowded data node selector

If the user wants to focus only on the 'initial\_dataset' and the data nodes from the scenario called 'Peter's', she can click on the pin icon next to these two items. Here is what the display would look like:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node_selector-pin2-d.png)

Data node selector with pinned items

Here is what the control looks like after the 'Pinned only' switch was set and the scenario item was expanded:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node_selector-pin3-d.png)

Filtering pinned data nodes

You can see that only the pinned data nodes are visible.

Note that the cycle item is not pinned because the other scenarios it contains are not, either.

-   If all data nodes for a scenario or a cycle are pinned, the scenario or cycle item is itself pinned.
-   A scenario or cycle item appears _not pinned_ if any of its data nodes is not pinned.
-   _Pinning_ a scenario item pins all its data nodes.  
    _Unpinning_ a scenario item unpins all its data nodes.
-   _Pinning_ a cycle item pins all the data nodes of all its scenarios.  
    _Unpinning_ a cycle item unpins all the data nodes of all its scenarios.

To reveal all existing data nodes, the _Pinned only_ switch must be turned off.