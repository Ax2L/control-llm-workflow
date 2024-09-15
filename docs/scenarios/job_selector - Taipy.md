Select jobs from the list of all job entities.

The job selector shows all the job entities handled by Taipy Core and lets the user select a job or a set of jobs from the list.

## Properties[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/job_selector/#properties "Permanent link")

<sup id="dv">(★)</sup>[`value`](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/job_selector/#p-value "Jump to the default property documentation.") is the default property for this visual element.

## Details[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/job_selector/#details "Permanent link")

The `job_selector` control lists all jobs resulting from submissions of entities.

All jobs are represented as a row in a table with all the related details.

Here is an example of what the job selector control would look like with default settings after a few jobs were executed:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/job_selector-init-d.png)

The list of Jobs

## Selection

The user can select one or more jobs from the list. The variable bound to the [_value_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/job_selector/#p-value) property is updated accordingly. A list of selected jobs is returned if several jobs were selected.

All jobs can be selected or deselected by switching the top-left check box to set or unset.

## Actions

If the [_show\_delete_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/job_selector/#p-show_delete) property is not set to False, a trash icon appears on the right side of the row, for jobs that can be deleted (jobs that are not running). This allows for removing the job from the list.  
Similarly, if jobs that can be deleted are selected, and if the [_show\_delete_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/job_selector/#p-show_delete) property is set to True, a trash icon appears at the top-right corner of the control, to delete all selected jobs from the list.

If the [_show\_cancel_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/job_selector/#p-show_cancel) property is not set to False, running jobs have a 'stop' icon in their row, allowing to cancel them.  
A similar icon appears at the top-right corner of the control when selected jobs can be canceled.

## Filters

In the top left corner of the job selector control, there is a _filter_ button that can be used to filter the displayed jobs depending on criteria that the user can specify:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/job_selector-filter-d.png)

The filter button

When the user clicks that button, a filter dialog pops up where one can set different filters with different criteria:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/job_selector-filter1-d.png)

The filter dialog

Initially, this dialog has no configured filter, therefore the _apply_ button indicates that '0' filters would be set.

To create a new filter, the user must select one of the control's columns, an operator (such as _is_ and _is not_), and an operand as a value.  
In the following image, the user has indicated that only the jobs where the _Status_ is set to "ABANDONED" should be listed:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/job_selector-filter2-d.png)

Specifying a filter

After the 'Add filter' button (with the '+' sign) is pressed, the filter is created:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/job_selector-filter3-d.png)

Adding a filter

The filter can be removed by pressing the trash icon to the right of the filter row.

Note that the 'Apply' button now indicates that there is a filter that can be applied.

Pressing the 'Apply' button applies the filter to the job selector list, resulting in the following image:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/job_selector-filter4-d.png)

The filter is applied

Note that next to the 'filter' button, the control now displays the number of currently applied filters.

## Usage[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/job_selector/#usage "Permanent link")

### Show or hide columns[¶](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/job_selector/#show-or-hide-columns "Permanent link")

The control's properties [_show\_id_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/job_selector/#p-show_id), [_show\_submitted\_label_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/job_selector/#p-show_submitted_label), [_show\_submitted\_id_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/job_selector/#p-show_submitted_id), [_show\_submission\_id_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/job_selector/#p-show_submission_id), [_show\_date_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/job_selector/#p-show_date), [_show\_cancel_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/job_selector/#p-show_cancel), and [_show\_delete_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/job_selector/#p-show_delete), and [_show\_submit\_sequences_](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/job_selector/#p-show_submit_sequences) let you indicate what columns the job selector control displays.

We can define our control so the job identifiers and the submission dates are not shown, to have a more compact display:

Page content

```
<span></span><code>&lt;|{job}|job_selector|don't show_id|don't show_date|&gt;
</code>
```

Here is what the control would look like:

![](https://docs.taipy.io/en/release-3.0/manuals/gui/corelements/job_selector-columns-d.png)

Choosing the displayed columns