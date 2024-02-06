-- Trigger Name: AfterOrderInsert
-- Description: Decreases the quantity of an item in the 'items' table after a new order is inserted into the 'orders' table.
-- Context: This trigger ensures data consistency by automatically updating the items' quantity,
-- mitigating issues caused by network disconnections, crashes, etc.

DELIMITER $$

CREATE TRIGGER AfterOrderInsert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Decrease the quantity of the ordered item in the items table
    UPDATE items
    SET quantity = quantity - NEW.quantity_ordered
    WHERE item_id = NEW.item_id;
END$$

DELIMITER ;
