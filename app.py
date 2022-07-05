# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 12:43:48 2022

@author: HP
"""
import streamlit as st
from streamlit_option_menu import option_menu
#import pandas as pd
#st.write("Mon Application Web Pour mes activitées Personneles")

#1. as sidebar menu
#with st.sidebar:
#    selected = option_menu(
#        menu_title = None,
#        options=["Home","Projects","Contact"],
#        icons = ["house","book","envelope"],
#        menu_icon = "cast",
#        default_index = 0,
#        orientation = "horizontal",
#        )

selected = option_menu(
    menu_title = None,
    options=["Home","Projects","Contact"],
    icons = ["house","book","envelope"],
    menu_icon = "cast",
    default_index = 0,
    orientation = "horizontal",
    )
if selected == "Home":
    st.title(f"tu as selectioné {selected}")
if selected == "Projects":
    st.title(f"tu as selectioné {selected}")
if selected == "Contact":
    st.title(f"tu as selectioné {selected}")