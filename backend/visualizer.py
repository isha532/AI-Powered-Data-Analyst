
import plotly.express as px


def create_bar_chart(df, x_column, y_column):

    fig = px.bar(
        df,
        x=x_column,
        y=y_column,
        title=f"{y_column} by {x_column}",
        text=y_column
    )

    fig.update_layout(
        xaxis_title=x_column,
        yaxis_title=y_column,
        template="plotly_white"
    )

    return fig


def create_pie_chart(df, category_column):

    category_counts = df[category_column].value_counts().reset_index()

    category_counts.columns = [
        category_column,
        "Count"
    ]

    fig = px.pie(
        category_counts,
        names=category_column,
        values="Count",
        title=f"{category_column} Distribution",
        hole=0.3
    )

    return fig



def create_line_chart(df, x_column, y_column):

    fig = px.line(
        df,
        x=x_column,
        y=y_column,
        title=f"{y_column} Trend",
        markers=True
    )

    fig.update_layout(
        xaxis_title=x_column,
        yaxis_title=y_column,
        template="plotly_white"
    )

    return fig
