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

@app.route("/index")
def index2():
   # """Return the homepage."""
    return render_template("index.html")

@app.route("/api/suicides")
def suicide_by_country_by_year():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    #results = session.query(Suicide.country).all()
    results = engine.execute("select country, sum(suicides_no) as suicides from suicidedata group by country")
    output = {}
    for result in results:
        output[result['country']] = int(result['suicides'])
    session.close()
    print(output)
    return jsonify(output)


@app.route("/api/suiciderate")    
def suicide_rate_by_country():
    session = Session(engine)
    result1 = engine.execute("select country, max(suicides_no) as suicide_rate from suicidedata group by country order by suicide_rate  desc limit 10")
    output1 = {}
    for result in result1:
        output1[result['country']] = int(result['suicide_rate'])
    session.close()
    print(output1)
    return jsonify(output1)


if __name__ == "__main__":
    app.run()