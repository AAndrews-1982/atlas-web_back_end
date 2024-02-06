-- Compute and store the average score for a student
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avgScore DECIMAL(10,2);

    -- Calculate the average score for the given user
    SELECT AVG(score) INTO avgScore FROM scores WHERE user_id = user_id;

    -- Update the user's record with the calculated average score
    UPDATE users SET average_score = avgScore WHERE id = user_id;
END //

DELIMITER ;
