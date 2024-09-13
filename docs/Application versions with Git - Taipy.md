When developing and deploying a Taipy application, it is straightforward to manage Taipy entities (scenarios, tasks, data nodes, etc.) and keep them up-to-date when the configuration changes.

In the following, we will use a basic Taipy application example defined in `main.py`.

| main.py |
| --- |
| 
```
<span></span><span> 1</span>
<span> 2</span>
<span> 3</span>
<span> 4</span>
<span> 5</span>
<span> 6</span>
<span> 7</span>
<span> 8</span>
<span> 9</span>
<span>10</span>
<span>11</span>
<span>12</span>
<span>13</span>
<span>14</span>
<span>15</span>
<span>16</span>
<span>17</span>
<span>18</span>
```



 | 

```
<span></span><code tabindex="0"><span>import</span> <span>taipy</span> <span>as</span> <span>tp</span>
<span>from</span> <span>taipy</span> <span>import</span> <span>Config</span>


<span>def</span> <span>example_algorithm</span><span>(</span><span>entry</span><span>:</span> <span>str</span><span>):</span>
    <span># does nothing!</span>
    <span>return</span> <span>entry</span>


<span>input_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>"my_input"</span><span>,</span> <span>default_data</span><span>=</span><span>"a_string"</span><span>)</span>
<span>output_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>"my_output"</span><span>)</span>
<span>task_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_task</span><span>(</span><span>"example_algorithm"</span><span>,</span> <span>example_algorithm</span><span>,</span> <span>input_cfg</span><span>,</span> <span>output_cfg</span><span>)</span>
<span>scenario_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_scenario</span><span>(</span><span>"my_scenario"</span><span>,</span> <span>[</span><span>task_cfg</span><span>])</span>

<span>if</span> <span>__name__</span> <span>==</span> <span>"__main__"</span><span>:</span>
    <span>tp</span><span>.</span><span>Core</span><span>()</span><span>.</span><span>run</span><span>()</span>
    <span>tp</span><span>.</span><span>create_scenario</span><span>(</span><span>scenario_cfg</span><span>)</span>
    <span>print</span><span>(</span><span>f</span><span>"Number of scenarios: </span><span>{</span><span>len</span><span>(</span><span>tp</span><span>.</span><span>get_scenarios</span><span>())</span><span>}</span><span>"</span><span>)</span>
</code>
```



 |

Basic knowledge of Git is required to follow this tutorial.

## Set up the Taipy application as a Git repository[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/8_version_management/#set-up-the-taipy-application-as-a-git-repository "Permanent link")

Your application directory must be initialized for Git. From the application directory run:

```
<span></span><code><span>$ </span>git<span> </span>init
<span>...</span>
<span>Initialized empty Git repository in ~/your_taipy_application/.git/</span>
</code>
```

We then need to create a `.gitignore` file to ignore the `.data` directory that contains Taipy entities: we don't want entities to be managed by Git. You can create the `.gitignore` file manually or by running the following command:

```
<span></span><code><span>$ </span><span>echo</span><span> </span><span>".data"</span><span> </span>&gt;<span> </span>.gitignore
</code>
```

Then we can commit the `.gitignore` file to Git:

```
<span></span><code><span>$ </span>git<span> </span>add<span> </span>.gitignore
<span>$ </span>git<span> </span>commit<span> </span>-m<span> </span><span>"Initialize .gitignore to ignore Taipy entities"</span>
</code>
```

Now you're ready to manage your Taipy application with Git and Taipy version management.

## Create a Taipy application version[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/8_version_management/#create-a-taipy-application-version "Permanent link")

By default, a Taipy application runs in development mode, which means entities from previous development run are deleted before running the application. To save the entities of a run, you can create a new experiment version of your application by running your Taipy application with the `--experiment` option to the `taipy` command. After running the application to make sure that it works, let's name the experiment version `1.0` and commit the version to Git.

```
<span></span><code><span>$ </span>taipy<span> </span>run<span> </span>main.py<span> </span>--experiment<span> </span><span>1</span>.0
<span>$ </span>git<span> </span>add<span> </span>main.py
<span>$ </span>git<span> </span>commit<span> </span>-m<span> </span><span>"Create experiment version 1.0"</span>
</code>
```

## Switching between versions[¶](https://docs.taipy.io/en/latest/tutorials/scenario_management/8_version_management/#switching-between-versions "Permanent link")

A commonly used Git workflow is to use `git checkout` to switch to a different branch and work on a new application version. Let's create a new Git branch called `1.1` and switch to it:

```
<span></span><code><span>$ </span>git<span> </span>checkout<span> </span>-b<span> </span><span>1</span>.1
<span>Switched to a new branch '1.1'</span>
</code>
```

After modifying the application code (to experiment with a new algorithm for example), we can run the application in experiment mode and name the experiment version `1.1` in the new branch. This run will create and use entities of version `1.1` only.

```
<span></span><code><span>$ </span>taipy<span> </span>run<span> </span>main.py<span> </span>--experiment<span> </span><span>1</span>.1
</code>
```

We then can commit the new version to Git.

```
<span></span><code><span>$ </span>git<span> </span>add<span> </span>.
<span>$ </span>git<span> </span>commit<span> </span>-m<span> </span><span>"create experiment version 1.1"</span>
</code>
```

Similarly, we can create a new branch `1.2` and create a new application version in it:

```
<span></span><code><span>$ </span>git<span> </span>checkout<span> </span>-b<span> </span><span>1</span>.2
<span>Switched to a new branch '1.2'</span>
<span>...</span>
<span># </span>modify<span> </span>the<span> </span>application<span> </span>code<span> </span>and<span> </span>run<span> </span>the<span> </span>application
<span>...</span>
<span>$ </span>git<span> </span>add<span> </span>.
<span>$ </span>git<span> </span>commit<span> </span>-m<span> </span><span>"create experiment version 1.2"</span>
</code>
```

The entities of all three versions 1.0, 1.1, and 1.2 are still stored in the `.data` directory. We can switch back to the version 1.1 of the application and run it again:

```
<span></span><code><span>$ </span>git<span> </span>checkout<span> </span><span>1</span>.1
<span>$ </span>taipy<span> </span>run<span> </span>main.py<span> </span>--experiment<span> </span><span>1</span>.1
</code>
```

Warning

You need to run provide the correct version number when running the application in experiment mode. Otherwise, the configuration maybe incompatible with the entities of the version you want to run and an error will be raised.