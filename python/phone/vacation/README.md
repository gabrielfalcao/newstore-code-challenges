**Vacation/Calendar Callenge**

Given a list of employee vacations, Return a summary of team vacations.

Input employee vacation will be stored as tuple, (start, end). For every tuple, start <= end.


Write a function, team_vacation() that takes a list of [(start, end)...] and return a list of merged tuples.

For example

    a) input Peter (1, 5) Bob (1, 4) ==> output [(1, 5)]
    a) input Peter (1, 5) Mike ( 7, 9) Bob (1, 6) ==> output [(1, 6) (7, 9)]
