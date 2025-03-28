
import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

# Load models and encoders
crop_classifier = joblib.load('crop_recommendation_model.pkl')
yield_regressor = joblib.load('yield_prediction_model.pkl')
crop_le = joblib.load('label_encoder_Crop.pkl')

# Customizing Page
st.set_page_config(page_title='Smart Crop & Yield Advisor', layout='wide')

st.title('🌾 Smart Crop & Yield Advisor')
st.markdown("### Optimize your farm's productivity by receiving instant crop recommendations and yield predictions.")

# Sidebar for inputs
st.sidebar.header("🌦️ Enter Farm Details")
region = st.sidebar.selectbox('Region', ['North', 'South', 'East', 'West'])
soil_type = st.sidebar.selectbox('Soil Type', ['Sandy Loam', 'Loam', 'Clay', 'Sand', 'Silt', 'Black Soil'])
climate = st.sidebar.selectbox('Climate', ['Sunny', 'Rainy'])
rainfall = st.sidebar.slider('Rainfall (mm)', 200.0, 2000.0, 500.0)
temperature = st.sidebar.slider('Temperature (°C)', 10.0, 40.0, 25.0)
fertilizer_used = 1  # always used based on dataset
days_to_harvest = st.sidebar.slider('Days to Harvest', 90, 210, 120)

# Prepare input dataframe with correct column order
input_data = pd.DataFrame({
    'Region': [region],
    'Soil_Type': [soil_type],
    'Rainfall_mm': [rainfall],
    'Temperature_Celsius': [temperature],
    'Fertilizer_Used': [fertilizer_used],
    'Climate': [climate],
    'Days_to_Harvest': [days_to_harvest]
})[['Region', 'Soil_Type', 'Rainfall_mm', 'Temperature_Celsius', 'Fertilizer_Used', 'Climate', 'Days_to_Harvest']]

# Encode categorical features
for col in ['Region', 'Soil_Type', 'Climate']:
    le = joblib.load(f'label_encoder_{col}.pkl')
    input_data[col] = le.transform(input_data[col])

# Prediction button
if st.sidebar.button('🚀 Get Recommendations'):
    crop_pred_encoded = crop_classifier.predict(input_data)[0]
    predicted_crop = crop_le.inverse_transform([crop_pred_encoded])[0]
    yield_pred = yield_regressor.predict(input_data)[0]

    # Results section
    col1, col2 = st.columns(2)

    with col1:
        st.subheader('🌱 Recommended Crop')
        st.success(f'**{predicted_crop}**')

        st.subheader('📈 Estimated Yield')
        st.info(f'**{yield_pred:.2f} tons per hectare**')

    with col2:
        # Visual representation of yield prediction
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=yield_pred,
            title={'text': "Yield (tons/hectare)"},
            gauge={'axis': {'range': [0, 12]},
                   'bar': {'color': "darkgreen"},
                   'steps': [
                       {'range': [0, 4], 'color': "red"},
                       {'range': [4, 8], 'color': "yellow"},
                       {'range': [8, 12], 'color': "lightgreen"}]
                   }))
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown('---')
    st.markdown('🔍 **Analysis:** Your yield prediction falls within a certain range indicating productivity potential. Adjust farm inputs to see different outcomes.')
