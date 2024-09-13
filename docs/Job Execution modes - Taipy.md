_Estimated Time for Completion: 15 minutes; Difficulty Level: Advanced_

[Download the code](https://docs.taipy.io/en/latest/tutorials/scenario_management/5_job_execution/src/job_execution.zip)

Taipy has [different ways](https://docs.taipy.io/en/latest/manuals/core/config/job-config/) to execute the code. Changing the execution mode can be useful for running multiple tasks in parallel.

-   _standalone_ mode: asynchronous. Jobs can be run in parallel depending on the graph of execution (if _max\_nb\_of\_workers_ > 1).
    
-   _development_ mode: synchronous. The default execution mode is _development_.
    

We define a configuration and functions to showcase the two execution modes.

```
<span></span><code><span># Normal function used by Taipy</span>
<span>def</span> <span>double</span><span>(</span><span>nb</span><span>):</span>
    <span>return</span> <span>nb</span> <span>*</span> <span>2</span>

<span>def</span> <span>add</span><span>(</span><span>nb</span><span>):</span>
    <span>print</span><span>(</span><span>"Wait 10 seconds in add function"</span><span>)</span>
    <span>time</span><span>.</span><span>sleep</span><span>(</span><span>10</span><span>)</span>
    <span>return</span> <span>nb</span> <span>+</span> <span>10</span>
</code>
```

![Configuration](https://docs.taipy.io/en/latest/tutorials/scenario_management/5_job_execution/images/config.svg)

This line of code alters the execution mode. Setting it to _standalone_ makes Taipy Core work asynchronously. In this configuration, a maximum of two tasks can run simultaneously.

```
<span></span><code><span>Config</span><span>.</span><span>configure_job_executions</span><span>(</span><span>mode</span><span>=</span><span>"standalone"</span><span>,</span> <span>max_nb_of_workers</span><span>=</span><span>2</span><span>)</span>
</code>
```

```
<span></span><code><span>if</span> <span>__name__</span><span>==</span><span>"__main__"</span><span>:</span>
    <span>tp</span><span>.</span><span>Core</span><span>()</span><span>.</span><span>run</span><span>()</span>
    <span>scenario_1</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>scenario_cfg</span><span>)</span>
    <span>scenario_2</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>scenario_cfg</span><span>)</span>

    <span>scenario_1</span><span>.</span><span>submit</span><span>()</span>
    <span>scenario_2</span><span>.</span><span>submit</span><span>()</span>

    <span>time</span><span>.</span><span>sleep</span><span>(</span><span>30</span><span>)</span>
</code>
```

Jobs from the two submissions are being executed simultaneously. If `max_nb_of_workers` was greater, we could run multiple scenarios at the same time and multiple tasks of a scenario at the same time.

Some options for the _submit_ function exist:

-   _wait_: if _wait_ is True, the submission waits for the end of all the jobs (if _timeout_ is not defined).
    
-   _timeout_: if _wait_ is True, Taipy waits for the end of the submission up to a certain amount of time.
    

```
<span></span><code><span>if</span> <span>__name__</span><span>==</span><span>"__main__"</span><span>:</span>
    <span>tp</span><span>.</span><span>Core</span><span>()</span><span>.</span><span>run</span><span>()</span>
    <span>scenario_1</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>scenario_cfg</span><span>)</span>
    <span>scenario_1</span><span>.</span><span>submit</span><span>(</span><span>wait</span><span>=</span><span>True</span><span>)</span>
    <span>scenario_1</span><span>.</span><span>submit</span><span>(</span><span>wait</span><span>=</span><span>True</span><span>,</span> <span>timeout</span><span>=</span><span>5</span><span>)</span>
</code>
```

## Entire code[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/5_job_execution/#entire-code "Permanent link")

```
<span></span><code><span>from</span> <span>taipy.core.config</span> <span>import</span> <span>Config</span>
<span>import</span> <span>taipy</span> <span>as</span> <span>tp</span>
<span>import</span> <span>datetime</span> <span>as</span> <span>dt</span>
<span>import</span> <span>pandas</span> <span>as</span> <span>pd</span>
<span>import</span> <span>time</span>

<span># Normal function used by Taipy</span>
<span>def</span> <span>double</span><span>(</span><span>nb</span><span>):</span>
    <span>return</span> <span>nb</span> <span>*</span> <span>2</span>

<span>def</span> <span>add</span><span>(</span><span>nb</span><span>):</span>
    <span>print</span><span>(</span><span>"Wait 10 seconds in add function"</span><span>)</span>
    <span>time</span><span>.</span><span>sleep</span><span>(</span><span>10</span><span>)</span>
    <span>return</span> <span>nb</span> <span>+</span> <span>10</span>

<span>Config</span><span>.</span><span>configure_job_executions</span><span>(</span><span>mode</span><span>=</span><span>"standalone"</span><span>,</span> <span>max_nb_of_workers</span><span>=</span><span>2</span><span>)</span>

<span># Configuration of Data Nodes</span>
<span>input_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>"my_input"</span><span>,</span> <span>default_data</span><span>=</span><span>21</span><span>)</span>
<span>intermediate_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>"intermediate"</span><span>,</span> <span>default_data</span><span>=</span><span>21</span><span>)</span>
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

<span># Configuration of scenario</span>
<span>scenario_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_scenario</span><span>(</span><span>id</span><span>=</span><span>"my_scenario"</span><span>,</span>
                                         <span>task_configs</span><span>=</span><span>[</span><span>first_task_cfg</span><span>,</span>
                                                       <span>second_task_cfg</span><span>])</span>

<span>Config</span><span>.</span><span>export</span><span>(</span><span>"config_07.toml"</span><span>)</span>

<span>if</span> <span>__name__</span><span>==</span><span>"__main__"</span><span>:</span>
    <span>tp</span><span>.</span><span>Core</span><span>()</span><span>.</span><span>run</span><span>()</span>
    <span>scenario_1</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>scenario_cfg</span><span>)</span>
    <span>scenario_2</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>scenario_cfg</span><span>)</span>
    <span>scenario_1</span><span>.</span><span>submit</span><span>()</span>
    <span>scenario_2</span><span>.</span><span>submit</span><span>()</span>

    <span>scenario_1</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>scenario_cfg</span><span>)</span>
    <span>scenario_1</span><span>.</span><span>submit</span><span>(</span><span>wait</span><span>=</span><span>True</span><span>)</span>
    <span>scenario_1</span><span>.</span><span>submit</span><span>(</span><span>wait</span><span>=</span><span>True</span><span>,</span> <span>timeout</span><span>=</span><span>5</span><span>)</span>
</code>
```