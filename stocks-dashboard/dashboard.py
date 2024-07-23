# filename: dashboard.py

import pandas as pd
import numpy as np
import plotly.express as px
import panel as pn
import datetime

# Sample static dataset
def get_sales_data():
    np.random.seed(42)
    products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    sales_figures = np.random.randint(100, 1000, size=len(products))
    return pd.DataFrame({'Product': products, 'Sales': sales_figures})

# Initialize sales data
df = get_sales_data()

# Plotly Express bar chart
def create_bar_chart(df):
    fig = px.bar(df, x='Product', y='Sales', title='Sales Data')
    fig.update_layout(xaxis_title='Product', yaxis_title='Sales')
    return fig

# Panel widgets
products = pn.widgets.MultiChoice(name='Products', options=['Product A', 'Product B', 'Product C', 'Product D', 'Product E'], value=['Product A', 'Product B', 'Product C', 'Product D', 'Product E'])
date_range = pn.widgets.DateRangeSlider(name='Date Range', start=datetime.date(2021, 1, 1), end=datetime.date.today(), value=(datetime.date(2021, 1, 1), datetime.date.today()))
refresh_button = pn.widgets.Button(name='Refresh Data')

# Callback function to update the chart
@pn.depends(products, date_range, refresh_button)
def update_chart(products, date_range, refresh_button):
    filtered_df = df[df['Product'].isin(products)]
    fig = create_bar_chart(filtered_df)
    return pn.pane.Plotly(fig)

# Configuration Tab
config_tab = pn.Column(
    '## Configuration',
    products,
    date_range,
    refresh_button,
    '### Instructions',
    "Use the widgets above to modify the list of products, change the date range for sales data, and refresh the chart by clicking the 'Refresh Data' button."
)

# Main Dashboard
dashboard = pn.Tabs(
    ('Dashboard', update_chart),
    ('Configuration', config_tab)
)

# Serve the dashboard
dashboard.servable()

# Uncomment the line below to serve the dashboard in a Jupyter notebook (if needed)
pn.serve(dashboard)