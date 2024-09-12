"""
This file and its contents have been adapted and inspired 
from the Churnometer Walkthrough Project 2.
"""

import streamlit as st

def page_hypothesis():

    st.success(
        f"### Project Hypotheses and Approval\n\n"
        f"* The following hypotheses have been formulated for this project: \n"
        f" By evaluating comparable houses in Ames, Iowa, with attributes "
        f"similar to the client's inherited properties, we aim to make "
        f"accurate predictions regarding the potential sale prices.\n\n"

        f"1. The ground floor living area, first floor, basement, and garage are "
        f"expected to significantly influence the sale price.\n"
        f"2. The year the house was built and the overall quality of materials "
        f"(including finishes) are also anticipated to play a crucial role in determining "
        f"the house's sale price."
    )

    st.write("---")
    st.write("### Hypothesis Validation")
    st.write("The following summarizes the validation of these hypotheses:\n\n"
             "1. The correlation analysis between the Ground Living Area (GrLivArea) and Sale Price "
             "shows a strong positive relationship.\n"
             "* This indicates that larger living areas generally result in higher sale prices.\n\n"
             "* The scatter plot below illustrates a clear linear trend between GrLivArea and Sale Price.\n")
    st.image("images/GrLivArea.png")

    st.write("\n\n2. The correlation analysis between the Year Built and Overall Quality (OverallQual) "
             "relative to Sale Price reveals a weaker relationship.\n")
    st.write("* These factors show a weaker correlation with sale price, and the evidence "
             "does not strongly support their predictive power.\n\n")
    st.write("* The scatter plots below provide a visual representation of these weaker correlations.\n")
    st.image("images/OverallQual.png")
    st.image("images/YearBuilt.png")
