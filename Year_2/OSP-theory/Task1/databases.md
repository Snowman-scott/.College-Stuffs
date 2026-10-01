# Databases 
## Data normalization
The process of organizing data within a database to minimize redundancy and enhance data integrity. (removing duplicate entries)
This is achieved by structuring tables and defining relationships according to specific rules known as normal forms (NF)

## Normal Forms
Data normalization follows a series of structured rules called Normal forms/ Each normal form builds upon the previous one, ensuring a systematic approach to organizing data.

### 1NF
Ensures that all entries in the table are unique and that there are no repeating groups
### 2NF
Builds on 1NF bt ensuring that all non-key attributes are fully functionally dependent on the primary key
### 3NF
Further refines the structure by eliminating transitive dependencies, ensuring that non-key attributes are not dependent on other non-key attributes.

## db questions
### What info is repeated?
Sarah jones is in the db 2 times, both have the same sales person just one table does not have a keyboard in it's product row

### Can every cell be described as containing one value?
No, Products and ProductPrices cells both have multiple pieces of data in them depending on who bought what

### What happens if sarah changes her email address?
It will have to update in 2 places in the database as there are 2 entries for them in the database

### What happens if the shop wants to add a product nobody has ordered?
They cannot as the Products list is only for purchases.
They would need to make a new table or group.

### What happens if order 1002 is deleted?
The whole row should get deleted as the orderID is the primary key
