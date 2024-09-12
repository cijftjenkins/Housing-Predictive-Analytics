import streamlit as st

def predict_sales_price(X_live, features, pipeline):
    # from live data, subset features related to this pipeline
    X_live_sale_price = X_live.filter(features)

    # Check if pipeline has 'predict' method
    if not hasattr(pipeline, 'predict'):
        raise ValueError("The provided pipeline does not have a 'predict' method.")

    # predict
    sale_price_prediction = pipeline.predict(X_live_sale_price)

    return float(sale_price_prediction.round(2))
