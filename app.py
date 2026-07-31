# app.py

import streamlit as st
import pandas as pd

from database import create_database, get_alerts


# -----------------------------
# PAGE CONFIGURATION
# -----------------------------

st.set_page_config(
    page_title="Network Topology Monitor",
    page_icon="🌐",
    layout="wide"
)


# -----------------------------
# INITIALIZE DATABASE
# -----------------------------

create_database()


# -----------------------------
# TITLE
# -----------------------------

st.title("🌐 Real-Time Network Topology Change Alerting System")

st.write(
    "Monitor network topology changes, detect suspicious devices "
    "and identify high-risk network events."
)

st.divider()


# -----------------------------
# SYSTEM STATUS
# -----------------------------

st.subheader("📡 Monitoring Status")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="System Status",
        value="Active"
    )

with col2:
    st.metric(
        label="Polling Interval",
        value="30 sec"
    )

with col3:
    st.metric(
        label="Connected Devices",
        value="4"
    )

with col4:
    st.metric(
        label="High Risk Alerts",
        value="1"
    )


st.divider()


# -----------------------------
# SAMPLE NETWORK TOPOLOGY
# -----------------------------

st.subheader("🖧 Current Network Topology")

st.code(
"""
                 Core-Switch
                  /       \\
               SW-1       SW-2
                |           |
             Server-1    Laptop-1
"""
)


st.divider()


# -----------------------------
# CURRENT DEVICES
# -----------------------------

st.subheader("💻 Discovered Devices")

devices = [
    {
        "Device": "Core-Switch",
        "Type": "Switch",
        "Status": "Online"
    },
    {
        "Device": "SW-1",
        "Type": "Switch",
        "Status": "Online"
    },
    {
        "Device": "Server-1",
        "Type": "Server",
        "Status": "Online"
    },
    {
        "Device": "Laptop-1",
        "Type": "Laptop",
        "Status": "Online"
    }
]

device_dataframe = pd.DataFrame(devices)

st.dataframe(
    device_dataframe,
    use_container_width=True,
    hide_index=True
)


st.divider()


# -----------------------------
# LIVE ALERT SECTION
# -----------------------------

st.subheader("🚨 Latest Network Alert")

sample_alert = {
    "risk": "HIGH",
    "device": "Unknown-Switch",
    "change": "NEW CONNECTION",
    "location": "Core-Switch Gi0/2"
}

if sample_alert["risk"] == "HIGH":

    st.error(
        f"""
        HIGH RISK TOPOLOGY CHANGE

        Device: {sample_alert['device']}

        Change: {sample_alert['change']}

        Location: {sample_alert['location']}
        """
    )


st.divider()


# -----------------------------
# DATABASE ALERT HISTORY
# -----------------------------

st.subheader("📜 Alert History")

alerts = get_alerts()

if alerts:

    alert_dataframe = pd.DataFrame(
        alerts,
        columns=[
            "ID",
            "Time",
            "Change Type",
            "Local Device",
            "Remote Device",
            "Local Port",
            "Remote Port",
            "Risk"
        ]
    )

    st.dataframe(
        alert_dataframe,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No alerts stored in the database.")


st.divider()


# -----------------------------
# MANUAL SCAN BUTTON
# -----------------------------

st.subheader("🔍 Network Scan")

if st.button(
    "Scan Network",
    type="primary"
):

    st.success(
        "Network scan completed successfully."
    )