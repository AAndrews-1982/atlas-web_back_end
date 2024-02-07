-- Change the delimiter to allow for the function definition in the script
DELIMITER //

-- Drop the function if it already exists to avoid errors upon recreation
DROP FUNCTION IF EXISTS SafeDiv;

-- Create the function SafeDiv
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    -- Check if the divisor is zero
    IF b = 0 THEN
        -- Return 0 if the divisor is zero to avoid division by zero errors
        RETURN 0;
    ELSE
        -- Perform the division if the divisor is not zero
        RETURN a / b;
    END IF;
END;
//

-- Reset the delimiter to its default value
DELIMITER ;
