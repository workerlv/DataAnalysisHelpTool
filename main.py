from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    data = pd.read_csv("train.csv")
    return render_template("index.html",
                           tables=[data.to_html()],
                           titles=[""],
                           described_data=[data.describe().applymap(lambda x: f"{x:0.2f}").to_html()],
                           described_data_cat=[data.describe(include="object").to_html()],
                           column_names=data.columns,
                           isnull=data.isnull().sum()
                           )


if __name__ == '__main__':
    app.run()

