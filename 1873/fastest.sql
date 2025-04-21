-- Time is 475 ms
-- Select employee_id column and calculates a computed column called 'bonus'
SELECT employee_id,
--  Start a CASE expression to determine bonus value conditionally
    CASE 
    /*  If employee_id is odd (remainder when divided by 2 equals 1)
        AND employee name does not start with 'M'
        Then set bonus equal to their salary
    */
        WHEN employee_id % 2 = 1 AND name NOT LIKE 'M%' THEN salary
        ELSE 0
    /*  Otherwise (for even employee_id or names starting with 'M')
        Set bonus to 0
    */
    END AS bonus 
-- Specify the table to get data from
FROM employees
-- Sort the employee_id in ascending order
ORDER BY employee_id;

/*Notes:
CASE expression = conditional logic in SQL that allows you to perform if-then-else type logic
within a query. It evaluates conditions and returns a value when the first condition is met.
*/