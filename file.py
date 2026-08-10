import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Analysis from file")
col_1, col_2 = st.columns(2)
file_path = col_1.file_uploader("Upload a file", max_upload_size=1000)

sep_types = [",", ";", "\\t", "|"]
file_type = ["excel", "csv"]

file_type = col_2.radio("Select File Type", file_type, horizontal=True)


if file_path:
    if file_type == "excel":
        df = pd.read_excel(file_path)
    else:
        sep = col_2.selectbox("Select Separator", sep_types, index=0)
        df = pd.read_csv(file_path, sep=sep)
    st.header("Data Report")
    st.subheader("Sample 5 records")
    st.dataframe(df.sample(5))
    st.subheader("Data Types")
    st.write(df.dtypes)

    # Charts
    st.subheader("Missing Values")
    missing_values = df.isnull().sum()
    missing_values = missing_values[missing_values > 0]
    fig, ax = plt.subplots()
    sns.barplot(y=missing_values.index, x=missing_values.values, ax=ax)
    ax.set_title("Barplot for missing values")
    ax.set_ylabel("Column name")
    ax.set_xlabel("Missing Count")
    st.pyplot(fig)

    column_names = df.columns.tolist()
    st.header("Dynamic Chart")

    col_1, col_2, col_3 = st.columns(3)

    x_column = col_1.selectbox("Choose X-axis Column", column_names)
    y_column = col_2.selectbox("Choose Y-axis Column", column_names)

    chart_types = ["line", "bar", "scatter"]
    chart_type = col_3.selectbox("Select Chart Type", chart_types, index=0)

    fig, ax = plt.subplots()
    if chart_type == "line":
        sns.lineplot(data=df, x=x_column, y=y_column, ax=ax)
    elif chart_type == "bar":
        sns.barplot(data=df, x=x_column, y=y_column, ax=ax)
    elif chart_type == "scatter":
        sns.scatterplot(data=df, x=x_column, y=y_column, ax=ax)

    ax.set_title(f"{chart_type.title()}plot of {x_column} vs {y_column}")
    plt.tight_layout()
    st.pyplot(fig)
