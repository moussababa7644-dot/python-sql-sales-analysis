-- =====================================
-- SALES DATA ANALYSIS
-- =====================================


-- Total sales
SELECT SUM(Sales) AS total_sales
FROM superstore;


-- Total profit
SELECT SUM(Profit) AS total_profit
FROM superstore;


-- Sales by country
SELECT Country, SUM(Sales) AS total_sales
FROM superstore
GROUP BY Country
ORDER BY total_sales DESC;


-- Profit by country
SELECT Country, SUM(Profit) AS total_profit
FROM superstore
GROUP BY Country
ORDER BY total_profit DESC;


-- Sales by category
SELECT Category, SUM(Sales) AS total_sales
FROM superstore
GROUP BY Category
ORDER BY total_sales DESC;


-- Top 10 products by sales
SELECT "Product Name", SUM(Sales) AS total_sales
FROM superstore
GROUP BY "Product Name"
ORDER BY total_sales DESC
LIMIT 10;


-- Top 10 customers by sales
SELECT "Customer Name", SUM(Sales) AS total_sales
FROM superstore
GROUP BY "Customer Name"
ORDER BY total_sales DESC
LIMIT 10;
