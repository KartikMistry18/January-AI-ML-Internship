import streamlit as st
import numpy as np
import pandas as pd

import pickle
from streamlit_option_menu import option_menu



data= pd.read_csv("Cleaned_Car_data.csv")

pipe = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

selected = option_menu(
    menu_title=None,
    options=["Predict Price", "About", "Contribute to Dataset"],
    icons=["search", "search", "book"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)



if selected == "Predict Price":
    
    st.title("CAR PRICE PREDICTION SYSTEM")
    name = st.selectbox("Car Name",['Hyundai Santro Xing', 'Mahindra Jeep CL550', 'Hyundai Grand i10',
       'Ford EcoSport Titanium', 'Ford Figo', 'Hyundai Eon',
       'Ford EcoSport Ambiente', 'Maruti Suzuki Alto',
       'Skoda Fabia Classic', 'Maruti Suzuki Stingray',
       'Hyundai Elite i20', 'Mahindra Scorpio SLE', 'Audi A8', 'Audi Q7',
       'Mahindra Scorpio S10', 'Hyundai i20 Sportz',
       'Maruti Suzuki Vitara', 'Mahindra Bolero DI',
       'Maruti Suzuki Swift', 'Maruti Suzuki Wagon', 'Toyota Innova 2.0',
       'Renault Lodgy 85', 'Skoda Yeti Ambition', 'Maruti Suzuki Baleno',
       'Renault Duster 110', 'Renault Duster 85', 'Honda City 1.5',
       'Maruti Suzuki Dzire', 'Honda Amaze', 'Honda Amaze 1.5',
       'Honda City', 'Datsun Redi GO', 'Maruti Suzuki SX4',
       'Mitsubishi Pajero Sport', 'Honda City ZX', 'Tata Indigo eCS',
       'Volkswagen Polo Highline', 'Chevrolet Spark LS',
       'Renault Duster 110PS', 'Mini Cooper S', 'Skoda Fabia 1.2L',
       'Renault Duster', 'Mahindra Scorpio S4', 'Mahindra Scorpio VLX',
       'Mahindra Quanto C8', 'Ford EcoSport', 'Honda Brio',
       'Volkswagen Vento Highline', 'Hyundai i20 Magna',
       'Toyota Corolla Altis', 'Hyundai Verna Transform', 'BMW 3 Series',
       'Maruti Suzuki A', 'Toyota Etios GD', 'Ford Figo Diesel',
       'Chevrolet Beat LT', 'BMW 7 Series', 'Mahindra XUV500 W8',
       'Hyundai i10 Magna', 'Hyundai Verna Fluidic',
       'Maruti Suzuki Ertiga', 'Honda Amaze 1.2', 'Hyundai i20 Asta',
       'Maruti Suzuki Eeco', 'Maruti Suzuki Esteem', 'Maruti Suzuki Ritz',
       'Toyota Etios Liva', 'Chevrolet Spark', 'Nissan Micra XV',
       'Chevrolet Beat', 'Ford EcoSport Trend', 'Tata Indica V2',
       'Hindustan Motors Ambassador', 'Toyota Innova 2.5',
       'Volkswagen Jetta Highline', 'Volkswagen Polo Comfortline',
       'Volkswagen Polo', 'Mahindra Scorpio', 'Nissan Sunny',
       'Renault Kwid', 'Chevrolet Spark LT', 'Fiat Punto Emotion',
       'Hyundai i10 Sportz', 'Chevrolet Beat LS', 'Tata Indigo CS',
       'Hyundai Eon Era', 'Mahindra XUV500', 'Ford Fiesta', 'Hyundai i20',
       'Hyundai Fluidic Verna', 'Fiat Petra ELX', 'Maruti Suzuki Ciaz',
       'Maruti Suzuki Zen', 'Hyundai Creta 1.6', 'Mahindra Scorpio SLX',
       'Tata Nano Cx', 'Tata Sumo Victa', 'Volkswagen Passat Diesel',
       'Renault Scala RxL', 'Hyundai i20 Active', 'Mahindra Xylo E4',
       'Mahindra Jeep MM', 'Mahindra Bolero SLE', 'Force Motors Force',
       'Toyota Etios', 'Honda City VX', 'Mahindra Thar CRDe',
       'Audi A4 1.8', 'Mercedes Benz GLA', 'Land Rover Freelander',
       'Renault Kwid RXT', 'Tata Aria Pleasure', 'Mercedes Benz B',
       'Datsun GO T', 'Honda Jazz VX', 'Chevrolet Tavera Neo',
       'Hyundai Eon Sportz', 'Tata Sumo Gold', 'Chevrolet Enjoy 1.4',
       'Nissan Terrano XL', 'Maruti Suzuki Maruti', 'Renault Kwid 1.0',
       'Hyundai Accent GLX', 'Mahindra TUV300 T4', 'Honda Accord',
       'Mahindra Scorpio 2.6', 'Honda Mobilio', 'Skoda Laura',
       'Tata Manza Aura', 'Chevrolet Sail UVA', 'Audi A4 2.0',
       'Hyundai Elantra SX', 'Mahindra KUV100 K8', 'Hyundai i10',
       'Hyundai Accent', 'Hyundai Verna', 'Toyota Fortuner',
       'Mahindra Bolero Power', 'Skoda Rapid Elegance',
       'Tata Vista Quadrajet', 'Chevrolet Beat Diesel',
       'Hyundai Verna 1.4', 'Maruti Suzuki Versa', 'Tata Indigo LX',
       'Volkswagen Vento Konekt', 'Mercedes Benz C', 'Maruti Suzuki Omni',
       'Hyundai Sonata Transform', 'Honda Jazz S', 'Mahindra Scorpio W',
       'Honda Brio V', 'Mahindra TUV300 T8', 'Nissan X Trail',
       'Ford Ikon 1.3', 'Toyota Fortuner 3.0', 'Tata Manza ELAN',
       'Mercedes Benz A', 'Tata Indigo LS', 'Hyundai Verna 1.6',
       'BMW 5 Series', 'Skoda Superb 1.8', 'Audi Q3 2.0',
       'Ford Figo Duratorq', 'Mahindra Logan Diesel', 'Tata Nano GenX',
       'Honda City SV', 'Ford Figo Petrol', 'Toyota Corolla H2',
       'Hyundai Xcent Base', 'Hyundai Accent Executive', 'Tata Zest XE',
       'Mahindra XUV500 W6', 'Tata Tigor Revotron', 'Maruti Suzuki 800',
       'Honda Mobilio S', 'Tata Indica', 'Honda Brio VX', 'Tata Nano Lx',
       'Jaguar XE XE', 'Hyundai Eon Magna', 'Hyundai Eon D',
       'Maruti Suzuki Estilo', 'Mahindra Scorpio Vlx',
       'Mitsubishi Lancer 1.8', 'Ford Fiesta SXi', 'Audi A6 2.0',
       'Hyundai Getz Prime', 'Hyundai Santro', 'Chevrolet Beat PS',
       'BMW X1 xDrive20d', 'Tata Nano', 'Chevrolet Cruze LTZ',
       'Mahindra XUV500 W10', 'Hyundai Accent GLE', 'Force Motors One',
       'Chevrolet Spark 1.0', 'Renault Duster 85PS', 'Chevrolet Enjoy',
       'Jeep Wrangler Unlimited', 'Hyundai Verna VGT',
       'Maruti Suzuki Celerio', 'Tata Zest Quadrajet', 'Hyundai i10 Era',
       'Tata Indigo Marina', 'Hyundai Xcent SX', 'Tata Nano LX',
       'Mahindra Xylo E8', 'Tata Manza Aqua', 'Tata Venture EX',
       'Skoda Octavia Classic', 'Ford Ikon 1.6', 'Nissan Sunny XL',
       'Volkswagen Polo Trendline', 'Hyundai Elantra 1.8',
       'Tata Indica eV2', 'Jaguar XF 2.2', 'Audi Q5 2.0',
       'BMW X1 sDrive20d', 'Maruti Suzuki S',
       'Volkswagen Vento Comfortline', 'Mahindra KUV100',
       'Volkswagen Jetta Comfortline', 'Volvo S80 Summum', 'BMW X1',
       'Renault Duster RxL', 'Honda WR V', 'Mahindra Scorpio LX',
       'Audi A3 Cabriolet', 'Hyundai Santro AE', 'Mahindra Xylo D2',
       'Hyundai Getz GLE', 'Nissan Micra XL', 'Chevrolet Tavera LS',
       'Tata Tiago Revotron', 'Tata Tiago Revotorq', 'Ford Fusion 1.4',
       'Fiat Linea Emotion', 'Toyota Corolla', 'Tata Sumo Grande',
       'Volkswagen Polo Highline1.2L', 'Hyundai Creta', 'Tata Bolt XM',
       'Datsun Go Plus', 'Ford Endeavor 4x4', 'Mahindra Logan',
       'Chevrolet Sail 1.2', 'Tata Manza', 'Toyota Etios G',
       'Toyota Qualis', 'Mahindra Quanto C4', 'Hyundai i20 Select',
       'Hyundai Getz', 'Skoda Fabia', 'Tata Zest XM'], index=0)
    
    company = st.selectbox("Company",['Hyundai', 'Mahindra', 'Ford', 'Maruti', 'Skoda', 'Audi', 'Toyota',
       'Renault', 'Honda', 'Datsun', 'Mitsubishi', 'Tata', 'Volkswagen',
       'Chevrolet', 'Mini', 'BMW', 'Nissan', 'Hindustan', 'Fiat', 'Force',
       'Mercedes', 'Land', 'Jaguar', 'Jeep', 'Volvo'], index=0)

    year = st.number_input("Year",min_value=2000, max_value=2024,step=1)
    
    kms_driven = st.number_input("Kms Driven",min_value=0, max_value=10000000,step=1000)

    fuel_type = st.selectbox("Fuel Type",['Petrol','Diesel'], index=0)

    input_data = pd.DataFrame({
        'name': [name],
        'company': [company],
        'year': [year],
        'kms_driven': [kms_driven],
        'fuel_type': [fuel_type]
    })

    if st.button("Predict"):
        pred = pipe.predict(input_data)
        st.write(pred)
    

    

if selected == "About":

    st.image("merc.jpg")
    st.header("What is Car Price Prediction System?")

    st.write(
        "A Car Price Prediction System employs machine learning algorithms to forecast car prices by analyzing diverse features and parameters. By tapping into historical data encompassing car sales and prevailing market trends, these systems extrapolate potential prices for specific vehicles. The process begins with collecting a comprehensive dataset that includes details like brand, model, manufacturing year, mileage, and engine specifications, alongside corresponding sale prices. Following data preprocessing to ensure consistency and handle outliers, feature selection identifies the most pertinent variables influencing car prices."
        "The chosen machine learning algorithm is then trained on this refined dataset, discerning patterns and relationships between features and the target variable - the car prices. Evaluation metrics such as Mean Squared Error or R-squared gauge the model's accuracy on unseen data. Once trained and validated, the model serves as a predictive tool for estimating car prices based on input features. These systems benefit both buyers and sellers in the automotive market, providing insights into fair market values and enabling data-driven pricing strategies. Ultimately, Car Price Prediction Systems contribute to a transparent and informed automotive marketplace, enhancing decision-making for consumers and industry stakeholders alike."
    )

    st.header("Key Components of this System")
    st.write(
        "Data Collection: Gather a dataset containing information on various cars, including features such as brand, model, year of manufacture, mileage, engine type, fuel efficiency, and other relevant specifications. The dataset should also include the corresponding sale prices."
    )
    
    st.write(
        "Data Preprocessing: Clean and preprocess the data to handle missing values, outliers, and ensure consistency. This step may involve data normalization, encoding categorical variables, and other techniques to make the data suitable for machine learning algorithms."
    )

    st.write(
        "Feature Selection: Identify the most relevant features that contribute to the pricing of cars. Not all features may have equal importance in determining the price, and feature selection helps in improving the model's accuracy and efficiency."
    )

    st.write(
        "Model Training: Choose a machine learning algorithm (such as linear regression, decision trees, random forests, or neural networks) and train the model using the preprocessed data. The model learns the patterns and relationships between the features and the target variable (car prices)."
    )

    st.write(
        "Model Evaluation: Assess the model's performance using a separate set of data that it hasn't seen during training. Common evaluation metrics include Mean Squared Error (MSE), Mean Absolute Error (MAE), or R-squared."
    )

    st.write(
        "Prediction: Once the model is trained and evaluated, it can be used to make predictions on new or unseen data. In the context of a Car Price Prediction System, this means providing information about a car, and the model will estimate its price based on the learned patterns."
    )


if selected == "Contribute to Dataset":

    st.header("Contribute to our dataset")
    
    name = st.selectbox("Car Name",['Hyundai Santro Xing', 'Mahindra Jeep CL550', 'Hyundai Grand i10',
       'Ford EcoSport Titanium', 'Ford Figo', 'Hyundai Eon',
       'Ford EcoSport Ambiente', 'Maruti Suzuki Alto',
       'Skoda Fabia Classic', 'Maruti Suzuki Stingray',
       'Hyundai Elite i20', 'Mahindra Scorpio SLE', 'Audi A8', 'Audi Q7',
       'Mahindra Scorpio S10', 'Hyundai i20 Sportz',
       'Maruti Suzuki Vitara', 'Mahindra Bolero DI',
       'Maruti Suzuki Swift', 'Maruti Suzuki Wagon', 'Toyota Innova 2.0',
       'Renault Lodgy 85', 'Skoda Yeti Ambition', 'Maruti Suzuki Baleno',
       'Renault Duster 110', 'Renault Duster 85', 'Honda City 1.5',
       'Maruti Suzuki Dzire', 'Honda Amaze', 'Honda Amaze 1.5',
       'Honda City', 'Datsun Redi GO', 'Maruti Suzuki SX4',
       'Mitsubishi Pajero Sport', 'Honda City ZX', 'Tata Indigo eCS',
       'Volkswagen Polo Highline', 'Chevrolet Spark LS',
       'Renault Duster 110PS', 'Mini Cooper S', 'Skoda Fabia 1.2L',
       'Renault Duster', 'Mahindra Scorpio S4', 'Mahindra Scorpio VLX',
       'Mahindra Quanto C8', 'Ford EcoSport', 'Honda Brio',
       'Volkswagen Vento Highline', 'Hyundai i20 Magna',
       'Toyota Corolla Altis', 'Hyundai Verna Transform', 'BMW 3 Series',
       'Maruti Suzuki A', 'Toyota Etios GD', 'Ford Figo Diesel',
       'Chevrolet Beat LT', 'BMW 7 Series', 'Mahindra XUV500 W8',
       'Hyundai i10 Magna', 'Hyundai Verna Fluidic',
       'Maruti Suzuki Ertiga', 'Honda Amaze 1.2', 'Hyundai i20 Asta',
       'Maruti Suzuki Eeco', 'Maruti Suzuki Esteem', 'Maruti Suzuki Ritz',
       'Toyota Etios Liva', 'Chevrolet Spark', 'Nissan Micra XV',
       'Chevrolet Beat', 'Ford EcoSport Trend', 'Tata Indica V2',
       'Hindustan Motors Ambassador', 'Toyota Innova 2.5',
       'Volkswagen Jetta Highline', 'Volkswagen Polo Comfortline',
       'Volkswagen Polo', 'Mahindra Scorpio', 'Nissan Sunny',
       'Renault Kwid', 'Chevrolet Spark LT', 'Fiat Punto Emotion',
       'Hyundai i10 Sportz', 'Chevrolet Beat LS', 'Tata Indigo CS',
       'Hyundai Eon Era', 'Mahindra XUV500', 'Ford Fiesta', 'Hyundai i20',
       'Hyundai Fluidic Verna', 'Fiat Petra ELX', 'Maruti Suzuki Ciaz',
       'Maruti Suzuki Zen', 'Hyundai Creta 1.6', 'Mahindra Scorpio SLX',
       'Tata Nano Cx', 'Tata Sumo Victa', 'Volkswagen Passat Diesel',
       'Renault Scala RxL', 'Hyundai i20 Active', 'Mahindra Xylo E4',
       'Mahindra Jeep MM', 'Mahindra Bolero SLE', 'Force Motors Force',
       'Toyota Etios', 'Honda City VX', 'Mahindra Thar CRDe',
       'Audi A4 1.8', 'Mercedes Benz GLA', 'Land Rover Freelander',
       'Renault Kwid RXT', 'Tata Aria Pleasure', 'Mercedes Benz B',
       'Datsun GO T', 'Honda Jazz VX', 'Chevrolet Tavera Neo',
       'Hyundai Eon Sportz', 'Tata Sumo Gold', 'Chevrolet Enjoy 1.4',
       'Nissan Terrano XL', 'Maruti Suzuki Maruti', 'Renault Kwid 1.0',
       'Hyundai Accent GLX', 'Mahindra TUV300 T4', 'Honda Accord',
       'Mahindra Scorpio 2.6', 'Honda Mobilio', 'Skoda Laura',
       'Tata Manza Aura', 'Chevrolet Sail UVA', 'Audi A4 2.0',
       'Hyundai Elantra SX', 'Mahindra KUV100 K8', 'Hyundai i10',
       'Hyundai Accent', 'Hyundai Verna', 'Toyota Fortuner',
       'Mahindra Bolero Power', 'Skoda Rapid Elegance',
       'Tata Vista Quadrajet', 'Chevrolet Beat Diesel',
       'Hyundai Verna 1.4', 'Maruti Suzuki Versa', 'Tata Indigo LX',
       'Volkswagen Vento Konekt', 'Mercedes Benz C', 'Maruti Suzuki Omni',
       'Hyundai Sonata Transform', 'Honda Jazz S', 'Mahindra Scorpio W',
       'Honda Brio V', 'Mahindra TUV300 T8', 'Nissan X Trail',
       'Ford Ikon 1.3', 'Toyota Fortuner 3.0', 'Tata Manza ELAN',
       'Mercedes Benz A', 'Tata Indigo LS', 'Hyundai Verna 1.6',
       'BMW 5 Series', 'Skoda Superb 1.8', 'Audi Q3 2.0',
       'Ford Figo Duratorq', 'Mahindra Logan Diesel', 'Tata Nano GenX',
       'Honda City SV', 'Ford Figo Petrol', 'Toyota Corolla H2',
       'Hyundai Xcent Base', 'Hyundai Accent Executive', 'Tata Zest XE',
       'Mahindra XUV500 W6', 'Tata Tigor Revotron', 'Maruti Suzuki 800',
       'Honda Mobilio S', 'Tata Indica', 'Honda Brio VX', 'Tata Nano Lx',
       'Jaguar XE XE', 'Hyundai Eon Magna', 'Hyundai Eon D',
       'Maruti Suzuki Estilo', 'Mahindra Scorpio Vlx',
       'Mitsubishi Lancer 1.8', 'Ford Fiesta SXi', 'Audi A6 2.0',
       'Hyundai Getz Prime', 'Hyundai Santro', 'Chevrolet Beat PS',
       'BMW X1 xDrive20d', 'Tata Nano', 'Chevrolet Cruze LTZ',
       'Mahindra XUV500 W10', 'Hyundai Accent GLE', 'Force Motors One',
       'Chevrolet Spark 1.0', 'Renault Duster 85PS', 'Chevrolet Enjoy',
       'Jeep Wrangler Unlimited', 'Hyundai Verna VGT',
       'Maruti Suzuki Celerio', 'Tata Zest Quadrajet', 'Hyundai i10 Era',
       'Tata Indigo Marina', 'Hyundai Xcent SX', 'Tata Nano LX',
       'Mahindra Xylo E8', 'Tata Manza Aqua', 'Tata Venture EX',
       'Skoda Octavia Classic', 'Ford Ikon 1.6', 'Nissan Sunny XL',
       'Volkswagen Polo Trendline', 'Hyundai Elantra 1.8',
       'Tata Indica eV2', 'Jaguar XF 2.2', 'Audi Q5 2.0',
       'BMW X1 sDrive20d', 'Maruti Suzuki S',
       'Volkswagen Vento Comfortline', 'Mahindra KUV100',
       'Volkswagen Jetta Comfortline', 'Volvo S80 Summum', 'BMW X1',
       'Renault Duster RxL', 'Honda WR V', 'Mahindra Scorpio LX',
       'Audi A3 Cabriolet', 'Hyundai Santro AE', 'Mahindra Xylo D2',
       'Hyundai Getz GLE', 'Nissan Micra XL', 'Chevrolet Tavera LS',
       'Tata Tiago Revotron', 'Tata Tiago Revotorq', 'Ford Fusion 1.4',
       'Fiat Linea Emotion', 'Toyota Corolla', 'Tata Sumo Grande',
       'Volkswagen Polo Highline1.2L', 'Hyundai Creta', 'Tata Bolt XM',
       'Datsun Go Plus', 'Ford Endeavor 4x4', 'Mahindra Logan',
       'Chevrolet Sail 1.2', 'Tata Manza', 'Toyota Etios G',
       'Toyota Qualis', 'Mahindra Quanto C4', 'Hyundai i20 Select',
       'Hyundai Getz', 'Skoda Fabia', 'Tata Zest XM'], index=0)
    
    company = st.selectbox("Company",['Hyundai', 'Mahindra', 'Ford', 'Maruti', 'Skoda', 'Audi', 'Toyota',
       'Renault', 'Honda', 'Datsun', 'Mitsubishi', 'Tata', 'Volkswagen',
       'Chevrolet', 'Mini', 'BMW', 'Nissan', 'Hindustan', 'Fiat', 'Force',
       'Mercedes', 'Land', 'Jaguar', 'Jeep', 'Volvo'], index=0)

    year = st.number_input("Year",min_value=2000, max_value=2024,step=1)
    
    kms_driven = st.number_input("Kms Driven",min_value=0, max_value=10000000,step=1000)

    fuel_type = st.selectbox("Fuel Type",['Petrol','Diesel'], index=0)

    if st.button("Submit"):
        to_add={"Car Name":[name], "Company":[company], "Year":[year], "Kms Driven":[kms_driven], "Fuel_type":[fuel_type]}
        to_add=pd.DataFrame(to_add)
        to_add.to_csv("Cleaned_Car_data.csv", mode = 'a', header=False, index=False)
        st.success("Submitted")
    if st.checkbox("Show Table"):
        st.table(data)