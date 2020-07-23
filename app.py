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
   # """Return the homepage."""
    return render_template("index.html")

@app.route("/api/suicides_by_country")
def suicides_by_country():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    # results = session.query(Suicide.country).all()
    results = engine.execute("SELECT country, SUM(suicides_no) AS suicides FROM suicide_data GROUP BY country")
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

if __name__ == "__main__":
    app.run()