'''
This file and its contents have been informed and adapted 
from the Churnometer Walkthrough Project 2.
'''

import streamlit as st

from src.manage_files import load_housing_price_data
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

def page_price_study():

    # load data
    df = load_housing_price_data()

    # hard copied from sale price study notebook
    # The 5 variables that correlate to Sale Price
    # These variables will be tested on strength to predicting Sale Price
    corr_var_list = ['1stFlrSF', 'GarageArea', 'GrLivArea', 'OverallQual', 'TotalBsmtSF', 'YearBuilt']

    st.write("### House Attribute Correlation Study")
    st.info(
        f"* The client aims to understand how various house characteristics "
        f"are related to the sale price.\n"
        f"* They require visualizations of the correlations between selected "
        f"attributes and sale price to validate the findings."
    )
    
    # 
     # Data preview option
    if st.checkbox("View Housing Data"):
        st.write(
            f"* The dataset contains {df.shape[0]} rows and {df.shape[1]} columns. "
            f"Below are the first 10 records."
        )
        st.write(df.head(10))

    st.write("---")

    # Summary of correlation analysis
    st.write(
        f"* A correlation study was conducted using both Pearson and Spearman methods "
        f"to assess how specific variables relate to house sale prices.\n"
        f"* The variables with the strongest correlations were identified as: \n"
        f"  * **1stFlrSF, GarageArea, GrLivArea, OverallQual, TotalBsmtSF, YearBuilt**"
    )

    # Insights derived from the sale price analysis notebook
    st.info(
        f"#### Correlation Findings and Visualizations\n"
        f"* The following variables demonstrated strong correlations in the analysis:\n"
        f"* 1stFlrSF: First-floor square footage\n"
        f"* GrLivArea: Above-ground living area square footage\n"
        f"* OverallQual: Overall material and finish quality\n"
        f"* TotalBsmtSF: Total basement area in square footage\n"
        f"* GarageArea: Garage area in square footage\n"
        f"* YearBuilt: Year the house was constructed\n\n"
        f"* The plots confirm that these variables show a significant correlation, "
        f"indicating their potential for predicting the sale price."
    )
    
    # "EDA on the Correlated Variable List" section
    df_eda = df.filter(corr_var_list + ['SalePrice'])

    # Individual plots per variable
    if st.checkbox("Variable correlation Sale Price"):
        variable_correlation_to_sale_price(df_eda, corr_var_list)


def variable_correlation_to_sale_price(df_eda, corr_var_list):
    # function based on the "sale price study" notebook
    # "Visualize correlation to Sale Price" section
    target_var = 'SalePrice'
    for col in corr_var_list:
        plot_numerical(df_eda, col, target_var)
        st.write("\n\n")


def plot_numerical(df, col, target_var):
    # function based on "sale price study" notebook
    # "Visualize correlation to Sale Price" section

    fig, axes = plt.subplots(figsize=(15, 8))
    sns.regplot(data=df, x=col, y=target_var)
    plt.title(f"{col}", fontsize=20)
    st.pyplot(fig)  # st.pyplot() renders image, in notebook is plt.show()