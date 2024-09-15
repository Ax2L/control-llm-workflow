# Workflow LLM Control

## Rules and Guidelines
To ensure we complete every task correctly and efficiently, we will follow these rules:

1. **Consistency**: Follow the same coding standards and practices throughout the project.
2. **Documentation**: Document every function, class, and module to ensure clarity and maintainability.
3. **Code Reviews**: Conduct code reviews for all major changes to maintain code quality.
4. **Task Management**: Use a task management tool to track progress and ensure timely completion of tasks.

## Folder Structure

### `config/`
Contains configuration files for the application. For example, `config.json` holds various settings used throughout the application.

### `data/`
Stores data files used by the application, such as task data in JSON format. For example, `tasks.json` contains the list of tasks.

### `modules/`
Includes utility modules and functions that support the main application logic. For example, `utils.py` contains functions for logging, loading conversations, and interacting with the LLM.

### `tasks/`
Holds task-related configuration files. For example, `test.toml` defines the structure and settings for task scenarios.

### `app.py`
The main entry point for the application, responsible for initializing and running the core logic.

## Running the Application

To run the application with a specific Taipy Scenario, use the following command:

```sh

python app.py -s <scenario_name> 

# For example, to run the `llm_oobabooga_instruction` scenario, use:

python app.py -s llm_oobabooga_instruction

```

## Project Goals
We aim to achieve the following with this project:

- **WebUI**: Develop a web-based user interface where users can create, view, schedule, and manually execute workflows.
- **Taipy**: Utilize the Python library "Taipy" to build and manage the web application efficiently.

## Taipy's Core Concepts
Taipy Core is an application builder designed to help Python developers turn their data algorithms into an interactive production-ready data-driven application. Taipy Core provides the necessary concepts for modeling, executing, and monitoring algorithms. The main Taipy concept to model an algorithm is called Scenario.

A scenario can be seen as a succession of functions that exchange data. It can be described as an execution graph (a Directed Acyclic Graph or DAG). With Taipy Core, one can model simple and very complex scenarios.

### Key Concepts

- **Data Node**: Represents a reference to a dataset. It can be used/shared by multiple tasks as input or output. It can refer to any type of data: a built-in Python object, a file, a machine learning model, etc.
- **Task**: A function receiving data node(s) as input and returning data node(s) as output.
- **Job**: Represents a unique execution of a Task.
- **Scenario**: A set of tasks connected through data nodes forming a Directed Acyclic Graph, executed as a whole to create a consistent algorithm.
- **Sequence**: A set of tasks connected through data nodes, executed as a whole, forming a consistent algorithm. It belongs to a scenario and can be thought of as a subgraph of the scenario's complete graph.
- **Cycle**: A time period corresponding to an iteration of a recurrent business problem, defined by the frequency of scenarios.
- **Scope**: Represents the visibility of a data node in the graph of entities, and the level of its owner (Scenario, Cycle, Global).

### Configuration vs Entities

Among the concepts described, data nodes, tasks, and scenarios have two types of Taipy objects related to them: configuration objects and runtime objects.

- **Configuration Objects**: Named configs (DataNodeConfig, TaskConfig, and ScenarioConfig). They describe the characteristics and behaviors of the concepts they relate to.
- **Runtime Objects**: Named entities (DataNode, Task, and Scenario). Each entity is instantiated from a config, and the same config can be used to instantiate multiple entities.

For more details, refer to the [Taipy Documentation](https://docs.taipy.io/).

### Examples

- **Simple Single Function Example**
- **Linear Example with Two Functions**
- **Branching Example**

This section aims to define the following Taipy Core concepts with visual examples and detailed explanations.

### Additional Resources

- [Taipy Core Concepts](https://docs.taipy.io/)
- [Taipy Cheat Sheets](https://github.com/tushar2704/Taipy-Cheat-Sheets)

Ensure to follow these guidelines and concepts during the development phase to maintain consistency and efficiency.
















