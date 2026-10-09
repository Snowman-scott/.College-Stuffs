# Task 3

## Problem Decomp

Input amount in currency X -> Convert Currency X into Currency Y (based on the most up to date figs)

Input Amount -> Input given amounts currency -> Input currency to convert too -> Convert currency X to Y -> output original amount+currency X, conversion rate (most up-to date), currency Y.

Currency X = Given currency
Currency Y = Converted Currency

## pseudo code

```
IMPORT pandas LIBARY AS pd
IMPORT matplotlib.pyplot LIBARY AS plt

FUNCTION get_currency IMPORT (amount, currency)
SET currencies = LIST ['GBP','EUR','AUD','JPY']

REPEAT
  OUTPUT 'Please enter the amount you would like to convert: '
  INPUT amount

  TRY
    SET verified_amount = float(amount)
  EXCEPT ValueError
    PRINT 'Enter a valid name'
  ELSE
    PRINT'Amount entered is {verified_amount}'
  END TRYCATCH
END REPEAT

REPEAT
  OUTPUT 'The currencies we support are: '
  REPEAT FOR x IN currencies
    OUTPUT {x}
  END REPEAT
  OUTPUT 'Enter the currency your amount is in: '
  INPUT currency
  IF currency NOT IN currencies THEN
    OUTPUT 'Enter a valid Currency'
  ELSE THEN
    OUTPUT 'You selected {currency}'
  END IF
END REPEAT

END FUNCTION get_currency

FUNCTION get_converting_currency IMPORT (convert_to)
SET currencies = LIST ['GBP','EUR','AUD','JPY']

REPEAT
  OUTPUT 'The currencies we support are: '
  REPEAT FOR x IN currencies
    OUTPUT {x}
  END REPEAT
  OUTPUT 'Enter the currency you wish to convert your amount to: '
  INPUT convert_to
  IF convert_to NOT IN currencies THEN
    OUTPUT 'Please Enter a valid Currency'
  ELSE THEN
    OUTPUT 'You selected {convert_to} as your currency to convert into'
  END IF
END REPEAT
END FUNCTION get_converting_currency

FUNCTION convert_amount IMPORT (amount, currency, convert_to)
SET df = OPEN FILE 'Task_3_RSBX_data.csv'
READ LINE BY LINE

SET conversions = DICTIONARY {
  'GBP EUR' : 'GBP +AC0- EUR',
  'EUR GBP' : 'EUR +AC0- GBP',
  'GBP AUD' : 'GBP +AC0- AUD',
  'AUD GBP' : 'AUD +AC0- GBP',
  'GBP JPY' : 'GBP +AC0- JPY',
  'JPY GBP' : 'JPY +IBM- GBP',
}

SET convert = currency ADD convert_to

// this would be 

```
