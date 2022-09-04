# Schemas

## Logical

Describes the structure of the database. Entities and features and their relationship

## Physical

How it is stored, the physical storage of the db. The entire database but at a very low level.

## View

Describes the database like an external user would want to see it. Only describes the part of the database that the specific user is interested in.

# Relationships

## One to one

Head of the department is related to one department

## One to many

One student enrolled in many courses

## Many to many

Supervisor and works. One worker can have two works, one supervisor can supervise many workers

# Relational Model

## Composition

Data, relationships and constraints

## Definitions

- Domain: depends on the data type. It has the set of acceptable and possible values based on the constraints.
- Record: a row in the table. It's also known as tuple
- Degree: the number of attributes (columns)
- Cardinality: number of rows

## Constraints

- Key constraint: identifier tahtat can be used to refer to a record. It makes the value on the column UNIQUE
- Domain constraint: it's the way to validate the data entered correspond to the data type required by the column
- Referential integrity constraints: Relationships by foreing keys and primary keys. It must be a matching value in the two tables.

# Normalization

1. First Normal Form
2. Second Normal Form
3. Third Normal Form

Single purpose for each table. Minimize duplacations, avoid errors during data modification and simplify queries from the database.

- Insert Anomalies
- Update Anomalies
- Delete Anomalies

##
