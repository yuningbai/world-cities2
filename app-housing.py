from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# 读取与本文件放在一起的住房数据
df = pd.read_csv(Path(__file__).with_name("housing.csv"))

# 标题
st.title("California Housing Data (1990) by Bai Yuning")

# 房价筛选滑块
min_value = st.slider(
    "Minimal Median House Value",
    min_value=0,
    max_value=500001,
    value=200000
)

st.subheader("See more filters in the sidebar:")

# 侧边栏：位置类型，默认全部选中
location_types = df["ocean_proximity"].unique().tolist()

selected_locations = st.sidebar.multiselect(
    "Choose the location type",
    options=location_types,
    default=location_types
)

# 侧边栏：收入水平
income_level = st.sidebar.radio(
    "Choose income level",
    options=["Low", "Medium", "High"]
)

# 先按房价和位置筛选
filtered_df = df[
    (df["median_house_value"] >= min_value)
    & (df["ocean_proximity"].isin(selected_locations))
]

# 再按收入水平筛选
if income_level == "Low":
    filtered_df = filtered_df[
        filtered_df["median_income"] <= 2.5
    ]
elif income_level == "Medium":
    filtered_df = filtered_df[
        (filtered_df["median_income"] > 2.5)
        & (filtered_df["median_income"] < 4.5)
    ]
else:
    filtered_df = filtered_df[
        filtered_df["median_income"] >= 4.5
    ]

# 显示地图和直方图
if filtered_df.empty:
    st.info("No districts match the selected filters.")
else:
    st.map(filtered_df[["latitude", "longitude"]])

    fig, ax = plt.subplots()
    ax.hist(
        filtered_df["median_house_value"],
        bins=30,
        edgecolor="black"
    )
    ax.set_xlabel("Median House Value (USD)")
    ax.set_ylabel("Number of Districts")
    ax.set_title("Distribution of Median House Value")

    st.pyplot(fig)
    plt.close(fig)