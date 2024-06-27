-- Script to display average temperature (Fahrenheit) by city ordered by temperature (descending)

SELECT city, ROUND(AVG(temp), 4) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
