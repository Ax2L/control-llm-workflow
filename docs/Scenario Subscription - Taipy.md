_Estimated Time for Completion: 15 minutes; Difficulty Level: Advanced_

To perform an action after a job status change, you can [subscribe a function](https://docs.taipy.io/en/latest/manuals/core/entities/orchestrating-and-job-execution/#subscribe-to-job-execution) to a scenario. When there is a status change, this function is triggered. This feature enables the creation of logs or specific events for the Taipy GUI.

[Download the code](https://docs.taipy.io/en/latest/tutorials/scenario_management/7_scenario_subscription/src/scenario_subscription.py)

```
<span></span><code tabindex="0"><span>def</span> <span>callback_scenario_state</span><span>(</span><span>scenario</span><span>,</span> <span>job</span><span>):</span>
<span>    </span><span>"""All the scenarios are subscribed to the callback_scenario_state function. It means whenever</span>
<span>    a job is done, it is called.</span>
<span>    Depending on the job and the status, it will update the message stored in a json that is then</span>
<span>    displayed on the GUI.</span>

<span>    Args:</span>
<span>        scenario (Scenario): the scenario of the job changed</span>
<span>        job (_type_): the job that has its status changed</span>
<span>    """</span>
    <span>print</span><span>(</span><span>f</span><span>'</span><span>{</span><span>job</span><span>.</span><span>id</span><span>}</span><span> to </span><span>{</span><span>job</span><span>.</span><span>status</span><span>}</span><span>'</span><span>)</span>

    <span>if</span> <span>job</span><span>.</span><span>status</span> <span>==</span> <span>tp</span><span>.</span><span>core</span><span>.</span><span>Status</span><span>.</span><span>COMPLETED</span><span>:</span>
        <span>for</span> <span>data_node</span> <span>in</span> <span>job</span><span>.</span><span>task</span><span>.</span><span>output</span><span>.</span><span>values</span><span>():</span>
            <span>print</span><span>(</span><span>"Data node value:"</span><span>,</span> <span>data_node</span><span>.</span><span>read</span><span>())</span>
</code>
```

A scenario can then subscribe to this callback. For example, a scenario with this configuration:

![Configuration](https://docs.taipy.io/en/latest/tutorials/scenario_management/7_scenario_subscription/images/config.svg)

```
<span></span><code><span>scenario</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenarios</span><span>(</span><span>scenario_cfg</span><span>)</span>

<span>scenario</span><span>.</span><span>subscribe</span><span>(</span><span>scenario_cfg</span><span>)</span>

<span>scenario</span><span>.</span><span>submit</span><span>()</span>
</code>
```

Results:

```
<span></span><code><span>JOB_double_... to Status.PENDING</span>
<span>JOB_add_... to Status.BLOCKED</span>
<span>JOB_double_... to Status.RUNNING</span>
<span>JOB_double_... to Status.COMPLETED</span>
<span>Data node value: 42</span>
<span>JOB_add_... to Status.PENDING</span>
<span>JOB_add_... to Status.RUNNING</span>
<span>JOB_add_... to Status.COMPLETED</span>
<span>Data node value: 52</span>
</code>
```

## Real-time feedback on the GUI[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/7_scenario_subscription/#real-time-feedback-on-the-gui "Permanent link")

The `on_submission_change` property extends this functionality in a GUI setting. It triggers a specific function upon each submission status change, enabling real-time updates to the user interface. This ensures that users are always informed of the current status, from SUBMITTED to COMPLETED or CANCELED, enhancing user experience through immediate feedback and interaction.

## Parameters of the Function[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/7_scenario_subscription/#parameters-of-the-function "Permanent link")

-   `state (State)`: The state instance.
-   `submittable (Submittable)`: The entity, usually a Scenario, that was submitted.
-   `details (dict)`: Details on this callback's invocation, including the new status of the submission and the Job causing the status change.

## Handling Different Submission Statuses[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/7_scenario_subscription/#handling-different-submission-statuses "Permanent link")

Here’s an example of how you can use this property in your code:

```
<span></span><code tabindex="0"><span>from</span> <span>taipy.gui</span> <span>import</span> <span>Gui</span><span>,</span> <span>notify</span>

<span>def</span> <span>on_submission_status_change</span><span>(</span><span>state</span><span>,</span> <span>submittable</span><span>,</span> <span>details</span><span>):</span>
    <span>submission_status</span> <span>=</span> <span>details</span><span>.</span><span>get</span><span>(</span><span>'submission_status'</span><span>)</span>

    <span>if</span> <span>submission_status</span> <span>==</span> <span>'COMPLETED'</span><span>:</span>
        <span>print</span><span>(</span><span>f</span><span>"</span><span>{</span><span>submittable</span><span>.</span><span>name</span><span>}</span><span> has completed."</span><span>)</span>
        <span>notify</span><span>(</span><span>state</span><span>,</span> <span>'success'</span><span>,</span> <span>'Completed!'</span><span>)</span>
        <span># Add additional actions here, like updating the GUI or logging the completion.</span>

    <span>elif</span> <span>submission_status</span> <span>==</span> <span>'FAILED'</span><span>:</span>
        <span>print</span><span>(</span><span>f</span><span>"</span><span>{</span><span>submittable</span><span>.</span><span>name</span><span>}</span><span> has failed."</span><span>)</span>
        <span>notify</span><span>(</span><span>state</span><span>,</span> <span>'error'</span><span>,</span> <span>'Completed!'</span><span>)</span>
        <span># Handle failure, like sending notifications or logging the error.</span>

    <span># Add more conditions for other statuses as needed.</span>
</code>
```

## Implementing in GUI[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/7_scenario_subscription/#implementing-in-gui "Permanent link")

When creating a GUI for your scenarios, you can associate this function with a visual element for real-time updates. For example:

```
<span></span><code>&lt;|{scenario}|scenario|on_submission_change=on_submission_status_change|&gt;
</code>
```

This visual element will be updated whenever there is a change in the submission status, providing real-time feedback on the GUI.

## Entire code[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/7_scenario_subscription/#entire-code "Permanent link")

```
<span></span><code tabindex="0"><span>from</span> <span>taipy.config</span> <span>import</span> <span>Config</span>
<span>from</span> <span>taipy.core</span> <span>import</span> <span>Status</span>
<span>import</span> <span>taipy</span> <span>as</span> <span>tp</span>
<span>import</span> <span>time</span>


<span># Normal function used by Taipy</span>
<span>def</span> <span>double</span><span>(</span><span>nb</span><span>):</span>
    <span>return</span> <span>nb</span> <span>*</span> <span>2</span>

<span>def</span> <span>add</span><span>(</span><span>nb</span><span>):</span>
    <span>return</span> <span>nb</span> <span>+</span> <span>10</span>


<span># Configuration of Data Nodes</span>
<span>input_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>"my_input"</span><span>,</span> <span>default_data</span><span>=</span><span>21</span><span>)</span>
<span>intermediate_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>"intermediate"</span><span>)</span>
<span>output_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>"my_output"</span><span>)</span>


<span># Configuration of tasks</span>
<span>first_task_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_task</span><span>(</span><span>"double"</span><span>,</span>
                                       <span>double</span><span>,</span>
                                       <span>input_cfg</span><span>,</span>
                                       <span>intermediate_cfg</span><span>)</span>

<span>second_task_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_task</span><span>(</span><span>"add"</span><span>,</span>
                                        <span>add</span><span>,</span>
                                        <span>intermediate_cfg</span><span>,</span>
                                        <span>output_cfg</span><span>)</span>


<span>def</span> <span>callback_scenario_state</span><span>(</span><span>scenario</span><span>,</span> <span>job</span><span>):</span>
<span>    </span><span>"""All the scenarios are subscribed to the callback_scenario_state function. It means whenever a job is done, it is called.</span>
<span>    Depending on the job and the status, it will update the message stored in a json that is then displayed on the GUI.</span>

<span>    Args:</span>
<span>        scenario (Scenario): the scenario of the job changed</span>
<span>        job (_type_): the job that has its status changed</span>
<span>    """</span>
    <span>print</span><span>(</span><span>scenario</span><span>.</span><span>name</span><span>)</span>
    <span>if</span> <span>job</span><span>.</span><span>status</span> <span>==</span> <span>Status</span><span>.</span><span>COMPLETED</span><span>:</span>
        <span>for</span> <span>data_node</span> <span>in</span> <span>job</span><span>.</span><span>task</span><span>.</span><span>output</span><span>.</span><span>values</span><span>():</span>
            <span>print</span><span>(</span><span>data_node</span><span>.</span><span>read</span><span>())</span>

<span># Configuration of scenario</span>
<span>scenario_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_scenario</span><span>(</span><span>id</span><span>=</span><span>"my_scenario"</span><span>,</span>
                                         <span>task_configs</span><span>=</span><span>[</span><span>first_task_cfg</span><span>,</span> <span>second_task_cfg</span><span>],</span>
                                         <span>name</span><span>=</span><span>"my_scenario"</span><span>)</span>


<span>if</span> <span>__name__</span><span>==</span><span>"__main__"</span><span>:</span>
    <span>tp</span><span>.</span><span>Core</span><span>()</span><span>.</span><span>run</span><span>()</span>
    <span>scenario_1</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>scenario_cfg</span><span>)</span>
    <span>scenario_1</span><span>.</span><span>subscribe</span><span>(</span><span>callback_scenario_state</span><span>)</span>

    <span>scenario_1</span><span>.</span><span>submit</span><span>(</span><span>wait</span><span>=</span><span>True</span><span>)</span>


<span>from</span> <span>taipy.gui</span> <span>import</span> <span>Gui</span><span>,</span> <span>notify</span>

<span>def</span> <span>on_submission_status_change</span><span>(</span><span>state</span><span>=</span><span>None</span><span>,</span> <span>submittable</span><span>=</span><span>None</span><span>,</span> <span>details</span><span>=</span><span>None</span><span>):</span>
    <span>submission_status</span> <span>=</span> <span>details</span><span>.</span><span>get</span><span>(</span><span>'submission_status'</span><span>)</span>

    <span>if</span> <span>submission_status</span> <span>==</span> <span>'COMPLETED'</span><span>:</span>
        <span>print</span><span>(</span><span>f</span><span>"</span><span>{</span><span>submittable</span><span>.</span><span>name</span><span>}</span><span> has completed."</span><span>)</span>
        <span>notify</span><span>(</span><span>state</span><span>,</span> <span>'success'</span><span>,</span> <span>'Completed!'</span><span>)</span>
        <span># Add additional actions here, like updating the GUI or logging the completion.</span>

    <span>elif</span> <span>submission_status</span> <span>==</span> <span>'FAILED'</span><span>:</span>
        <span>print</span><span>(</span><span>f</span><span>"</span><span>{</span><span>submittable</span><span>.</span><span>name</span><span>}</span><span> has failed."</span><span>)</span>
        <span>notify</span><span>(</span><span>state</span><span>,</span> <span>'error'</span><span>,</span> <span>'Completed!'</span><span>)</span>
        <span># Handle failure, like sending notifications or logging the error.</span>

    <span># Add more conditions for other statuses as needed.</span>


<span>if</span> <span>__name__</span><span>==</span><span>"__main__"</span><span>:</span>
    <span>scenario_md</span> <span>=</span> <span>"""</span>
<span>&lt;|</span><span>{scenario_1}</span><span>|scenario|on_submission_change=on_submission_status_change|&gt;</span>
<span>"""</span>
    <span>Gui</span><span>(</span><span>scenario_md</span><span>)</span><span>.</span><span>run</span><span>()</span>
</code>
```