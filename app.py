
import streamlit as st
import pandas as pd

from backend.data_loader import load_data
from backend.profiler import profile_data
from backend.cleaner import (
    clean_missing_values,
    remove_duplicates
)
from backend.visualizer import (
    create_bar_chart,
    create_pie_chart,
    create_line_chart
)
from backend.query_engine import run_query
from backend.ai_engine import ask_gemini


# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI Powered Data Analyst",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Powered Data Analyst")
st.caption(
    "Analyze, clean, visualize and query your data using AI."
)


# ==========================================
# 2. SIDEBAR - FILE UPLOAD
# ==========================================

st.sidebar.title("📁 Upload Dataset")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV or Excel file",
    type=["csv", "xlsx", "xls"]
)


if uploaded_file is None:

    st.info("👈 Upload a CSV or Excel file to get started.")

    st.markdown("""
    ### Features

    - 📂 CSV and Excel file upload
    - 📋 Automatic data profiling
    - 🧹 Data cleaning
    - 📊 Interactive visualizations
    - 🗄️ SQL query engine
    - 🤖 Gemini AI Data Analyst
    """)

    st.stop()


# ==========================================
# 3. LOAD DATA
# ==========================================

try:

    df = load_data(uploaded_file)

    st.sidebar.success("Dataset loaded successfully!")

except Exception as e:

    st.error(f"Data Loading Error: {e}")
    st.stop()


# ==========================================
# 4. DATA OVERVIEW
# ==========================================

st.header("📌 Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Rows", len(df))
col2.metric("Total Columns", len(df.columns))
col3.metric("Duplicate Rows", int(df.duplicated().sum()))
col4.metric("Missing Values", int(df.isnull().sum().sum()))

st.subheader("👀 Dataset Preview")

st.dataframe(
    df,
    use_container_width=True
)


# ==========================================
# 5. DATA PROFILING
# ==========================================

st.header("📋 Data Profiling")

try:

    profile = profile_data(df)

    tab1, tab2, tab3 = st.tabs([
        "Dataset Information",
        "Missing Values",
        "Statistical Summary"
    ])

    with tab1:

        st.json({
            "Total Rows": profile["total_rows"],
            "Total Columns": len(df.columns),
            "Duplicate Rows": profile["duplicate_rows"]
        })

        dtype_df = pd.DataFrame(
            list(profile["data_types"].items()),
            columns=["Column", "Data Type"]
        )

        st.subheader("Column Data Types")
        st.dataframe(dtype_df, use_container_width=True)

    with tab2:

        missing_df = pd.DataFrame(
            list(profile["missing_values"].items()),
            columns=["Column", "Missing Values"]
        )

        st.dataframe(
            missing_df,
            use_container_width=True
        )

    with tab3:

        summary_df = pd.DataFrame(
            profile["numerical_summary"]
        )

        if summary_df.empty:
            st.info("No numerical columns available.")
        else:
            st.dataframe(
                summary_df,
                use_container_width=True
            )

except Exception as e:

    st.error(f"Profiling Error: {e}")


# ==========================================
# 6. DATA CLEANING
# ==========================================

st.header("🧹 Data Cleaning")

st.write(
    "Handle missing values and remove duplicate records."
)

if st.button("Clean Dataset", key="clean_button"):

    try:

        cleaned_df = clean_missing_values(df)
        cleaned_df = remove_duplicates(cleaned_df)

        st.session_state["cleaned_df"] = cleaned_df

        st.success("Dataset cleaned successfully!")

    except Exception as e:

        st.error(f"Cleaning Error: {e}")


if "cleaned_df" in st.session_state:

    cleaned_df = st.session_state["cleaned_df"]

    col1, col2 = st.columns(2)

    col1.metric("Original Rows", len(df))
    col2.metric("Cleaned Rows", len(cleaned_df))

    st.subheader("Cleaned Dataset")

    st.dataframe(
        cleaned_df,
        use_container_width=True
    )

    st.download_button(
        label="⬇️ Download Cleaned CSV",
        data=cleaned_df.to_csv(index=False),
        file_name="cleaned_dataset.csv",
        mime="text/csv"
    )


# ==========================================
# 7. DATA VISUALIZATION
# ==========================================

st.header("📊 Data Visualization")

all_columns = df.columns.tolist()

numeric_columns = df.select_dtypes(
    include="number"
).columns.tolist()

if len(all_columns) > 0:

    chart_type = st.selectbox(
        "Select Chart Type",
        ["Bar Chart", "Pie Chart", "Line Chart"]
    )

    if chart_type == "Bar Chart":

        x_column = st.selectbox(
            "Select X Axis",
            all_columns,
            key="bar_x"
        )

        y_column = st.selectbox(
            "Select Y Axis",
            numeric_columns,
            key="bar_y"
        ) if numeric_columns else None

        if y_column:

            fig = create_bar_chart(
                df,
                x_column,
                y_column
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        else:
            st.info("No numerical columns available for Bar Chart.")

    elif chart_type == "Pie Chart":

        category_column = st.selectbox(
            "Select Category",
            all_columns,
            key="pie_category"
        )

        fig = create_pie_chart(
            df,
            category_column
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    elif chart_type == "Line Chart":

        x_column = st.selectbox(
            "Select X Axis",
            all_columns,
            key="line_x"
        )

        y_column = st.selectbox(
            "Select Y Axis",
            numeric_columns,
            key="line_y"
        ) if numeric_columns else None

        if y_column:

            fig = create_line_chart(
                df,
                x_column,
                y_column
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        else:
            st.info("No numerical columns available for Line Chart.")


# ==========================================
# 8. SQL QUERY ENGINE
# ==========================================

st.header("🗄️ SQL Query Engine")

st.write(
    "Execute SQL SELECT queries on your uploaded dataset."
)

st.caption("Your DataFrame is available as a SQL table named sales.")

sql_query = st.text_area(
    "Enter SQL Query",
    value="SELECT * FROM sales LIMIT 10",
    height=120
)

if st.button("Run SQL Query"):

    try:

        result = run_query(
            df,
            sql_query
        )

        st.subheader("SQL Query Result")

        st.dataframe(
            result,
            use_container_width=True
        )

        st.success(
            f"Query executed successfully! {len(result)} rows returned."
        )

    except Exception as e:

        st.error(f"SQL Error: {e}")


# ==========================================
# 9. AI DATA ANALYST
# ==========================================

st.header("🤖 AI Data Analyst")

st.write(
    "Ask questions about your uploaded dataset using Gemini AI."
)

question = st.text_area(
    "Ask your question",
    placeholder="Example: Which product has the highest price?",
    height=100
)

if st.button("Ask AI Analyst"):

    if not question.strip():

        st.warning("Please enter a question.")

    else:

        try:

            with st.spinner("Gemini is analyzing your dataset..."):

                answer = ask_gemini(
                    df,
                    question
                )

            st.subheader("🤖 AI Analyst Answer")

            st.markdown(answer)

        except Exception as e:

            st.error(f"AI Analysis Error: {e}")


# ==========================================
# 10. FOOTER
# ==========================================

st.divider()

st.caption(
    "AI Powered Data Analyst | Python | Pandas | "
    "Streamlit | Plotly | SQLite | Gemini AI"
)
