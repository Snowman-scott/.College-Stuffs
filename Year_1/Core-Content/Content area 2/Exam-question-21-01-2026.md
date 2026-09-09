# Exam question
### Evaluate the suitability of a for loop and while loop for an algorithm that adds the prices of a shopping list together (9)

Both loops would get the job done, A for loop would need code in it to see howmany items are in the list and loop through it to add up the total price, this means the code would need to run a length check on the array or dictionary to see how many items are in the list before it can start going through the array / dictionary and start adding up the prices.

A while loop would loop through the program until a condition is met. So it would start looping through the list until the lsit cannot give anymore data to add to the price. This method would use less or the same amount of code but look nicer. This could impose the issue of the loop skipping back to the start of the lsit by accident and adding more to the total, where as a for loop would only go for the amount of items in the list, so this is less of an issue.

You could also use both a for and while loop for this job, wrap the program in a while True loop and make the rest run in there so it is constantly checking to see if the user adds more items to their cart and add the toatl up again.

```
Items = []
while True:
x = 0
for x in range(items.len)
  Total = Total + Items[x]
  x = x + 1

```
That code is probably wrong but I'm like fkd
