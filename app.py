import streamlit as st
import pandas as pd


view = [10,20,30]
st.write('# Youtube view') # 마크다운 가능

st.bar_chart(view)

sview = pd.Series(view)

sview