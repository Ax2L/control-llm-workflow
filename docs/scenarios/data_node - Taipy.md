Displays and edits of a data node.

The data node viewer control displays a data node entity's information and lets users edit it.

## Properties[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node/#properties "Permanent link")

<sup id="dv">(★)</sup>[`data_node`](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node/#p-data_node "Jump to the default property documentation.") is the default property for this visual element.

## Details[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node/#details "Permanent link")

The data node viewer displays the attributes of the data node set to the [_data\_node_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node/#p-data_node) property:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node-init-d.png)

The Data Node viewer

The topmost section shows the data node's label and storage type.  
The arrow button lets the user collapse or expand the whole control.

The lower section is made of three tabs whose content is described below.

### The 'Properties' tab[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node/#the-properties-tab "Permanent link")

From this tab, you can access the attributes of the data node:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node-properties-d.png)

The Properties section

The label of the data node can be changed using the 'Label' field: click in the value area, change the content, then press the 'Apply' button (with the ✓ icon.)  
To cancel the change, press the 'Cancel' button (with the ⨉ icon).

If the data node is owned by a scenario or a cycle, and if the [_show\_owner_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node/#p-show_owner) property is set to True (which is its default value), the label of the owning entity appears in the 'Owner' information line:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node-properties-owner-d.png)

The data node is owned by a scenario

When the selected data node is owned by a scenario, a button is visible next to the scenario's label. This button can be pressed to display the list of the owning scenarios so the user can select one from there. As a result, any variable bound to the [_scenario_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node/#p-scenario) is set to the selected scenario entity: the application can use that to update other parts of the page from an `on_change` callback.

The section at the bottom lists the custom properties for the selected data node. This is visible only if the [_show\_properties_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node/#p-show_properties) property is set to True (which is its default value).  
The user can create new properties by clicking the 'New Property Key' line, providing a property name and value, and then pressing the 'Apply' button (with the ✓ icon.).  
The user can cancel the creation of a new property by pressing the 'Cancel' button (with the ⨉ icon).  
The user can delete a property by selecting it and pressing the _trash_ button.

### The 'History' tab[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node/#the-history-tab "Permanent link")

The section is visible only if the [_show\_history_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node/#p-show_history) is set to True (which is its default value).

In this section, the user has access to the chronological list of changes applied to the selected data node.

Each history entry holds the date and time when the change was done and potentially some information on the data changes.

### The 'Data' tab[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node/#the-data-tab "Permanent link")

The section is visible only if the [_show\_data_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node/#p-show_data) is set to True (which is its default value).

In this section, the user can visualize the data referenced by the selected data node and change the data interactively.

Depending on the data type the data node uses, there are two display and edit modes.

#### Scalar data[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node/#scalar-data "Permanent link")

When the data node refers to a scalar value, it is displayed as a simple text:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node-data-scalar-d.png)

Scalar value

To edit the data node, the user can click the line where the value is displayed:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node-data-scalar-edit-d.png)

Editing a scalar value

Note that a 'Comment' field allows the user to explain why this value is changed. This information is part of the history of the data node.

When the new value is entered, the user presses the 'Apply' (✓) or the 'Cancel' (⨉) button to apply or cancel the change, respectively.

#### Tabular data[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node/#tabular-data "Permanent link")

Tabular data can be represented in tables or charts.  
The way the data is represented depends on the setting of the representation switch located in the top-left corner of the 'Properties' section:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node-data-tabular-switch-d.png)

Data representation switch

In the image above, the switch is set to the 'Table' mode.  
The other option is the 'Chart' mode.

Tabular data can be edited in the 'Table' mode only, as described in [this section](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node/#editing-tabular-data).

##### Table mode[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node/#table-mode "Permanent link")

Here is an example of tabular data represented in a table:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node-data-tabular-table-d.png)

Tabular data in a table

The down-down button labeled 'Columns' lets the user select the dataset columns that must be represented in the table.  
The 'Reset view' button resets that setting so all columns are visible.

###### Editing tabular data[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node/#editing-tabular-data "Permanent link")

The tabular mode has an 'Edit data' switch in the top-right corner of the 'Data' section. If this switch is turned on, the user can edit the table cells by clicking the relevant pencil button next to cell values:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node-data-tabular-edit-d.png)

Editing tabular data

The user will typically edit several cells before quitting the edit mode.  
When values are correctly updated manually, the user can set a comment (that will appear in the data node history) and quit the edit mode.

##### Chart mode[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node/#chart-mode "Permanent link")

The chart mode displays the data node's referenced data in a chart that can be customized:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node-data-tabular-chart-d.png)

Tabular data in a chart

Several traces can be added (using the '+ Add trace' button), and their respective settings can be indicated (in the 'Category', 'x', and 'y' drop-down menus).  
The user can also indicate that traces should be represented as accumulating values setting the 'Cumulative' switch _on_.  
Here is an example of a data node that references data with several columns, represented as a cumulative area chart:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/data_node-data-tabular-chart-2-d.png)

Tabular data in a chart