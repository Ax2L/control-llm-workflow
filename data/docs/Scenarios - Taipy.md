In the fast-moving world of business today, people who make decisions need to adapt fast to changes and look at different possibilities to make smart choices. Taipy scenarios are a strong tool for running and saving sets of tasks. They can create different versions of a business problem with different guesses. This helps users understand the effects and possibilities, which are really important for big decisions.

![Scenarios](https://docs.taipy.io/en/latest/tutorials/scenario_management/1_scenarios/images/scenario.png)

In this tip, we will examine Taipy scenarios more closely. We will explore what they can do and how they can be useful when making decisions.

As a reminder, Taipy [scenarios](https://docs.taipy.io/en/latest/manuals/core/concepts/scenario/) are one of the fundamental concept in Taipy.

## Taipy Scenarios: An Overview[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/1_scenarios/#taipy-scenarios-an-overview "Permanent link")

A Taipy scenario is like a test run of a business problem using specific data and settings.

You can make, save, change, and run different scenarios in one application. This makes it easy to study various versions of a business problem. It's really useful for businesses that need to consider many scenarios with different ideas to make the best choice.

## Example: Monthly Production Planning[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/1_scenarios/#example-monthly-production-planning "Permanent link")

Imagine a manufacturing company that has to figure out how much to produce each month based on expected sales. The person using the system starts by setting up a plan for January. They put in all the data they need and the rules for calculating sales predictions, deciding how much to make, and generating production orders for January.

Next, for February, they make a new plan using updated information for that month. They can keep doing this every month, which helps the company adjust its production plans as things change and new information comes in.

```
<span></span><code><span>import</span> <span>taipy</span> <span>as</span> <span>tp</span>
<span>from</span> <span>datetime</span> <span>import</span> <span>datetime</span>
<span>import</span> <span>my_config</span>

<span># Creating a scenario for January</span>
<span>january_scenario</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>my_config</span><span>.</span><span>monthly_scenario_cfg</span><span>,</span>
                                      <span>creation_date</span><span>=</span><span>datetime</span><span>(</span><span>2023</span><span>,</span> <span>1</span><span>,</span> <span>1</span><span>),</span>
                                      <span>name</span><span>=</span><span>"Scenario for January"</span><span>)</span>

<span># Creating a scenario for February</span>
<span>february_scenario</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>my_config</span><span>.</span><span>monthly_scenario_cfg</span><span>,</span>
                                       <span>creation_date</span><span>=</span><span>datetime</span><span>(</span><span>2023</span><span>,</span> <span>2</span><span>,</span> <span>1</span><span>),</span>
                                       <span>name</span><span>=</span><span>"Scenario for February"</span><span>)</span>
</code>
```

## Scenarios[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/1_scenarios/#scenarios "Permanent link")

Taipy scenarios include tasks and data nodes modeling any kind of data workflow. These tasks can be submitted as a whole submitting the scenario or independently if needed. When it is possible, Taipy runs the tasks in parallel.

### Scenario Configuration and Creation[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/1_scenarios/#scenario-configuration-and-creation "Permanent link")

To instantiate a Taipy scenario, users first need to configure it with the `Config.configure_scenario()` method. They need to set certain things like a name, the tasks it uses, how often it runs, what it compares, and its properties. Then users can create a scenario with the `create_scenario()` function passing as a parameter the scenario configuration.

```
<span></span><code><span>from</span> <span>taipy</span> <span>import</span> <span>Config</span>

<span># Configuration of Data Nodes, Tasks, ...</span>
<span>...</span>

<span># Creating a scenario configuration from task configurations</span>
<span>scenario_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_scenario</span><span>(</span><span>"multiply_scenario"</span><span>,</span>
                                         <span>task_configs</span><span>=</span><span>[</span><span>task_cfg</span><span>])</span>
</code>
```

### Accessing and Managing Scenarios[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/1_scenarios/#accessing-and-managing-scenarios "Permanent link")

Taipy offers different ways to work with scenarios. You can do things like getting a scenario by its ID, getting all scenarios, making one scenario the main one, and comparing scenarios.

You can also add tags to scenarios to keep them organized. If you want to transfer your scenario from one environment to the other, it is possible to export them with the last command.

```
<span></span><code tabindex="0"><span>...</span>

<span># Run of the Core service</span>
<span>tp</span><span>.</span><span>Core</span><span>()</span><span>.</span><span>run</span><span>()</span>

<span># Get a scenario by id</span>
<span>scenario_retrieved</span> <span>=</span> <span>tp</span><span>.</span><span>get</span><span>(</span><span>scenario</span><span>.</span><span>id</span><span>)</span>

<span># Get all scenarios</span>
<span>all_scenarios</span> <span>=</span> <span>tp</span><span>.</span><span>get_scenarios</span><span>()</span>

<span># Get primary scenarios</span>
<span>all_primary_scenarios</span> <span>=</span> <span>tp</span><span>.</span><span>get_primary_scenarios</span><span>()</span>

<span># Promote a scenario as primary</span>
<span>tp</span><span>.</span><span>set_primary</span><span>(</span><span>scenario</span><span>)</span>

<span># Compare scenarios (use the compare function defined in the configuration)</span>
<span>comparison_results</span> <span>=</span> <span>tp</span><span>.</span><span>compare_scenarios</span><span>(</span><span>january_scenario</span><span>,</span> <span>february_scenario</span><span>,</span> <span>data_node_config_id</span><span>=</span><span>"sales_predictions"</span><span>)</span>

<span># Tag a scenario</span>
<span>tp</span><span>.</span><span>tag</span><span>(</span><span>scenario</span><span>,</span> <span>"my_tag"</span><span>)</span>

<span># Export a scenario</span>
<span>tp</span><span>.</span><span>export</span><span>(</span><span>scenario</span><span>.</span><span>id</span><span>,</span> <span>folder_path</span><span>=</span><span>"./monthly_scenario"</span><span>)</span>
</code>
```

The primary benefit of having a scenario is to access the Data Nodes of the different scenarios that are made. Accessing a data node is as as simple as `<scenario>.<Data Node name>.read()`. By exploring the data nodes, end users can analyse the results of their data workflow and make decisions upon it.

### Scenario management visual elements[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/1_scenarios/#scenario-management-visual-elements "Permanent link")

The [Scenario management visual elements](https://docs.taipy.io/en/latest/manuals/gui/viselements/controls/) allow you to include visual elements in the Taipy backend. This makes it easier than ever to build a web application that matches your backend.

You can add these few lines of code to your script's configuration to create a web application that lets you:

-   Choose from the scenarios you've made.
-   Create new scenarios.
-   Submit them.
-   View the configuration used by the scenario.

```
<span></span><code><span>from</span> <span>taipy</span> <span>import</span> <span>Gui</span>
<span>import</span> <span>taipy</span> <span>as</span> <span>tp</span>

<span>...</span>

<span>scenario</span> <span>=</span> <span>None</span>

<span>scenario_md</span> <span>=</span> <span>"""</span>
<span>&lt;|</span><span>{scenario}</span><span>|scenario_selector|&gt;</span>
<span>&lt;|</span><span>{scenario}</span><span>|scenario|&gt;</span>
<span>&lt;|</span><span>{scenario}</span><span>|scenario_dag|&gt;</span>
<span>"""</span>

<span>tp</span><span>.</span><span>Core</span><span>()</span><span>.</span><span>run</span><span>()</span>
<span>Gui</span><span>(</span><span>scenario_md</span><span>)</span><span>.</span><span>run</span><span>()</span>
</code>
```

## Conclusion[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/1_scenarios/#conclusion "Permanent link")

Taipy scenarios are a strong and adaptable tool that businesses can use to investigate different situations with different assumptions. This helps in making smart decisions and analyzing their effects.

By using Taipy scenarios, companies can gain a deeper understanding of what might happen as a result of their choices. This knowledge allows them to make informed decisions that can lead to success in their business.