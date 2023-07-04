# SqlAlchemy

## So what would be the main features when importing `sqlalchemy`?

When you import `sqlalchemy`, you get access to the core functionality of the 
SQLAlchemy library, which includes:

+ Creating database tables and columns using the `Table` and `Column` classes
+ Defining relationships between tables using foreign keys and ForeignKey constraints
+ Executing SQL statements using the `create_engine` and `execute` functions
+ Interacting with databases using the `Connection` and `Transaction` objects
+ Generating SQL statements using the SQL expression language
+ Working with data types and type conversion using the `types` module
+ Managing database metadata and schema using the `MetaData` and `Schema` classes

With the `sqlalchemy` module, you have fine-grained control over the low-level 
details of working with databases. This is useful when you need to execute 
custom or complex SQL statements, or when you're working with a database that 
doesn't have a straightforward object-relational mapping.

However, if you're working with a more conventional database schema and want 
to use a higher-level object-relational mapper (ORM), you should import 
`sqlalchemy.orm` instead. The `sqlalchemy.orm` module builds on top of 
sqlalchemy to provide a higher-level API for interacting with databases 
using Python objects.


## What can I import from `sqlalchemy`?

When you import sqlalchemy, you get access to the core SQLAlchemy library, 
which provides low-level database abstractions and SQL expression language 
constructs. Here are some of the main features that you can import from sqlalchemy:

**create_engine**: A function that creates a new database engine object. You 
can use `create_engine` to specify the database URL, which includes the 
database type, location, and authentication information.

**Table**: A class that represents a database table. You can use `Table` to 
define the structure of a table, including its columns and constraints.

**Column**: A class that represents a database column. You can use `Column` 
to define the type and properties of a column.

**ForeignKey**: A class that represents a foreign key constraint. You can use 
ForeignKey to define a relationship between two tables.

**Index**: A class that represents a database index. You can use `Index` to 
create an index on one or more columns.

**MetaData**: A class that represents metadata about a database, such as the 
tables and columns that are defined in it. You can use MetaData to define the 
structure of a database without creating actual tables.

**select**: A function that creates a new SQL `SELECT` statement. You can use 
select to query data from a table or multiple tables.

**insert**: A function that creates a new SQL `INSERT` statement. You can use 
insert to insert data into a table.

**update**: A function that creates a new SQL `UPDATE` statement. You can use 
update to update data in a table.

**delete**: A function that creates a new SQL `DELETE` statement. You can use 
delete to delete data from a table.

**and_**, **or_**, **not_**: Functions that create logical operators that can 
be used in SQL expressions. You can use these functions to construct complex queries.

These are just a few examples of the features that you can import from 
`sqlalchemy`. The sqlalchemy module provides a powerful set of low-level 
abstractions for working with databases, and is designed to be flexible and 
extensible to support a wide range of use cases.
