from flask import Flask, render_template, request
app =Flask(__name__)

import pickle
model= pickle.load(open(r'D:/6th sem externship/Flask_Project/model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Online_Shoppers_intension', methods=['POST'])
def Online_Shoppers_intension():
    
    ProductRelated =  request.form('ProductRelated')
    ProductRelated_Duration =  request.form('ProductRelated_Duration')
    BounceRates  = request. form('BounceRates')
    ExitRates =  request.form('ExitRates')
    PageValues = request.form('PageValues')
    SpecialDay = request.form('specialday')
    Month = request.form('month')
    Region = request.form('Region')
    TrafficType = request.form('TrafficType')
    VisitorType = request.form('VisitorType')
    Weekend = request.form('weekend')
    total= [[int(ProductRelated), int(ProductRelated_Duration), float(BounceRates), float(ExitRates), float(PageValues), float(SpecialDay), int(Month), int(Region), int(TrafficType), int(VisitorType), int(Weekend)]]
    print(total)
    prediction = model.predict(total)
    print(prediction)
    if prediction == 0:
        return render_template("index.html", prediction_text="The Visitor is not interested in buying products.")
    else:
         return render_template("index.html", prediction_text="The Visitor is interested in buying products")
    

if __name__ == "__main__":
    app.run(debug=False)