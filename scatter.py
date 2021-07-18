import pandas as pd
import plotly_express as px
df = pd.read_csv("C:/Users/Asus/Desktop/whj/project 103/covid.csv")
scatter1 = px.scatter(df,x="date",y="cases",color="country",size_max=60)
scatter1.show()