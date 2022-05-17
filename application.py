from flask import(
  Flask, render_template, request
)
import pandas as pd
import numpy as np
import pickle
import sklearn
import cv2
import os
from tensorflow import keras
from keras.models import load_model
import urllib.request
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

#from flask_ngrok import run_with_ngrok
model = 'CropRecommender.pkl'
model2 = 'Onion.pkl'
model3 = load_model('v3_pred_cott_dis.h5')
model4 = 'Final-Fruit.h5'

# Initialize the app
application = Flask(__name__)
UFOLDER = os.path.join('static', 'uploads')
application.config['UPLOAD_FOLDER']=UFOLDER
#run_with_ngrok(application)
Crop_Rec = pickle.load(open(model, 'rb'))
Market_predictor = pickle.load(open(model2, 'rb'))

#Fruit_Quality = 

@application.route('/', methods=['GET'])
def home():
  return render_template('index.html', font_url = "http://fonts.googleapis.com/css?family=Playball&amp;subset=latin-ext",
                         font_url2 = "http://fonts.googleapis.com/css?family=Raleway:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i",
                         font_url3 = "http://fonts.googleapis.com/css?family=Roboto+Condensed:400,700italic,700,400italic,300italic,300")

@application.route('/templates/soil.html/', methods=['GET', "POST"])
def soil():
  return render_template('soil.html')
@application.route('/templates/soil_pred.html/', methods=['GET', "POST"])
def predict():
  N = request.form.get("N")
  P = request.form.get("P")
  K = request.form.get("K")
  ph = request.form.get("ph")
  ec = request.form.get("ec")
  S = request.form.get("S")
  Cu = request.form.get("Cu")
  Fe = request.form.get("Fe")
  Mn = request.form.get("Mn")
  Zn = request.form.get("Zn")
  B = request.form.get("B")
  inp_features = [N, P, K, ph, ec, S, Cu, Fe, Mn, Zn, B]
  inp_features = np.array(inp_features)
  inp_features = inp_features.reshape(1,-1)
  prediction = Crop_Rec.predict(inp_features)
  return render_template('soil_pred.html', prediction_text = prediction)

@application.route('/templates/market.html/', methods=['GET', "POST"])
def market():
  return render_template('market.html')

@application.route('/templates/market_pred.html/', methods=['GET', "POST"])
def predict_mp():
  #S = request.form.get("State")
  #V = request.form.get("Variety")
  #Mi = request.form.get("Min_price")
  #Ma = request.form.get("Max_price")
  x_test = [x for x in request.form.values()]
  if(x_test[0]=='Andhra Pradesh'):
        x_test[0] = 0
  elif(x_test[0]=='Chattisgarh'):
        x_test[0] = 1
  elif(x_test[0]=='Goa'):
        x_test[0] = 2
  elif(x_test[0]=='Gujarat'):
        x_test[0] = 3
  elif(x_test[0]=='Haryana'):
        x_test[0] = 4
  elif(x_test[0]=='Himachal Pradesh'):
        x_test[0] = 5
  elif (x_test[0] == 'Jammu and Kashmir'):
        x_test[0] = 6
  elif (x_test[0] == 'Jharkhand'):
        x_test[0] = 7
  elif (x_test[0] == 'Karnataka'):
        x_test[0] = 8
  elif (x_test[0] == 'Kerala'):
        x_test[0] = 9
  elif (x_test[0] == 'Madhya Pradesh'):
        x_test[0] = 10
  elif (x_test[0] == 'Maharashtra'):
        x_test[0] = 11
  elif (x_test[0] == 'Nagaland'):
        x_test[0] = 12
  elif (x_test[0] == 'NCT of Delhi'):
        x_test[0] = 13
  elif (x_test[0] == 'Odisha'):
        x_test[0] = 14
  elif (x_test[0] == 'Punjab'):
        x_test[0] = 15
  elif (x_test[0] == 'Rajasthan'):
        x_test[0] = 16
  elif (x_test[0] == 'Telangana'):
        x_test[0] = 17
  elif (x_test[0] == 'Tripura'):
        x_test[0] = 18
  elif (x_test[0] == 'Uttar Pradesh'):
        x_test[0] = 19
  elif (x_test[0] == 'Uttarakhand'):
        x_test[0] = 20
  elif (x_test[0] == 'West Bengal'):
        x_test[0] = 21

  if (x_test[1] == 'Local'):
        x_test[1] = 0
  elif (x_test[1] == 'Other'):
        x_test[1] = 1
  elif (x_test[1] == 'Onion'):
        x_test[1] = 2
  elif (x_test[1] == 'Nasik'):
        x_test[1] = 3
  elif (x_test[1] == 'Red'):
        x_test[1] = 4
  elif (x_test[1] == 'White'):
        x_test[1] = 5
  elif (x_test[1] == 'Beelary-Red'):
        x_test[1] = 6
  elif (x_test[1] == '1st Sort'):
        x_test[1] = 7
  elif (x_test[1] == 'Bangalore-Samall'):
        x_test[1] = 8
  elif (x_test[1] == 'Puna'):
        x_test[1] = 9
  elif (x_test[1] == 'Pusa-Red'):
        x_test[1] = 10
  elif (x_test[1] == 'Bombay (U.P.)'):
        x_test[1] = 11
  elif (x_test[1] == 'Telagi'):
        x_test[1] = 12
  elif (x_test[1] == 'Hybrid'):
        x_test[1] = 13
  elif (x_test[1] == 'Small'):
        x_test[1] = 14
  elif (x_test[1] == '2nd Sort'):
        x_test[1] = 15
  elif (x_test[1] == 'Pole'):
        x_test[1] = 16
  elif (x_test[1] == 'Dry F.A.Q.'):
        x_test[1] = 17
  elif (x_test[1] == 'Medium'):
        x_test[1] = 18
  elif (x_test[1] == 'Bellary'):
        x_test[1] = 19
  x_test = [float(x)  for x in x_test]
  final_features = [np.array(x_test)]
  print(final_features)
  prediction = Market_predictor.predict(final_features)
  print(prediction)
  output = round(prediction[0], 2)
  msg = output

  #inp_features = [S, V, Mi, Ma]
  #inp_features = np.array(inp_features)
  #inp_features = inp_features.reshape(1,-1)
  #prediction = Market_predictor.predict(inp_features)
  return render_template('market_pred.html', prediction_text = msg, minim = request.form["Min_price"], maxi = request.form["Max_price"])
  

@application.route('/templates/leaf-disease.html', methods=['GET', "POST"])
def LD():
  return render_template('leaf-disease.html')

def pred_cot_dieas(cott_plant):
  test_image = load_img(cott_plant, target_size = (150, 150)) # load image 
  print("@@ Got Image for prediction")
  
  test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
  result = model3.predict(test_image).round(3) # predict diseased palnt or not
  print('@@ Raw result = ', result)
  
  pred = np.argmax(result) # get the index of max value

  if pred == 0:
    return "Healthy Cotton Plant", 'healthy_plant_leaf.html' # if index 0 burned leaf
  elif pred == 1:
      return 'Diseased Cotton Plant', 'disease_plant.html' # # if index 1
  elif pred == 2:
      return 'Healthy Cotton Plant', 'healthy_plant.html'  # if index 2  fresh leaf
  else:
    return "Healthy Cotton Plant", 'healthy_plant.html' # if index 3
    
@application.route("/predict", methods = ['GET','POST'])
def predictl():
     if request.method == 'POST':
        file = request.files['image'] # fetch input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        path = os.path.join(application.config['UPLOAD_FOLDER'], filename)
        file.save(path)
        #file_path = os.path.join('static/user uploaded', filename)
        #file.save(file_path)
        
        print("@@ Predicting class......")
        pred, output_page = pred_cot_dieas(cott_plant=path)
              
        return render_template(output_page, pred_output = pred, user_image = path)


@application.route('/templates/fruit-disease.html', methods=['GET', "POST"])
def FD():
  return render_template('fruit-disease.html')

@application.route('/fpred', methods=['GET', "POST"])
def Fpredict():
  if request.method == 'POST':
        file = request.files['image'] # fetch input      
        filename = file.filename
        #full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        path = os.path.join(application.config['UPLOAD_FOLDER'], filename)
        file.save(path)
        image = cv2.imread(path)  
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (224, 224))
        img = np.asarray(image)
        cl = load_model(model4)
        img_class = cl.predict(img.reshape(1,224,224,3))[0]
        classes = ["Apple-(Bad)","Apple-(Good)","Apple-(Mixed)","Banana-(Bad)","Banana-(Good)","Banana-(Mixed)",
  "Guava-(Bad)","Guava-(Good)","Guava-(Mixed)","Lemon-(Mixed)","Lemon-(Bad)","Lemon-(Good)",
  "Orange-(Bad)","Orange-(Good)","Orange-(Mixed)","Pomegranate-(Bad)","Pomegranate-(Good)","Pomegranate-(Mixed)"]
        op = int(np.argmax(img_class))
        message = classes[op]
        if op%3 == 0 and op!= 9:
         warn = "Cannot Expect high market price" #if bad quality
        elif op == 1 or op == 4 or op == 7 or op == 11 or op == 13 or op == 16:
         warn = "Highest market price Likely"
        else:
         warn = "Higher market price is not likely"
        return render_template("fruit_pred.html", info=message, w = warn,user_image = path) 
  
  '''
  if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('static/user uploaded', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred, output_page = pred_cot_dieas(cott_plant=file_path)
              
        return render_template(output_page, pred_output = pred, user_image = file_path) '''
  
@application.route('/templates/about.html/', methods=['GET', "POST"])
def about():
  return render_template('about.html')

@application.route('/templates/contact.html/', methods=['GET', "POST"])
def contact():
  return render_template('contact.html')
  
#@application.route('/flaskapp/templates/Farm Life/market.html', methods=['GET', "POST"])
#def market():
#  return render_template('market.html')

# Run the app
if __name__ == "__main__":
  application.run()



