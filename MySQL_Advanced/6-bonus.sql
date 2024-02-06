-- Adds a new correction for a student with the option to create a new project if it doesn't exist
-- Inputs: user_id (linked to an existing user), project_name (new or existing), score (value for the correction)
-- Procedure to add bonuses for both new and existing projects
DELIMITER //

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE project_id INT;

    -- Check if the project already exists
    SELECT id INTO project_id FROM projects WHERE name = project_name LIMIT 1;

    -- If the project does not exist, insert the new project
    IF project_id IS NULL THEN
        INSERT INTO projects(name) VALUES(project_name);
        SET project_id = LAST_INSERT_ID(); -- Capture the new project's ID
    END IF;
    
    -- Insert the bonus for the specified user and project
    INSERT INTO corrections(user_id, project_id, score) VALUES(user_id, project_id, score);
END;//

DELIMITER ;
