from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from flask import render_template
import pandas as pd
import json
import plotly
import plotly.express as px
from credentials import credentials


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+credentials['user']+':'+credentials['pwd']+'@'+credentials['host']+':'+credentials['port']+'/'+credentials['db']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()


locs = db.Table('estados',db.metadata, autoload_with = db.engine)
hechos = db.Table('hechos',db.metadata, autoload_with = db.engine)

@app.route('/')
def notdash():
   #query = (db.session.query(locs).join(hechos, (locs.c.cfips ==hechos.c.cfips) & (locs.c.id_state==hechos.c.id_state))).statement
   
   
   query2 = (db.session.query(
                hechos.c.id_state, 
                db.func.sum(hechos.c.active).label("total")
            ).
            group_by(hechos.c.id_state)
            ).order_by(db.func.sum(hechos.c.active).desc()).limit(10)
   df = pd.read_sql_query(query2.statement,con=db.engine)
   df2 = df[['id_state','total']].groupby('id_state').sum().reset_index().sort_values(by='total').iloc[:10,:]
   fig = px.bar(df2, x='id_state', y='total')
   graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
   return render_template('notdash.htlm', graphJSON=graphJSON)
   
if __name__ == '__main__':
   app.run(host = '127.0.0.1',port=4000,debug=True)