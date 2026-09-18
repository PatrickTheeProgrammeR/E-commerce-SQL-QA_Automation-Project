-- Liczba zamówień każdego użytkownika
SELECT
    users.name,
    COUNT(orders.id) AS orders_count
FROM users
LEFT JOIN orders
    ON users.id = orders.user_id
GROUP BY users.id, users.name
ORDER BY orders_count DESC;


  -- Łączna wartość zamówień każdego użytkownika
SELECT
    users.name,
    COALESCE(SUM(orders.total_amount), 0) AS total_spent
FROM users
LEFT JOIN orders
    ON users.id = orders.user_id
GROUP BY users.id, users.name
ORDER BY total_spent DESC;


-- Najczęściej kupowane produkty
SELECT
    products.name,
    SUM(order_items.quantity) AS total_quantity_sold
FROM products
JOIN order_items
    ON products.id = order_items.product_id
GROUP BY products.id, products.name
ORDER BY total_quantity_sold DESC;


-- Najdroższe zamówienie
SELECT
    users.name,
    orders.id AS order_id,
    orders.total_amount
FROM users
JOIN orders
    ON users.id = orders.user_id
ORDER BY orders.total_amount DESC
LIMIT 1;


-- Użytkownicy z końcówką emailu - @example.com
SELECT *
FROM users
WHERE email
LIKE '%@example.com';


-- Zapytanie z IN
SELECT *
FROM products
WHERE name IN ('Laptop', 'Keyboard', 'Headphones');


-- Zapytanie z BETWEEN (100-500)
SELECT *
FROM products
WHERE price
BETWEEN 100 and 500;


-- Zapytanie z podzapytaniem
SELECT *
FROM users
WHERE id IN (
SELECT user_id
FROM orders
);


-- Tworzę index na kolumnie user_id w orders, jeżeli nie istnieje.
CREATE INDEX
IF NOT EXISTS idx_user_id
ON orders(user_id);