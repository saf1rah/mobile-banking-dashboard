import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Dashboard Mobile Banking",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

/* =========================
BACKGROUND
========================= */

.stApp {
    background-color: #f5f7fa;
}

/* =========================
SIDEBAR
========================= */

section[data-testid="stSidebar"] {

    background: linear-gradient(
        180deg,
        #0f9d9d,
        #13b5b1
    );

    padding-top: 20px;
}

/* TEXT SIDEBAR */

section[data-testid="stSidebar"] * {

    color: white !important;
}

/* =========================
SELECTBOX FIX
========================= */

/* BOX */

div[data-baseweb="select"] {

    background-color: white !important;

    border-radius: 10px !important;
}

/* INSIDE BOX */

div[data-baseweb="select"] > div {

    background-color: white !important;

    color: black !important;

    border-radius: 10px !important;
}

/* SELECTED VALUE */

div[data-baseweb="select"] span {

    color: black !important;

    font-weight: 500 !important;
}

/* INPUT */

div[data-baseweb="input"] {

    color: black !important;
}

/* DROPDOWN */

div[role="listbox"] {

    background-color: white !important;

    border-radius: 10px !important;
}

/* OPTION */

div[role="option"] {

    color: black !important;

    background-color: white !important;
}

/* OPTION HOVER */

div[role="option"]:hover {

    background-color: #d1fae5 !important;

    color: black !important;
}

/* =========================
METRIC CARD
========================= */

[data-testid="stMetric"] {

    background-color: white;

    padding: 20px;

    border-radius: 15px;

    box-shadow: 0px 4px 10px rgba(0,0,0,0.08);

    border-left: 5px solid #0f9d9d;
}

/* LABEL */

[data-testid="stMetricLabel"] {

    color: #6b7280 !important;

    font-size: 18px !important;
}

/* VALUE */

[data-testid="stMetricValue"] {

    color: #111827 !important;

    font-size: 40px !important;

    font-weight: bold !important;
}

/* =========================
TITLE
========================= */

h1, h2, h3 {

    color: #1f2937;
}

/* =========================
TABLE
========================= */

[data-testid="stDataFrame"] {

    background-color: white;

    border-radius: 15px;

    padding: 10px;
}
            
/* =========================
FORCE SELECTBOX TEXT
========================= */

.stSelectbox * {

    color: black !important;
}

/* CURRENT VALUE */

.stSelectbox div {

    color: black !important;
}

/* INPUT */

.stSelectbox input {

    color: black !important;
}

/* SVG DROPDOWN ICON */

.stSelectbox svg {

    fill: black !important;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# DATA
# =====================================================

summary = pd.DataFrame({

    'Scenario': [
        'Normal',
        'Busy',
        'Improvement',
        'High Capacity'
    ],

    'Average Waiting Time': [
        4.12,
        6.84,
        3.91,
        2.76
    ],

    'Success Rate': [
        0.97,
        0.89,
        0.94,
        0.98
    ],

    'Drop Rate': [
        0.03,
        0.11,
        0.06,
        0.02
    ]
})

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("📋 Dashboard Menu")

selected_scenario = st.sidebar.selectbox(
    "Pilih Skenario",
    summary['Scenario']
)

chart_type = st.sidebar.selectbox(
    "Pilih Jenis Grafik",
    ["Bar Chart", "Line Chart"]
)

st.sidebar.markdown("---")

st.sidebar.info("""
Dashboard simulasi sistem antrean login mobile banking 
menggunakan metode Monte Carlo.
""")

# =====================================================
# FILTER DATA
# =====================================================

selected_data = summary[
    summary['Scenario'] == selected_scenario
]

# =====================================================
# TITLE
# =====================================================

st.title("📊 Dashboard Simulasi Login Mobile Banking")

st.markdown("""
Dashboard ini menampilkan hasil simulasi sistem antrean login mobile banking 
saat jam sibuk menggunakan metode Monte Carlo.
""")

# =====================================================
# METRIC CARDS
# =====================================================

st.subheader(f"Hasil Skenario: {selected_scenario}")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Average Waiting Time",
        round(
            float(selected_data['Average Waiting Time'].iloc[0]),
            2
        )
    )

with col2:
    st.metric(
        "Success Rate",
        round(
            float(selected_data['Success Rate'].iloc[0]),
            2
        )
    )

with col3:
    st.metric(
        "Drop Rate",
        round(
            float(selected_data['Drop Rate'].iloc[0]),
            2
        )
    )

# =====================================================
# TABLE
# =====================================================

st.subheader("📋 Tabel Perbandingan")

st.dataframe(
    summary,
    use_container_width=True
)

# =====================================================
# WAITING TIME CHART
# =====================================================

st.subheader("📈 Average Waiting Time")

fig1, ax1 = plt.subplots(figsize=(8, 4))

if chart_type == "Bar Chart":

    ax1.bar(
        summary['Scenario'],
        summary['Average Waiting Time']
    )

else:

    ax1.plot(
        summary['Scenario'],
        summary['Average Waiting Time'],
        marker='o',
        linewidth=3
    )

ax1.set_ylabel("Waiting Time")

st.pyplot(fig1)

# =====================================================
# SUCCESS RATE CHART
# =====================================================

st.subheader("✅ Success Rate")

fig2, ax2 = plt.subplots(figsize=(8, 4))

if chart_type == "Bar Chart":

    ax2.bar(
        summary['Scenario'],
        summary['Success Rate']
    )

else:

    ax2.plot(
        summary['Scenario'],
        summary['Success Rate'],
        marker='o',
        linewidth=3
    )

ax2.set_ylabel("Success Rate")

st.pyplot(fig2)

# =====================================================
# DROP RATE CHART
# =====================================================

st.subheader("❌ Drop Rate")

fig3, ax3 = plt.subplots(figsize=(8, 4))

if chart_type == "Bar Chart":

    ax3.bar(
        summary['Scenario'],
        summary['Drop Rate']
    )

else:

    ax3.plot(
        summary['Scenario'],
        summary['Drop Rate'],
        marker='o',
        linewidth=3
    )

ax3.set_ylabel("Drop Rate")

st.pyplot(fig3)

# =====================================================
# KESIMPULAN
# =====================================================

st.subheader("📌 Kesimpulan")

st.write("""
Hasil simulasi menunjukkan bahwa peningkatan kapasitas server 
dapat menurunkan waiting time dan meningkatkan success rate.

Skenario High Capacity memiliki performa terbaik dibandingkan 
skenario lainnya.
""")