SELECT name, COUNT(orders.id)
FROM users
LEFT JOIN orders
    ON users.id = orders.user_id
GROUP BY name;


SELECT products.name, SUM(order_items.quantity)
FROM products
JOIN order_items
    ON products.id = order_items.product_id
GROUP BY products.name
ORDER BY SUM(order_items.quantity) DESC;


SELECT products.name, SUM(products.price * order_items.quantity)
FROM products
JOIN order_items
    ON products.id = order_items.product_id
GROUP BY products.name
ORDER BY SUM(products.price * order_items.quantity) DESC;


SELECT users.name, SUM(orders.total_amount)
FROM users
LEFT JOIN orders
    ON users.id = orders.user_id
GROUP BY users.name
ORDER BY SUM(orders.total_amount) DESC;


SELECT users.name, orders.total_amount
FROM users
JOIN orders
    ON users.id = orders.user_id
ORDER BY orders.total_amount DESC
LIMIT 1;


SELECT products.name
FROM products
WHERE price > 300;


ALTER TABLE products ADD COLUMN category TEXT;

UPDATE products set category = 'Electronics' where name = 'Laptop';
UPDATE products set category = 'Electronics' where name = 'Headphones';
UPDATE products set category = 'Accessories' where name = 'Mouse';
UPDATE products set category = 'Accessories' where name = 'Keyboard';


SELECT products.category, COUNT(category)
FROM products
GROUP BY products.category;


SELECT products.category, AVG(products.price)
FROM products
GROUP BY products.category
HAVING AVG(products.price) > 500;


UPDATE products SET price = 119.99 WHERE name = 'Mouse';
DELETE FROM products WHERE name = 'Mouse';


BEGIN;

UPDATE products SET price = 299.99 WHERE name = 'Keyboard';

ROLLBACK;



BEGIN;

UPDATE products SET price = 279.99 WHERE name = 'Keyboard';

COMMIT;