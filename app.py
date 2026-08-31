import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Banking Customer Churn Dashboard",
    layout="wide"
)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('data/raw/Bank Customer Churn Prediction.csv')
    return df

df = load_data()

# ----------------- SIDEBAR FILTERS -----------------
st.sidebar.header("🔍 Dashboard Filters")

country_filter = st.sidebar.multiselect(
    "Select Country:",
    options=df['country'].unique(),
    default=df['country'].unique()
)

gender_filter = st.sidebar.multiselect(
    "Select Gender:",
    options=df['gender'].unique(),
    default=df['gender'].unique()
)

# Apply filters
filtered_df = df[
    (df['country'].isin(country_filter)) & 
    (df['gender'].isin(gender_filter))
]

# ----------------- MAIN DASHBOARD -----------------
st.title("🏦 Banking Customer Churn & Retention Analytics")
st.markdown("Interactive executive dashboard monitoring customer attrition, revenue risk, and risk segmentation.")

# KPI Cards
total_customers = len(filtered_df)
churned_customers = int(filtered_df['churn'].sum())
churn_rate = (churned_customers / total_customers * 100) if total_customers > 0 else 0
total_lost_balance = filtered_df[filtered_df['churn'] == 1]['balance'].sum()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Customers", f"{total_customers:,}")
col2.metric("Churned Customers", f"{churned_customers:,}")
col3.metric("Churn Rate", f"{churn_rate:.2f}%")
col4.metric("Capital at Risk / Lost", f"${total_lost_balance:,.2f}")

st.divider()

# ----------------- CHARTS SECTION -----------------
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("Churn Rate by Geography")
    geo_df = filtered_df.groupby('country')['churn'].mean().reset_index()
    geo_df['churn_rate_pct'] = geo_df['churn'] * 100
    fig_geo = px.bar(
        geo_df, 
        x='country', 
        y='churn_rate_pct', 
        color='country',
        text_auto='.2f',
        labels={'churn_rate_pct': 'Churn Rate (%)', 'country': 'Country'},
        color_discrete_sequence=px.colors.qualitative.Safe
    )
    st.plotly_chart(fig_geo, use_container_width=True)

with row1_col2:
    st.subheader("Product Holdings vs. Attrition")
    prod_df = filtered_df.groupby('products_number')['churn'].agg(['count', 'mean']).reset_index()
    prod_df['churn_rate_pct'] = prod_df['mean'] * 100
    fig_prod = px.bar(
        prod_df, 
        x='products_number', 
        y='churn_rate_pct', 
        text_auto='.2f',
        labels={'products_number': 'Number of Products', 'churn_rate_pct': 'Churn Rate (%)'},
        color='churn_rate_pct',
        color_continuous_scale='Reds'
    )
    st.plotly_chart(fig_prod, use_container_width=True)

row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.subheader("Age Distribution by Churn Status")
    fig_age = px.histogram(
        filtered_df, 
        x='age', 
        color=filtered_df['churn'].map({0: 'Retained', 1: 'Churned'}),
        barmode='overlay',
        nbins=30,
        labels={'color': 'Status', 'age': 'Customer Age'}
    )
    st.plotly_chart(fig_age, use_container_width=True)

with row2_col2:
    st.subheader("Active Membership Impact")
    active_df = filtered_df.groupby('active_member')['churn'].mean().reset_index()
    active_df['active_member'] = active_df['active_member'].map({1: 'Active Member', 0: 'Inactive Member'})
    active_df['churn_rate_pct'] = active_df['churn'] * 100
    fig_active = px.pie(
        active_df, 
        names='active_member', 
        values='churn_rate_pct', 
        color='active_member',
        hole=0.4,
        color_discrete_map={'Active Member': '#2ecc71', 'Inactive Member': '#e74c3c'}
    )
    st.plotly_chart(fig_active, use_container_width=True)