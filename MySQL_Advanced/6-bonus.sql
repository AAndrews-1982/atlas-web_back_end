-- Adds a new correction for a student with the option to create a new project if it doesn't exist
-- Inputs: user_id (linked to an existing user), project_name (new or existing), score (value for the correction)
DELIMITER //

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    -- Check if the project exists in the 'projects' table
    DECLARE project_id INT DEFAULT NULL;
    
    SELECT id INTO project_id FROM projects WHERE name = project_name LIMIT 1;
    
    -- If the project does not exist, insert it into the 'projects' table
    IF project_id IS NULL THEN
        INSERT INTO projects(name) VALUES(project_name);
        SET project_id = LAST_INSERT_ID(); -- Get the ID of the newly inserted project
    END IF;
    
    -- Insert the correction record into the 'corrections' table
    INSERT INTO corrections(user_id, project_id, score) VALUES(user_id, project_id, score);
END$$

DELIMITER ;
