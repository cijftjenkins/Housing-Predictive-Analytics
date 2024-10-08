'''
This file and its contents have been informed and adapted 
from the Churnometer Walkthrough Project 2.
'''

import streamlit as st
import pandas as pd
import pickle  # Importing pickle to handle .pkl files
from src.manage_files import load_clean_data
from src.predictive_analysis_ui import predict_sales_price

def load_pkl_file(file_path):
    """ Load a pickle file using the pickle module """
    with open(file_path, 'rb') as file:
        return pickle.load(file)

def page_price_predictor():
    # load predict sale price files
    ver = 'v3'
    path = f"outputs/ml_pipeline/{ver}"

    price_pipe = load_pkl_file(f"{path}/best_regressor_model.pkl")  # Loading using pickle
    price_features = (pd.read_csv(f"{path}/X_train.csv")
                      .columns
                      .to_list()
                      )
    feature_importance = list(pd.read_csv(f"{path}/feature_importance.csv")['Feature'])

    st.write("### Sale Price Prediction Interface")
    st.info(
        f"* The client would like to predict the house sales price"
        f" for her 4 inherited houses, and any other house in Ames, Iowa."
        )
    st.write("---")

    st.write("### Inherited houses price prediction")
    st.info(
        f"* Below we can find the details of the inherited "
        f"houses and their individual price predictions."
        )
    total_price = predict_inherited_house_price(price_pipe, price_features)
    total_price = "%.2f" % total_price
    st.info(
        f"The sum total sale price for all your "
        f"properties is ${total_price}"
        )
    st.write("---")

    # Live Data Production
    check_var = False
    if check_var:
        check_variables_for_UI(price_features)

    st.write("### Houses Price Predictor")
    st.info(
        f"* Input the values of a property that "
        f" you wish to make a **price prediction**."
        )
    X_live = DrawInputsWidgets()

    # Live Data Prediction
    if st.button("Run Predictive Analysis"):
        price_prediction = predict_sales_price(X_live,
                                              price_features,
                                              price_pipe)
        # logic for displaying the targetted sale price
        statement = (
            f"The predicted selling price for this house "
            f"is ${price_prediction}"
            )

        st.info(statement)


def predict_inherited_house_price(price_pipe, price_features):
    inherited = load_clean_data("inherited")
    row_count = len(inherited)
    inherited.index = range(1, row_count+1)
    total_price = 0
    for x in range(row_count):
        X_live = inherited.iloc[[x]]
        st.write(X_live)
        price_prediction = predict_sales_price(X_live,
                                              price_features,
                                              price_pipe)
        price_prediction = "%.2f" % price_prediction
        statement = (
            f"* Predicted selling price for targetted house "
            f"{x+1} is ${price_prediction}"
            )
        total_price += float(price_prediction)
        st.write(statement)
        
    return total_price

def check_variables_for_UI(price_features):
    import itertools

    # Widget inputs are the features used
    #  for all pipelines
    # We combine them only using unique values
    combined_features = set(
        list(
            itertools.chain(price_features)
            )
        )
    st.write(f"* There are {len(combined_features)} features"
             f"for the UI: \n\n {combined_features}")


def DrawInputsWidgets():

    # Dataset load
    df = load_clean_data("clean")
    percentageMin, percentageMax = 0.4, 2.0

    # Here we create input widgets for all focused features
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
   
    # Features to feed the ML pipeline
    # - values copied from check_variables_for_UI() result
    # '1stFlrSF', 'GarageArea', 'GrLivArea', 'YearBuilt'
 
    # create empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # from here on we draw the widget based on the variable
    # type (numerical or categorical) and set initial values
    with col1:
        feature = "1stFlrSF"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
        X_live[feature] = st_widget

    with col2:
        feature = "GrLivArea"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
        X_live[feature] = st_widget

    with col3:
        feature = "GarageArea"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
        X_live[feature] = st_widget

    with col4:
        feature = "YearBuilt"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
        X_live[feature] = st_widget

    st.write(X_live)

    return X_live
