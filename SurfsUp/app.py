## declare libraries used in this API program

from flask import Flask,jsonify
import sqlalchemy as sa
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine,inspect, func, Table, Column, Integer, String, Date, Float
import datetime as dt

# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(autoload_with=engine)

#Define classes to reference in queries
Measurement=Base.classes.measurement
Station=Base.classes.station

#Define app to run api using Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<br> Station and Measurement info from DB hawaii\
            <br> This site is for developers only\
            <br> These are the routes:\
            <br> \
            <a href='http://127.0.0.1:5000/api/v1.01/precipitation'>Get precipitation data for the last 12 months</a><br>\
            <a href='http://127.0.0.1:5000/api/v1.01/stations'>Get the list of all stations in DB</a><br>\
            <a href='http://127.0.0.1:5000/api/v1.01/tobs'> Returns data for the most active station (just info obtained the last year for the station mentioned) <br>"

# precipitation API route
@app.route("/api/v1.01/precipitation")
def precipitation():

    # open conexion
    session = Session(engine)

    # Find the most recent date in the data set.
    sel = [func.max(func.strftime("%Y-%m-%d",Measurement.date))]
    recent_date = session.query(*sel).scalar()

    # conver str date to a date object
    query_date = dt.datetime.strptime(str(recent_date), "%Y-%m-%d").date()

    # Calculate the date one year from the last date in data set.
    query_date = query_date - dt.timedelta(days=365)

    # executes the query: obtain date and prcp fields of Measurement table, but just the last 12 months of data
    result_Station = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= query_date).order_by(Measurement.date).all()

    # closed the conexion
    session.close()

    #Create dictionary to save results and return a json object
    result={}
    for row in result_Station:
        result[row[0]]=row[1]
    return jsonify(result)


#Stations API app
@app.route("/api/v1.01/stations")
def stations():

    # open conexion
    session = Session(engine)

    # execute query : obtain all data in Station table
    list=session.query(Station).all()

    # close conextion
    session.close()

    #Create dictionary to save results
    list_dict={}

    # create a dictionary with detail of all stations obtained in query 
    for row in list:
        list_dict[row.id]={"id": row.id,
                                "station": row.station,
                                "name": row.name,
                                "lat": row.latitude,
                                "long": row.longitude}
    #Return jsonified dictionary
    return jsonify(list_dict)

#Temperatures API App
@app.route("/api/v1.01/tobs")
def tobs():

    # open conexion
    session = Session(engine)

    # Find the most recent date in the data set.
    sel = [func.max(func.strftime("%Y-%m-%d",Measurement.date))]
    recent_date = session.query(*sel).scalar()

    # convert str date to a date object
    query_date = dt.datetime.strptime(str(recent_date), "%Y-%m-%d").date()

    # Calculate the date one year from the last date in data set.
    query_date = query_date - dt.timedelta(days=365)
    
    sel = [Measurement.station,func.count(Measurement.id)]
    
    # execute query : get the most active station
    first_station = session.query(*sel).group_by(Measurement.station).order_by(func.count(Measurement.id).desc()).first()

    sel = [Measurement.date, Measurement.tobs]

    # execute query : obtain date and tobs fields of Measurement table, of the most active station, but just the last 12 months of data 
    tobs_list  = session.query(*sel).filter(Measurement.station==first_station[0]).filter(Measurement.date >= query_date).order_by(Measurement.date).all()

    # close the conexion
    session.close()

    #Create dictionary to save results
    tobs_dict={}
    for line in tobs_list:
        tobs_dict[line[0]]=line[1]
    #Return jsonified dictionary

    return jsonify(tobs_dict)

#Run app code
if __name__=="__main__":
    app.run(debug=True)