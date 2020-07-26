import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify , render_template

password ="prasu@123"
rds_connection_string = f"postgres:{password}@localhost:5432/suicideDB"
engine = create_engine(f'postgresql://{rds_connection_string}')

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

# @app.route("/index")
# def index2():
#     #"""Return the homepage."""
#     return render_template("index.html")

@app.route("/api/suicides_by_country")
def suicides_by_country():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # results = session.query(Suicide.country).all()
    results = engine.execute("SELECT country, SUM(suicides_no) AS suicides FROM suicide_data GROUP BY country;")
    print(results)
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

if __name__ == '__main__':
    app.run(debug=True)
