/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
select city from station where  (city LIKE 'a%' OR city LIKE 'i%' OR city LIKE 'u%' OR city LIKE 'e%' OR city LIKE 'o%') and (city LIKE '%a' OR city LIKE '%i' OR city LIKE '%u' OR city LIKE '%e' OR city LIKE '%o');