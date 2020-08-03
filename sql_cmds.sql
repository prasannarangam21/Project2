SELECT country, AVG(suicidesper100pop) from suicide_data group by country order by country;
SELECT country, AVG(derivedtable.suicide_rates) AS avg_suicide_rates, AVG(gdp_per_capita) AS avg_gdp_per_capita FROM (SELECT year, country, SUM(suicidesper100pop) AS suicide_rates, MAX(gdp_per_capita) AS gdp_per_capita FROM suicide_data GROUP BY year, country ORDER BY year) AS derivedTable GROUP BY country;
SELECT c.iso_abr, s.country, s.suicides FROM country_data c JOIN (SELECT country, SUM(suicides_no) AS suicides FROM suicide_data GROUP BY country) s ON c.name = s.country;
SELECT generation, SUM(suicides_no) AS suicides FROM suicide_data GROUP BY generation ORDER BY suicides DESC;
SELECT sex, SUM(suicides_no) AS suicides FROM suicide_data GROUP BY sex;
SELECT c.iso_abr, s.country, s.suicides FROM country_data c JOIN (
  SELECT country, SUM(suicides_no) AS suicides FROM suicide_data GROUP BY country
) s ON c.name = s.country;
SELECT country, SUM(suicides_no) AS suicides FROM suicide_data GROUP BY country ORDER By suicides DESC LIMIT 10;
SELECT country, AVG(derivedtable.suicide_rates) AS suicides, AVG(derivedTable.hdi) AS hdi FROM (SELECT year, country, SUM(suicidesper100pop) AS suicide_rates, MAX(hdi_for_year) AS hdi FROM suicide_data WHERE hdi_for_year <>0 GROUP BY year, country ORDER BY year) AS derivedTable GROUP BY country; 
SELECT year, AVG(derivedTable.suicidesper100pop) AS suicide_rates, AVG(derivedTable.hdi) AS hdi FROM (SELECT country,year,SUM(suicidesper100pop) AS suicidesper100pop,MAX(hdi_for_year) AS hdi FROM suicide_data WHERE hdi_for_year <>0 GROUP BY country,year) AS derivedTable GROUP BY year;


