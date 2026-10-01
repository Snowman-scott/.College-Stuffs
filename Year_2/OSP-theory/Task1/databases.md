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

### the data

| OrderID | CustomerName | CustomerEmail | Products | ProductPrices | SalesPerson | SalesPersonEmail |
|---------|--------------|---------------|----------|---------------|-------------|------------------|
| 1001 | Sarah Jones | sarah@email.com | Keyboard, Mouse | £40, £20 | Ahmed Khan | ahmed@shop.co.uk |
| 1002 | Ben Smith | ben@email.com | Monitor | £180 | Helen Green | helen@shop.co.uk |
| 1003 | Sarah Jones | sarah@email.com | Mouse | £20 | Ahmed Khan | ahmed@shop.co.uk |
| 1004 | Emily Brown | emily@email.com | Keyboard, Monitor | £40, £180 | Helen Green | helen@shop.co.uk |

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

## Normalizing data

### Customers
| CustomerID (PK) | CustomerName | CustomerEmail |
|-----------------|--------------|---------------|
| CO1 | Sarah Jones | sarah@email.com |
| CO2 | Ben Smith | ben@email.com |
| CO3 | Emily Brown | emily@email.com |

### SalesPeople
| SalesPersonID (PK) | SalesPersonName | SalesPersonEmail |
|--------------------|-----------------|------------------|
| SO1 | Ahmed Khan | ahmed@shop.co.uk |
| SO2 | Helen Green | helen@shop.co.uk |

### Products
| ProductID (PK) | ProductName | ProductPrice |
|----------------|-------------|--------------|
| P01 | Keyboard | £40 |
| P02 | Mouse | £20 |
| P03 | Monitor | £180 |

### Orders
| OrderID (PK) | CustomerID (FK) | SalesPersonID (FK) |
|--------------|-----------------|--------------------|
| 1001 | 1 | 1 |
| 1002 | 2 | 2 |
| 1003 | 1 | 1 |
| 1004 | 3 | 2 |

### OrderItems (linking table)
| OrderID (PK, FK) | ProductID (PK, FK) |
|------------------|--------------------|
| 1001 | 1 |
| 1001 | 2 |
| 1002 | 3 |
| 1003 | 2 |
| 1004 | 1 |
| 1004 | 3 |

## Data Dict

| Field Name | Table Name | Data Type | Description | Constraints |
|------------|------------|-----------|-------------|-------------|
| CustomerID | Customers | Intager | Unique number for each customer | Unique, Primary Key - Auto increment |
| CustomerName | Customers | String | Name of the customer | Required, Maximum of 50 chars |
| CustomerEmail | Customers | String | Customers Email | Required, Unique, must be a valid email |
| SalesPersonID | Salespeople | Intager | Unique number for each sales person | Unique, Primary Key - Auto Increment |
| SalesPersonName | Salespeople | String | name of sales person | Reuired, Maximum of 50 chars |
| SalesPersonEmail | Salespeople | String | Email of salesperson | Required, Unique, valid email |
| ProductID | Products | Intager | Unique number for each product | Unique, Primary key - Auto increment |
| ProductName | Products | String | Name of product | Required, max 100 chars, Unique | 
| ProductPrice | Products | Float | Price of product | Price to 2 Decimal places, Type of currency (£, $, €) |
| OrderID | Orders | Intager | Unique number for every order | Unique, Primary key, Auto Incrament |
| CustomerID | Orders | Intager | ID of user making the order | Foreign Key (Customers) |
| ProductID | Orders | Intager | ID for products in the order | Foreign Key (Products) |
| SalesPerson | Orders | Intager | ID of the sales person who made the sale | Foreign Key (Salespeople) |
