Taipy is a Python tool for making web applications that use data. It can do many things, but we're going to talk about two important things in Taipy: Data nodes and Tasks.

Data nodes are like a bridge to get data from different places. They help us access data easily. This tip is mostly about data nodes, what they do, and how we use them in Taipy scenarios.

Data nodes in Taipy are like tools to work with data. They don't hold data themselves, but they know how to get it from different places. Think of a data node as something that can read and write data, and it's really good at doing that.

Now, we'll talk about two types of data nodes:

-   **Input data nodes**: These are data nodes that help us bring data into our system.
    
-   **Output data nodes**: These are data nodes that help us send data out of our system.
    

So, data nodes are like helpers for handling data, and they come in these two varieties: _my\_input_ and _my\_output_.

![data nodes](https://docs.taipy.io/en/latest/tutorials/scenario_management/2_the_data_nodes/images/data_notes_2.svg)

Taipy has a set of predefined data nodes ready to be used when configuring your data workflow.

Here’s the list of predefined data nodes:

![data nodes](https://docs.taipy.io/en/latest/tutorials/scenario_management/2_the_data_nodes/images/data_notes.png)

### Pickle Data Node[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/2_the_data_nodes/#pickle-data-node "Permanent link")

The [Pickle](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#pickle) data node is the standard data node in Taipy. It can handle various types of Python stuff like strings, numbers, lists, dictionaries, models (for machine learning or other things), and data tables. Here's some code that uses two Pickle data nodes: one for getting data in and one for sending data out.

-   _model_ is an input _Pickle_ data node. It looks at a Pickle file called _model.p_ and gets data from there.
    
-   _predictions_ is an output data node, but right now, it doesn't have any data in it. We haven't told it where to get data from yet.
    

 Your browser does not support the video tag.

The Python configuration translates as the code below:

```
<span></span><code><span>from</span> <span>taipy.config</span> <span>import</span> <span>Config</span>

<span>model_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>"model"</span><span>,</span> <span>default_path</span><span>=</span><span>"model.p"</span><span>)</span>
<span>predictions_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>"predictions"</span><span>)</span>
<span>task_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_task</span><span>(</span><span>"task"</span><span>,</span> <span>predict</span><span>,</span> <span>model_cfg</span><span>,</span> <span>predictions_cfg</span><span>)</span>

<span>scenario_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_scenario</span><span>(</span><span>"my_scenario"</span><span>,</span> <span>[</span><span>task_cfg</span><span>])</span>
</code>
```

Once you've set up this basic graph, the next step is to create a scenario using it and then submit it for execution.

```
<span></span><code><span>scenario</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>scenario_cfg</span><span>)</span>
<span>tp</span><span>.</span><span>submit</span><span>(</span><span>scenario</span><span>)</span>
</code>
```

When submitting the scenario (for execution), Taipy:

-   retrieves and reads the model,
-   executes the _predict()_ function,
-   and writes the results in a Pickle file.

Taipy makes things easy by handling the paths for Pickle files automatically if you haven't defined them. This simplifies the configuration process. When you create several scenarios, the output data nodes from each scenario will automatically point to separate files.

```
<span></span><code><span>scenario_2</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>scenario_cfg</span><span>)</span>
<span>tp</span><span>.</span><span>submit</span><span>(</span><span>scenario_2</span><span>)</span>
</code>
```

In this example, when we create a second scenario, it also brings in a new pair of data nodes: _model_ and _predictions_. The _model_ data node still points to the same Pickle file because its path was set by the developer in advance. However, the new _predictions_ data node points to a different Pickle file. Taipy creates this new Pickle file on the fly during runtime, so it's separate from the one used in the first scenario. All data nodes that writes in the local system share this behavior.

### Tabular data nodes[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/2_the_data_nodes/#tabular-data-nodes "Permanent link")

Tabular data nodes in Taipy are a collection of data nodes designed for handling tabular data. By default, the data they point to is presented to the user or developer as a Pandas DataFrame.

The predefined tabular data nodes in Taipy include:

-   [SQL](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#sql)
-   [CSV](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#csv)
-   [Excel](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#excel)
-   [Parquet](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#parquet)

These data nodes allow you to work with tabular data from different sources with ease.

 Your browser does not support the video tag.

To use Tabular data nodes in Taipy, you only need to include them in the configuration and specify certain parameters, like a default path for CSV or Parquet files. It's important to note that you can change this path during runtime. For instance, if you create a new scenario, you can instruct the Tabular data nodes to save the results in a different file or directory, thereby preventing the overwriting of previous data. Taipy can also manage file destinations in cases where no 'default\_path' has been specified.

```
<span></span><code><span>scenario</span> <span>=</span> <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>scenario_cfg</span><span>)</span>
<span>tp</span><span>.</span><span>submit</span><span>(</span><span>scenario</span><span>)</span>
</code>
```

When you submit the scenario described above for execution in Taipy, the following steps occur:

-   Taipy reads the CSV file named `data.csv` because it is the input data node.
    
-   It takes the data from the CSV file and passes it to the _some\_preprocessing()_ function using the chosen exposed type, which is typically a Pandas DataFrame by default.
    
-   After the processing is done, Taipy writes or overwrites the result, which is typically in the form of a Pandas DataFrame, into the Parquet file located at _data.parquet_.
    
-   This Parquet file may overwrite any existing data in that file if it already exists.
    

Here, we'll demonstrate how you can change the exposed type from the default Pandas DataFrame to other types, such as _Numpy arrays_:

 Your browser does not support the video tag.

### Generic data nodes[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/2_the_data_nodes/#generic-data-nodes "Permanent link")

The **Generic** data node in Taipy is a flexible option that users can customize to include their own _read()_ and _write()_ functions. This feature is particularly useful when dealing with data sources that don't have a predefined Taipy Data node. With a Generic data node, you can tailor it to access data in specific formats or from custom sources.

For more detailed information and guidance on using the Generic data node and customizing it to your specific needs, check the [Taipy documentation](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#generic). It will provide you with step-by-step instructions and examples.

Taipy integrates two other predefined storage types to work with documents. Check the documentation for more details.

-   [Mongo](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#mongo-collection)
-   [Json](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#json)

### Conclusion[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/2_the_data_nodes/#conclusion "Permanent link")

As mentioned before, data nodes serve as references to data sources, and they hide the complexities of how data is stored and fetched. This simplifies the process of working with data within a complete web application.

Furthermore, Taipy's capability to model data nodes enables it to eliminate redundant tasks. Taipy can recognize situations where inputs have remained unchanged between two runs, resulting in the same outputs. As a result, it becomes unnecessary to re-execute the task. This _skippability_ feature enhances the efficiency of data processing, ultimately saving users valuable time and resources.