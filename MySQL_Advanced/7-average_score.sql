-- TASK7: Enhance the stored procedure to compute and store the average score for a student.
-- The procedure handles decimal values for precise average score calculations.
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    -- Directly update the 'average_score' in the 'users' table by calculating
    -- the average score from the 'corrections' table for the given user.
    -- The subquery selects the average 'score' where the 'user_id' matches.
    UPDATE users 
    SET average_score = (
        SELECT AVG(score) 
        FROM corrections
        AS user 
        WHERE user.user_id = user_id
    )
    WHERE id = user_id;
END;
//
DELIMITER ;
