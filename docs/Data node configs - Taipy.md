## New data node config[¶](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#new-data-node-config "Permanent link")

To create an instance of a [Data node](https://docs.taipy.io/en/latest/manuals/core/concepts/data-node/), a data node configuration must first be provided. [`DataNodeConfig`](https://docs.taipy.io/en/latest/manuals/reference/taipy.core.config.DataNodeConfig) is used to configure data nodes. To configure a new [`DataNodeConfig`](https://docs.taipy.io/en/latest/manuals/reference/taipy.core.config.DataNodeConfig), one can use the function [`Config.configure_data_node()`](https://docs.taipy.io/en/latest/manuals/reference/taipy.config.Config/index.html#taipy.config.Config.configure_data_node).

<table><tbody><tr><td></td><td><div><pre id="__code_0"><span></span><code><span>from</span> <span>taipy</span> <span>import</span> <span>Config</span>

<span>data_node_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>id</span><span>=</span><span>"data_node_cfg"</span><span>)</span>
</code></pre></div></td></tr></tbody></table>

We configured a simple data node in the previous code by providing an identifier as the string "data\_node\_cfg". The [`Config.configure_data_node()`](https://docs.taipy.io/en/latest/manuals/reference/taipy.config.Config/index.html#taipy.config.Config.configure_data_node) method actually creates a data node configuration, and registers it in the [`Config`](https://docs.taipy.io/en/latest/manuals/reference/taipy.config.Config) singleton.

The attributes available on data nodes are:

-   _**id**_ is the string identifier of the data node config.  
    It is a **mandatory** parameter and must be a unique and valid Python identifier.
-   _**scope**_ is a [`Scope`](https://docs.taipy.io/en/latest/manuals/reference/taipy.config.Scope).  
    It corresponds to the [scope](https://docs.taipy.io/en/latest/manuals/core/concepts/scope/) of the data node that will be instantiated from the data node configuration. The **default value** is `Scope.SCENARIO`.
-   _**validity\_period**_ is a [timedelta object](https://docs.python.org/3/library/datetime.html#timedelta-objects) that represents the duration since the last edit date for which the data node can be considered up-to-date. Once the validity period has passed, the data node is considered stale and relevant tasks will run even if they are skippable (see the [Task configs page](https://docs.taipy.io/en/latest/manuals/core/config/task-config/) for more details). If _validity\_period_ is set to the default value None, the data node is always up-to-date.
-   _**storage\_type**_ is an attribute that indicates the storage type of the data node.  
    The possible values are ["pickle"](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#pickle) (**the default value**), ["csv"](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#csv), ["excel"](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#excel), ["json"](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#json), ["mongo\_collection"](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#mongo-collection), ["parquet"](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#parquet), ["sql"](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#sql), ["sql\_table"](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#sql_table), ["in\_memory"](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#in-memory), ["generic"](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#generic) or ["Amazon Web Service S3 Object"](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#amazon-web-service-s3-object).  
    As explained in the following subsections, depending on the _storage\_type_, other configuration attributes must be provided in the _properties_ parameter.
-   Any other custom attribute can be provided through the parameter _**properties**_, a kwargs dictionary accepting any number of custom parameters (a description, a label, a tag, etc.) (It is recommended to read [doc](https://realpython.com/python-kwargs-and-args/) if you are not familiar with __kwargs arguments)  
    This_ properties_ dictionary is used to configure the parameters specific to each storage type. It is copied in the dictionary properties of all the data nodes instantiated from this data node configuration.  
    

Reserved keys

Note that we cannot use the word "\_entity\_owner" as a key in the properties as it has been reserved for internal use.

Below are two examples of data node configurations.

<table><tbody><tr><td><div><pre><span></span><span> 1</span>
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
<span>16</span></pre></div></td><td><div><pre id="__code_1"><span></span><code><span>from</span> <span>datetime</span> <span>import</span> <span>timedelta</span>
<span>from</span> <span>taipy</span> <span>import</span> <span>Config</span><span>,</span> <span>Scope</span>

<span>date_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span>
    <span>id</span><span>=</span><span>"date_cfg"</span><span>,</span>
    <span>description</span><span>=</span><span>"The current date of the scenario"</span><span>,</span>
<span>)</span>

<span>model_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span>
    <span>id</span><span>=</span><span>"model_cfg"</span><span>,</span>
    <span>scope</span><span>=</span><span>Scope</span><span>.</span><span>CYCLE</span><span>,</span>
    <span>storage_type</span><span>=</span><span>"pickle"</span><span>,</span>
    <span>validity_period</span><span>=</span><span>timedelta</span><span>(</span><span>days</span><span>=</span><span>2</span><span>),</span>
    <span>description</span><span>=</span><span>"Trained model shared by all scenarios"</span><span>,</span>
    <span>code</span><span>=</span><span>54</span><span>,</span>
<span>)</span>
</code></pre></div></td></tr></tbody></table>

In lines 4-7, we configured a simple data node with the id "date\_cfg". The default value for _scope_ is `SCENARIO`. The _storage\_type_ is set to the default value "pickle".  
An optional custom property called _description_ is also added: this property is propagated to the data nodes instantiated from this config.

In lines 9-16, we add another data node configuration with the id "model\_cfg". The _scope_ is set to `CYCLE` so that all the scenarios from the same cycle will share the corresponding data nodes. The _storage\_type_ is "pickle". The _validity\_period_ is set to 2 days, which indicate that the data node is going to stale after 2 days of being modified. Finally, two optional custom properties are added: a _description_ string and an integer _code_. These two properties are propagated to the data nodes instantiated from this config.

## Storage type[¶](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#storage-type "Permanent link")

Taipy proposes predefined _data nodes_ corresponding to the most popular _storage types_. Thanks to predefined _data nodes_, the Python developer does not need to spend much time configuring the _storage types_ or the _query system_. A predefined data node will often satisfy the user's required format: pickle, CSV, SQL table, MongoDB collection, Excel sheet, Amazon Web Service S3 Object, etc.

The various predefined _storage types_ are typically used for input data. Indeed, the input data is usually provided by external sources, where the Python developer user does not control the format.

For intermediate or output _data nodes_, the developer often does not have any particular specifications regarding the _storage type_. In such a case, using the default _storage type_ pickle that does not require any configuration is recommended.

If a more specific method to store, read and write the data is needed, Taipy provides a Generic data node that can be used for any storage type (or any kind of query system). The developer only needs to provide two Python functions, one for reading and one for writing the data. Please refer to the [generic data node config section](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#generic) for more details on generic data node.

All predefined data nodes are described in the subsequent sections.

### Pickle[¶](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#pickle "Permanent link")

A [`PickleDataNode`](https://docs.taipy.io/en/latest/manuals/reference/taipy.core.data.PickleDataNode) is a specific data node used to model _pickle_ data. The [`Config.configure_pickle_data_node()`](https://docs.taipy.io/en/latest/manuals/reference/taipy.config.Config/index.html#taipy.config.Config.configure_pickle_data_node) method configures a new _pickle_ data node configuration. In addition to the generic parameters described in the [Data node configuration](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/) section, two optional parameters can be provided.

-   _**default\_path**_ represents the default file path used to read and write the data of the data nodes instantiated from the _pickle_ configuration.  
    It is used to populate the path property of the entities (_pickle_ data nodes) instantiated from the _pickle_ data node configuration. That means by default all the entities (_pickle_ data nodes) instantiated from the same _pickle_ configuration will inherit/share the same _pickle_ file provided in the default\_path. To avoid this, the path property of a _pickle_ data node entity can be changed at runtime right after its instantiation.  
    If no value is provided, Taipy will use an internal path in the Taipy storage folder (more details on the Taipy storage folder configuration are available in the [Core configuration](https://docs.taipy.io/en/latest/manuals/core/config/core-config/) documentation).
    
-   _**default\_data**_ indicates data automatically written to the data node _pickle_ upon creation.  
    Any serializable Python object can be used. The default value is None.
    

<table><tbody><tr><td></td><td><div><pre id="__code_2"><span></span><code><span>from</span> <span>taipy</span> <span>import</span> <span>Config</span>
<span>from</span> <span>datetime</span> <span>import</span> <span>datetime</span>

<span>date_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_pickle_data_node</span><span>(</span>
    <span>id</span><span>=</span><span>"date_cfg"</span><span>,</span>
    <span>default_data</span><span>=</span><span>datetime</span><span>(</span><span>2022</span><span>,</span> <span>1</span><span>,</span> <span>25</span><span>))</span>

<span>model_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_pickle_data_node</span><span>(</span>
    <span>id</span><span>=</span><span>"model_cfg"</span><span>,</span>
    <span>default_path</span><span>=</span><span>"path/to/my/model.p"</span><span>,</span>
    <span>description</span><span>=</span><span>"The trained model"</span><span>)</span>
</code></pre></div></td></tr></tbody></table>

In lines 4-6, we configure a simple pickle data node with the id "date\_cfg". The scope is `SCENARIO` (default value), and default data is provided.

In lines 8-11, we add another pickle data node configuration with the id "model\_cfg". The default `SCENARIO` scope is used. Since the data node config corresponds to a pre-existing pickle file, a default path "path/to/my/model.p" is provided. We also added an optional custom description.

### CSV[¶](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#csv "Permanent link")

A [`CSVDataNode`](https://docs.taipy.io/en/latest/manuals/reference/taipy.core.data.CSVDataNode) data node is a specific data node used to model CSV file data. To add a new _CSV_ data node configuration, the [`Config.configure_csv_data_node()`](https://docs.taipy.io/en/latest/manuals/reference/taipy.config.Config/index.html#taipy.config.Config.configure_csv_data_node) method can be used. In addition to the generic parameters described in the [Data node configuration](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/) section, the following parameters can be provided:

-   _**default\_path**_ represents the default file path used to read and write data pointed by the data nodes instantiated from the _csv_ configuration.  
    It is used to populate the path property of the entities (_csv_ data nodes) instantiated from the _csv_ data node configuration. That means by default all the entities (_csv_ data nodes) instantiated from the same _csv_ configuration will inherit/share the same _csv_ file provided in the default\_path. To avoid this, the path property of a _csv_ data node entity can be changed at runtime right after its instantiation.  
    
-   _**encoding**_ represents the encoding of the CSV file.  
    The default value of _encoding_ is "utf-8".
    
-   _**has\_header**_ indicates if the file has a header of not.  
    By default, _has\_header_ is True and Taipy will use the 1st row in the CSV file as the header.
    
-   _**exposed\_type**_ indicates the data type returned when reading the data node (more examples of reading from a CSV data node with different _exposed\_type_ are available in the [Read / Write a data node](https://docs.taipy.io/en/latest/manuals/core/entities/data-node-mgt/#csv) documentation):
    
    -   By default, _exposed\_type_ is "pandas", and the data node reads the CSV file as a Pandas DataFrame (`pandas.DataFrame`) when executing the read method.
    -   If the _exposed\_type_ provided is "modin", the data node reads the CSV file as a Modin DataFrame (`modin.pandas.DataFrame`) when executing the read method.
    -   If the _exposed\_type_ provided is "numpy", the data node reads the CSV file as a NumPy array (`numpy.ndarray`) when executing the read method.
    -   If the provided _exposed\_type_ is a custom Python class, the data node creates a list of custom objects with the given custom class. Each object represents a row in the CSV file.

<table><tbody><tr><td><div><pre><span></span><span> 1</span>
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
<span>19</span>
<span>20</span>
<span>21</span></pre></div></td><td><div><pre id="__code_3"><span></span><code><span>from</span> <span>taipy</span> <span>import</span> <span>Config</span>

<span>class</span> <span>SaleRow</span><span>:</span>
    <span>date</span><span>:</span> <span>str</span>
    <span>nb_sales</span><span>:</span> <span>int</span>

<span>temp_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_csv_data_node</span><span>(</span>
    <span>id</span><span>=</span><span>"historical_temperature"</span><span>,</span>
    <span>default_path</span><span>=</span><span>"path/hist_temp.csv"</span><span>,</span>
    <span>has_header</span><span>=</span><span>True</span><span>,</span>
    <span>exposed_type</span><span>=</span><span>"numpy"</span><span>)</span>

<span>log_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_csv_data_node</span><span>(</span>
    <span>id</span><span>=</span><span>"log_history"</span><span>,</span>
    <span>default_path</span><span>=</span><span>"path/hist_log.csv"</span><span>,</span>
    <span>exposed_type</span><span>=</span><span>"modin"</span><span>)</span>

<span>sales_history_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_csv_data_node</span><span>(</span>
    <span>id</span><span>=</span><span>"sales_history"</span><span>,</span>
    <span>default_path</span><span>=</span><span>"path/sales.csv"</span><span>,</span>
    <span>exposed_type</span><span>=</span><span>SaleRow</span><span>)</span>
</code></pre></div></td></tr></tbody></table>

In lines 3-5, we define a custom class `SaleRow` representing a row of the CSV file.

In lines 7-11, we configure a basic CSV data node with the identifier "historical\_temperature". Its _scope_ is by default `SCENARIO`. The default path points to the file "path/hist\_temp.csv". The property _has\_header_ is set to True.

In lines 13-16, we configure another CSV data node with the identifier "log\_history". It uses the default `SCENARIO` scope again. The default path points to "path/hist\_log.csv". The _exposed\_type_ provided is "modin".

In lines 18-21, we add another CSV data node configuration with the identifier "sales\_history". The default `SCENARIO` scope is used again. Since we have a custom class called `SaleRow` that is defined for this CSV file, we provide it as the _exposed\_type_ parameter.

### Excel[¶](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#excel "Permanent link")

An [`ExcelDataNode`](https://docs.taipy.io/en/latest/manuals/reference/taipy.core.data.ExcelDataNode) is a specific data node used to model xlsx file data. To add a new _Excel_ data node configuration, the [`Config.configure_excel_data_node()`](https://docs.taipy.io/en/latest/manuals/reference/taipy.config.Config/index.html#taipy.config.Config.configure_excel_data_node) method can be used. In addition to the generic parameters described in the [Data node configuration](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/) section, a mandatory and three optional parameters are provided.

-   _**default\_path**_ represents the default file path used to read and write data pointed by the data nodes instantiated from the _Excel_ configuration.  
    It is used to populate the path property of the entities (_Excel_ data nodes) instantiated from the _Excel_ data node configuration. That means by default all the entities (_Excel_ data nodes) instantiated from the same _Excel_ configuration will inherit/share the same _Excel_ file provided in the default\_path. To avoid this, the path property of a _Excel_ data node entity can be changed at runtime right after its instantiation.  
    
-   _**has\_header**_ indicates if the file has a header of not.  
    By default, _has\_header_ is True and Taipy will use the 1st row in the Excel file as the header.
    
-   _**sheet\_name**_ represents which specific sheet in the Excel file to read:
    
    -   By default, _sheet\_name_ is None and the data node will return all sheets in the Excel file when reading it.
    -   If _sheet\_name_ is provided as a string, the data node will read only the data of the corresponding sheet.
    -   If _sheet\_name_ is provided with a list of sheet names, the data node will return a dictionary with the key being the sheet name and the value being the data of the corresponding sheet.
-   _**exposed\_type**_ indicates the data type returned when reading the data node (more examples of reading from an Excel data node with different _exposed\_type_ are available in the [Read / Write a data node](https://docs.taipy.io/en/latest/manuals/core/entities/data-node-mgt/#excel) documentation):
    
    -   By default, _exposed\_type_ is "pandas", and the data node reads the Excel file as a Pandas DataFrame (`pandas.DataFrame`) when executing the read method.
    -   If the _exposed\_type_ provided is "modin", the data node reads the Excel file as a Modin DataFrame (`modin.pandas.DataFrame`) when executing the read method.
    -   If the _exposed\_type_ provided is "numpy", the data node reads the Excel file as a NumPy array (`numpy.ndarray`) when executing the read method.
    -   If the provided _exposed\_type_ is a custom Python class, the data node creates a list of custom objects with the given custom class. Each object represents a row in the Excel file.

<table><tbody><tr><td><div><pre><span></span><span> 1</span>
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
<span>19</span>
<span>20</span>
<span>21</span></pre></div></td><td><div><pre id="__code_4"><span></span><code><span>from</span> <span>taipy</span> <span>import</span> <span>Config</span>

<span>class</span> <span>SaleRow</span><span>:</span>
    <span>date</span><span>:</span> <span>str</span>
    <span>nb_sales</span><span>:</span> <span>int</span>

<span>hist_temp_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_excel_data_node</span><span>(</span>
    <span>id</span><span>=</span><span>"historical_temperature"</span><span>,</span>
    <span>default_path</span><span>=</span><span>"path/hist_temp.xlsx"</span><span>,</span>
    <span>exposed_type</span><span>=</span><span>"numpy"</span><span>)</span>

<span>hist_log_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_excel_data_node</span><span>(</span>
    <span>id</span><span>=</span><span>"log_history"</span><span>,</span>
    <span>default_path</span><span>=</span><span>"path/hist_log.xlsx"</span><span>,</span>
    <span>exposed_type</span><span>=</span><span>"modin"</span><span>)</span>

<span>sales_history_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_excel_data_node</span><span>(</span>
    <span>id</span><span>=</span><span>"sales_history"</span><span>,</span>
    <span>default_path</span><span>=</span><span>"path/sales.xlsx"</span><span>,</span>
    <span>sheet_name</span><span>=</span><span>[</span><span>"January"</span><span>,</span> <span>"February"</span><span>],</span>
    <span>exposed_type</span><span>=</span><span>SaleRow</span><span>)</span>
</code></pre></div></td></tr></tbody></table>

In lines 3-5, we define a custom class `SaleRow`, representing a row in the Excel file.

In lines 7-10, we configure an Excel data node. The identifier is "historical\_temperature". Its _scope_ is `SCENARIO` (default value), and the default path is the file hist\_temp.xlsx. _has\_header_ is set to True, the Excel file must have a header. The _sheet\_name_ is not provided so Taipy uses the default value "Sheet1".

In lines 12-15, we configure a new Excel data node. The identifier is "log\_history", the default `SCENARIO` scope is used, and the default path is "path/hist\_log.xlsx". "modin" is used as the exposed\_type\*\*.

In lines 17-21, we add another Excel data node configuration. The identifier is "sales\_history", the default `SCENARIO` scope is used. Since we have a custom class pre-defined for this Excel file, we provide it in the exposed\_type__. We also provide the list of specific sheets we want to use as the_ sheet\_name_ parameter.

### SQL Table[¶](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#sql-table "Permanent link")

Note

-   To be able to use a [`SQLTableDataNode`](https://docs.taipy.io/en/latest/manuals/reference/taipy.core.data.SQLTableDataNode) with Microsoft SQL Server, you need to run optional dependencies with `pip install taipy[mssql]` and install your corresponding [Microsoft ODBC Driver for SQLServer](https://docs.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server).
-   To be able to use a [`SQLTableDataNode`](https://docs.taipy.io/en/latest/manuals/reference/taipy.core.data.SQLTableDataNode) with MySQL Server, you need to run optional dependencies with `pip install taipy[mysql]` and install your corresponding [MySQL Driver for MySQL](https://pypi.org/project/PyMySQL/).
-   To be able to use a [`SQLTableDataNode`](https://docs.taipy.io/en/latest/manuals/reference/taipy.core.data.SQLTableDataNode) with PostgreSQL Server, you need to run optional dependencies with `pip install taipy[postgresql]` and install your corresponding [Postgres JDBC Driver for PostgreSQL](https://www.postgresql.org/docs/7.4/jdbc-use.html).

A [`SQLTableDataNode`](https://docs.taipy.io/en/latest/manuals/reference/taipy.core.data.SQLTableDataNode) is a specific data node that models data stored in a single SQL table. To add a new _SQL table_ data node configuration, the [`Config.configure_sql_table_data_node()`](https://docs.taipy.io/en/latest/manuals/reference/taipy.config.Config/index.html#taipy.config.Config.configure_sql_table_data_node) method can be used. In addition to the generic parameters described in the [Data node configuration](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/) section, the following parameters can be provided:

-   _**db\_name**_ represents the name of the database.
-   _**db\_engine**_ represents the engine of the database.  
    Possible values are _"sqlite"_, _"mssql"_, _"mysql"_, or _"postgresql"_.
-   _**table\_name**_ represents the name of the table to read from and write into.
-   _**db\_username**_ represents the database username that will be used by Taipy to access the database. Required by _"mssql"_, _"mysql"_, and _"postgresql"_ engines.
-   _**db\_password**_ represents the database user's password that will be used by Taipy to access the database. Required by _"mssql"_, _"mysql"_, and _"postgresql"_ engines.
-   _**db\_host**_ represents the database host that will be used by Taipy to access the database.  
    The default value of _db\_host_ is "localhost".
-   _**db\_port**_ represents the database port that will be used by Taipy to access the database.  
    The default value of _db\_port_ is 1433.
-   _**db\_driver**_ represents the database driver that will be used by Taipy.
-   _**sqlite\_folder\_path**_ represents the path to the folder that contains the SQLite database file. The default value of _sqlite\_folder\_path_ is the current working folder.
-   _**sqlite\_file\_extension**_ represents the file extension of the SQLite database file. The default value of _sqlite\_file\_extension_ is ".db".
-   _**db\_extra\_args**_ is a dictionary of additional arguments that need to be passed into the database connection string.
-   _**exposed\_type**_ indicates the data type returned when reading the data node (more examples of reading from a SQL table data node with different _exposed\_type_ are available in the [Read / Write a data node](https://docs.taipy.io/en/latest/manuals/core/entities/data-node-mgt/#sql-table) documentation):
    -   By default, _exposed\_type_ is "pandas", and the data node reads the SQL table as a Pandas DataFrame (`pandas.DataFrame`) when executing the read method.
    -   If the _exposed\_type_ provided is "modin", the data node reads the SQL table as a Modin DataFrame (`modin.pandas.DataFrame`) when executing the read method.
    -   If the _exposed\_type_ provided is "numpy", the data node reads the SQL table as a NumPy array (`numpy.ndarray`) when executing the read method.
    -   If the provided _exposed\_type_ is a custom Python class, the data node creates a list of custom objects with the given custom class. Each object represents a record in the SQL table.

#### Example with a Microsoft SQL database table[¶](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#example-with-a-microsoft-sql-database-table "Permanent link")

First, let's take a look at an example on how to configure a _SQL table_ data node with the database engine is `mssql` (short for Microsoft SQL).

<table><tbody><tr><td><div><pre><span></span><span> 1</span>
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
<span>12</span></pre></div></td><td><div><pre id="__code_5"><span></span><code><span>from</span> <span>taipy</span> <span>import</span> <span>Config</span>

<span>sales_history_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_sql_table_data_node</span><span>(</span>
    <span>id</span><span>=</span><span>"sales_history"</span><span>,</span>
    <span>db_username</span><span>=</span><span>"admin"</span><span>,</span>
    <span>db_password</span><span>=</span><span>"password"</span><span>,</span>
    <span>db_name</span><span>=</span><span>"taipy"</span><span>,</span>
    <span>db_engine</span><span>=</span><span>"mssql"</span><span>,</span>
    <span>table_name</span><span>=</span><span>"sales"</span><span>,</span>
    <span>db_driver</span><span>=</span><span>"ODBC Driver 17 for SQL Server"</span><span>,</span>
    <span>db_extra_args</span><span>=</span><span>{</span><span>"TrustServerCertificate"</span><span>:</span> <span>"yes"</span><span>},</span>
<span>)</span>
</code></pre></div></td></tr></tbody></table>

In this example, we configure a _SQL table_ data node with the id "sales\_history". Its scope is the default value `SCENARIO`. The database username is "admin", the user's password is "password" (refer to [advance configuration](https://docs.taipy.io/en/latest/manuals/core/config/advanced-config/) to pass password as an environment variable), the database name is "taipy". The table name is "sales". To ensure secure connection with the SQL server, "TrustServerCertificate" is defined as "yes" in the _db\_extra\_args_.

#### Example with a SQLite database table[¶](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#example-with-a-sqlite-database-table "Permanent link")

In the next example, we configure a _SQL table_ data node with the database engine is `sqlite`.

<table><tbody><tr><td></td><td><div><pre id="__code_6"><span></span><code><span>from</span> <span>taipy</span> <span>import</span> <span>Config</span>

<span>sales_history_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_sql_table_data_node</span><span>(</span>
    <span>id</span><span>=</span><span>"sales_history"</span><span>,</span>
    <span>db_name</span><span>=</span><span>"taipy"</span><span>,</span>
    <span>db_engine</span><span>=</span><span>"sqlite"</span><span>,</span>
    <span>table_name</span><span>=</span><span>"sales"</span><span>,</span>
    <span>sqlite_folder_path</span><span>=</span><span>"database"</span><span>,</span>
    <span>sqlite_file_extension</span><span>=</span><span>".sqlite3"</span><span>,</span>
<span>)</span>
</code></pre></div></td></tr></tbody></table>

Here, the database username and password are unnecessary. The folder containing SQLite database file is "database", with the file extension is ".sqlite3". Since the database name is "taipy", this SQL table data node will read and write to the SQLite database stored at "database/taipy.sqlite3".

When the data node is read, it reads all the rows from the table "sales", and when the data node is written, it deletes all the data in the table and insert the new data.

### SQL[¶](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#sql "Permanent link")

Note

-   To be able to use a [`SQLDataNode`](https://docs.taipy.io/en/latest/manuals/reference/taipy.core.data.SQLDataNode) with Microsoft SQL Server, you need to install optional dependencies with `pip install taipy[mssql]` and install your corresponding [Microsoft ODBC Driver for SQL Server](https://docs.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server).
-   To be able to use a [`SQLDataNode`](https://docs.taipy.io/en/latest/manuals/reference/taipy.core.data.SQLDataNode) with MySQL Server, you need to install optional dependencies with `pip install taipy[mysql]` and install your corresponding [MySQL Driver for MySQL](https://pypi.org/project/PyMySQL/).
-   To be able to use a [`SQLDataNode`](https://docs.taipy.io/en/latest/manuals/reference/taipy.core.data.SQLDataNode) with PostgreSQL Server, you need to install optional dependencies with `pip install taipy[postgresql]` and install your corresponding [Postgres JDBC Driver for PostgreSQL](https://www.postgresql.org/docs/7.4/jdbc-use.html).

A [`SQLDataNode`](https://docs.taipy.io/en/latest/manuals/reference/taipy.core.data.SQLDataNode) is a specific data node used to model data stored in a SQL Database. To add a new _SQL_ data node configuration, the [`Config.configure_sql_data_node()`](https://docs.taipy.io/en/latest/manuals/reference/taipy.config.Config/index.html#taipy.config.Config.configure_sql_data_node) method can be used. In addition to the generic parameters described in the [Data node configuration](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/) section, the following parameters can be provided:

-   _**db\_name**_ represents the name of the database.
-   _**db\_engine**_ represents the engine of the database.  
    Possible values are _"sqlite"_, _"mssql"_, _"mysql"_, or _"postgresql"_.
-   _**read\_query**_ represents the SQL query that will be used by Taipy to read the data from the database.
-   _**write\_query\_builder**_ is a callable function that takes in the data as an input parameter and returns a list of SQL queries to be executed when the write method is called.
-   _**append\_query\_builder**_ is a callable function that takes in the data as an input parameter and returns a list of SQL queries to be executed when the append method is called.
-   _**db\_username**_ represents the database username that will be used by Taipy to access the database. Required by _"mssql"_, _"mysql"_, and _"postgresql"_ engines.
-   _**db\_password**_ represents the database user's password that will be used by Taipy to access the database. Required by _"mssql"_, _"mysql"_, and _"postgresql"_ engines.
-   _**db\_host**_ represents the database host that will be used by Taipy to access the database.  
    The default value of _db\_host_ is "localhost".
-   _**db\_port**_ represents the database port that will be used by Taipy to access the database.  
    The default value of _db\_port_ is 1433.
-   _**db\_driver**_ represents the database driver that will be used by Taipy.
-   _**sqlite\_folder\_path**_ represents the path to the folder that contains the SQLite database file. The default value of _sqlite\_folder\_path_ is the current working folder.
-   _**sqlite\_file\_extension**_ represents the file extension of the SQLite database file. The default value of _sqlite\_file\_extension_ is ".db".
-   _**db\_extra\_args**_ is a dictionary of additional arguments that need to be passed into the database connection string.
-   _**exposed\_type**_ indicates the data type returned when reading the data node (more examples of reading from a SQL data node with different _exposed\_type_ are available in the [Read / Write a data node](https://docs.taipy.io/en/latest/manuals/core/entities/data-node-mgt/#sql) documentation):
    -   By default, _exposed\_type_ is "pandas", and the data node reads the data as a Pandas DataFrame (`pandas.DataFrame`) when execute the _read\_query_.
    -   If the _exposed\_type_ provided is "modin", the data node reads the CSV file as a Modin DataFrame (`modin.pandas.DataFrame`) when execute the _read\_query_.
    -   If the _exposed\_type_ provided is "numpy", the data node reads the CSV file as a NumPy array (`numpy.ndarray`) when execute the _read\_query_.
    -   If the provided _exposed\_type_ is a custom Python class, the data node creates a list of custom objects with the given custom class. Each object represents a record in the table returned by the _read\_query_.

#### Example with a Microsoft SQL database table[¶](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#example-with-a-microsoft-sql-database-table_1 "Permanent link")

First, let's take a look at an example on how to configure a _SQL table_ data node with the database engine is `mssql` (short for Microsoft SQL).

<table><tbody><tr><td><div><pre><span></span><span> 1</span>
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
<span>19</span>
<span>20</span>
<span>21</span></pre></div></td><td><div><pre id="__code_7"><span></span><code><span>from</span> <span>taipy</span> <span>import</span> <span>Config</span>
<span>import</span> <span>pandas</span> <span>as</span> <span>pd</span>

<span>def</span> <span>write_query_builder</span><span>(</span><span>data</span><span>:</span> <span>pd</span><span>.</span><span>DataFrame</span><span>):</span>
    <span>insert_data</span> <span>=</span> <span>data</span><span>[[</span><span>"date"</span><span>,</span> <span>"nb_sales"</span><span>]]</span><span>.</span><span>to_dict</span><span>(</span><span>"records"</span><span>)</span>
    <span>return</span> <span>[</span>
        <span>"DELETE FROM sales"</span><span>,</span>
        <span>(</span><span>"INSERT INTO sales VALUES (:date, :nb_sales)"</span><span>,</span> <span>insert_data</span><span>)</span>
    <span>]</span>

<span>sales_history_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_sql_data_node</span><span>(</span>
    <span>id</span><span>=</span><span>"sales_history"</span><span>,</span>
    <span>db_username</span><span>=</span><span>"admin"</span><span>,</span>
    <span>db_password</span><span>=</span><span>"password"</span><span>,</span>
    <span>db_name</span><span>=</span><span>"taipy"</span><span>,</span>
    <span>db_engine</span><span>=</span><span>"mssql"</span><span>,</span>
    <span>read_query</span><span>=</span><span>"SELECT * from sales"</span><span>,</span>
    <span>write_query_builder</span><span>=</span><span>write_query_builder</span><span>,</span>
    <span>db_driver</span><span>=</span><span>"ODBC Driver 17 for SQL Server"</span><span>,</span>
    <span>db_extra_args</span><span>=</span><span>{</span><span>"TrustServerCertificate"</span><span>:</span> <span>"yes"</span><span>},</span>
<span>)</span>
</code></pre></div></td></tr></tbody></table>

In this example, we configure a _SQL_ data node with the id "sales\_history". Its scope is the default value `SCENARIO`. The database username is "admin", the user's password is "password" (refer to [advance configuration](https://docs.taipy.io/en/latest/manuals/core/config/advanced-config/) to pass password as an environment variable), and the database name is "taipy". The read query will be "SELECT \* from sales".

The _write\_query\_builder_ is a callable function that takes in a `pandas.DataFrame` and return a list of queries. The first query will delete all the data in the table "sales", and the second query is a prepared statement that takes in two values, which is the data from the two columns "date" and "nb\_sales" in the `pandas.DataFrame`. Since this is a prepared statement, it must be passed as a tuple with the first element being the query and the second element being the data.

The very first parameter of _write\_query\_builder_ (i.e. data) is expected to have the same type as the return type of the task function whose output is the data node. In this example, the task function must return a `pandas.DataFrame`, since the data parameter of the _write\_query\_builder_ is a `pandas.DataFrame`.

#### Example with a SQLite database table[¶](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#example-with-a-sqlite-database-table_1 "Permanent link")

In the next example, we configure a _SQL table_ data node with the database engine is `sqlite`.

<table><tbody><tr><td><div><pre><span></span><span> 1</span>
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
<span>19</span></pre></div></td><td><div><pre id="__code_8"><span></span><code><span>from</span> <span>taipy</span> <span>import</span> <span>Config</span>
<span>import</span> <span>pandas</span> <span>as</span> <span>pd</span>

<span>def</span> <span>write_query_builder</span><span>(</span><span>data</span><span>:</span> <span>pd</span><span>.</span><span>DataFrame</span><span>):</span>
    <span>insert_data</span> <span>=</span> <span>data</span><span>[[</span><span>"date"</span><span>,</span> <span>"nb_sales"</span><span>]]</span><span>.</span><span>to_dict</span><span>(</span><span>"records"</span><span>)</span>
    <span>return</span> <span>[</span>
        <span>"DELETE FROM sales"</span><span>,</span>
        <span>(</span><span>"INSERT INTO sales VALUES (:date, :nb_sales)"</span><span>,</span> <span>insert_data</span><span>)</span>
    <span>]</span>

<span>sales_history_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_sql_data_node</span><span>(</span>
    <span>id</span><span>=</span><span>"sales_history"</span><span>,</span>
    <span>db_name</span><span>=</span><span>"taipy"</span><span>,</span>
    <span>db_engine</span><span>=</span><span>"sqlite"</span><span>,</span>
    <span>read_query</span><span>=</span><span>"SELECT * from sales"</span><span>,</span>
    <span>write_query_builder</span><span>=</span><span>write_query_builder</span><span>,</span>
    <span>sqlite_folder_path</span><span>=</span><span>"database"</span><span>,</span>
    <span>sqlite_file_extension</span><span>=</span><span>".sqlite3"</span><span>,</span>
<span>)</span>
</code></pre></div></td></tr></tbody></table>

Here, the database username and password are unnecessary. The folder containing SQLite database file is "database", with the file extension is ".sqlite3". Since the database name is "taipy", this SQL table data node will read and write to the SQLite database stored at "database/taipy.sqlite3".

### JSON[¶](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#json "Permanent link")

A [`JSONDataNode`](https://docs.taipy.io/en/latest/manuals/reference/taipy.core.data.JSONDataNode) is a predefined data node that models JSON file data. The [`Config.configure_json_data_node()`](https://docs.taipy.io/en/latest/manuals/reference/taipy.config.Config/index.html#taipy.config.Config.configure_json_data_node) method adds a new _JSON_ data node configuration. In addition to the generic parameters described in the [Data node configuration](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/) section, the following parameters can be provided:

-   _**default\_path**_ represents the default file path used to read and write data pointed by the data nodes instantiated from the _json_ configuration.  
    It is used to populate the path property of the entities (_json_ data nodes) instantiated from the _json_ data node configuration. That means by default all the entities (_json_ data nodes) instantiated from the same _json_ configuration will inherit/share the same _json_ file provided in the default\_path. To avoid this, the path property of a _json_ data node entity can be changed at runtime right after its instantiation.  
    
-   _**encoding**_ represents the encoding of the JSON file.  
    The default value of _encoding_ is "utf-8".
    
-   _**encoder**_ and _**decoder**_ parameters are optional parameters representing the encoder (json.JSONEncoder) and decoder (json.JSONDecoder) used to serialize and deserialize JSON data.  
    Check out [JSON Encoders and Decoders](https://docs.python.org/3/library/json.html#encoders-and-decoders) documentation for more details.
    

<table><tbody><tr><td></td><td><div><pre id="__code_9"><span></span><code><span>from</span> <span>taipy</span> <span>import</span> <span>Config</span>

<span>hist_temp_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_json_data_node</span><span>(</span>
    <span>id</span><span>=</span><span>"historical_temperature"</span><span>,</span>
    <span>default_path</span><span>=</span><span>"path/hist_temp.json"</span><span>,</span>
<span>)</span>
</code></pre></div></td></tr></tbody></table>

In this example, we configure a JSON data node. The _id_ argument is "historical\_temperature". Its _scope_ is `SCENARIO` (default value), and the path points to _hist\_temp.json_ file.

Without specific _encoder_ and _decoder_ parameters, _hist\_temp\_cfg_ will use default encoder and decoder provided by Taipy, which can encode and decode Python [`enum.Enum`](https://docs.python.org/3/library/enum.html), [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime-objects), [`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#timedelta-objects), and [dataclass](https://docs.python.org/3/library/dataclasses.html) object.

<table><tbody><tr><td><div><pre><span></span><span> 1</span>
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
<span>19</span>
<span>20</span>
<span>21</span>
<span>22</span>
<span>23</span>
<span>24</span>
<span>25</span>
<span>26</span>
<span>27</span>
<span>28</span>
<span>29</span>
<span>30</span>
<span>31</span>
<span>32</span>
<span>33</span>
<span>34</span>
<span>35</span>
<span>36</span>
<span>37</span></pre></div></td><td><div><pre id="__code_10"><span></span><code><span>from</span> <span>taipy</span> <span>import</span> <span>Config</span>
<span>import</span> <span>json</span>


<span>class</span> <span>SaleRow</span><span>:</span>
    <span>date</span><span>:</span> <span>str</span>
    <span>nb_sales</span><span>:</span> <span>int</span>


<span>class</span> <span>SaleRowEncoder</span><span>(</span><span>json</span><span>.</span><span>JSONEncoder</span><span>):</span>
    <span>def</span> <span>default</span><span>(</span><span>self</span><span>,</span> <span>obj</span><span>):</span>
        <span>if</span> <span>isinstance</span><span>(</span><span>obj</span><span>,</span> <span>SaleRow</span><span>):</span>
            <span>return</span> <span>{</span>
                <span>'__type__'</span><span>:</span> <span>"SaleRow"</span><span>,</span>
                <span>'date'</span><span>:</span> <span>obj</span><span>.</span><span>date</span><span>,</span>
                <span>'nb_sales'</span><span>:</span> <span>obj</span><span>.</span><span>nb_sales</span><span>}</span>
        <span>return</span> <span>json</span><span>.</span><span>JSONEncoder</span><span>.</span><span>default</span><span>(</span><span>self</span><span>,</span> <span>obj</span><span>)</span>


<span>class</span> <span>SaleRowDecoder</span><span>(</span><span>json</span><span>.</span><span>JSONDecoder</span><span>):</span>
    <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>,</span> <span>*</span><span>args</span><span>,</span> <span>**</span><span>kwargs</span><span>):</span>
        <span>json</span><span>.</span><span>JSONDecoder</span><span>.</span><span>__init__</span><span>(</span><span>self</span><span>,</span>
                                  <span>object_hook</span><span>=</span><span>self</span><span>.</span><span>object_hook</span><span>,</span>
                                  <span>*</span><span>args</span><span>,</span>
                                  <span>**</span><span>kwargs</span><span>)</span>

    <span>def</span> <span>object_hook</span><span>(</span><span>self</span><span>,</span> <span>d</span><span>):</span>
        <span>if</span> <span>d</span><span>.</span><span>get</span><span>(</span><span>'__type__'</span><span>)</span> <span>==</span> <span>"SaleRow"</span><span>:</span>
            <span>return</span> <span>SaleRow</span><span>(</span><span>date</span><span>=</span><span>d</span><span>[</span><span>'date'</span><span>],</span> <span>nb_sales</span><span>=</span><span>d</span><span>[</span><span>'nb_sales'</span><span>])</span>
        <span>return</span> <span>d</span>


<span>sales_history_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_json_data_node</span><span>(</span>
    <span>id</span><span>=</span><span>"sales_history"</span><span>,</span>
    <span>path</span><span>=</span><span>"path/sales.json"</span><span>,</span>
    <span>encoder</span><span>=</span><span>SaleRowEncoder</span><span>,</span>
    <span>decoder</span><span>=</span><span>SaleRowDecoder</span><span>)</span>
</code></pre></div></td></tr></tbody></table>

In this next example, we configure a [`JSONDataNode`](https://docs.taipy.io/en/latest/manuals/reference/taipy.core.data.JSONDataNode) with a custom JSON _encoder_ and _decoder_:

-   In lines 5-7, we define a custom class `SaleRow`, representing data in a JSON object.
    
-   In lines 9-30, we define a custom encoder and decoder for the `SaleRow` class.
    
    -   When [writing a JSONDataNode](https://docs.taipy.io/en/latest/manuals/core/entities/data-node-mgt/#write-data-node), the `SaleRowEncoder` encodes a `SaleRow` object in JSON format. For example, after the creation of the scenario `scenario`,
        
        ```
        <span></span><code><span>scenario</span><span>.</span><span>sales_history</span><span>.</span><span>write</span><span>(</span><span>SaleRow</span><span>(</span><span>"12/24/2018"</span><span>,</span> <span>1550</span><span>))</span>
        </code>
        ```
        
        the previous code writes the following object
        
        ```
        <span></span><code><span>{</span>
        <span>    </span><span>"__type__"</span><span>:</span><span> </span><span>"SaleRow"</span><span>,</span>
        <span>    </span><span>"date"</span><span>:</span><span> </span><span>"12/24/2018"</span><span>,</span>
        <span>    </span><span>"nb_sales"</span><span>:</span><span> </span><span>1550</span><span>,</span>
        <span>}</span>
        </code>
        ```
        
        to the file _path/sales.json_.
    -   When reading a JSONDataNode, the `SaleRowDecoder` converts a JSON object with the attribute `__type__` into a Python object corresponding to the attribute's value. In this example, the "SaleRow"\` data class.
-   In lines 33-37, we create a JSON data node configuration. The _id_ identifier is "sales\_history". The default `SCENARIO` scope is used. The encoder and decoder are the custom encoder and decoder defined above.
    

### Parquet[¶](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#parquet "Permanent link")

Note

-   To be able to use a [`ParquetDataNode`](https://docs.taipy.io/en/latest/manuals/reference/taipy.core.data.ParquetDataNode), you need to install optional dependencies with `pip install taipy[parquet]`.

A [`ParquetDataNode`](https://docs.taipy.io/en/latest/manuals/reference/taipy.core.data.ParquetDataNode) data node is a specific data node used to model [Parquet](https://parquet.apache.org/) file data. The [`Config.configure_parquet_data_node()`](https://docs.taipy.io/en/latest/manuals/reference/taipy.config.Config/index.html#taipy.config.Config.configure_parquet_data_node) adds a new _Parquet_ data node configuration. In addition to the generic parameters described in the [Data node configuration](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/) section, the following parameters can be provided:

-   _**default\_path**_ represents the default file path used to read and write data pointed by the data nodes instantiated from the _Parquet_ configuration.  
    It is used to populate the path property of the entities (_Parquet_ data nodes) instantiated from the _Parquet_ data node configuration. That means by default all the entities (_Parquet_ data nodes) instantiated from the same _Parquet_ configuration will inherit/share the same _Parquet_ file provided in the default\_path. To avoid this, the path property of a _Parquet_ data node entity can be changed at runtime right after its instantiation.  
    
-   _**engine**_ represents the Parquet library to use.  
    Possible values are _"fastparquet"_ or _"pyarrow"_. The default value is _"pyarrow"_.
    
-   _**compression**_ is the name of the compression to use.  
    Possible values are _"snappy"_, _"gzip"_, _"brotli"_ and None. The default value is _"snappy"_. Use None for no compression.
    
-   _**read\_kwargs**_ is a dictionary of additional parameters passed to the [`pandas.read_parquet`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_parquet.html) method.
    
-   _**write\_kwargs**_ is a dictionary of additional parameters passed to the [`pandas.DataFrame.to_parquet`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_parquet.html) method.  
    The parameters _read\_kwargs_ and _write\_kwargs_ have a **higher precedence** than the top-level parameters (_engine_ and _compression_) which are also passed to Pandas. Passing `read_kwargs= {"engine": "fastparquet", "compression": "gzip"}` will override the _engine_ and _compression_ properties of the data node.
    

-   _**exposed\_type**_ indicates the data type returned when reading the data node (more examples of reading from Parquet data node with different _exposed\_type_ are available on [Read / Write a data node](https://docs.taipy.io/en/latest/manuals/core/entities/data-node-mgt/#parquet) documentation):
    -   By default, _exposed\_type_ is "pandas", and the data node reads the Parquet file as a Pandas DataFrame (`pandas.DataFrame`) when executing the read method.
    -   If the _exposed\_type_ provided is "modin", the data node reads the Parquet file as a Modin DataFrame (`modin.pandas.DataFrame`) when executing the read method.
    -   If the _exposed\_type_ provided is "numpy", the data node reads the Parquet file as a NumPy array (`numpy.ndarray`) when executing the read method.
    -   If the provided _exposed\_type_ is a `Callable`, the data node creates a list of objects as returned by the `Callable`. Each object represents a record in the Parquet file. The Parquet file is read as a `pandas.DataFrame` and each row of the DataFrame is passed to the Callable as keyword arguments where the key is the column name, and the value is the corresponding value for that row.

<table><tbody><tr><td></td><td><div><pre id="__code_13"><span></span><code><span>from</span> <span>taipy</span> <span>import</span> <span>Config</span>

<span>temp_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_parquet_data_node</span><span>(</span>
    <span>id</span><span>=</span><span>"historical_temperature"</span><span>,</span>
    <span>default_path</span><span>=</span><span>"path/hist_temp.parquet"</span><span>)</span>
</code></pre></div></td></tr></tbody></table>

In lines 3-5, we configure a basic Parquet data node. The only two required parameters are _id_ and _default\_path_.

<table><tbody><tr><td><div><pre><span></span><span> 1</span>
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
<span>13</span></pre></div></td><td><div><pre id="__code_14"><span></span><code tabindex="0"><span>from</span> <span>taipy</span> <span>import</span> <span>Config</span>

<span>read_kwargs</span> <span>=</span> <span>{</span><span>"filters"</span><span>:</span> <span>[(</span><span>"log_level"</span><span>,</span> <span>"in"</span><span>,</span> <span>{</span><span>"ERROR"</span><span>,</span> <span>"CRITICAL"</span><span>})]}</span>
<span>write_kwargs</span> <span>=</span> <span>{</span><span>"partition_cols"</span><span>:</span> <span>[</span><span>"log_level"</span><span>],</span> <span>"compression"</span><span>:</span> <span>None</span><span>}</span>

<span>log_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_parquet_data_node</span><span>(</span>
    <span>id</span><span>=</span><span>"log_history"</span><span>,</span>
    <span>default_path</span><span>=</span><span>"path/hist_log.parquet"</span><span>,</span>
    <span>engine</span><span>=</span><span>"pyarrow"</span><span>,</span> <span># default</span>
    <span>compression</span><span>=</span><span>"snappy"</span><span>,</span> <span># default, but overridden by the key in write_kwargs</span>
    <span>exposed_type</span><span>=</span><span>"modin"</span><span>,</span>
    <span>read_kwargs</span><span>=</span><span>read_kwargs</span><span>,</span>
    <span>write_kwargs</span><span>=</span><span>write_kwargs</span><span>)</span>
</code></pre></div></td></tr></tbody></table>

In this larger example, we illustrate some specific benefits of using ParquetDataNode for storing tabular data. This time, we provide the _read\_kwargs_ and _write\_kwargs_ dictionary parameters to be passed as keyword arguments to [`pandas.read_parquet`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_parquet.html) and [`pandas.DataFrame.to_parquet`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_parquet.html) respectively.

Here, the dataset is partitioned (using _partition\_cols_ on line 4) by the "log\_level" column when written to disk. Also, filtering is performed (using _filters_ on line 3) to read only the rows where the "log\_level" column value is either "ERROR" or "CRITICAL", speeding up the read, especially when dealing with a large amount of data.

Note that even though line 10 specifies the _compression_ as "snappy", since the "compression" key was also provided in the _write\_kwargs_ dictionary on line 4, the last value is used, hence the _compression_ is None.

### Mongo Collection[¶](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#mongo-collection "Permanent link")

Note

-   To be able to use a [`MongoCollectionDataNode`](https://docs.taipy.io/en/latest/manuals/reference/taipy.core.data.MongoCollectionDataNode), you need to install optional dependencies with `pip install taipy[mongo]`.

A [`MongoCollectionDataNode`](https://docs.taipy.io/en/latest/manuals/reference/taipy.core.data.MongoCollectionDataNode) is a specific data node used to model data stored in a Mongo collection. To add a new _mongo\_collection_ data node configuration, the [`Config.configure_mongo_collection_data_node()`](https://docs.taipy.io/en/latest/manuals/reference/taipy.config.Config/index.html#taipy.config.Config.configure_mongo_collection_data_node) method can be used. In addition to the generic parameters described in the [Data node configuration](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/) section, multiple parameters can be provided.

-   _**db\_name**_ represents the name of the database in MongoDB.
-   _**collection\_name**_ represents the name of the data collection in the database.
-   _**custom\_document**_ represents the custom class used to store, encode, and decode data when reading and writing to a Mongo collection. The data returned by the read method is a list of custom\_document object(s), and the data passed as a parameter of the write method is a (list of) custom\_document object(s). The custom\_document can have:
    -   An optional `decoder()` method to decode data in the Mongo collection to a custom object when reading.
    -   An optional `encoder()` method to encode the object's properties to the Mongo collection format when writing.
-   _**db\_username**_ represents the username to be used to access MongoDB.
-   _**db\_password**_ represents the user's password to be used by Taipy to access MongoDB.
-   _**db\_port**_ represents the database port to be used to access MongoDB.  
    The default value of _db\_port_ is 27017.
-   _**db\_host**_ represents the database host to be used to access MongoDB.  
    The default value of _db\_host_ is "localhost".

<table><tbody><tr><td></td><td><div><pre id="__code_15"><span></span><code><span>from</span> <span>taipy</span> <span>import</span> <span>Config</span>

<span>historical_data_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_mongo_collection_data_node</span><span>(</span>
    <span>id</span><span>=</span><span>"historical_data"</span><span>,</span>
    <span>db_username</span><span>=</span><span>"admin"</span><span>,</span>
    <span>db_password</span><span>=</span><span>"pa$$w0rd"</span><span>,</span>
    <span>db_name</span><span>=</span><span>"taipy"</span><span>,</span>
    <span>collection_name</span><span>=</span><span>"historical_data_set"</span><span>,</span>
<span>)</span>
</code></pre></div></td></tr></tbody></table>

In this example, we configure a _mongo\_collection_ data node with the id "historical\_data":

-   Its scope is the default value `SCENARIO`.
-   The database username is "admin", the user's password is "pa$$w0rd"
-   The database name is "taipy"
-   The collection name is "historical\_data\_set".
-   Without being specified, the custom document class is defined as `taipy.core.MongoDefaultDocument`.

<table><tbody><tr><td><div><pre><span></span><span> 1</span>
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
<span>19</span>
<span>20</span>
<span>21</span>
<span>22</span>
<span>23</span>
<span>24</span>
<span>25</span>
<span>26</span>
<span>27</span>
<span>28</span>
<span>29</span></pre></div></td><td><div><pre id="__code_16"><span></span><code><span>from</span> <span>taipy</span> <span>import</span> <span>Config</span>
<span>from</span> <span>datetime</span> <span>import</span> <span>datetime</span>

<span>class</span> <span>DailyMinTemp</span><span>:</span>
    <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>,</span> <span>Date</span> <span>:</span> <span>datetime</span><span>=</span><span>None</span><span>,</span> <span>Temp</span> <span>:</span> <span>float</span><span>=</span><span>None</span><span>):</span>
        <span>self</span><span>.</span><span>Date</span> <span>=</span> <span>Date</span>
        <span>self</span><span>.</span><span>Temp</span> <span>=</span> <span>Temp</span>

    <span>def</span> <span>encode</span><span>(</span><span>self</span><span>):</span>
        <span>return</span> <span>{</span>
            <span>"date"</span><span>:</span> <span>self</span><span>.</span><span>Date</span><span>.</span><span>isoformat</span><span>(),</span>
            <span>"temperature"</span><span>:</span> <span>self</span><span>.</span><span>Temp</span><span>,</span>
        <span>}</span>

    <span>@classmethod</span>
    <span>def</span> <span>decode</span><span>(</span><span>cls</span><span>,</span> <span>data</span><span>):</span>
        <span>return</span> <span>cls</span><span>(</span>
            <span>datetime</span><span>.</span><span>fromisoformat</span><span>(</span><span>data</span><span>[</span><span>"date"</span><span>]),</span>
            <span>data</span><span>[</span><span>"temperature"</span><span>],</span>
        <span>)</span>

<span>historical_data_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_mongo_collection_data_node</span><span>(</span>
    <span>id</span><span>=</span><span>"historical_data"</span><span>,</span>
    <span>db_username</span><span>=</span><span>"admin"</span><span>,</span>
    <span>db_password</span><span>=</span><span>"pa$$w0rd"</span><span>,</span>
    <span>db_name</span><span>=</span><span>"taipy"</span><span>,</span>
    <span>collection_name</span><span>=</span><span>"historical_data_set"</span><span>,</span>
    <span>custom_document</span><span>=</span><span>DailyMinTemp</span><span>,</span>
<span>)</span>
</code></pre></div></td></tr></tbody></table>

In this next example, we configure another _mongo\_collection_ data node, with the custom document is defined as `DailyMinTemp` class.

-   The custom _encode_ method encodes `datetime.datetime` to the ISO 8601 string format.
-   The corresponding _decode_ method decodes an ISO 8601 string to `datetime.datetime`.
-   The `_id` of the Mongo document is discarded.

Without these two methods, the default decoder will map the key of each document to the corresponding property of a `DailyMinTemp` object, and the default encoder will convert `DailyMinTemp` object's properties to a dictionary without any special formatting.

### Generic[¶](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#generic "Permanent link")

A [`GenericDataNode`](https://docs.taipy.io/en/latest/manuals/reference/taipy.core.data.GenericDataNode) is a specific data node used to model generic data types where the user defines the read and the write functions. The [`Config.configure_generic_data_node()`](https://docs.taipy.io/en/latest/manuals/reference/taipy.config.Config/index.html#taipy.config.Config.configure_generic_data_node) method adds a new _generic_ data node configuration. In addition to the parameters described in the [Data node configuration](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/) section, the following parameters can be provided:

-   _**read\_fct**_ represents a Python function, which is used to read the data. More optional parameters can be passed through the _**read\_fct\_args**_ parameter.
    
-   _**write\_fct**_ represents a Python function, which is used to write/serialize the data. The provided function must have at least one parameter to receive data to be written. It must be the first parameter. More optional parameters can be passed through the _**write\_fct\_args**_ parameter.
    
-   _**read\_fct\_args**_ represents the parameters passed to the _read\_fct_ to read/de-serialize the data. It must be a `List` type object.
    
-   _**write\_fct\_args**_ represents the parameters passed to the _write\_fct_ to write the data. It must be a `List` type object.
    

Note

At least one of the _read\_fct_ or _write\_fct_ is required to configure a generic data node.

<table><tbody><tr><td><div><pre><span></span><span> 1</span>
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
<span>19</span>
<span>20</span></pre></div></td><td><div><pre id="__code_17"><span></span><code><span>from</span> <span>taipy</span> <span>import</span> <span>Config</span>


<span>def</span> <span>read_text</span><span>(</span><span>path</span><span>:</span> <span>str</span><span>)</span> <span>-&gt;</span> <span>str</span><span>:</span>
    <span>with</span> <span>open</span><span>(</span><span>path</span><span>,</span> <span>'r'</span><span>)</span> <span>as</span> <span>text_reader</span><span>:</span>
        <span>data</span> <span>=</span> <span>text_reader</span><span>.</span><span>read</span><span>()</span>
    <span>return</span> <span>data</span>


<span>def</span> <span>write_text</span><span>(</span><span>data</span><span>:</span> <span>str</span><span>,</span> <span>path</span><span>:</span> <span>str</span><span>)</span> <span>-&gt;</span> <span>None</span><span>:</span>
    <span>with</span> <span>open</span><span>(</span><span>path</span><span>,</span> <span>'w'</span><span>)</span> <span>as</span> <span>text_writer</span><span>:</span>
        <span>text_writer</span><span>.</span><span>write</span><span>(</span><span>data</span><span>)</span>


<span>historical_data_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_generic_data_node</span><span>(</span>
    <span>id</span><span>=</span><span>"historical_data"</span><span>,</span>
    <span>read_fct</span><span>=</span><span>read_text</span><span>,</span>
    <span>write_fct</span><span>=</span><span>write_text</span><span>,</span>
    <span>read_fct_args</span><span>=</span><span>[</span><span>"../path/data.txt"</span><span>],</span>
    <span>write_fct_args</span><span>=</span><span>[</span><span>"../path/data.txt"</span><span>])</span>
</code></pre></div></td></tr></tbody></table>

In this small example is configured a generic data node with the id "historical\_data".

In lines 17-18, we provide two Python functions (previously defined) as _read\_fct_ and _write\_fct_ parameters to read and write the data in a text file. Note that the first parameter of _write\_fct_ is mandatory and is used to pass the data on writing.

In line 19, we provide _read\_fct\_args_ with a path to let the _read\_fct_ know where to read the data.

In line 20, we provide a list of parameters to _write\_fct\_args_ with a path to let the _write\_fct_ know where to write the data. Note that the data parameter will be automatically passed at runtime when writing the data.

The generic data node can also be used in situations requiring a specific business logic in reading or writing data, and the user can easily provide that. Follows an example using a custom delimiter when writing and reading a CSV file.

<table><tbody><tr><td><div><pre><span></span><span> 1</span>
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
<span>19</span>
<span>20</span>
<span>21</span>
<span>22</span>
<span>23</span>
<span>24</span>
<span>25</span>
<span>26</span></pre></div></td><td><div><pre id="__code_18"><span></span><code><span>import</span> <span>csv</span>
<span>from</span> <span>typing</span> <span>import</span> <span>List</span><span>,</span> <span>Iterator</span>
<span>from</span> <span>taipy</span> <span>import</span> <span>Config</span>


<span>def</span> <span>read_csv</span><span>(</span><span>path</span><span>:</span> <span>str</span><span>,</span> <span>delimiter</span><span>:</span> <span>str</span> <span>=</span> <span>","</span><span>)</span> <span>-&gt;</span> <span>Iterator</span><span>:</span>
    <span>with</span> <span>open</span><span>(</span><span>path</span><span>,</span> <span>newline</span><span>=</span><span>' '</span><span>)</span> <span>as</span> <span>csvfile</span><span>:</span>
        <span>data</span> <span>=</span> <span>csv</span><span>.</span><span>reader</span><span>(</span><span>csvfile</span><span>,</span> <span>delimiter</span><span>=</span><span>delimiter</span><span>)</span>
    <span>return</span> <span>data</span>


<span>def</span> <span>write_csv</span><span>(</span><span>data</span><span>:</span> <span>List</span><span>[</span><span>str</span><span>],</span> <span>path</span><span>:</span> <span>str</span><span>,</span> <span>delimiter</span><span>:</span> <span>str</span> <span>=</span> <span>","</span><span>)</span> <span>-&gt;</span> <span>None</span><span>:</span>
    <span>headers</span> <span>=</span> <span>[</span><span>"country_code"</span><span>,</span> <span>"country"</span><span>]</span>
    <span>with</span> <span>open</span><span>(</span><span>path</span><span>,</span> <span>'w'</span><span>)</span> <span>as</span> <span>csvfile</span><span>:</span>
        <span>writer</span> <span>=</span> <span>csv</span><span>.</span><span>writer</span><span>(</span><span>csvfile</span><span>,</span> <span>delimiter</span><span>=</span><span>delimiter</span><span>)</span>
        <span>writer</span><span>.</span><span>writerow</span><span>(</span><span>headers</span><span>)</span>
        <span>for</span> <span>row</span> <span>in</span> <span>data</span><span>:</span>
            <span>writer</span><span>.</span><span>writerow</span><span>(</span><span>row</span><span>)</span>


<span>csv_country_data_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_generic_data_node</span><span>(</span>
    <span>id</span><span>=</span><span>"csv_country_data"</span><span>,</span>
    <span>read_fct</span><span>=</span><span>read_csv</span><span>,</span>
    <span>write_fct</span><span>=</span><span>write_csv</span><span>,</span>
    <span>read_fct_args</span><span>=</span><span>[</span><span>"../path/data.csv"</span><span>,</span> <span>";"</span><span>],</span>
    <span>write_fct_args</span><span>=</span><span>[</span><span>"../path/data.csv"</span><span>,</span> <span>";"</span><span>])</span>
</code></pre></div></td></tr></tbody></table>

It is also possible to use a generic data node custom functions to perform some data preparation:

<table><tbody><tr><td><div><pre><span></span><span> 1</span>
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
<span>19</span>
<span>20</span>
<span>21</span>
<span>22</span>
<span>23</span>
<span>24</span>
<span>25</span>
<span>26</span>
<span>27</span>
<span>28</span>
<span>29</span>
<span>30</span>
<span>31</span></pre></div></td><td><div><pre id="__code_19"><span></span><code tabindex="0"><span>from</span> <span>datetime</span> <span>import</span> <span>datetime</span> <span>as</span> <span>dt</span>
<span>import</span> <span>pandas</span> <span>as</span> <span>pd</span>
<span>from</span> <span>taipy</span> <span>import</span> <span>Config</span>


<span>def</span> <span>read_csv</span><span>(</span><span>path</span><span>:</span> <span>str</span><span>)</span> <span>-&gt;</span> <span>pd</span><span>.</span><span>DataFrame</span><span>:</span>
    <span># reading a csv file, define some column types and parse a string into datetime</span>
    <span>custom_parser</span> <span>=</span> <span>lambda</span> <span>x</span><span>:</span> <span>dt</span><span>.</span><span>strptime</span><span>(</span><span>x</span><span>,</span> <span>"%Y %m </span><span>%d</span><span> %H:%M:%S"</span><span>)</span>
    <span>data</span> <span>=</span> <span>pd</span><span>.</span><span>read_csv</span><span>(</span>
        <span>path</span><span>,</span>
        <span>parse_dates</span><span>=</span><span>[</span><span>'date'</span><span>],</span>
        <span>date_parser</span><span>=</span><span>custom_parser</span><span>,</span>
        <span>dtype</span><span>=</span><span>{</span>
            <span>"name"</span><span>:</span> <span>str</span><span>,</span>
            <span>"grade"</span><span>:</span> <span>int</span>
        <span>}</span>
    <span>)</span>
    <span>return</span> <span>data</span>


<span>def</span> <span>write_csv</span><span>(</span><span>data</span><span>:</span> <span>pd</span><span>.</span><span>DataFrame</span><span>,</span> <span>path</span><span>:</span> <span>str</span><span>)</span> <span>-&gt;</span> <span>None</span><span>:</span>
    <span># dropping not a number values before writing</span>
    <span>data</span><span>.</span><span>dropna</span><span>()</span><span>.</span><span>to_csv</span><span>(</span><span>path</span><span>)</span>


<span>student_data</span> <span>=</span> <span>Config</span><span>.</span><span>configure_generic_data_node</span><span>(</span>
    <span>id</span><span>=</span><span>"student_data"</span><span>,</span>
    <span>read_fct</span><span>=</span><span>read_csv</span><span>,</span>
    <span>write_fct</span><span>=</span><span>write_csv</span><span>,</span>
    <span>read_fct_args</span><span>=</span><span>[</span><span>"../path/data.csv"</span><span>],</span>
    <span>write_fct_args</span><span>=</span><span>[</span><span>"../path/data.csv"</span><span>])</span>
</code></pre></div></td></tr></tbody></table>

### In memory[¶](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#in-memory "Permanent link")

An [`InMemoryDataNode`](https://docs.taipy.io/en/latest/manuals/reference/taipy.core.data.InMemoryDataNode) is a specific data node used to model any data in the RAM. The [`Config.configure_in_memory_data_node()`](https://docs.taipy.io/en/latest/manuals/reference/taipy.config.Config/index.html#taipy.config.Config.configure_in_memory_data_node) method is used to add a new in\_memory data node configuration. In addition to the generic parameters described in the [Data node configuration](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/) section, an optional parameter can be provided:

-   If the _**default\_data**_ is given as a parameter of the data node configuration, the data node entity is automatically written with the corresponding value (note that any serializable Python object can be used) upon its instantiation.

<table><tbody><tr><td></td><td><div><pre id="__code_20"><span></span><code><span>from</span> <span>taipy</span> <span>import</span> <span>Config</span>
<span>from</span> <span>datetime</span> <span>import</span> <span>datetime</span>

<span>date_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_in_memory_data_node</span><span>(</span>
    <span>id</span><span>=</span><span>"date"</span><span>,</span>
    <span>default_data</span><span>=</span><span>datetime</span><span>(</span><span>2022</span><span>,</span> <span>1</span><span>,</span> <span>25</span><span>))</span>
</code></pre></div></td></tr></tbody></table>

In this example, we configure an _in\_memory_ data node with the id "date". The scope is `SCENARIO` (default value), and default data is provided.

Warning

Since the data is stored in memory, it cannot be used in a multi-process environment. (See [Job configuration](https://docs.taipy.io/en/latest/manuals/core/config/job-config/#standalone) for more details).

### Amazon Web Service S3 Object[¶](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#amazon-web-service-s3-object "Permanent link")

Note

-   To be able to use a [`S3ObjectDataNode`](https://docs.taipy.io/en/latest/manuals/reference/taipy.core.data.S3ObjectDataNode), you need to install optional dependencies with `pip install taipy[s3]`.

An [`S3ObjectDataNode`](https://docs.taipy.io/en/latest/manuals/reference/taipy.core.data.S3ObjectDataNode) is a specific data node used to model data stored in an S3 bucket. To add a new _S3Object_ data node configuration, the [`Config.configure_s3_object_data_node()`](https://docs.taipy.io/en/latest/manuals/reference/taipy.config.Config/index.html#taipy.config.Config.configure_s3_object_data_node) method can be used. In addition to the generic parameters described in the [Data node configuration](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/) section, multiple parameters can be provided.

-   _**aws\_access\_key**_ represents the Amazon Web Services (AWS) identity account.
-   _**aws\_secret\_access\_key**_ represents the AWS access key to authenticate programmatic requests.
-   _**aws\_region**_ represnets the geographic area where the AWS infrastructure is located.
-   _**aws\_s3\_bucket\_name**_ represnts the name of the AWS S3 bucket.
-   _**aws\_s3\_object\_key**_ represents the name of the object (file) that needs to be read or written.
-   _**aws\_s3\_object\_parameters**_ represents additional arguments to be passed to interact with AWS.

In this example, we configure an _s3\_object_ data node with the id "my\_s3\_object":

-   Its scope is the default value `SCENARIO`.
-   The object\_key name is "taipy\_object".
-   An additional argument is passed to the AWS S3 to set the max age of the cache.

<table><tbody><tr><td></td><td><div><pre id="__code_21"><span></span><code><span>from</span> <span>taipy</span> <span>import</span> <span>Config</span>

<span>s3_object_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_s3_object_data_node</span><span>(</span>
    <span>id</span><span>=</span><span>"my_s3_object"</span><span>,</span>
    <span>aws_access_key</span><span>=</span><span>"YOUR AWS ACCESS KEY"</span><span>,</span>
    <span>aws_secret_access_key</span><span>=</span><span>"YOUR AWS SECRET ACCESS KEY"</span><span>,</span>
    <span>aws_s3_bucket_name</span><span>=</span><span>"YOUR AWS BUCKET NAME"</span><span>,</span>
    <span>aws_s3_object_key</span><span>=</span><span>"taipy_object"</span><span>,</span>
    <span>aws_s3_object_parameters</span> <span>=</span> <span>{</span><span>'CacheControl'</span><span>:</span> <span>'max-age=86400'</span><span>}</span>
<span>)</span>
</code></pre></div></td></tr></tbody></table>

## Default data node configuration[¶](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#default-data-node-configuration "Permanent link")

By default, if there is no information provided when configuring a datanode (except for the mandatory _**id**_), the [`Config.configure_data_node()`](https://docs.taipy.io/en/latest/manuals/reference/taipy.config.Config/index.html#taipy.config.Config.configure_data_node) method will return a _pickle_ data node configuration with the [`Scope`](https://docs.taipy.io/en/latest/manuals/reference/taipy.config.Scope) is set to `SCENARIO`.

To override the default data node configuration, one can use the [`Config.set_default_data_node_configuration()`](https://docs.taipy.io/en/latest/manuals/reference/taipy.config.Config/index.html#taipy.config.Config.set_default_data_node_configuration) method. Then, a new data node configuration will:

-   have the same properties as the default data node configuration if the _**storage\_type**_ is the same as the default one.
-   ignore the default data node configuration if the _**storage\_type**_ is different from the default one.

<table><tbody><tr><td><div><pre><span></span><span> 1</span>
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
<span>19</span>
<span>20</span>
<span>21</span>
<span>22</span></pre></div></td><td><div><pre id="__code_22"><span></span><code tabindex="0"><span>from</span> <span>taipy</span> <span>import</span> <span>Config</span><span>,</span> <span>Scope</span>

<span>Config</span><span>.</span><span>set_default_data_node_configuration</span><span>(</span>
    <span>storage_type</span><span>=</span><span>"sql_table"</span><span>,</span>
    <span>db_username</span><span>=</span><span>"username"</span><span>,</span>
    <span>db_password</span><span>=</span><span>"p4$$w0rD"</span><span>,</span>
    <span>db_name</span><span>=</span><span>"sale_db"</span><span>,</span>
    <span>db_engine</span><span>=</span><span>"mssql"</span><span>,</span>
    <span>table_name</span><span>=</span><span>"products"</span><span>,</span>
    <span>db_host</span><span>=</span><span>"localhost"</span><span>,</span>
    <span>db_port</span><span>=</span><span>1437</span><span>,</span>
    <span>db_driver</span><span>=</span><span>"ODBC Driver 17 for SQL Server"</span><span>,</span>
    <span>db_extra_args</span><span>=</span><span>{</span><span>"TrustServerCertificate"</span><span>:</span> <span>"yes"</span><span>},</span>
    <span>scope</span><span>=</span><span>Scope</span><span>.</span><span>GLOBAL</span><span>,</span>
<span>)</span>

<span>products_data_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>id</span><span>=</span><span>"products_data"</span><span>)</span>
<span>users_data_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>id</span><span>=</span><span>"users_data"</span><span>,</span> <span>table_name</span><span>=</span><span>"users"</span><span>)</span>
<span>retail_data_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>id</span><span>=</span><span>"retail_data"</span><span>,</span> <span>storage_type</span><span>=</span><span>"sql_table"</span><span>,</span> <span>table_name</span><span>=</span><span>"retail_data"</span><span>)</span>
<span>wholesale_data_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_sql_table_data_node</span><span>(</span><span>id</span><span>=</span><span>"wholesale_data"</span><span>,</span> <span>table_name</span><span>=</span><span>"wholesale_data"</span><span>)</span>

<span>forecast_data_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node</span><span>(</span><span>id</span><span>=</span><span>"forecast_data"</span><span>,</span> <span>storage_type</span><span>=</span><span>"csv"</span><span>,</span> <span>default_path</span><span>=</span><span>"forecast.csv"</span><span>)</span>
</code></pre></div></td></tr></tbody></table>

We override the default data node configuration by a SQL table data node configuration in the previous code example, providing all necessary properties for a SQL table data node in lines 3-14.

Then we configure 5 data nodes:

-   Line 16 configures a SQL Table data node `products_data_cfg`. By providing only the _**id**_, `products_data_cfg` has the exact same properties as the default data node configuration as above, which reads and writes to the "products" table.
-   Line 17 configures a SQL Table data node `users_data_cfg`. By also providing `table_name="users"`, this data node reads and writes to the "users" table.
-   Lines 18 and 19 configure 2 SQL Table data nodes, one using [`Config.configure_data_node()`](https://docs.taipy.io/en/latest/manuals/reference/taipy.config.Config/index.html#taipy.config.Config.configure_data_node) with `storage_type="sql_table"`, one using [`Config.configure_sql_table_data_node()`](https://docs.taipy.io/en/latest/manuals/reference/taipy.config.Config/index.html#taipy.config.Config.configure_sql_table_data_node). Since both have the same _**storage\_type**_ as the default data node configuration, both have the same properties except for the table name.
-   Line 21 configures a CSV data node `forecast_data_cfg`. Since the _**storage\_type**_ is `"csv"`, which is different from the `"sql_table"` configured in line 9, the default data node configuration is ignored. Therefore, the scope of `forecast_data_cfg` is `SCENARIO` by default.

## Configure a data node from another configuration[¶](https://docs.taipy.io/en/latest/manuals/core/config/data-node-config/#configure-a-data-node-from-another-configuration "Permanent link")

Taipy also provides the possibility to use an existing configuration as a scaffold to configure a new data node. This can be useful when the application has a lot of data nodes with similar properties.

To utilize the information of an existing configuration to create a new data node configuration, one can use the [`Config.configure_data_node_from()`](https://docs.taipy.io/en/latest/manuals/reference/taipy.config.Config/index.html#taipy.config.Config.configure_data_node_from) method. This method accepts the following parameters:

-   _**source\_configuration**_ is a mandatory parameter representing the source data node configuration.
-   _**id**_ represents the unique mandatory identifier of the new data node configuration.
-   Any other attribute can be provided through the parameter _**properties**_, a kwargs dictionary accepting any number of custom parameters (the scope, the validity period, a description, a label, a tag, etc.)  
    This _properties_ dictionary will override any attribute of the source data node configuration if provided.

<table><tbody><tr><td><div><pre><span></span><span> 1</span>
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
<span>19</span>
<span>20</span>
<span>21</span>
<span>22</span>
<span>23</span>
<span>24</span>
<span>25</span>
<span>26</span>
<span>27</span>
<span>28</span>
<span>29</span>
<span>30</span>
<span>31</span>
<span>32</span>
<span>33</span></pre></div></td><td><div><pre id="__code_23"><span></span><code><span>from</span> <span>taipy</span> <span>import</span> <span>Config</span><span>,</span> <span>Scope</span>

<span>products_data_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_sql_table_data_node</span><span>(</span>
    <span>id</span><span>=</span><span>"products_data"</span><span>,</span>
    <span>db_username</span><span>=</span><span>"foo"</span><span>,</span>
    <span>db_password</span><span>=</span><span>"bar"</span><span>,</span>
    <span>db_name</span><span>=</span><span>"db"</span><span>,</span>
    <span>db_engine</span><span>=</span><span>"mssql"</span><span>,</span>
    <span>db_host</span><span>=</span><span>"localhost"</span><span>,</span>
    <span>db_port</span><span>=</span><span>1437</span><span>,</span>
    <span>db_driver</span><span>=</span><span>"ODBC Driver 17 for SQL Server"</span><span>,</span>
    <span>db_extra_args</span><span>=</span><span>{</span><span>"TrustServerCertificate"</span><span>:</span> <span>"yes"</span><span>},</span>
    <span>table_name</span><span>=</span><span>"products"</span><span>,</span>
<span>)</span>

<span>users_data_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node_from</span><span>(</span>
    <span>source_configuration</span><span>=</span><span>products_data_cfg</span><span>,</span>
    <span>id</span><span>=</span><span>"users_data"</span><span>,</span>
    <span>scope</span><span>=</span><span>Scope</span><span>.</span><span>GLOBAL</span><span>,</span>
    <span>table_name</span><span>=</span><span>"users"</span><span>,</span>
<span>)</span>

<span>retail_data_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node_from</span><span>(</span>
    <span>source_configuration</span><span>=</span><span>products_data_cfg</span><span>,</span>
    <span>id</span><span>=</span><span>"retail_data"</span><span>,</span>
    <span>table_name</span><span>=</span><span>"retail_data"</span><span>,</span>
<span>)</span>

<span>wholesale_data_cfg</span> <span>=</span> <span>Config</span><span>.</span><span>configure_data_node_from</span><span>(</span>
    <span>source_configuration</span><span>=</span><span>products_data_cfg</span><span>,</span>
    <span>id</span><span>=</span><span>"wholesale_data"</span><span>,</span>
    <span>table_name</span><span>=</span><span>"wholesale_data"</span><span>,</span>
<span>)</span>
</code></pre></div></td></tr></tbody></table>

In this example, we first configure the `product_data_cfg` SQL table data node with all necessary properties in lines 3-14.

Then we configure 3 similar data nodes, `users_data_cfg`, `retail_data_cfg`, and `wholesale_data_cfg` in lines 16-33, by using the [`Config.configure_data_node_from()`](https://docs.taipy.io/en/latest/manuals/reference/taipy.config.Config/index.html#taipy.config.Config.configure_data_node_from) method with `product_data_cfg` as the source configuration, only changing the table name and the scope of the new data nodes.

[The next section introduces the task configuration](https://docs.taipy.io/en/latest/manuals/core/config/task-config/).