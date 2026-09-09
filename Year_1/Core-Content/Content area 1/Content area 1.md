Problem Decomposition:
This is Taking a task and breaking it down into smaller more manageable tasks. 
you can give these tasks to different people to work on at one time

Top down:
Break the task down into subtasks and work through the tasks 

Bottom up:
You give other people a task to work on individually, it then gets pieced together to form a fully functional program 

Modularisation:
Breaking a problem / task down into smaller modules 
Break down the code into functions

Abstraction:
It takes a Complex task and hides information, from users so you know what you’re working on. It makes it simpler for the end user 

Pattern Recognition:
Can be used to solve problems by looking for common trends between problems to see if they have common solutions

Pseudo code: Fake code:
```
SET INTAGER number TO 42
SET BOOLEAN correct TO False
FOR 10 Iterations 
INPUT guess AS Integer
OUTPUT “Guess a number between 1 – 100”
	IF guess EQUALS number
		OUTPUT “Correct”
		SET correct TO True
		BREAK
	ELSE IF guess IS HIGHER 
		OUTPUT “Higher”
		Break
	ELSE 
		Output “Lower”
		Break
	END IF
END FOR
IF correct Equals False
	OUTPUT “You lose”
END IF
```

For example
```
DEFINE calculator
	SET INTAGER number TO INPUT “How many numbers do you need”
	IF number EQUALS 1
		SET INTAGER num TO INPUT OUTPUT “Enter First Number”
		BREAK
	ELSE IF number EQUALS 2
		SET INTAGER num TO INPUT OUTPUT “Enter First Number”
		SET INTAGER num2 TO INPUT OUTPUT “Enter Second Number”
		BREAK
	ELSE IF number EQUALS 3
		SET INTAGER num TO INPUT OUTPUT “Enter First Number”
		SET INTAGER num2 TO INPUT OUPUT “Enter Second Number”
		SET INTAGER num3 TO INPUT OUTPUT “Enter third number”
		BREAK
	SET op TO INPUT “Enter an operator”
	IF op EQUALS +
		PRINT addition num, num2, num3
	ELSE IF op EQUALS –
		PRINT subtraction num, num2, num3
	ELSE IF op EQUALS *
		PRINT multiplication num, num2, num3
	ELSE IF op EQUALS /
		PRINT division num, num2, num3
	ELSE IF op EQUALS Aot
		PRINT Aoat num, num2
	ELSE IF op EQUALS Aoc
		PRINT Aoac num
	ELSE IF op EQUALS Aor
		PRINT Aoar num, num2
	END IF
END DEFINE

DEFINE addition num, num2, num3
	RETURN num + num2 + num3
END DEFINE

DEFINE subtraction num, num2, num3
	RETURN num – num2 – num3
END DEFINE 

DEFINE multiplication num, num2, num3
	RETURN num * num2 * num3
END DEFINE

DEFINE division num, num2, num3
	RETURN num / num2 / num3
END DEFINE

DEFINE Aoat num, num2
	RETURN ½ * num * num2
END DEFINE

DEFINE Aoac num
	RETURN 3.14 * numSQUARED
END DEFINE

DEFINE Aoar num, num2
	RETURN num * num2
END DEFINE

CALL calculator
```
