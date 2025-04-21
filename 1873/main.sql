-- Time is 663 mms
-- Calculate employee bonuses based on specific conditions
SELECT 
    employee_id,
--  Select the employee ID column
    CASE 
        WHEN employee_id % 2 = 1 AND name NOT LIKE 'M%' THEN salary
    /*  ID is odd AND name doesn't start with 'M'
        Set bonus to 100% of salary
    */
        ELSE 0
    -- Otherwise, set bonus to 0
    END AS bonus
--  Name this calculated column as 'bonus'
FROM 
    Employees
--  Get data from the Employees table
ORDER BY 
    employee_id;
--  Sort results by employee_id in ascending order