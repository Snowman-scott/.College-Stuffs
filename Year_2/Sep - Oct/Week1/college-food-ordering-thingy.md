## Pitch

We made a backend,

The backend has 3 main parts

Feature set 1 Ordering:
- Menu - Shows the users what they can get to eat  
- Inventory - Shows the staff how many items of a certain food are left  
- Scheduled menus (breakfast/lunch/dinner) - The menu will be able to automatically change based on time of day  
- Order placement - Adding items into the basket, calculating total and placing the order 
- Order canceling - This allows users to cancel an order
- Order editing - This allows users to add or remove items from an order without having to cancel the whole order 
- Order status tracking - Shows the user the current status of their order  
- Order-ready notifications - User gets a notification when their food is ready so they can collect it  

Feature set 2 Users:
- Login system - Allowing the user to login to their account  
- Authentication - Makes sure the user loging in is logging into their account and not a random bad actor  
- Role-based access - Users have access to the normal ordering front, admins have access to change prices and add or remove menu items  
- Payment method selection - Users will be able to select an option like apple pay, google pay, card number etc....  
- Payment calculation - Will calculate the total for the users order  

Feature set 3 records:
- Transaction/order history - Will allow users to see past orders and amounts for the orders  
- Recommendations - Using historical records, we can send notifications to users suggesting upcoming food items

## Example endpoints 

```
## Users
POST   /auth/login
POST   /auth/register

## Ordering
GET    /menu                 ← auto-filtered by meal period
POST   /orders               ← basket → total → placed
PATCH  /orders/:id/status    ← staff updates status, triggers notification
GET    /notifications/:userId

## Records
GET    /transactions/:userId
```

## Requests methods

- GET — read/fetch data (doesn't change anything)
- POST — create something new (e.g. a new order)
- PATCH — update part of an existing thing (e.g. just the status field on an order)
- PUT — replace the whole thing with a new version (less common for small updates)
- DELETE — remove something
