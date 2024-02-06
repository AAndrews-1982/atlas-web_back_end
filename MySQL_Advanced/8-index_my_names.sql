-- task. Identify students requiring follow-up meetings
-- SQL script that creates a view 'need_meeting'
-- for students with scores under 80 and no recent meeting.
CREATE VIEW need_meeting AS
SELECT student_name
FROM students
WHERE score < 80 AND (last_meeting IS NULL OR last_meeting <= CURDATE() - INTERVAL 1 MONTH);
