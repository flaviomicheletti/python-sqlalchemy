# SqlAlchemy


## sqlalchemy and sqlalchemy.orm

In my code I can import both things from `sqlalchemy` and `sqlalchemy.orm`. 
What would be the difference between one and the other?

- `sqlalchemy` provides the core functionality of SQLAlchemy, such as defining 
database tables, columns, and relationships, as well as creating and executing 
SQL statements.

- `sqlalchemy.orm` provides a higher-level object-relational mapper (ORM) that 
sits on top of sqlalchemy and allows you to work with database tables as if 
they were regular Python objects. The ORM provides a more convenient way to 
interact with the database and can handle complex relationships between tables.

In other words, `sqlalchemy` is the low-level interface for working with 
databases, while sqlalchemy.orm provides a higher-level API for working with 
objects that represent database rows.

To use the ORM functionality of SQLAlchemy, you need to create a session 
object using sqlalchemy.orm.sessionmaker and use that session to interact 
with the database. The session provides a high-level interface for querying, 
inserting, updating, and deleting database rows, and takes care of managing 
transactions and session state.

If you only need to execute simple SQL statements, such as creating tables or
inserting data, then you can use the sqlalchemy module directly. However, 
if you need to work with complex relationships between tables or perform 
advanced queries, then the ORM provided by sqlalchemy.orm will likely be 
more appropriate.

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



## What can I import from `sqlalchemy.orm`?

When you import `sqlalchemy.orm`, you get access to the SQLAlchemy 
Object-Relational Mapping (ORM) system, which provides a higher-level API for 
interacting with databases using Python objects. Here are some of the main 
features that you can import from `sqlalchemy.orm`:

**Session**: A class that provides a high-level interface for managing 
transactions and interacting with the database. You can use Session objects 
to query, add, update, and delete records in the database, and to manage 
transactions.

**sessionmaker**: A function that creates a factory for creating new Session 
objects. You can use `sessionmaker` to configure the session with options 
such as the database engine and transaction isolation level.

**scoped_session**: A function that creates a thread-local `Session` object 
that can be shared across multiple functions or modules. This can be useful 
in web applications, where each request needs its own session.

**Query**: A class that provides a high-level interface for querying the 
database. You can use `Query` objects to filter, order, and limit the results of a query.

**declarative_base**: A function that creates a base class for defining model 
classes. You can subclass the base class to define your own model classes, 
and the base class provides several conveniences such as automatic table 
name generation and automatic primary key generation.

**relationship**: A function that defines a relationship between two model 
classes. You can use `relationship` to define one-to-one, one-to-many, and 
many-to-many relationships between model classes.

**backref**: A function that defines a back-reference to a related model. 
You can use `backref` to simplify queries that involve related models.

**joinedload**: A function that optimizes queries by loading related objects 
in a single query. You can use `joinedload` to reduce the number of queries 
needed to load related objects.

These are just a few examples of the features that you can import from 
`sqlalchemy.orm`. The `sqlalchemy.orm` module provides a rich set of tools for 
working with databases using Python objects, and is designed to be 
flexible and extensible to support a wide range of use cases.
