_Estimated Time for Completion: 15 minutes; Difficulty Level: Beginner_

Taipy brings a suite of features to streamline data pipeline orchestration:

-   It registers each pipeline execution, enabling users to monitor KPIs over time and benchmark different runs, providing _what-if_ scenarios.
-   Taipy includes ready-to-use UI components for pipeline interaction—allowing for the selection of inputs and parameters, execution and tracking of pipelines, and visualization of results.
-   Taipy efficiently manages computations, avoiding unnecessary reruns of unchanged data.
-   Taipy easily integrates with most popular data sources.
-   It supports concurrent computing, enhancing processing speed and scalability.

[Download the code](https://docs.taipy.io/en/latest/tutorials/fundamentals/2_scenario_management_overview/src/scenario_management.zip)

By the end of this tutorial, you'll have a solid foundation to develop a simple application leveraging Taipy's scenario management capabilities.

![Scenario management demo](https://docs.taipy.io/en/latest/tutorials/fundamentals/2_scenario_management_overview/images/demo.gif)

Before looking at some code examples, to apprehend what is a _Scenario_, you need to understand the _Data node_ and _Task_ concepts.

-   [**Data Nodes**](https://docs.taipy.io/en/latest/manuals/core/concepts/data-node/): represents a variable in Taipy. Data Nodes don't contain the data itself but point to the data and know how to retrieve it. These Data Nodes can point to different types of data sources like CSV files, Pickle files, databases, etc., and they can represent various types of Python variables such as integers, strings, data frames, lists, and more. They are fully generic and can be used to represent datasets, parameters, KPIs, intermediate data, or any variable.
    
-   [**Tasks**](https://docs.taipy.io/en/latest/manuals/core/concepts/task/): are the translation of functions in Taipy where their inputs and outputs are data nodes.
    
-   [**Scenarios**](https://docs.taipy.io/en/latest/manuals/core/concepts/scenario/): Scenarios are created by combining Data Nodes and Tasks to form a graph that maps the execution flow. Each scenario can be submitted, resulting in the execution of its tasks. End-Users very often require modifying various parameters to reflect different business situations. Taipy provide the framework to execute various scenarios under different situations (i.e. various data/parameters values set by end-users).
    

[**Configuration**](https://docs.taipy.io/en/latest/manuals/core/config/) is a structure to define scenarios. It serves as the blueprint for our Directed Acyclic Graph(s) and models the data sources, parameters, and tasks. After being defined, a configuration functions like a superclass and is employed to generate various instances of scenarios.

## Configuring a Scenario[¶](https://docs.taipy.io/en/latest/tutorials/fundamentals/2_scenario_management_overview/#configuring-a-scenario "Permanent link")

First, we'll import the necessary libraries and load a dataset:

```
<span></span><code tabindex="0"><span>from</span> <span>taipy</span> <span>import</span> <span>Config</span>
<span>import</span> <span>taipy</span> <span>as</span> <span>tp</span>
<span>import</span> <span>pandas</span> <span>as</span> <span>pd</span>
<span>import</span> <span>datetime</span> <span>as</span> <span>dt</span>


<span>data</span> <span>=</span> <span>pd</span><span>.</span><span>read_csv</span><span>(</span><span>"https://raw.githubusercontent.com/Avaiga/taipy-getting-started-core/develop/src/daily-min-temperatures.csv"</span><span>)</span>
</code>
```

Think about the most basic pipeline: one function that needs two things to work – some data and a date. It uses these to generate a prediction for that date.

See the code for this function below:

```
<span></span><code tabindex="0"><span>def</span> <span>predict</span><span>(</span><span>historical_temperature</span><span>:</span> <span>pd</span><span>.</span><span>DataFrame</span><span>,</span> <span>date_to_forecast</span><span>:</span> <span>dt</span><span>.</span><span>datetime</span><span>)</span> <span>-&gt;</span> <span>float</span><span>:</span>
    <span>print</span><span>(</span><span>f</span><span>"Running baseline..."</span><span>)</span>
    <span>historical_temperature</span><span>[</span><span>'Date'</span><span>]</span> <span>=</span> <span>pd</span><span>.</span><span>to_datetime</span><span>(</span><span>historical_temperature</span><span>[</span><span>'Date'</span><span>])</span>
    <span>historical_same_day</span> <span>=</span> <span>historical_temperature</span><span>.</span><span>loc</span><span>[</span>
        <span>(</span><span>historical_temperature</span><span>[</span><span>'Date'</span><span>]</span><span>.</span><span>dt</span><span>.</span><span>day</span> <span>==</span> <span>date_to_forecast</span><span>.</span><span>day</span><span>)</span> <span>&amp;</span>
        <span>(</span><span>historical_temperature</span><span>[</span><span>'Date'</span><span>]</span><span>.</span><span>dt</span><span>.</span><span>month</span> <span>==</span> <span>date_to_forecast</span><span>.</span><span>month</span><span>)</span>
    <span>]</span>
    <span>return</span> <span>historical_same_day</span><span>[</span><span>'Temp'</span><span>]</span><span>.</span><span>mean</span><span>()</span>
</code>
```

The scenario can be represented as the following graph:

![Simple scenario](https://docs.taipy.io/en/latest/tutorials/fundamentals/2_scenario_management_overview/images/config.svg)

Three Data Nodes are being configured (**historical\_temperature**, **date\_to\_forecast** and **predictions**). The task **predict** links the three Data Nodes through the Python function.

Configuration

**Alternative 1:** Configuration using Python Code

Here is the code to configure a simple scenario.

```
<span></span><code tabindex="0"><span># Configuration of Data Nodes</span>
<span>historical_temperature_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>"historical_temperature"</span><span>)</span>
<span>date_to_forecast_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>"date_to_forecast"</span><span>)</span>
<span>predictions_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>"predictions"</span><span>)</span>

<span># Configuration of tasks</span>
<span>task_predict_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_task</span><span>(</span><span>id</span><span>=</span><span>"predict"</span><span>,</span>
                                    <span>function</span><span>=</span><span>predict</span><span>,</span>
                                    <span>input</span><span>=</span><span>[</span><span>historical_temperature_cfg</span><span>,</span> <span>date_to_forecast_cfg</span><span>],</span>
                                    <span>output</span><span>=</span><span>predictions_cfg</span><span>)</span>

<span># Configuration of scenario</span>
<span>scenario_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_scenario</span><span>(</span><span>id</span><span>=</span><span>"my_scenario"</span><span>,</span>
                                         <span>task_configs</span><span>=</span><span>[</span><span>task_predict_cfg</span><span>])</span>
</code>
```

The configuration is done! Let's use it to instantiate scenarios and submit them.

## Instantiate Scenario[¶](https://docs.taipy.io/en/latest/tutorials/fundamentals/2_scenario_management_overview/#instantiate-scenario "Permanent link")

First, run the Core service in your code (`tp.Core().run()`). Then, you can play with Taipy:

-   create scenarios ([`tp.create_scenario(<ScenarioConfig>)`](https://docs.taipy.io/en/latest/tutorials/scenario_management/1_scenarios/#scenario-configuration-and-creation)),
    
-   write your input data nodes ([`<Data Node>.write(<new value>)`](https://docs.taipy.io/en/latest/manuals/core/entities/data-node-mgt/#read-write-a-data-node)),
    
-   submit them to run the task ([`<Scenario>.submit()`](https://docs.taipy.io/en/latest/tutorials/scenario_management/1_scenarios/#scenario-configuration-and-creation)),
    
-   read your output data node ([`<Data Node>.read()`](https://docs.taipy.io/en/latest/manuals/core/entities/data-node-mgt/#read-write-a-data-node)).
    

Creating a scenario creates all its related entities (**tasks**, **Data Nodes**, etc). These entities are being created thanks to the previous configuration. Still, no scenario has been run yet. `tp.submit(<Scenario>)` is the line of code that triggers the run of all the scenario-related tasks.

```
<span></span><code><span># Run of the Core</span>
<span>tp</span><span>.</span><span>Core</span><span>()</span><span>.</span><span>run</span><span>()</span>

<span># Creation of the scenario and execution</span>
<span>scenario</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>scenario_cfg</span><span>)</span>
<span>scenario</span><span>.</span><span>historical_temperature</span><span>.</span><span>write</span><span>(</span><span>data</span><span>)</span>
<span>scenario</span><span>.</span><span>date_to_forecast</span><span>.</span><span>write</span><span>(</span><span>dt</span><span>.</span><span>datetime</span><span>.</span><span>now</span><span>())</span>
<span>tp</span><span>.</span><span>submit</span><span>(</span><span>scenario</span><span>)</span>

<span>print</span><span>(</span><span>"Value at the end of task"</span><span>,</span> <span>scenario</span><span>.</span><span>predictions</span><span>.</span><span>read</span><span>())</span>
</code>
```

Results:

```
<span></span><code>[2022-12-22 16:20:02,740][Taipy][INFO] job JOB_predict_... is completed.
Value at the end of task 23.45
</code>
```

In this code, you can see how to create and submit scenarios, retrieve data nodes, read and write data.

Some useful functions

As a quick note, here are some other basic functions to use for data and scenario managament.

-   [`tp.get_scenarios()`](https://docs.taipy.io/en/latest/manuals/core/entities/scenario-cycle-mgt/#get-all-scenarios): this function returns the list of all the scenarios.

For instance, the following Python code retrieves all the scenarios, extracts their names, and pairs them with their respective predictions. The names and predictions are then compiled into a list:

```
<span></span><code><span>print</span><span>([(</span><span>s</span><span>.</span><span>name</span><span>,</span> <span>s</span><span>.</span><span>predictions</span><span>.</span><span>read</span><span>())</span> <span>for</span> <span>s</span> <span>in</span> <span>tp</span><span>.</span><span>get_scenarios</span><span>()])</span>
</code>
```

-   [`tp.get(<Taipy object ID>)`](https://docs.taipy.io/en/latest/manuals/core/entities/data-node-mgt/#get-data-node): this function returns an entity based on the id of the entity.
    
-   [`tp.delete(<Taipy object ID>)`](https://docs.taipy.io/en/latest/manuals/core/entities/scenario-cycle-mgt/#delete-a-scenario): this function deletes the entity and nested elements based on the id of the entity.
    

You can also have a look to this [tutorial](https://docs.taipy.io/en/latest/tutorials/scenario_management/6_scenario_comparison/) to learn how scenarios can be compared easily. Many other functions are described in the manuals, in particular in the [scenario](https://docs.taipy.io/en/latest/manuals/core/entities/scenario-cycle-mgt/) and [data node](https://docs.taipy.io/en/latest/manuals/core/entities/data-node-mgt/) documentation pages.

## Visual elements[¶](https://docs.taipy.io/en/latest/tutorials/fundamentals/2_scenario_management_overview/#visual-elements "Permanent link")

The small piece of code of the previous section shows how to manage scenarios. The scenario or data node management is usually done by end-users through a graphical interface. Taipy provides visual elements dedicated to Scenario management to replace the code above.

Add these few lines to the code of your script. This creates a web application, so end-users can:

-   select scenarios,
    
-   create new ones,
    
-   submit them,
    
-   access their properties.
    

```
<span></span><code><span>def</span> <span>save</span><span>(</span><span>state</span><span>):</span>
    <span># write values of Data Node to submit scenario</span>
    <span>state</span><span>.</span><span>scenario</span><span>.</span><span>historical_temperature</span><span>.</span><span>write</span><span>(</span><span>data</span><span>)</span>
    <span>state</span><span>.</span><span>scenario</span><span>.</span><span>date_to_forecast</span><span>.</span><span>write</span><span>(</span><span>state</span><span>.</span><span>date</span><span>)</span>
    <span>state</span><span>.</span><span>refresh</span><span>(</span><span>'scenario'</span><span>)</span>
    <span>tp</span><span>.</span><span>gui</span><span>.</span><span>notify</span><span>(</span><span>state</span><span>,</span> <span>"s"</span><span>,</span> <span>"Saved! Ready to submit"</span><span>)</span>

<span>date</span> <span>=</span> <span>None</span>
<span>scenario_md</span> <span>=</span> <span>"""</span>
<span>&lt;|</span><span>{scenario}</span><span>|scenario_selector|&gt;</span>

<span>Select a Date</span>
<span>&lt;|</span><span>{date}</span><span>|date|on_change=save|active=</span><span>{scenario}</span><span>|&gt;</span>

<span>Run the scenario</span>
<span>&lt;|</span><span>{scenario}</span><span>|scenario|&gt;</span>
<span>&lt;|</span><span>{scenario}</span><span>|scenario_dag|&gt;</span>

<span>View all the information on your prediction here</span>
<span>&lt;|</span><span>{scenario.predictions}</span><span>|data_node|&gt;</span>
<span>"""</span>

<span>tp</span><span>.</span><span>Gui</span><span>(</span><span>scenario_md</span><span>)</span><span>.</span><span>run</span><span>()</span>
</code>
```

The [Scenario management controls](https://docs.taipy.io/en/latest/manuals/gui/viselements/controls/#scenario-management-controls) provide all the necessary features to access and manage scenarios and data nodes. In fact, creating a Scenario based application connected to your pipelines has never been simpler.

![Scenario management demo](https://docs.taipy.io/en/latest/tutorials/fundamentals/2_scenario_management_overview/images/demo.gif)

## Entire code[¶](https://docs.taipy.io/en/latest/tutorials/fundamentals/2_scenario_management_overview/#entire-code "Permanent link")

```
<span></span><code tabindex="0"><span>from</span> <span>taipy</span> <span>import</span> <span>Config</span>
<span>import</span> <span>taipy</span> <span>as</span> <span>tp</span>
<span>import</span> <span>pandas</span> <span>as</span> <span>pd</span>
<span>import</span> <span>datetime</span> <span>as</span> <span>dt</span>


<span>data</span> <span>=</span> <span>pd</span><span>.</span><span>read_csv</span><span>(</span><span>"https://raw.githubusercontent.com/Avaiga/taipy-getting-started-core/develop/src/daily-min-temperatures.csv"</span><span>)</span>


<span># Normal function used by Taipy</span>
<span>def</span> <span>predict</span><span>(</span><span>historical_temperature</span><span>:</span> <span>pd</span><span>.</span><span>DataFrame</span><span>,</span> <span>date_to_forecast</span><span>:</span> <span>dt</span><span>.</span><span>datetime</span><span>)</span> <span>-&gt;</span> <span>float</span><span>:</span>
    <span>print</span><span>(</span><span>f</span><span>"Running baseline..."</span><span>)</span>
    <span>historical_temperature</span><span>[</span><span>'Date'</span><span>]</span> <span>=</span> <span>pd</span><span>.</span><span>to_datetime</span><span>(</span><span>historical_temperature</span><span>[</span><span>'Date'</span><span>])</span>
    <span>historical_same_day</span> <span>=</span> <span>historical_temperature</span><span>.</span><span>loc</span><span>[</span>
        <span>(</span><span>historical_temperature</span><span>[</span><span>'Date'</span><span>]</span><span>.</span><span>dt</span><span>.</span><span>day</span> <span>==</span> <span>date_to_forecast</span><span>.</span><span>day</span><span>)</span> <span>&amp;</span>
        <span>(</span><span>historical_temperature</span><span>[</span><span>'Date'</span><span>]</span><span>.</span><span>dt</span><span>.</span><span>month</span> <span>==</span> <span>date_to_forecast</span><span>.</span><span>month</span><span>)</span>
    <span>]</span>
    <span>return</span> <span>historical_same_day</span><span>[</span><span>'Temp'</span><span>]</span><span>.</span><span>mean</span><span>()</span>

<span># Configuration of Data Nodes</span>
<span>historical_temperature_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>"historical_temperature"</span><span>)</span>
<span>date_to_forecast_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>"date_to_forecast"</span><span>)</span>
<span>predictions_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>"predictions"</span><span>)</span>

<span># Configuration of tasks</span>
<span>predictions_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_task</span><span>(</span><span>"predict"</span><span>,</span>
                                        <span>predict</span><span>,</span>
                                        <span>[</span><span>historical_temperature_cfg</span><span>,</span> <span>date_to_forecast_cfg</span><span>],</span>
                                        <span>predictions_cfg</span><span>)</span>

<span># Configuration of scenario</span>
<span>scenario_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_scenario</span><span>(</span><span>id</span><span>=</span><span>"my_scenario"</span><span>,</span> <span>task_configs</span><span>=</span><span>[</span><span>predictions_cfg</span><span>])</span>

<span>Config</span><span>.</span><span>export</span><span>(</span><span>'config.toml'</span><span>)</span>

<span>if</span> <span>__name__</span> <span>==</span> <span>'__main__'</span><span>:</span>
    <span># Run of the Core</span>
    <span>tp</span><span>.</span><span>Core</span><span>()</span><span>.</span><span>run</span><span>()</span>

    <span># Creation of the scenario and execution</span>
    <span>scenario</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>scenario_cfg</span><span>)</span>
    <span>scenario</span><span>.</span><span>historical_temperature</span><span>.</span><span>write</span><span>(</span><span>data</span><span>)</span>
    <span>scenario</span><span>.</span><span>date_to_forecast</span><span>.</span><span>write</span><span>(</span><span>dt</span><span>.</span><span>datetime</span><span>.</span><span>now</span><span>())</span>
    <span>tp</span><span>.</span><span>submit</span><span>(</span><span>scenario</span><span>)</span>

    <span>print</span><span>(</span><span>"Value at the end of task"</span><span>,</span> <span>scenario</span><span>.</span><span>predictions</span><span>.</span><span>read</span><span>())</span>

    <span>def</span> <span>save</span><span>(</span><span>state</span><span>):</span>
        <span>state</span><span>.</span><span>scenario</span><span>.</span><span>historical_temperature</span><span>.</span><span>write</span><span>(</span><span>data</span><span>)</span>
        <span>state</span><span>.</span><span>scenario</span><span>.</span><span>date_to_forecast</span><span>.</span><span>write</span><span>(</span><span>state</span><span>.</span><span>date</span><span>)</span>
        <span>state</span><span>.</span><span>refresh</span><span>(</span><span>'scenario'</span><span>)</span>
        <span>tp</span><span>.</span><span>gui</span><span>.</span><span>notify</span><span>(</span><span>state</span><span>,</span> <span>"s"</span><span>,</span> <span>"Saved! Ready to submit"</span><span>)</span>

    <span>date</span> <span>=</span> <span>None</span>
    <span>scenario_md</span> <span>=</span> <span>"""</span>
<span>&lt;|</span><span>{scenario}</span><span>|scenario_selector|&gt;</span>

<span>Select a Date</span>
<span>&lt;|</span><span>{date}</span><span>|date|on_change=save|active=</span><span>{scenario}</span><span>|&gt;</span>

<span>Run the scenario</span>
<span>&lt;|</span><span>{scenario}</span><span>|scenario|&gt;</span>
<span>&lt;|</span><span>{scenario}</span><span>|scenario_dag|&gt;</span>

<span>View all the information on your prediction here</span>
<span>&lt;|</span><span>{scenario.predictions}</span><span>|data_node|&gt;</span>
<span>"""</span>

    <span>tp</span><span>.</span><span>Gui</span><span>(</span><span>scenario_md</span><span>)</span><span>.</span><span>run</span><span>()</span>
</code>
```