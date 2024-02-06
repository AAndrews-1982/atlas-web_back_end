-- This SQL script is designed to optimize queries on the 'names' table,
-- specifically targeting the first letter of the 'name' field in combination with the 'score' field.
-- The approach involves creating a generated column for the first letter of 'name',
-- and then indexing this generated column together with 'score'.

-- Add a generated column to store the first letter of the 'name' column
-- for the purpose of indexing it along with the 'score' column.
ALTER TABLE names
ADD COLUMN name_first_letter CHAR(1) AS (LEFT(name, 1)) STORED;

-- Create the index 'idx_name_first_score' on the newly added generated column and the 'score' column.
-- This index aims to improve performance for queries filtering or sorting by the first letter of 'name' and 'score'.
CREATE INDEX idx_name_first_score ON names(name_first_letter, score);