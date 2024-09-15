Select scenarios from the list of all scenario entities.

The scenario selector shows all the scenario entities handled by Taipy Core and lets the user select a scenario from a list, create new scenarios or edit existing scenarios.

## Properties[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_selector/#properties "Permanent link")

<sup id="dv">(★)</sup>[`value`](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_selector/#p-value "Jump to the default property documentation.") is the default property for this visual element.

## Details[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_selector/#details "Permanent link")

The scenario selector displays a tree selector where scenarios are grouped based on their cycle (if the property [_display\_cycles_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_selector/#p-display_cycles) has not been set to False).  
If the [_show\_primary\_flag_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_selector/#p-show_primary_flag) property has not been forced to False, the label of the primary scenario are overlaid with a small visual hint that lets users spot them immediately.

If no created scenario has been created yet, the tree selector will appear empty. The default behavior, controlled by the [_show\_add\_button_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_selector/#p-show_add_button) property, is to display a button letting users create new scenarios:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_selector-empty-d.png)

Empty scenario selector

When the user presses that button, a form appears so that the settings of the new scenario can be set:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_selector-create-d.png)

Dialog to create a new scenario

In this form, the user must indicate which scenario configuration should be used and specify the scenario creation date.  
Custom properties can also be added to the new scenario by pressing the '+' button located on the right side of the property key and value fields.

When several new scenarios are created, the scenario selector will list all the scenarios, potentially grouped in their relevant cycle:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_selector-filled-d.png)

Showing all the created scenarios

Notice how the primary scenario for a cycle is immediately flagged as "primary" (you may choose not to show that icon by setting the [_show\_primary\_flag_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_selector/#p-show_primary_flag) property to False).

### Editing a scenario[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_selector/#editing-a-scenario "Permanent link")

Users can press the pencil icon located next to the scenario labels. When that happens, a dialog box similar to the scenario creation dialog is displayed to let users modify the scenario settings.

Here is how this dialog box looks like:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_selector-edition-d.png)

Editing a scenario

The user can change the scenario label and custom properties then press the 'Apply' button to propagate the changes.  
To add a new custom property, the user has to fill the 'Key' and 'Value' fields in the 'Custom Properties' section, then press the '+' button.  
A custom property can be removed by pressing the trash button next to it.  

The 'Cancel' button closes the dialog without changing anything.  
The 'Delete' button deletes the edited scenario.

Note that there is no way to change the scenario configuration or its creation date.

### Selecting a scenario[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_selector/#selecting-a-scenario "Permanent link")

When the user selects a scenario in the tree selector, the [_value_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_selector/#p-value) property is set to the selected entity and the [_on\_change_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_selector/#p-on_change) callback is invoked. The application can then use the selected value.

If no scenario is selected, [_value_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_selector/#p-value) is set no None.

## Usage[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_selector/#usage "Permanent link")

### Customizing the creation[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_selector/#customizing-the-creation "Permanent link")

You can set the [_on\_creation_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_selector/#p-on_creation) property to a callback function that lets you customize how a new scenario is created when pressing the 'Add Scenario' button.

This callback function expects three parameters:

-   _state_: the [`State`](https://docs.taipy.io/en/release-3.0/manuals/reference/taipy.gui.State) of the user;
-   _id_: the identifier of the control, if any;
-   _payload_: a dictionary that contains the following keys:
    -   _action_: the name of the callback function;
    -   _config_: the [`ScenarioConfig`](https://docs.taipy.io/en/release-3.0/manuals/reference/taipy.core.config.ScenarioConfig) that was selected in the dialog;
    -   _date_: a `datetime.datetime` object representing the date and time when the creation was requested;
    -   _label_: the scenario label as specified in the dialog. This string is used as the scenario name;
    -   _properties_: a dictionary that contains all the custom properties that the user has defined in the creation dialog.

The _payload_ parameter contains all the information that is needed to create a new scenario. In the callback function, you can use these parameters to customize the new scenario creation further.

-   If all those parameters look just fine in terms of what needs to be achieved, the callback function can simply return None. That will get Taipy to carry on with the scenario creation with no customization whatsoever.  
    That is the default behavior of a `scenario_selector` control that has no value in its [_on\_creation_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_selector/#p-on_creation).
-   If the parameters (typically the custom property keys or values) are invalid in the application's context, you may want to refuse the creation of the scenario. In this case, the callback function should return a string that provides visual feedback to the user (or an empty string if this is not needed).
-   You can also create the scenario in the function callback and return it. This is the opportunity to change the scenario creation parameters to fit the application's needs.

Here is an example of a creation callback function that deals with these three situations.

Imagine that the application, if the user has added the "index" custom property to a scenario, needs to check that the property value is valid and transform it before the scenario is actually created.  
In our example, we expect the user to set a positive integer value to the property "index". The code will check that the value is valid and replace it with a string representation of this value minus one, prefixed with the sharp ('#') sign.  
Here is the code for the creation callback function:

<table><tbody><tr><td><div><pre><span></span><span> 1</span>
<span> 2</span>
<span> 3</span>
<span> 4</span>
<span> 5</span>
<span> 6</span>
<span> 7</span>
<span> 8</span>
<span> 9</span>
<span>10</span>
<span>11</span>
<span>12</span>
<span>13</span>
<span>14</span>
<span>15</span>
<span>16</span>
<span>17</span>
<span>18</span>
<span>19</span>
<span>20</span>
<span>21</span>
<span>22</span>
<span>23</span></pre></div></td><td><div><pre id="__code_0"><span></span><code><span>def</span> <span>check_index</span><span>(</span><span>state</span><span>,</span> <span>id</span><span>,</span> <span>payload</span><span>):</span>
  <span># Retrieve the custom properties</span>
    <span>properties</span> <span>=</span> <span>payload</span><span>.</span><span>get</span><span>(</span><span>"properties"</span><span>,</span> <span>None</span><span>)</span>
    <span>if</span> <span>not</span> <span>properties</span> <span>or</span> <span>not</span> <span>"index"</span> <span>in</span> <span>properties</span><span>:</span>
        <span># No custom 'index' property</span>
        <span># Create a regular scenario</span>
        <span>return</span> <span>None</span>
    <span># Read the 'index' property</span>
    <span>index</span> <span>=</span> <span>None</span>
    <span>try</span><span>:</span>
        <span>index</span> <span>=</span> <span>int</span><span>(</span><span>properties</span><span>[</span><span>"index"</span><span>])</span>
        <span># Invalid value: must be greater than 1</span>
        <span>if</span> <span>index</span> <span>&lt;</span> <span>1</span><span>:</span>
            <span>return</span> <span>"'index' must be strictly positive"</span>
        <span># Replace the property value</span>
        <span>properties</span><span>[</span><span>"index"</span><span>]</span> <span>=</span> <span>f</span><span>"#</span><span>{</span><span>index</span><span>-</span><span>1</span><span>}</span><span>"</span>
    <span>except</span><span>:</span> <span># Invalid value: not an integer</span>
        <span>return</span> <span>"'index' property is not a valid integer"</span>
    <span># Create a new scenario with the same configuration, label, and date</span>
    <span>scenario</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>payload</span><span>[</span><span>"config"</span><span>],</span> <span>payload</span><span>[</span><span>"date"</span><span>],</span> <span>payload</span><span>[</span><span>"label"</span><span>])</span>
    <span># Set the scenario properties</span>
    <span>scenario</span><span>.</span><span>properties</span><span>.</span><span>update</span><span>(</span><span>properties</span><span>)</span>
    <span>return</span> <span>scenario</span>
</code></pre></div></td></tr></tbody></table>

When the user requests the creation of a new scenario, the creation dialog pops up. When fields are properly set (only the label is mandatory), the user will press the 'Create' button to confirm the scenario creation.  
At this time, the application will invoke the creation callback to customize the scenario parameters.

Lines 4-7 deal with the case where the _index_ custom property was _not_ set. In this case, we want to do nothing special and carry on with the regular creation of the control, returning None from the callback function.

Line 9-18 verify that the _index_ custom property is a valid integer greater than one. If this is not the case, an error message is returned to the user for correction.

Finally, lines 20-22 take care of creating the scenario with the new settings.  
This scenario is returned by the callback function to let Taipy know it was created properly.

The scenario selector control definition needs to have the [_on\_creation_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario_selector/#p-on_creation) property set to the function:

Page content

```
<span></span><code>&lt;|{scenario}|scenario_selector|on_creation=check_index|&gt;
</code>
```