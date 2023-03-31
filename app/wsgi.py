from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px
import os
import hvac

app = Flask(__name__)

app.app_context().push()
@app.route('/')
def notdash():


   df = pd.read_csv('/app/train.csv')
   df2 = df[['state','active']].groupby('state').sum().reset_index().rename({'active':'total'},axis=1).sort_values(by='total').iloc[:10,:]
   fig = px.bar(df2, x='state', y='total',color='total',title='Densidad de negocios activos por estado')
   graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

   client = hvac.Client(url='http://vault:8200', token="root")
   if client.sys.is_initialized():
      secret = client.secrets.kv.v2.read_secret_version(path='myapp/config')
      secret = secret['data']
   else:
      secret = 'La conexión falló'
   

   
   return render_template('index.html', graphJSON=graphJSON, line = secret)

   
if __name__ == "__main__":
   app.run(debug=True)
