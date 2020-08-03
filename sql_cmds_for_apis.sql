#/api/suicides_by_country

SELECT c.iso_abr, s.country, s.suicides FROM countrydata c JOIN (SELECT country, SUM(suicides_no) AS suicides FROM suicide_data GROUP BY country) s ON c.name = s.country;

#/api/suicides_by_TopTenCountry

SELECT country, SUM(suicides_no) AS suicides FROM suicide_data GROUP BY country ORDER By suicides DESC LIMIT 10;

#/api/suicides_by_gender

SELECT sex, SUM(suicides_no) AS suicides FROM suicide_data GROUP BY sex;

#/api/yearly_suicides_by_gender

SELECT year, sex, SUM(suicides_no) AS suicides FROM suicide_data GROUP BY year,sex;

#/api/yearly_suicides_by_generation

SELECT generation,year, sum(suicides_no) as numsuicides FROM suicide_data GROUP BY year, generation order by year;

#/api/suicides_by_generation

SELECT generation, SUM(suicides_no) AS suicides FROM suicide_data GROUP BY generation ORDER BY suicides DESC;

#/api/suicides_by_age

SELECT age, SUM(suicides_no) AS suicides FROM suicide_data GROUP BY age ORDER BY suicides DESC;

#/api/suicides_by_age_country

SELECT age, country, SUM(suicides_no) AS suicides FROM suicide_data GROUP BY age, country ORDER BY suicides;

#/api/suicides_and_gdp

SELECT country, AVG(derivedtable.suicide_rates) AS avg_suicide_rates, AVG(gdp_per_capita) AS avg_gdp_per_capita FROM (SELECT year, country, SUM(suicidesper100pop) AS suicide_rates, MAX(gdp_per_capita) AS gdp_per_capita FROM suicide_data GROUP BY year, country ORDER BY year) AS derivedTable GROUP BY country;

#/api/yearly_suicides_and_gdp

SELECT year, AVG(derivedTable.suicidesper100pop) AS suicide_rates, AVG(derivedTable.gdp_per_capita) AS gdp_per_capita FROM (SELECT country,year,SUM(suicidesper100pop) AS suicidesper100pop,MAX(gdp_per_capita) AS gdp_per_capita FROM suicide_data GROUP BY country,year) AS derivedTable GROUP BY year;

#/api/suicides_per_100k_by_year

SELECT year, AVG(suicidesper100pop) from suicide_data group by year order by year;

#/api/suicides_and_hdi

SELECT country, AVG(derivedtable.suicide_rates) AS suicides, AVG(derivedTable.hdi) AS hdi FROM (SELECT year, country, SUM(suicidesper100pop) AS suicide_rates, MAX(hdi_for_year) AS hdi FROM suicide_data WHERE hdi_for_year <>0 GROUP BY year, country ORDER BY year) AS derivedTable GROUP BY country ;

#/api/yearly_suicides_and_hdi

SELECT year, AVG(derivedTable.suicidesper100pop) AS suicide_rates, AVG(derivedTable.hdi) AS hdi FROM (SELECT country,year,SUM(suicidesper100pop) AS suicidesper100pop,MAX(hdi_for_year) AS hdi FROM suicide_data WHERE hdi_for_year <>0 GROUP BY country,year) AS derivedTable GROUP BY year;

