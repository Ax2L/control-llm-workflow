_Estimated Time for Completion: 30 minutes; Difficulty Level: Intermediate_

In this section, we will explore the intricate relationship between [Scopes](https://docs.taipy.io/en/latest/manuals/core/concepts/scope/) and [Cycles](https://docs.taipy.io/en/latest/manuals/core/concepts/cycle/), two core concepts that help manage data nodes and scenarios effectively in Taipy.

[Download the code](https://docs.taipy.io/en/latest/tutorials/scenario_management/4_cycles_scopes/src/scope_and_cycle.zip)

## Cycles[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/4_cycles_scopes/#cycles "Permanent link")

Using [Cycles](https://docs.taipy.io/en/latest/manuals/core/concepts/cycle/) allow you to:

-   Share variables between scenarios in the same time frame

For example, if I have three sales prediction scenarios for the month of June, I do not have to duplicate the data for each scenario. I can share the June sales data between the three scenarios.

-   Better organize the data nodes in your application

![Data Node Selector](https://docs.taipy.io/en/latest/tutorials/scenario_management/4_cycles_scopes/images/data_node_selector.png)

Here we have a single month\_data node for all scenarios of October 2022 and it is part of the October 2022 cycle. I do not need to create a new data node for each scenario and clutter my application.

### Example: Filtering by Month[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/4_cycles_scopes/#example-filtering-by-month "Permanent link")

```
<span></span><code><span>def</span> <span>filter_by_month</span><span>(</span><span>df</span><span>,</span> <span>month</span><span>):</span>
    <span>df</span><span>[</span><span>'Date'</span><span>]</span> <span>=</span> <span>pd</span><span>.</span><span>to_datetime</span><span>(</span><span>df</span><span>[</span><span>'Date'</span><span>])</span>
    <span>df</span> <span>=</span> <span>df</span><span>[</span><span>df</span><span>[</span><span>'Date'</span><span>]</span><span>.</span><span>dt</span><span>.</span><span>month</span> <span>==</span> <span>month</span><span>]</span>
    <span>return</span> <span>df</span>
</code>
```

![Configuration](https://docs.taipy.io/en/latest/tutorials/scenario_management/4_cycles_scopes/images/config.svg)

### Configuration[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/4_cycles_scopes/#configuration "Permanent link")

Configuration

![](https://docs.taipy.io/en/latest/tutorials/scenario_management/4_cycles_scopes/images/config.gif)

-   Construct the configuration
    
-   Add the frequency property for the scenario and put "MONTHLY:FREQUENCY" (DAYLY, WEEKLY, MONTHLY, YEARLY)
    
-   Load the new [configuration](https://docs.taipy.io/en/latest/tutorials/scenario_management/4_cycles_scopes/src/config.toml) in the code
    

Since we have specified `frequency=Frequency.MONTHLY`, the corresponding scenario when created, is automatically attached to the correct period (month).

The Cycle which a Scenario belongs to is based on the _creation\_date_ of the scenario. It can be "attached" to a specific cycle by manually setting its _creation\_date_, as we are doing in the following example.

```
<span></span><code><span>tp</span><span>.</span><span>Core</span><span>()</span><span>.</span><span>run</span><span>()</span>

<span>scenario_1</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>scenario_cfg</span><span>,</span>
                                <span>creation_date</span><span>=</span><span>dt</span><span>.</span><span>datetime</span><span>(</span><span>2022</span><span>,</span><span>10</span><span>,</span><span>7</span><span>),</span>
                                <span>name</span><span>=</span><span>"Scenario 2022/10/7"</span><span>)</span>
<span>scenario_2</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>scenario_cfg</span><span>,</span>
                                <span>creation_date</span><span>=</span><span>dt</span><span>.</span><span>datetime</span><span>(</span><span>2022</span><span>,</span><span>10</span><span>,</span><span>5</span><span>),</span>
                                <span>name</span><span>=</span><span>"Scenario 2022/10/5"</span><span>)</span>
</code>
```

Scenario 1 and Scenario 2 are two separate scenario entities created using the same scenario configuration. They are part of the same `Cycle` but have different data nodes. By default, each scenario instance has its own data node instances, and they are not shared with any other scenario.

### Interplay between Scopes and Cycles[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/4_cycles_scopes/#interplay-between-scopes-and-cycles "Permanent link")

Cycles are generated according to the _creation\_date_ of scenarios. The scope, on the other hand, determines how data nodes are shared within these cycles and scenarios.

## Scopes[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/4_cycles_scopes/#scopes "Permanent link")

Sharing data nodes between entities allows you to organize and manage your data better. It avoids data duplications and allows Taipy to better manage execution (see [skippable tasks](https://docs.taipy.io/en/latest/tutorials/scenario_management/3_skippable_tasks/)). The developer may decide:

-   `Scope.SCENARIO` (_default_): Having one data node for each scenario.
-   `Scope.CYCLE`: Extend the scope by sharing data nodes across all scenarios of a given cycle.
-   `Scope.GLOBAL`: Expand the scope globally, applying it across all scenarios in all cycles.

Modifying the scope of a Data Node is straightforward. Let's change the configuration of our data nodes:

-   _historical\_data_: is a Global data node. It will be shared by every cycle and scenario.
    
-   _month_: is a Cycle data node. All scenarios of the same month will share this data.
    
-   _month\_values_: same for _month\_values_.
    

![Configuration with Scope](https://docs.taipy.io/en/latest/tutorials/scenario_management/4_cycles_scopes/images/config_scope.svg)

Configuration

![](https://docs.taipy.io/en/latest/tutorials/scenario_management/4_cycles_scopes/images/config_scope.gif)

-   Change the Scope of historical\_data to be global
    
-   Change the Scope of month\_data and month to be Cycle
    

Defining the _month_ of scenario 1 will also determine the _month_ of scenario 2 since they share the same Data Node.

```
<span></span><code><span>scenario_1</span><span>.</span><span>month</span><span>.</span><span>write</span><span>(</span><span>10</span><span>)</span>


<span>print</span><span>(</span><span>"Month Data Node of Scenario 1:"</span><span>,</span> <span>scenario_1</span><span>.</span><span>month</span><span>.</span><span>read</span><span>())</span>
<span>print</span><span>(</span><span>"Month Data Node of Scenario 2:"</span><span>,</span> <span>scenario_2</span><span>.</span><span>month</span><span>.</span><span>read</span><span>())</span>

<span>scenario_1</span><span>.</span><span>submit</span><span>()</span>
<span>scenario_2</span><span>.</span><span>submit</span><span>()</span>
</code>
```

Results:

```
<span></span><code>Month Data Node of Scenario 1: 10
Month Data Node of Scenario 2: 10
</code>
```

In this unusual example where both scenarios are in the same cycle and all their data nodes are at least with a `Cycle` Scope, executing one is the same as executing the other as they share all their data nodes.

## Going further into Cycles[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/4_cycles_scopes/#going-further-into-cycles "Permanent link")

### Primary scenarios[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/4_cycles_scopes/#primary-scenarios "Permanent link")

In each `Cycle`, there is a primary scenario. A primary scenario is interesting because it represents the important scenario of the `Cycle`, the reference. By default, the first scenario created for a cycle is primary.

#### Python code associated to primary scenarios[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/4_cycles_scopes/#python-code-associated-to-primary-scenarios "Permanent link")

[`tp.set_primary(<Scenario>)`](https://docs.taipy.io/en/latest/manuals/core/entities/scenario-cycle-mgt/#promote-a-scenario-as-primary) allows changing the primary scenario in a `Cycle`.

`<Scenario>.is_primary` identifies as a boolean whether the scenario is primary or not.

```
<span></span><code><span>before_set_1</span> <span>=</span> <span>scenario_1</span><span>.</span><span>is_primary</span>
<span>before_set_2</span> <span>=</span> <span>scenario_2</span><span>.</span><span>is_primary</span>

<span>tp</span><span>.</span><span>set_primary</span><span>(</span><span>scenario_2</span><span>)</span>

<span>print</span><span>(</span><span>'Scenario 1: Primary?'</span><span>,</span> <span>before_set_1</span><span>,</span> <span>scenario_1</span><span>.</span><span>is_primary</span><span>)</span>
<span>print</span><span>(</span><span>'Scenario 2: Primary?'</span><span>,</span> <span>before_set_2</span><span>,</span> <span>scenario_2</span><span>.</span><span>is_primary</span><span>)</span>
</code>
```

Results:

```
<span></span><code>Scenario 1: Primary? True False
Scenario 2: Primary? False True
</code>
```

### Useful functions on cycles[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/4_cycles_scopes/#useful-functions-on-cycles "Permanent link")

-   `tp.get_primary_scenarios()`: returns a list of all primary scenarios.
    
-   `tp.get_scenarios(cycle=<Cycle>)`: returns all the scenarios in the Cycle.
    
-   `tp.get_cycles()`: returns the list of Cycles.
    
-   `tp.get_primary(<Cycle>)`: returns the primary scenario of the Cycle.
    

#### Scenario management visual elements[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/4_cycles_scopes/#scenario-management-visual-elements "Permanent link")

You can use Scenario management visual elements to control Cycles. Cycles can be seen in either the `scenario_selector` or `data_node_selector`. Additionally, it's possible to designate a scenario as primary directly through the `scenario` visual element.

```
<span></span><code><span>data_node</span> <span>=</span> <span>None</span>
<span>scenario</span> <span>=</span> <span>None</span>

<span>tp</span><span>.</span><span>Gui</span><span>(</span><span>"""&lt;|</span><span>{scenario}</span><span>|scenario_selector|&gt;</span>
<span>          &lt;|</span><span>{scenario}</span><span>|scenario|&gt;</span>
<span>          &lt;|</span><span>{scenario}</span><span>|scenario_dag|&gt;</span>
<span>          &lt;|</span><span>{data_node}</span><span>|data_node_selector|&gt;"""</span><span>)</span><span>.</span><span>run</span><span>()</span>
</code>
```

![Visual Elements](https://docs.taipy.io/en/latest/tutorials/scenario_management/4_cycles_scopes/images/visual_elements.png)

## Conclusion[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/4_cycles_scopes/#conclusion "Permanent link")

By understanding the dynamics between scopes and cycles, developers can effectively manage data nodes and scenarios to suit specific business needs and scenarios. Experiment with different configurations to gain deeper insights into their functionalities and applications.

## Entire code[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/4_cycles_scopes/#entire-code "Permanent link")

```
<span></span><code tabindex="0"><span>from</span> <span>taipy.config</span> <span>import</span> <span>Config</span><span>,</span> <span>Frequency</span><span>,</span> <span>Scope</span>
<span>import</span> <span>taipy</span> <span>as</span> <span>tp</span>
<span>import</span> <span>datetime</span> <span>as</span> <span>dt</span>
<span>import</span> <span>pandas</span> <span>as</span> <span>pd</span>


<span>def</span> <span>filter_by_month</span><span>(</span><span>df</span><span>,</span> <span>month</span><span>):</span>
    <span>df</span><span>[</span><span>'Date'</span><span>]</span> <span>=</span> <span>pd</span><span>.</span><span>to_datetime</span><span>(</span><span>df</span><span>[</span><span>'Date'</span><span>])</span>
    <span>df</span> <span>=</span> <span>df</span><span>[</span><span>df</span><span>[</span><span>'Date'</span><span>]</span><span>.</span><span>dt</span><span>.</span><span>month</span> <span>==</span> <span>month</span><span>]</span>
    <span>return</span> <span>df</span>


<span>historical_data_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_csv_data_node</span><span>(</span><span>id</span><span>=</span><span>"historical_data"</span><span>,</span>
                                                     <span>default_path</span><span>=</span><span>"time_series.csv"</span><span>,</span>
                                                     <span>scope</span><span>=</span><span>Scope</span><span>.</span><span>GLOBAL</span><span>)</span>
<span>month_cfg</span> <span>=</span>  <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>id</span><span>=</span><span>"month"</span><span>,</span>
                                        <span>scope</span><span>=</span><span>Scope</span><span>.</span><span>CYCLE</span><span>)</span>
<span>month_values_cfg</span> <span>=</span>  <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>id</span><span>=</span><span>"month_data"</span><span>,</span>
                                               <span>scope</span><span>=</span><span>Scope</span><span>.</span><span>CYCLE</span><span>)</span>


<span>task_filter_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_task</span><span>(</span><span>id</span><span>=</span><span>"filter_by_month"</span><span>,</span>
                                        <span>function</span><span>=</span><span>filter_by_month</span><span>,</span>
                                        <span>input</span><span>=</span><span>[</span><span>historical_data_cfg</span><span>,</span> <span>month_cfg</span><span>],</span>
                                        <span>output</span><span>=</span><span>month_values_cfg</span><span>)</span>


<span>scenario_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_scenario</span><span>(</span><span>id</span><span>=</span><span>"my_scenario"</span><span>,</span>
                                         <span>task_configs</span><span>=</span><span>[</span><span>task_filter_cfg</span><span>],</span>
                                         <span>frequency</span><span>=</span><span>Frequency</span><span>.</span><span>MONTHLY</span><span>)</span>


<span>if</span> <span>__name__</span> <span>==</span> <span>'__main__'</span><span>:</span>
    <span>tp</span><span>.</span><span>Core</span><span>()</span><span>.</span><span>run</span><span>()</span>

    <span>scenario_1</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>scenario_cfg</span><span>,</span>
                                    <span>creation_date</span><span>=</span><span>dt</span><span>.</span><span>datetime</span><span>(</span><span>2022</span><span>,</span><span>10</span><span>,</span><span>7</span><span>),</span>
                                    <span>name</span><span>=</span><span>"Scenario 2022/10/7"</span><span>)</span>
    <span>scenario_2</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>scenario_cfg</span><span>,</span>
                                    <span>creation_date</span><span>=</span><span>dt</span><span>.</span><span>datetime</span><span>(</span><span>2022</span><span>,</span><span>10</span><span>,</span><span>5</span><span>),</span>
                                    <span>name</span><span>=</span><span>"Scenario 2022/10/5"</span><span>)</span>

    <span>scenario_1</span><span>.</span><span>month</span><span>.</span><span>write</span><span>(</span><span>10</span><span>)</span>

    <span>print</span><span>(</span><span>"Month Data Node of Scenario 1:"</span><span>,</span> <span>scenario_1</span><span>.</span><span>month</span><span>.</span><span>read</span><span>())</span>
    <span>print</span><span>(</span><span>"Month Data Node of Scenario 2:"</span><span>,</span> <span>scenario_2</span><span>.</span><span>month</span><span>.</span><span>read</span><span>())</span>

    <span>scenario_1</span><span>.</span><span>submit</span><span>()</span>

    <span>before_set_1</span> <span>=</span> <span>scenario_1</span><span>.</span><span>is_primary</span>
    <span>before_set_2</span> <span>=</span> <span>scenario_2</span><span>.</span><span>is_primary</span>

    <span>tp</span><span>.</span><span>set_primary</span><span>(</span><span>scenario_2</span><span>)</span>

    <span>print</span><span>(</span><span>'Scenario 1: Primary?'</span><span>,</span> <span>before_set_1</span><span>,</span> <span>scenario_1</span><span>.</span><span>is_primary</span><span>)</span>
    <span>print</span><span>(</span><span>'Scenario 2: Primary?'</span><span>,</span> <span>before_set_2</span><span>,</span> <span>scenario_2</span><span>.</span><span>is_primary</span><span>)</span>

    <span>scenario</span> <span>=</span> <span>None</span>
    <span>data_node</span> <span>=</span> <span>None</span>

    <span>tp</span><span>.</span><span>Gui</span><span>(</span><span>"""&lt;|</span><span>{scenario}</span><span>|scenario_selector|&gt;</span>
<span>              &lt;|</span><span>{scenario}</span><span>|scenario|&gt;</span>
<span>              &lt;|</span><span>{scenario}</span><span>|scenario_dag|&gt;</span>
<span>              &lt;|</span><span>{data_node}</span><span>|data_node_selector|&gt;"""</span><span>)</span><span>.</span><span>run</span><span>()</span>
</code>
```