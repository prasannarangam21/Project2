import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify , render_template

#password =""
#rds_connection_string = f"postgres:{password}@localhost:5432/suicideDB"
conn = 'postgres://kenfdsronoxmvl:831328583d56d888d0a487e6ecbe1f903607d8acb31b5928953c9a2d97db5f4a@ec2-52-1-95-247.compute-1.amazonaws.com:5432/d8mun3mrvnl2q1'
# engine = create_engine(f'postgresql://{rds_connection_string}')
engine = create_engine(conn)


# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)
print(Base.classes.keys())
  
# Save reference to the table
#Suicide = Base.classes.suicidedata

app = Flask(__name__)



@app.route("/")
def index():
    #"""Return the homepage."""
    return render_template("index.html")

@app.route("/gender")
def gender():
    #"""Return the homepage."""
    return render_template("gender.html")

@app.route("/generation")
def generation():
    #"""Return the homepage."""
    return render_template("generation.html")

@app.route("/byCountry")
def byCountry():
    #"""Return the homepage."""
    return render_template("byCountry.html")

@app.route("/yearlyRates")
def yearlyRates():
    #"""Return the homepage."""
    return render_template("yearlyRates.html")

@app.route("/byAge")
def byAge():
    #"""Return the homepage."""
    return render_template("byAge.html")

@app.route("/gdp_scatter")
def gdp_scatter():
    #"""Return the homepage."""
    return render_template("gdp_scatter.html")

@app.route("/hdi_scatter")
def hdi_scatter():
    #"""Return the homepage."""
    return render_template("hdi_scatter.html")

@app.route("/map")
def map():
    #"""Return the homepage."""
    return render_template("map.html")

@app.route("/api/suicides_by_country")
def suicides_by_country():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # results = session.query(Suicide.country).all()
    results = engine.execute("SELECT c.iso_abr, s.country, s.suicides FROM country_data c JOIN (SELECT country, SUM(suicides_no) AS suicides FROM suicide_data GROUP BY country) s ON c.name = s.country;")
    print(results)
    output = {}
    for result in results:
        output[result['iso_abr']] = {
            'suicides': int(result['suicides']),
            'iso_abr': result['iso_abr'],
            'country': result['country']
        }

    session.close()
    return jsonify(output)

@app.route("/api/suicides_by_TopTenCountry")
def suicides_by_TopTenCountry():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # results = session.query(Suicide.country).all()
    results = engine.execute("SELECT country, SUM(suicides_no) AS suicides FROM suicide_data GROUP BY country ORDER By suicides DESC LIMIT 10;")
    
    output = {}
    for result in results:
        output[result['country']] = int(result['suicides'])
    session.close()
    return jsonify(output)    

@app.route("/api/suicides_by_gender")
def suicides_by_gender():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # results = session.query(Suicide.country).all()
    results = engine.execute("SELECT sex, SUM(suicides_no) AS suicides FROM suicide_data GROUP BY sex")
    print(results)
    output = {}
    for result in results:
        output[result['sex']] = int(result['suicides'])
    session.close()
    return jsonify(output)

@app.route("/api/suicides_by_generation")
def suicides_by_generation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # results = session.query(Suicide.country).all()
    results = engine.execute("SELECT generation, SUM(suicides_no) AS suicides FROM suicide_data GROUP BY generation ORDER BY suicides DESC")
    print(results)
    output = {}
    for result in results:
        output[result['generation']] = int(result['suicides'])
    session.close()
    return jsonify(output)


@app.route("/api/suicides_by_age")
def suicides_by_age():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # results = session.query(Suicide.country).all()
    results = engine.execute("SELECT age, SUM(suicides_no) AS suicides FROM suicide_data GROUP BY age ORDER BY suicides DESC")
    print(results)
    output = {}
    for result in results:
        output[result['age']] = int(result['suicides'])
    session.close()
    return jsonify(output)

@app.route("/api/suicides_and_gdp")
def suicides_and_gdp():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # results = session.query(Suicide.country).all()
    results = engine.execute("SELECT country, AVG(derivedtable.suicide_rates) AS avg_suicide_rates, AVG(gdp_per_capita) AS avg_gdp_per_capita FROM (SELECT year, country, SUM(suicidesper100pop) AS suicide_rates, MAX(gdp_per_capita) AS gdp_per_capita FROM suicide_data GROUP BY year, country ORDER BY year) AS derivedTable GROUP BY country;")
    print(results)
    output = {}
    for result in results:
        output[result['country']] = {
            'suicides': int(result['avg_suicide_rates']),
            'gdp': int(result['avg_gdp_per_capita'])
        }
    session.close()
    return jsonify(output)


@app.route("/api/suicides_per_100k_by_year")
def suicides_per_100k_by_year():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    # results = session.query(Suicide.country).all()
    results = engine.execute("SELECT year, AVG(suicidesper100pop) from suicide_data group by year order by year")
    print(results)
    output = {}
    for result in results:
        output[result['year']] = float(result['avg'])
    session.close()
    return jsonify(output)

@app.route("/api/suicides_and_hdi")
def suicides_and_hdi():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    # results = session.query(Suicide.country).all()
    results = engine.execute("SELECT country, AVG(derivedtable.suicide_rates) AS suicides, AVG(derivedTable.hdi) AS hdi FROM (SELECT year, country, SUM(suicidesper100pop) AS suicide_rates, MAX(hdi_for_year) AS hdi FROM suicide_data WHERE hdi_for_year <>0 GROUP BY year, country ORDER BY year) AS derivedTable GROUP BY country ;")
    
    output = {}
    for result in results:
        output[result['country']] = {
            'suicides': int(result['suicides']),
            'hdi':float(result['hdi'])
        }
    session.close()
    return jsonify(output)

@app.route("/api/yearly_suicides_and_hdi")
def yearly_suicides_and_hdi():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # results = session.query(Suicide.country).all()
    results = engine.execute("SELECT year, AVG(derivedTable.suicidesper100pop) AS suicide_rates, AVG(derivedTable.hdi) AS hdi FROM (SELECT country,year,SUM(suicidesper100pop) AS suicidesper100pop,MAX(hdi_for_year) AS hdi FROM suicide_data WHERE hdi_for_year <>0 GROUP BY country,year) AS derivedTable GROUP BY year")
    
    output = {}
    for result in results:
        output[result['year']] = {
            'suicide_rates': int(result['suicide_rates']),
            'hdi': float(result['hdi'])
        }
    session.close()
    return jsonify(output)    


if __name__ == '__main__':
    app.run(debug=True)
