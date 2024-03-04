import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np
sns.set(style='dark')

st.title("Dashboard Sederhana")
data13 = pd.read_csv("Dashboard/all_data.csv")

# Copy from Streamlit web
@st.cache_data
def load_data():
    return pd.DataFrame(
        {
            "Kategori Produk": ["cama_mesa_banho", "beleza_saude", "esporte_lazer",
                                "informatica_acessorios","moveis_decoracao"],
            "Telah di order sebanyak": [2561, 2373, 2057, 1848, 1710],
        }
    )

# Boolean to resize the dataframe, stored as a session state variable
st.checkbox("Perbesar Ukuran", value=False, key="use_container_width")

df = load_data()
st.dataframe(df, use_container_width=st.session_state.use_container_width)
with st.sidebar:
    st.image('Dashboard/bek.png', caption='Mari Berbelanja')
    