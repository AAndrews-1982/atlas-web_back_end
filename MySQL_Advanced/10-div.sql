-- Define the function SafeDiv to perform safe division
DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS DECIMAL(10,2)
BEGIN
    -- Check if the divisor is zero
    IF b = 0 THEN
        -- Return 0 if the divisor is zero to avoid division by zero error
        RETURN 0;
    ELSE
        -- Perform the division and return the result if the divisor is not zero
        RETURN a / b;
    END IF;
END//

DELIMITER ;
