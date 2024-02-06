-- Adjust the attribute 'valid_email' when the 'email' field is updated
DELIMITER //

CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        -- Email has been changed, reset 'valid_email'
        SET NEW.valid_email = FALSE;
    END IF;
END;
//
DELIMITER ;
