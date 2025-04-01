# AI-Based Crop Recommendation System 
A software application that suggests the best crops based on soil type, climate, and weather conditions, helping farmers maximize yield and efficiency.

## Dataset
Agriculture Crop Yield
This dataset contains agricultural data for 1,000,000 samples aimed at predicting crop yield (in tons per hectare) based on various factors.
[https://www.kaggle.com/datasets/samuelotiattakorah/agriculture-crop-yield?utm_source=chatgpt.com&select=crop_yield.csv](https://www.kaggle.com/datasets/samuelotiattakorah/agriculture-crop-yield?utm_source=chatgpt.com&select=crop_yield.csv)

## Models Used
Random Forest, XGBoost
Achieved high accuracy (R² around 0.87-0.88).

Feature importance analysis:
Identified Rainfall, Fertilizer, and Irrigation as the most influential factors impacting yield.

Visualization: 
Provided clear visual insights for key relationships.

**Key Factors Identified**
Rainfall (Rainfall_mm):
Strongest predictor, significantly influencing crop yield.
Suggests rainfall amount is critical for yield optimization.

Fertilizer Usage (Fertilizer_Used):
Second most impactful factor, clearly improving yields.

Indicates the substantial role fertilizer plays in crop productivity.
Irrigation (Irrigation_Used):

Third most influential feature, also noticeably boosting yields.
Suggests controlled water management greatly enhances crop yields.

Other Features (Temperature, Days to Harvest, Crop, Soil Type, Region, Weather Condition):
Relatively lower influence compared to rainfall and fertilizer/irrigation usage.
