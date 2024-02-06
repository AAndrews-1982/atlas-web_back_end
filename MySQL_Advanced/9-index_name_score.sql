-- Ensure the 'names' table is imported from the 'names.sql.zip' file into your database.

-- Add a generated column to store the first letter of the 'name' column.
-- This is necessary to create an index that includes the first letter of 'name' and the 'score'.
ALTER TABLE names
ADD COLUMN name_first_letter CHAR(1) AS (LEFT(name, 1)) STORED;

-- Create an index on the generated column and the 'score' column.
-- This index, named 'idx_name_first_score', will help optimize queries that filter or sort
-- based on the first letter of the name and the score.
CREATE INDEX idx_name_first_score ON names(name_first_letter, score);
