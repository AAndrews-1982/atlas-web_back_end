-- This SQL script creates a view named 'need_meeting'
-- The view lists all students who have a score strictly under 80
-- AND either have no recorded 'last_meeting' date OR their last meeting was more than a month ago.
-- This is intended to identify students who need a follow-up meeting based on their academic performance and meeting history.

CREATE VIEW need_meeting AS
SELECT 
    student_name -- Adjust this column name based on your schema
FROM 
    students -- Adjust this table name based on your schema
WHERE 
    score < 80 -- Filter for scores strictly under 80
    AND (
        last_meeting IS NULL -- No last meeting date recorded
        OR 
        last_meeting <= CURDATE() - INTERVAL 1 MONTH -- Last meeting more than a month ago
    );
