-- Add a generated column to 'names' table that stores the first letter of 'name'
ALTER TABLE names
ADD COLUMN name_first_letter CHAR(1) AS (LEFT(name, 1)) STORED;

-- Create an index on the generated column
CREATE INDEX idx_name_first ON names(name(1));
