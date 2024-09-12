

import streamlit as st

def page_summary():

    st.write("### Project Overview")

    # "Dataset Content" section
    st.info(
        f"**Project Dataset**\n"
        f"* The dataset used in this project comes from **[Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data)**.\n"
        f"* It contains nearly 1.5 thousand entries, representing housing data from Ames, Iowa. "
        f"The dataset includes various attributes of homes such as Year Built, Floor Areas, Garage, Basement, Kitchen, Lot, Porch, "
        f"and their corresponding sale prices, covering houses constructed between 1872 and 2010."
    )

    # "Business Requirements" section
    st.success(
        f"There are two requirements client asks for this project:\n"
        f"* 1 - The client wants to explore how different house characteristics influence sale prices.\n"
        f"  * They expect visual representations of correlations between key variables and sale prices.\n"
        f"* 2 - The client also wants to predict the sale prices of four inherited homes, as well as other properties in Ames, Iowa."
    )
