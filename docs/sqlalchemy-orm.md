# SqlAlchemy ORM

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
