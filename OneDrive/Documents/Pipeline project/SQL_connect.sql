create database vehicle_sales_db;
use vehicle_sales_db;
show tables;
select*from dim_customer;
select * from fact_sales;
select * from dim_date;
select * from dim_location;
select * from dim_vehicle;

-- Top brands by net revenue
SELECT brand, SUM(net_revenue) AS total_rev,
       COUNT(*) AS units
FROM fact_sales f JOIN dim_vehicle v USING(vehicle_id)
GROUP BY brand ORDER BY total_rev DESC;

-- Monthly trend
SELECT year, SUM(net_revenue) AS monthly_rev
FROM fact_sales GROUP BY year ORDER BY year;

-- City performance
SELECT city, SUM(net_revenue) AS city_rev
FROM fact_sales f JOIN dim_location l USING(location_id)
GROUP BY city ORDER BY city_rev DESC LIMIT 5;