-- This SQL script creates a view named 'need_meeting' that lists students
-- who require a meeting based on their academic performance and the
-- recency of their last meeting. Specifically, it targets students with
-- scores below 80 who haven't had a meeting in the last month or at all.

CREATE OR REPLACE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting <= NOW() - INTERVAL 1 MONTH);
