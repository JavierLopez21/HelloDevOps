from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px
from credentials import credentials


app = Flask(__name__)

app.app_context().push()



@app.route('/')
def notdash():
   
   df = pd.read_csv('train.csv')
   df2 = df[['state','active']].groupby('state').sum().reset_index().rename({'active':'total'},axis=1).sort_values(by='total').iloc[:10,:]
   fig = px.bar(df2, x='state', y='total',color='total',title='Densidad de negocios activos por estado')
   graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
   return render_template('notdash.htlm', graphJSON=graphJSON)
   
if __name__ == '__main__':
   app.run(host = '0.0.0.0',port=4000,debug=True)