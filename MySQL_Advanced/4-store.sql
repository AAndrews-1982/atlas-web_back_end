-- Establish a trigger to adjust item quantities
-- prior to confirming a new order entry
DELIMITER //

CREATE TRIGGER decrease_quantity_item
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    -- Deduct the ordered amount from the item's stock
    UPDATE items
    SET quantity = quantity - NEW.ordered_quantity
    WHERE item_identifier = NEW.item_id;
END;
//
DELIMITER ;
