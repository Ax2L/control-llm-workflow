Displays and modify the definition of a scenario.

## Properties[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario/#properties "Permanent link")

<sup id="dv">(★)</sup>[`scenario`](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario/#p-scenario "Jump to the default property documentation.") is the default property for this visual element.

## Details[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario/#details "Permanent link")

The _scenario control_ displays the information stored in a given scenario, lets the user change its parameters at runtime, and provides ways to submit it or one of its sequences.

When the [_scenario_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario/#p-scenario) property is set to a [`Scenario`](https://docs.taipy.io/en/release-3.0/manuals/reference/taipy.core.Scenario) instance, the control displays the information for that scenario.

Here is what the control would look like when representing a scenario entity:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario-init-d.png)

Viewing the parameters of a scenario

Next to the scenario's label at the top of the control and if the scenario is _primary_ in its cycle, there is an icon showing a flag.  
On the right side of the label, a 'play' button can trigger the scenario submission.

The user can see the scenario's tags in the 'Tags' section.  
To add a tag, simply enter some text in the tags area and press 'Enter'. You can create as many tags as you want. When you are done, and you want to add those tags to the scenario, press the 'Apply' button located to the right of the tags area.  
You can cancel your actions by pressing the 'Cancel' button.

If the scenario has sequences, the user can submit each sequence independently by pressing the 'play' button to the right of the sequence's label.

The user can click the scenario label to change it:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario-edit-label-d.png)

Editing the scenario label

The user must click the 'check' button to apply the change or the 'cross' button to cancel the operation.

Users can also add or modify custom properties. Click on an existing property name or value to modify it, and the "New Property Key" label or "Value" next to it to create a new custom property.  
Here is what the section looks like when the user requests the creation of a new property:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario-edit-props-d.png)

Editing custom properties

To delete a custom property, the user must select it, then press The 'trash' button that appears on the right side.

## Usage[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario/#usage "Permanent link")

### Show or hide sections[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario/#show-or-hide-sections "Permanent link")

A few properties (namely [_show\_submit_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario/#p-show_submit), [_show\_delete_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario/#p-show_delete), [_show\_config_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario/#p-show_config), [_show\_cycle_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario/#p-show_cycle), [_show\_tags_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario/#p-show_tags), [_show\_properties_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario/#p-show_properties), [_show\_sequences_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario/#p-show_sequences), and [_show\_submit\_sequences_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario/#p-show_submit_sequences)) let you customize what sections of the `scenario` control are visible.

Here is the definition of such a control where the _tags_, _properties_ and _sequences_ sections are hidden:

Page content

```
<span></span><code>&lt;|{scenario}|scenario|don't show_tags|don't show_properties|don't show_sequences|&gt;
</code>
```

The control appears as follows, in a more compact manner:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/scenario-flags-d.png)

Hiding some sections