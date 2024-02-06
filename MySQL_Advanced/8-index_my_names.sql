-- First, ensure that any existing index that might conflict is removed
DROP INDEX IF EXISTS idx_name_first ON names;

-- Then, create the index on the first letter of the 'name' column
CREATE INDEX idx_name_first ON names(name(1));
