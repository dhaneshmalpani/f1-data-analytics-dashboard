import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🏎️ Formula 1 Data Analytics Dashboard")

# Load dataset
df = pd.read_csv("data/f1_merged.csv")

# Clean position column
df["position"] = pd.to_numeric(df["position"], errors="coerce")

# Create win column
df["win"] = df["position"] == 1

# -----------------------------
# Top Drivers
# -----------------------------
top_drivers = df.groupby("driver_name")["win"].sum().sort_values(ascending=False).head(10)

st.subheader("Top Drivers by Wins")

fig1, ax1 = plt.subplots()
top_drivers.plot(kind="bar", ax=ax1)
ax1.set_ylabel("Wins")
ax1.set_xlabel("Driver")

st.pyplot(fig1)

# -----------------------------
# Top Constructors
# -----------------------------
top_teams = df.groupby("name_y")["win"].sum().sort_values(ascending=False).head(10)

st.subheader("Top Constructors by Wins")

fig2, ax2 = plt.subplots()
top_teams.plot(kind="bar", ax=ax2, color="red")
ax2.set_ylabel("Wins")
ax2.set_xlabel("Constructor")

st.pyplot(fig2)

# -----------------------------
# Most Frequent Circuits
# -----------------------------
top_circuits = df.groupby("name_x").size().sort_values(ascending=False).head(10)

st.subheader("Circuits Hosting Most F1 Races")

fig3, ax3 = plt.subplots()
top_circuits.plot(kind="bar", ax=ax3, color="green")
ax3.set_ylabel("Number of Races")
ax3.set_xlabel("Circuit")

st.pyplot(fig3)