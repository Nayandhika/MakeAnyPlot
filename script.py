import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

st.set_page_config(
    page_title="MakeAnyPlot",
    page_icon="📈",  
    layout="wide"
)

# primaryColor = st.get_option("theme.primaryColor")
# secondaryColor = st.get_option("theme.secondaryBackgroundColor")
# backgroundColor = st.get_option("theme.backgroundColor")
# textColor = st.get_option("theme.textColor")
# font=st.get_option("theme.font")

background_html = """
<style>
body {
background-image: url(image1.jpg);
background-size: cover;
}
</style>
"""


st.title("MakeAnyPlot")
st.markdown("""---""")
uploadedFile = st.file_uploader('Upload File', type=['csv','xlsx'],accept_multiple_files=False,key="fileUploader")
st.sidebar.image('image.jpg')
st.sidebar.markdown("""---""")
if uploadedFile is not None:
    try:
        if uploadedFile.name.endswith('.csv'):
            df = pd.read_csv(uploadedFile, encoding='latin-1') 
        elif uploadedFile.name.endswith('.xlsx'):
            df = pd.read_excel(uploadedFile, engine='openpyxl')
        else:
            st.error("Unsupported File format")
            st.stop()
        st.write(df)  
    except Exception as e:
        st.error(f"Error: {e}")  
    columns = df.columns.tolist()

    if st.sidebar.checkbox("## SINGLE VARIABLE PLOT", key='CHECHK1'):
        st.sidebar.title('Select column for plotting a single variable')
        axis = st.sidebar.selectbox('Select column', columns)
        if axis:
            if st.sidebar.button("PLOT", key='BUTTON1'):
                TAB1, TAB2, TAB3, TAB4, TAB5 = st.tabs(["Histogram", "Line Plot","Scatter Plot","Violin Plot", "Box Plot"])
                with TAB2:
                    fig = px.line(x=df[axis], title=f'Line Plot of {axis}', labels={'x': axis, 'y':'Count'})
                    st.write("## Line Plot")
                    st.plotly_chart(fig)

                with TAB3:
                    fig_scatter = px.scatter(df, x=axis, title=f'Scatter Plot of {axis}')
                    st.write("## Scatter Plot")
                    st.plotly_chart(fig_scatter)
                
                with TAB4:
                    st.write("## Violin Plot")
                    fig = px.violin(y=df[axis], title=f'Violin Plot of {axis}',
                    labels={'y': axis})
                    fig.update_layout(
                        yaxis_title_text=axis,
                    )
                    st.plotly_chart(fig)

                with TAB5:
                    st.write("## Box Plot")
                    fig = px.box(df, y=df[axis], title=f'Box Plot of {axis}',
                                labels={'y': axis})
                    fig.update_layout(yaxis_title_text=axis)
                    st.plotly_chart(fig)
                    
                with TAB1:
                    fig_x = px.histogram(x=df[axis], title=f'Histogram of {axis}',labels={'x': axis})
                    st.write("## Histogram")
                    st.plotly_chart(fig_x)

    if st.sidebar.checkbox("## TWO - VARIABLE PLOT", key='CHECHK2'):
        st.sidebar.title('Select columns for plotting 2 variables')
        x_axis = st.sidebar.selectbox('Select X-axis column', columns, key=2)
        y_axis = st.sidebar.selectbox('Select Y-axis column', columns, key=3)

        if x_axis and y_axis:
            if st.sidebar.button("PLOT", key='BUTTON2'):
                tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(["Line Plot", "Bar Plot", "Bubble Plot","Scatter Plot","Area Plot","Violin Plot", "Box Plot", "2D Histogram", "2D Histogram Contour", "Density Contour"])
                with tab1:

                    fig = px.line(df, x= x_axis, y= y_axis, title=f'Line Plot of {x_axis} vs {y_axis}')
                    st.write("## Line Plot")
                    st.plotly_chart(fig)

                with tab2:

                    fig_bar = px.bar(df,x=x_axis, y=y_axis, title=f'Bar Plot of {x_axis} vs {y_axis}')
                    st.write("## Bar Plot")
                    st.plotly_chart(fig_bar)
                    
                with tab8:

                    fig_x = px.histogram(x=df[x_axis], title=f'Histogram of {x_axis}', labels={'x': x_axis})
                    fig_y = px.histogram(x=df[y_axis], title=f'Histogram of {y_axis}', labels={'x': y_axis})
                    st.write("## Histogram of "+x_axis)
                    st.plotly_chart(fig_x)
                    st.write("## Histogram of "+y_axis)
                    st.plotly_chart(fig_y)

                    fig = go.Figure(go.Histogram2d(x=df[x_axis], y=df[y_axis]))
                    fig.update_layout(
                        title=f'2D Histogram of {x_axis} and {y_axis}',
                        xaxis=dict(title=x_axis),
                        yaxis=dict(title=y_axis),
                        barmode='overlay'
                    )
                    st.write("## 2D Histogram")
                    st.plotly_chart(fig)
                
                with tab4:

                    fig_scatter = px.scatter(df, x=x_axis, y=y_axis, title=f'Scatter Plot of {x_axis} and {y_axis}')
                    st.write("## Scatter Plot")
                    st.plotly_chart(fig_scatter)

                with tab5:

                    fig_scatter = px.area(df, x=x_axis, y=y_axis, title=f'Area Plot of {x_axis} vs {y_axis}')
                    st.write("## Area Plot")
                    st.plotly_chart(fig_scatter)

                with tab6:
                    fig = px.violin(df, x=x_axis, y=y_axis, title=f'Violin plot of {y_axis} vs {x_axis}')
                    st.plotly_chart(fig)
                
                with tab7:
                    fig = px.box(df, x=x_axis, y=y_axis, title=f'Box plot of {y_axis} vs {x_axis}')
                    st.plotly_chart(fig)
                
                with tab10:
                    fig_scatter = px.density_contour(df, x=x_axis, y=y_axis, title=f'Density Contour plot of {x_axis} and {y_axis}')
                    st.write("##  Density Contour Plot")
                    st.plotly_chart(fig_scatter)

                with tab9:
                    fig = go.Figure(go.Histogram2dContour(x=df[x_axis], y=df[y_axis]))
                    fig.update_layout(
                        title=f'2D Histogram Contour plot of of {x_axis} and {y_axis}',
                        xaxis=dict(title=x_axis),
                        yaxis=dict(title=y_axis),
                        barmode='overlay'
                    )
                    st.write("## 2D Histogram Contour plot")
                    st.plotly_chart(fig)
                
                with tab3:
                    df['sizes'] = np.random.rand(len(df[x_axis])) * 1000
                    fig = px.scatter(df, x=x_axis, y=y_axis, size='sizes', size_max=30,
                    title=f'Bubble Plot of {x_axis} and{y_axis}',
                    labels={'x': x_axis, 'y': y_axis})
                    st.write("## Bubble Plot")
                    st.plotly_chart(fig)

    if st.sidebar.checkbox("## THREE - VARIABLE PLOT", key='CHECHK3'):
        st.sidebar.title('Select columns for plotting 3 variables')
        x_axis = st.sidebar.selectbox('Select X-axis column', columns, key=4)
        y_axis = st.sidebar.selectbox('Select Y-axis column', columns, key=5)
        z_axis = st.sidebar.selectbox('Select Z-axis column', columns)
        if x_axis and y_axis and z_axis:
            if st.sidebar.button("PLOT", key='BUTTON3'):
                tab1, tab2, tab3 = st.tabs(["3D Scatter Plot", "3D Surface Plot", "3D Line Plot" ])
                with tab1:
                    fig = go.Figure(data=[go.Scatter3d(x=df[x_axis], y=df[y_axis], z=df[z_axis], mode='markers')])
                    fig.update_layout(title=f'3D Scatter Plot of {x_axis}, {y_axis} and {z_axis}', scene=dict(xaxis_title=x_axis, yaxis_title=y_axis, zaxis_title=z_axis), width=800, height=600 )
                    st.write("## 3D Scatter Plot")
                    st.plotly_chart(fig)
                with tab2:
                    fig = go.Figure(data=[go.Surface(x=df[x_axis], y=df[y_axis], z=df[z_axis], colorscale='Viridis')])
                    fig.update_layout(title=f'3D Surface Plot of {x_axis}, {y_axis} and {z_axis}', scene=dict(xaxis_title=x_axis, yaxis_title=y_axis, zaxis_title=z_axis), width=800, height=600)
                    st.write("## 3D Surface Plot")
                    st.plotly_chart(fig)
                with tab3:
                    fig = go.Figure(data=[go.Scatter3d(x=df[x_axis], y=df[y_axis], z=df[z_axis], mode='lines')])
                    fig.update_layout(title=f'3D Line Plot of {x_axis}, {y_axis} and {z_axis}', scene=dict(xaxis_title=x_axis, yaxis_title=y_axis, zaxis_title=z_axis), width=800, height=600 )
                    st.write("## 3D Line Plot")
                    st.plotly_chart(fig)
