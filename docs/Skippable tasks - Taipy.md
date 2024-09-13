Taipy is a Python library that's user-friendly and made for creating web applications with interactive interfaces that handle data. This tip is all about Taipy's back-end capabilities. Just as a reminder, the main goal of Taipy's back-end is to help you build and manage complex workflows, such as data processing pipelines.

![Skippable Tasks](https://docs.taipy.io/en/latest/tutorials/scenario_management/3_skippable_tasks/images/skippable_tasks.png)

When engineers create Directed Acyclic Graphs (DAGs), they often leave out certain tasks. This common practice allows tasks to be orchestrated in a more dynamic and advanced way. One of the key features of Taipy's back-end is _skippable_ tasks, which can be skipped under specific conditions. In this tip, we'll explore how skippable tasks work in Taipy and how to use them effectively.

### Setting up Data Nodes for Tasks[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/3_skippable_tasks/#setting-up-data-nodes-for-tasks "Permanent link")

A Task in Taipy is a way to represent a Python function that you want to use in the execution graph.

It contains:

-   Input and output Data nodes.
-   The Python function that you've defined and want to use.

![Setting up Data Nodes for Tasks](https://docs.taipy.io/en/latest/tutorials/scenario_management/3_skippable_tasks/images/skippable_tasks_2.png)

Before you start using skippable tasks, it's important to configure your tasks correctly with their Data nodes. You can refer to documentation for more details on [Data nodes](https://docs.taipy.io/en/latest/tutorials/scenario_management/2_the_data_nodes/).

For instance, let's say you have a function like _multiply\_and\_add()_ that takes two parameters and returns two values. How can you represent this function as a Taipy Task?

```
<span></span><code><span>def</span> <span>multiply_and_add</span><span>(</span><span>nb1</span><span>,</span> <span>nb2</span><span>):</span>
    <span>return</span> <span>nb1</span> <span>+</span> <span>nb2</span><span>,</span> <span>nb1</span> <span>*</span> <span>nb2</span>
</code>
```

In the animation below:

-   The first tab corresponds to the creation of the configuration graphically using Taipy Studio.
-   The second tab corresponds to the creation of the very same configuration programmatically.

The order in which you supply Data nodes to the Task is critical. Taipy calls the function using the parameters in the same order as the Data nodes, and the results are returned in that exact order.

 Your browser does not support the video tag.

```
<span></span><code tabindex="0"><span>from</span> <span>taipy.config</span> <span>import</span> <span>Config</span>

<span>nb_1_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>'nb1'</span><span>)</span>
<span>nb_2_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>'nb2'</span><span>)</span>

<span>sum_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>'sum'</span><span>)</span>
<span>product_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>'product'</span><span>)</span>

<span>task_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_task</span><span>(</span><span>"multiply_and_add"</span><span>,</span> <span>multiply_and_add</span><span>,</span> <span>[</span><span>nb_1_cfg</span><span>,</span> <span>nb_2_cfg</span><span>],</span> <span>[</span><span>sum_cfg</span><span>,</span> <span>product_cfg</span><span>])</span>
<span>scenario_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_scenario</span><span>(</span><span>"scenario"</span><span>,</span> <span>[</span><span>task_cfg</span><span>])</span>
</code>
```

In this example, the _multiply\_and\_add()_ function takes two parameters (_nb1_ and _nb2_). It returns two values: the product and the sum. We create configurations for the input Data nodes (_nb\_1\_cfg_ and _nb\_2\_cfg_ in this order) and the output Data nodes (_sum\_cfg_ and _product\_cfg_).

Finally, we configure the Task with the appropriate input and output Data nodes.

### Leveraging Skippability in Taipy Tasks[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/3_skippable_tasks/#leveraging-skippability-in-taipy-tasks "Permanent link")

Skippability is an optional setting that you can enable when configuring a Task.

When you set skippable to True, Taipy will skip executing the Task if its input Data nodes have not changed since the last execution. In other words, if running the task again would produce the same output, it is skipped.

This feature can significantly improve the performance of your data workflow by preventing unnecessary computations, which saves time and resources.

![Leveraging Skippability in Taipy Tasks](https://docs.taipy.io/en/latest/tutorials/scenario_management/3_skippable_tasks/images/skippable_tasks_3.png)

### Use Case[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/3_skippable_tasks/#use-case "Permanent link")

Let’s take the previous execution graph and set _skippable=True_ to our Task.

 Your browser does not support the video tag.

```
<span></span><code><span>...</span>
<span>task_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_task</span><span>(</span><span>"multiply_and_add"</span><span>,</span>
                                  <span>function</span><span>=</span><span>multiply_and_add</span><span>,</span>
                                  <span>input</span><span>=</span><span>[</span><span>nb_1_cfg</span><span>,</span> <span>nb_2_cfg</span><span>],</span>
                                  <span>output</span><span>=</span><span>[</span><span>sum_cfg</span><span>,</span> <span>product_cfg</span><span>],</span> <span>skippable</span><span>=</span><span>True</span><span>)</span>
<span>...</span>
</code>
```

With the code below, we create and submit an instance of this scenario configuration.

```
<span></span><code><span>scenario</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>scenario_cfg</span><span>)</span>
<span>tp</span><span>.</span><span>submit</span><span>(</span><span>scenario</span><span>)</span>
<span>print</span><span>(</span><span>"Results (sum):"</span><span>,</span> <span>scenario</span><span>.</span><span>sum</span><span>.</span><span>read</span><span>())</span>
</code>
```

```
<span></span><code><span>[</span><span>...</span><span>]</span> <span>[</span><span>Taipy</span><span>]</span> <span>[</span><span>INFO</span><span>]</span>   <span>job</span>   <span>JOB_multiply_and_add_</span><span>...</span>   <span>is</span>
<span>completed</span><span>.</span>
<span>Results</span> <span>(</span><span>sum</span><span>):</span> <span>23</span>
</code>
```

The task associated with my Task has been completed, which means that my function has been executed.

The line below is resubmitting the scenario, but please note that I haven't made any changes to my input Data nodes in any way.

```
<span></span><code><span>tp</span><span>.</span><span>submit</span><span>(</span><span>scenario</span><span>)</span>
<span>print</span><span>(</span><span>"Results (sum):"</span><span>,</span> <span>scenario</span><span>.</span><span>sum</span><span>.</span><span>read</span><span>())</span>
</code>
```

As expected, Taipy is skipping the Task because the input parameters haven't changed. If there are multiple tasks in this scenario, Taipy may skip several of them.

The code below shows what happens when we submit the scenario after making a change to an input Data node. In this case, the value of _nb\_1_ is updated from 21 to 42.

```
<span></span><code><span>scenario</span><span>.</span><span>nb_1</span><span>.</span><span>write</span><span>(</span><span>42</span><span>)</span>
<span>tp</span><span>.</span><span>submit</span><span>(</span><span>scenario</span><span>)</span>
<span>print</span><span>(</span><span>"Results (sum):"</span><span>,</span> <span>scenario</span><span>.</span><span>sum</span><span>.</span><span>read</span><span>())</span>
</code>
```

```
<span></span><code><span>[</span><span>...</span><span>]</span> <span>[</span><span>Taipy</span><span>]</span> <span>[</span><span>INFO</span><span>]</span>   <span>job</span>   <span>JOB_multiply_and_add_</span><span>...</span>   <span>is</span>
<span>completed</span><span>.</span>
<span>Results</span> <span>(</span><span>sum</span><span>):</span> <span>44</span>
</code>
```

The input changed, so Taipy will re-execute my Task and give the appropriate results (44).

### Using Global Data Nodes[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/3_skippable_tasks/#using-global-data-nodes "Permanent link")

Skipping tasks doesn't only happen when you resubmit a scenario; it can also occur when creating and submitting a completely new scenario with Global Data nodes.

For instance, if you want to preprocess a raw data set and make the result accessible globally across the entire application, you can change the scope of both Data nodes (the raw data set and the result) to Global. This means that all scenarios will share these Data nodes, and the Task related to this operation might be skipped across different scenarios.

Let's revisit our previous code and modify the Data nodes to have a Global scope.

 Your browser does not support the video tag.

```
<span></span><code tabindex="0"><span>from</span> <span>taipy.config</span> <span>import</span> <span>Config</span><span>,</span> <span>Scope</span>

<span>nb_1_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>'nb1'</span><span>,</span> <span>scope</span><span>=</span><span>Scope</span><span>.</span><span>GLOBAL</span><span>)</span>
<span>nb_2_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>'nb2'</span><span>,</span> <span>scope</span><span>=</span><span>Scope</span><span>.</span><span>GLOBAL</span><span>)</span>

<span>sum_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>'sum'</span><span>,</span> <span>scope</span><span>=</span><span>Scope</span><span>.</span><span>GLOBAL</span><span>)</span>
<span>product_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>'product'</span><span>,</span> <span>scope</span><span>=</span><span>Scope</span><span>.</span><span>GLOBAL</span><span>)</span>

<span>task_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_task</span><span>(</span><span>"multiply_and_add"</span><span>,</span> <span>multiply_and_add</span><span>,</span> <span>[</span><span>nb_1_cfg</span><span>,</span> <span>nb_2_cfg</span><span>],</span> <span>[</span><span>sum_cfg</span><span>,</span> <span>product_cfg</span><span>])</span>
<span>scenario_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_scenario</span><span>(</span><span>"scenario"</span><span>,</span> <span>[</span><span>task_cfg</span><span>])</span>
</code>
```

The first line creates a scenario consisting of Data nodes, and tasks. Following this, we submit it.

```
<span></span><code><span>scenario_1</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>scenario_cfg</span><span>)</span>
<span>tp</span><span>.</span><span>submit</span><span>(</span><span>scenario_1</span><span>)</span>
<span>print</span><span>(</span><span>"Results (sum):"</span><span>,</span> <span>scenario_1</span><span>.</span><span>sum</span><span>.</span><span>read</span><span>())</span>
</code>
```

```
<span></span><code><span>[</span><span>...</span><span>]</span> <span>[</span><span>Taipy</span><span>]</span> <span>[</span><span>INFO</span><span>]</span>   <span>job</span>   <span>JOB_task_multiply_and_add_</span><span>...</span>   <span>is</span>
<span>completed</span><span>.</span>
</code>
```

The only task has been completed, and the results have been computed.

Now, let's create another scenario. This new scenario won't create new Global Data nodes (both input and output). Instead, it will reuse the ones that were created by _scenario\_1_.

```
<span></span><code><span>scenario_2</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>scenario_cfg</span><span>)</span>
<span>tp</span><span>.</span><span>submit</span><span>(</span><span>scenario_2</span><span>)</span>
<span>print</span><span>(</span><span>"Results (sum):"</span><span>,</span> <span>scenario_2</span><span>.</span><span>sum</span><span>.</span><span>read</span><span>())</span>
</code>
```

```
<span></span><code><span>[</span><span>...</span><span>]</span> <span>[</span><span>Taipy</span><span>]</span> <span>[</span><span>INFO</span><span>]</span>   <span>job</span>   <span>JOB_task_multiply_and_add_</span><span>...</span>   <span>is</span>
<span>skipped</span><span>.</span>
<span>Results</span> <span>(</span><span>sum</span><span>):</span> <span>23</span>
</code>
```

Taipy skips the Task if the input Data nodes have not changed and reuses the existing output's Data.

### Manual Changes[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/3_skippable_tasks/#manual-changes "Permanent link")

Taipy uses the last modification date of a Data Node to determine if an input Data node has been changed. This modification date can be altered in three ways:

-   When you submit a Task or a scenario, it automatically updates the last modification date.
-   You can manually update it by writing: `DataNode.write()`.
-   Taipy also monitors the last modification date of the file that your Data Node refers to. If you (or a separate process) modify a file (e.g., CSV, JSON, etc.) that the Data Node is linked to, Taipy detects this change and adjusts the skippable logic accordingly.

### Conclusion[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/3_skippable_tasks/#conclusion "Permanent link")

In conclusion, Taipy simplifies the management of complex workflows and their execution. The use of skippable tasks allows developers to enhance efficiency significantly by avoiding redundant computations, ultimately saving time and resources for end users. Skippable tasks can be applied in various scenarios, including when resubmitting scenarios or making manual changes to Data nodes.

By grasping and utilizing skippable tasks effectively in Taipy, developers can create efficient and streamlined applications that provide better service to their users.