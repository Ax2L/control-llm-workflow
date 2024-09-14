_Estimated Time for Completion: 15 minutes; Difficulty Level: Advanced_

![Configuration](https://docs.taipy.io/en/latest/tutorials/scenario_management/6_scenario_comparison/images/config.svg)

Taipy offers a way to compare data nodes across scenarios by including a function directly in the configuration of the scenario. This is particularly useful to visualize the differences between scenarios and make decision upon it.

[Download the code](https://docs.taipy.io/en/latest/tutorials/scenario_management/6_scenario_comparison/src/scenario_comparison.py)

## Comparing scenarios[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/6_scenario_comparison/#comparing-scenarios "Permanent link")

**Step 1:** Declare data nodes on which the comparison functions are applied.

In this example, we want to apply a comparison to the '_revenues_' Data Node. It is indicated in the comparators parameter of the `configure_scenario`.

```
<span></span><code><span># Scenario configuration</span>
<span>scenario_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_scenario</span><span>(</span>
    <span>id</span><span>=</span><span>"pricing_strategy"</span><span>,</span>
    <span>task_configs</span><span>=</span><span>[</span><span>predict_sales_task_cfg</span><span>,</span> <span>calculate_revenue_task_cfg</span><span>],</span>
    <span>comparators</span><span>=</span><span>{</span><span>revenue_output_cfg</span><span>.</span><span>id</span><span>:</span> <span>compare_revenue</span><span>}</span>
<span>)</span>
</code>
```

**Step 2:** Implement the comparison function (`compare_function()`) used above.

_revenues_ is the list of the Output (_revenues_) Data Nodes from all scenarios passed in the comparator. We iterate through it to compare scenarios.

```
<span></span><code><span>def</span> <span>compare_revenue</span><span>(</span><span>*</span><span>revenues</span><span>):</span>
    <span>scenario_names</span> <span>=</span> <span>[</span><span>f</span><span>"Scenario </span><span>{</span><span>i</span><span>}</span><span>"</span> <span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>len</span><span>(</span><span>revenues</span><span>))]</span>
    <span>comparisons</span> <span>=</span> <span>{</span><span>"Scenarios"</span><span>:</span> <span>scenario_names</span><span>,</span>
                   <span>"Revenues"</span><span>:</span> <span>list</span><span>(</span><span>revenues</span><span>)}</span>
    <span>return</span> <span>pd</span><span>.</span><span>DataFrame</span><span>(</span><span>comparisons</span><span>)</span>
</code>
```

Now, the `compare_scenarios` can be used within Taipy.

```
<span></span><code><span>core</span> <span>=</span> <span>tp</span><span>.</span><span>Core</span><span>()</span>
<span>core</span><span>.</span><span>run</span><span>()</span>

<span># Create scenarios with different pricing strategies</span>
<span>scenario_1</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>scenario_cfg</span><span>)</span>
<span>scenario_2</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>scenario_cfg</span><span>)</span>

<span>scenario_1</span><span>.</span><span>price_input</span><span>.</span><span>write</span><span>(</span><span>120</span><span>)</span>  <span># Higher price scenario</span>
<span>scenario_2</span><span>.</span><span>price_input</span><span>.</span><span>write</span><span>(</span><span>80</span><span>)</span>   <span># Lower price scenario</span>

<span>scenario_1</span><span>.</span><span>submit</span><span>()</span>
<span>scenario_2</span><span>.</span><span>submit</span><span>()</span>

<span># Compare the scenarios</span>
<span>comparisons</span> <span>=</span> <span>tp</span><span>.</span><span>compare_scenarios</span><span>(</span><span>scenario_1</span><span>,</span> <span>scenario_2</span><span>)</span>
<span>print</span><span>(</span><span>comparisons</span><span>)</span>
</code>
```

Results:

```
<span></span><code>...
{'revenue_output': {'compare_revenue':     Scenarios  Revenues
0  Scenario 0    9120.0
1  Scenario 1   11200.0}}
</code>
```

## Compare Scenario with a GUI[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/6_scenario_comparison/#compare-scenario-with-a-gui "Permanent link")

Taipy can then generate a GUI that compares scenarios easily. Our comparison will be shown through a chart and a table in this case. This application can be as interactive and complete as possible.

```
<span></span><code><span>from</span> <span>taipy.gui</span> <span>import</span> <span>Gui</span> 
<span>import</span> <span>taipy.gui.builder</span> <span>as</span> <span>tgb</span> 

<span>with</span> <span>tgb</span><span>.</span><span>Page</span><span>()</span> <span>as</span> <span>compare_page</span><span>:</span>
    <span>tgb</span><span>.</span><span>text</span><span>(</span><span>"# Compare Scenarios"</span><span>,</span> <span>mode</span><span>=</span><span>"md)</span>

    <span>tgb</span><span>.</span><span>chart</span><span>(</span><span>"</span><span>{comparisons_revenue}</span><span>"</span><span>,</span> <span>type</span><span>=</span><span>"bar"</span><span>,</span> <span>x</span><span>=</span><span>"Scenarios"</span><span>,</span> <span>y</span><span>=</span><span>"Revenues"</span><span>)</span>
    <span>tgb</span><span>.</span><span>table</span><span>(</span><span>"</span><span>{comparisons_revenue}</span><span>"</span><span>)</span>

<span>Gui</span><span>(</span><span>compare_page</span><span>)</span><span>.</span><span>run</span><span>()</span>
</code>
```

![Comparison GUI](https://docs.taipy.io/en/latest/tutorials/scenario_management/6_scenario_comparison/images/comparison.png)

## Entire code[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/6_scenario_comparison/#entire-code "Permanent link")

Here is the entire code to recreate the example. A GUI has been created to show the results.

```
<span></span><code tabindex="0"><span>from</span> <span>taipy</span> <span>import</span> <span>Core</span><span>,</span> <span>Config</span>
<span>import</span> <span>taipy</span> <span>as</span> <span>tp</span>
<span>import</span> <span>pandas</span> <span>as</span> <span>pd</span>
<span>import</span> <span>numpy</span> <span>as</span> <span>np</span>

<span># Simulation function to predict sales based on pricing</span>
<span>def</span> <span>predict_sales</span><span>(</span><span>price</span><span>):</span>
<span>    </span><span>"""</span>
<span>    Simulate sales volume based on price.</span>
<span>    Elasticity affects how demand reacts to price changes.</span>
<span>    """</span>
    <span>base_demand</span> <span>=</span> <span>100</span>
    <span>elasticity</span> <span>=</span> <span>-</span><span>1.5</span>

    <span>demand</span> <span>=</span> <span>base_demand</span> <span>*</span> <span>(</span><span>price</span> <span>/</span> <span>100</span><span>)</span> <span>**</span> <span>elasticity</span>
    <span>return</span> <span>max</span><span>(</span><span>0</span><span>,</span> <span>np</span><span>.</span><span>round</span><span>(</span><span>demand</span><span>))</span>  <span># Ensure non-negative sales volume</span>

<span># Function to calculate revenue from sales volume and price</span>
<span>def</span> <span>calculate_revenue</span><span>(</span><span>price</span><span>,</span> <span>sales_volume</span><span>):</span>
    <span>return</span> <span>price</span> <span>*</span> <span>sales_volume</span>

<span># Data Node configuration</span>
<span>price_input_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>"price_input"</span><span>,</span> <span>default_data</span><span>=</span><span>100</span><span>)</span>
<span>sales_output_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>"sales_output"</span><span>)</span>
<span>revenue_output_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>"revenue_output"</span><span>)</span>

<span># Task configurations</span>
<span>predict_sales_task_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_task</span><span>(</span>
    <span>id</span><span>=</span><span>"predict_sales"</span><span>,</span>
    <span>function</span><span>=</span><span>predict_sales</span><span>,</span>
    <span>input</span><span>=</span><span>price_input_cfg</span><span>,</span>
    <span>output</span><span>=</span><span>sales_output_cfg</span>
<span>)</span>

<span>calculate_revenue_task_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_task</span><span>(</span>
    <span>id</span><span>=</span><span>"calculate_revenue"</span><span>,</span>
    <span>function</span><span>=</span><span>calculate_revenue</span><span>,</span>
    <span>input</span><span>=</span><span>[</span><span>price_input_cfg</span><span>,</span> <span>sales_output_cfg</span><span>],</span>
    <span>output</span><span>=</span><span>revenue_output_cfg</span>
<span>)</span>

<span># Comparator function to compare revenue outputs</span>
<span>def</span> <span>compare_revenue</span><span>(</span><span>*</span><span>revenues</span><span>):</span>
    <span>scenario_names</span> <span>=</span> <span>[</span><span>f</span><span>"Scenario </span><span>{</span><span>i</span><span>}</span><span>"</span> <span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>len</span><span>(</span><span>revenues</span><span>))]</span>
    <span>comparisons</span> <span>=</span> <span>{</span><span>"Scenarios"</span><span>:</span> <span>scenario_names</span><span>,</span>
                   <span>"Revenues"</span><span>:</span> <span>list</span><span>(</span><span>revenues</span><span>)}</span>
    <span>return</span> <span>pd</span><span>.</span><span>DataFrame</span><span>(</span><span>comparisons</span><span>)</span>

<span># Scenario configuration</span>
<span>scenario_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_scenario</span><span>(</span>
    <span>id</span><span>=</span><span>"pricing_strategy"</span><span>,</span>
    <span>task_configs</span><span>=</span><span>[</span><span>predict_sales_task_cfg</span><span>,</span> <span>calculate_revenue_task_cfg</span><span>],</span>
    <span>comparators</span><span>=</span><span>{</span><span>revenue_output_cfg</span><span>.</span><span>id</span><span>:</span> <span>compare_revenue</span><span>}</span>
<span>)</span>

<span>Config</span><span>.</span><span>export</span><span>(</span><span>"config_pricing.toml"</span><span>)</span>

<span>if</span> <span>__name__</span><span>==</span><span>"__main__"</span><span>:</span>
    <span>core</span> <span>=</span> <span>Core</span><span>()</span>
    <span>core</span><span>.</span><span>run</span><span>()</span>

    <span># Create scenarios with different pricing strategies</span>
    <span>scenario_1</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>scenario_cfg</span><span>)</span>
    <span>scenario_2</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>scenario_cfg</span><span>)</span>

    <span>scenario_1</span><span>.</span><span>price_input</span><span>.</span><span>write</span><span>(</span><span>120</span><span>)</span>  <span># Higher price scenario</span>
    <span>scenario_2</span><span>.</span><span>price_input</span><span>.</span><span>write</span><span>(</span><span>80</span><span>)</span>   <span># Lower price scenario</span>

    <span>scenario_1</span><span>.</span><span>submit</span><span>()</span>
    <span>scenario_2</span><span>.</span><span>submit</span><span>()</span>

    <span># Compare the scenarios</span>
    <span>comparisons</span> <span>=</span> <span>tp</span><span>.</span><span>compare_scenarios</span><span>(</span><span>scenario_1</span><span>,</span> <span>scenario_2</span><span>)</span>
    <span>print</span><span>(</span><span>comparisons</span><span>)</span>

    <span>comparisons_revenue</span> <span>=</span> <span>comparisons</span><span>[</span><span>"revenue_output"</span><span>][</span><span>'compare_revenue'</span><span>]</span>

    <span># Creation of an GUI</span>
    <span>from</span> <span>taipy.gui</span> <span>import</span> <span>Gui</span> 
    <span>import</span> <span>taipy.gui.builder</span> <span>as</span> <span>tgb</span> 

    <span>with</span> <span>tgb</span><span>.</span><span>Page</span><span>()</span> <span>as</span> <span>compare_page</span><span>:</span>
        <span>tgb</span><span>.</span><span>text</span><span>(</span><span>"# Compare Scenarios"</span><span>,</span> <span>mode</span><span>=</span><span>"md)</span>

        <span>tgb</span><span>.</span><span>chart</span><span>(</span><span>"</span><span>{comparisons_revenue}</span><span>"</span><span>,</span> <span>type</span><span>=</span><span>"bar"</span><span>,</span> <span>x</span><span>=</span><span>"Scenarios"</span><span>,</span> <span>y</span><span>=</span><span>"Revenues"</span><span>)</span>
        <span>tgb</span><span>.</span><span>table</span><span>(</span><span>"</span><span>{comparisons_revenue}</span><span>"</span><span>)</span>

    <span>Gui</span><span>(</span><span>compare_page</span><span>)</span><span>.</span><span>run</span><span>()</span>
</code>
```