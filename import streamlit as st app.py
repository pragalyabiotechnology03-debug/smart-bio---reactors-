import streamlit as st
import pandas as pd
from datetime import datetime

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Smart Bioreactor",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# PROFESSIONAL CSS
# ==========================================================

st.markdown("""
<style>

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    .main-title {
        font-size: 36px;
        font-weight: 700;
        margin-bottom: 0px;
    }

    .subtitle {
        font-size: 16px;
        opacity: 0.7;
        margin-bottom: 25px;
    }

    .status {
        padding: 10px 15px;
        border-radius: 8px;
        border: 1px solid #444;
        margin-bottom: 15px;
    }

    .stage {
        padding: 18px 10px;
        border-radius: 12px;
        border: 1px solid #444;
        text-align: center;
        min-height: 120px;
    }

    .stage-title {
        font-size: 16px;
        font-weight: 700;
    }

    .stage-text {
        font-size: 13px;
        opacity: 0.7;
        margin-top: 8px;
    }

    .footer {
        text-align: center;
        opacity: 0.6;
        padding-top: 20px;
    }

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.markdown(
    '<div class="main-title">💧 SMART BIOREACTOR</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-IoT Enabled Household Greywater Treatment & Reuse System'
    '</div>',
    unsafe_allow_html=True
)

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.header("⚙️ System Control")

    operating_mode = st.selectbox(
        "Operating Mode",
        [
            "Automatic",
            "Manual",
            "Monitoring Only"
        ]
    )

    st.divider()

    st.subheader("Actuators")

    aeration = st.toggle(
        "Aeration",
        value=True
    )

    agitator = st.toggle(
        "Agitator",
        value=True
    )

    uv = st.toggle(
        "UV Disinfection",
        value=True
    )

    st.divider()

    st.subheader("Controller")

    st.write("ESP32")
    st.write("Python")
    st.write("Streamlit")

    st.divider()

    st.caption(
        "Sensor values shown now are demonstration values. "
        "ESP32 integration will provide real measurements."
    )

# ==========================================================
# SYSTEM STATUS
# ==========================================================

st.subheader("System Overview")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.success("🟢 System Online")

with c2:
    st.info(f"⚙️ {operating_mode}")

with c3:
    st.info(
        "Aeration: ON" if aeration else "Aeration: OFF"
    )

with c4:
    st.info(
        datetime.now().strftime("%H:%M:%S")
    )

# ==========================================================
# SENSOR DATA
# ==========================================================

# DEMO VALUES
# These will later come from ESP32.

ph = 7.20
temperature = 28.5
tds = 420
turbidity = 15.0
do = 3.2

st.subheader("📊 Real-Time Water Quality")

s1, s2, s3, s4, s5 = st.columns(5)

with s1:
    st.metric(
        "pH",
        f"{ph:.2f}"
    )

with s2:
    st.metric(
        "Temperature",
        f"{temperature:.1f} °C"
    )

with s3:
    st.metric(
        "TDS",
        f"{tds:.0f} ppm"
    )

with s4:
    st.metric(
        "Turbidity",
        f"{turbidity:.1f} NTU"
    )

with s5:
    st.metric(
        "DO",
        f"{do:.2f} mg/L"
    )

# ==========================================================
# TREATMENT PROCESS
# ==========================================================

st.subheader("🔄 Treatment Process")

p1, p2, p3, p4, p5 = st.columns(5)

stages = [
    ("①", "PRE-FILTER", "Oil & solids"),
    ("②", "BIOREACTOR", "Microbial treatment"),
    ("③", "MFC", "Energy recovery"),
    ("④", "POLISHING", "Biochar + Zeolite"),
    ("⑤", "DISINFECTION", "UV treatment")
]

for column, stage in zip(
    [p1, p2, p3, p4, p5],
    stages
):

    with column:

        st.markdown(
            f"""
            <div class="stage">
                <div class="stage-title">
                    {stage[0]} {stage[1]}
                </div>

                <div class="stage-text">
                    {stage[2]}
                </div>

                <br>
                🟢 ACTIVE
            </div>
            """,
            unsafe_allow_html=True
        )

# ==========================================================
# SENSOR TREND DATA
# ==========================================================

st.subheader("📈 Sensor Trends")

data = pd.DataFrame({

    "Time": [
        "10:00",
        "10:05",
        "10:10",
        "10:15",
        "10:20",
        "10:25",
        "10:30"
    ],

    "pH": [
        7.00,
        7.05,
        7.10,
        7.15,
        7.18,
        7.20,
        7.20
    ],

    "Temperature": [
        28.0,
        28.1,
        28.2,
        28.3,
        28.4,
        28.4,
        28.5
    ],

    "TDS": [
        450,
        445,
        438,
        432,
        428,
        424,
        420
    ],

    "Turbidity": [
        25,
        23,
        21,
        19,
        18,
        16,
        15
    ],

    "DO": [
        2.2,
        2.4,
        2.6,
        2.8,
        3.0,
        3.1,
        3.2
    ]
})

g1, g2 = st.columns(2)

with g1:

    st.write("**pH Trend**")

    st.line_chart(
        data.set_index("Time")[["pH"]]
    )

with g2:

    st.write("**Turbidity Trend**")

    st.line_chart(
        data.set_index("Time")[["Turbidity"]]
    )

g3, g4 = st.columns(2)

with g3:

    st.write("**Temperature Trend**")

    st.line_chart(
        data.set_index("Time")[["Temperature"]]
    )

with g4:

    st.write("**Dissolved Oxygen Trend**")

    st.line_chart(
        data.set_index("Time")[["DO"]]
    )

# ==========================================================
# AI WATER QUALITY
# ==========================================================

st.subheader("🤖 AI Water Quality Estimation")

a1, a2, a3 = st.columns(3)

# DEMONSTRATION VALUES ONLY
estimated_cod = 185
estimated_bod = 95
treatment_progress = 72

with a1:

    st.metric(
        "Estimated COD",
        f"{estimated_cod} mg/L"
    )

with a2:

    st.metric(
        "Estimated BOD₅",
        f"{estimated_bod} mg/L"
    )

with a3:

    st.metric(
        "Treatment Progress",
        f"{treatment_progress}%"
    )

st.warning(
    "AI COD/BOD values are demonstration values. "
    "Validated predictions will be added after laboratory "
    "data collection and machine-learning model training."
)

# ==========================================================
# MFC MONITORING
# ==========================================================

st.subheader("⚡ Microbial Fuel Cell")

mfc_voltage = 0.42
mfc_current = 8.5

mfc_power = mfc_voltage * (mfc_current / 1000)

m1, m2, m3 = st.columns(3)

with m1:

    st.metric(
        "Voltage",
        f"{mfc_voltage:.2f} V"
    )

with m2:

    st.metric(
        "Current",
        f"{mfc_current:.1f} mA"
    )

with m3:

    st.metric(
        "Power",
        f"{mfc_power * 1000:.2f} mW"
    )

st.caption(
    "MFC values shown are demonstration values until "
    "voltage/current sensors are integrated."
)

# ==========================================================
# DIAGNOSTICS
# ==========================================================

st.subheader("🔍 System Diagnostics")

diagnostics = pd.DataFrame({

    "Component": [
        "ESP32",
        "pH Sensor",
        "Temperature Sensor",
        "TDS Sensor",
        "Turbidity Sensor",
        "DO Sensor",
        "Aeration",
        "Agitator",
        "UV System"
    ],

    "Status": [
        "DEMO MODE",
        "READY",
        "READY",
        "READY",
        "READY",
        "READY",
        "ON" if aeration else "OFF",
        "ON" if agitator else "OFF",
        "ON" if uv else "OFF"
    ]
})

st.dataframe(
    diagnostics,
    use_container_width=True,
    hide_index=True
)

# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.markdown(
    '<div class="footer">'
    'SMART BIOREACTOR • Household Greywater Treatment & Reuse<br>'
    'ESP32 • IoT • AI • MFC • Sensor Monitoring'
    '</div>',
    unsafe_allow_html=True
)