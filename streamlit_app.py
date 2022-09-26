import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
from scipy import stats
from PIL import Image
import datetime
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
from time import sleep

st.set_page_config(layout="wide")   # Set the layout of web app as wide mode

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style.css")  # Load file "style.css"


def page2():
    
    ### Set my face image
    st.markdown(
        """
        <style>
        .css-1v0mbdj {
        display: block;
        margin-left: auto;
        margin-right: auto;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    image = Image.open('asset/My face.png') 
    
    #st.title('Hello 😊')
    st.image(image)
    st.write('')
    st.write('')
    st.write("""I\'m Sangchai Paijit. You can call me Babe. I\'m 26 years old.\
        I graduated with a bachelor\'s degree of electronic engineering from Suranaree University of Technology.\
        Also, I just have graduated with a master\'s degree of electrical engineering from Suranaree University of Technology.\
        I have an experiences with the digital holography (DH) during a master\'s degree studeis.\
        For a brief explanation, we store the hologram signal of the particle by using the CCD sensor with the resolution of 640×480 pixel.
        Next, we import the data to MATLAB then analyze the hologram signal by calculating the numerical reconstruction by using\
        Fresnel diffraction integral. We analyze the hologram signal from row-by-row according to the number of rows of the CCD sensor\
        in vertical axis (480 rows) by taking the numerical computation of Fresnel diffraction integral, that is expressed by Fourier transform.\
        As a result, we measure the particle depth position (a position between the CCD sensor and particle)\
        and particle diameter by image processing technique. Finally, we construct the digital 3-D particle from the\
        depth potision and its diameter measurements that is extracted from the digital hologram.\
        Also, a user can interact with the digital 3-D particle image by using hand detection system based on the blob analysis method.\
        As described above, all computations were done by using MATLAB.\
        This field is related to an image processing and digital signal processing. 
        Currently, I'm seeking the data scientist position where utilize my abilities, analysis, and laterel thinking to\
        achieve organization objectives.""")

    ### WORK EXPERINCE ###
    st.title('WORK EXPERIENCE')
    st.write("#### March 2018 - June 2018")
    st.write('● Drive Test Engineer internship at Seagate Technology (Thailand) Co., Ltd. (Korat)')
    
    ### EDUCATIONS ###
    st.title('EDUCATIONS')
    st.write("#### 2018 - 2022")
    st.write("""●&nbsp;Master of Engineering (Electrical Engineering),\
              Suranaree University of Technology, Nakhon Ratchasima, Thailand""")   ### Use\n in front of text to make new line
    st.write("#### 2014 - 2018")
    st.write("""●Bachelor of Engineering (Electronic Engineering),\
              Suranaree University of Technology, Nakhon Ratchasima, Thailand""") 
    
    ### TECHNICAL SKILLS ###
    st.title('TECHNICAL SKILLS')
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("● MATLAB\
        \n● Python\
        \n● C/C++\
        \n● Streamlit")
    
    with col2:
        st.write("● SQL\
        \n● Power BI\
        \n● HTML\
        \n● CSS")

    with col3:
        st.write("● JavaScipt (basic)\
        \n● Image processing\
        \n● Digital signal processing")

    ### SOFT SKILLS ###
    st.title('SOFT SKILLS')
    col11, col22 = st.columns(2)

    with col11:
        st.write("● Self-motivation\
        \n● Self-confidence")
    
    with col22:
        st.write("● Planning and problem solving\
        \n● Accepting feedback")

    ### LANGUAGES ###
    st.title('LANGUAGES')
    st.write("● Native Thai\
        \n● Good command in English")

    ### HOBBIES ###
    st.title('HOBBIES')
    col111, col222, col333 = st.columns(3)
    
    with col111:
        
        joy_icon = '''                                                                                                                                                   
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />                                                                                                                    
        <span class="material-symbols-outlined"; style = "font-size:50px; margin-left: 27px;">stadia_controller</span>
        '''   
        st.write(joy_icon, unsafe_allow_html=True)  
        st.write("&nbsp;Mobile Games", unsafe_allow_html=True)
        st.write('')   

        coffee_icon = '''                                                                                                                                                   
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />                                                                                                                     
        <span class="material-symbols-outlined"; style = "font-size:50px; margin-left: 27px;">coffee_maker</span>        
        '''  
        st.write(coffee_icon, unsafe_allow_html=True)       
        st.write("Coffee brewing")
        st.write('')   
    
    with col222:
        
        movies_icon = '''                                                                                                                                                   
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />                                                                                                                     
        <span class="material-symbols-outlined"; style = "font-size:50px; margin-left: 25px;">movie</span>        
        '''  
        st.write(movies_icon, unsafe_allow_html=True)       
        st.write("&nbsp; &nbsp; &nbsp; &nbsp; Movies")
        st.write('')   

        walk_icon = '''                                                                                                                                                   
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />                                                                                                                     
        <span class="material-symbols-outlined"; style = "font-size:50px; margin-left: 25px;">sports_martial_arts</span>        
        '''  
        st.write(walk_icon, unsafe_allow_html=True)       
        st.write("&nbsp; &nbsp; &nbsp; &nbsp; Exercise")
        st.write('')   

    with col333:
        
        guitar_icon = '''                                                                                                                                                   
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />                                                                                                                     
        <span class="material-symbols-outlined"; style = "font-size:50px; margin-left: -2px;">music_note</span>        
        '''  
        st.write(guitar_icon, unsafe_allow_html=True)       
        st.write("Guitar")
        st.write('')   

        coding_icon = '''                                                                                                                                                   
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />
        <span class="material-symbols-outlined"; style = "font-size:50px; margin-left: 0px;">code</span>
        '''
        st.write(coding_icon, unsafe_allow_html=True)       
        st.write("Coding")
        st.write('')   

    ### CONTACT ###
    st.title('CONTACT')

    # Location
    location_icon = '''                                                                                                                                                   
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />                                                                                                                    
        <span class="material-symbols-outlined"; style = "position: absolute; font-size:32px; margin-left: 5px;">location_on</span>   
        <p style = "margin-left: 40px;">&nbsp;&nbsp;717 (Always Place 1) Village No.5\
        Suranaree Sub-district, Mueang District,\
        <br>&nbsp;&nbsp;Nakhon Ratchasima, 30000</p>     
        '''
    st.write(location_icon, unsafe_allow_html=True)

    # Email
    email_icon = '''                                                                                                                                                   
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />                                                                                                                      
        <span class="material-symbols-outlined"; style = "position: absolute; font-size:32px; margin-left: 5px;">mail</span> 
        <p style = "margin-left: 40px">&nbsp;&nbsp;sangchai.g@gmail.com</p> 
        '''
    st.write(email_icon, unsafe_allow_html=True)

    # Tel
    tel_icon = '''                                                                                                                                                   
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />                                                                                                                      
        <span class="material-symbols-outlined"; style = "position: absolute; font-size:32px; margin-left: 5px;">call</span>        
        <p style = "margin-left: 40px">&nbsp;&nbsp;0893055458</p> 
        '''
    st.write(tel_icon, unsafe_allow_html=True)

def page3():

    df = pd.read_csv("sample-store.csv")   # Import the data file
    state_lat_long = pd.read_csv("states.csv") 

    df['Order Date']= pd.to_datetime(df['Order Date']) 
    dashboard_icon = '''                                                                                                                                                   
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />
        <span class="material-symbols-outlined"; style = "position: absolute; font-size:40px; margin-top: 25px;">dashboard</span>
        <h1>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Sales dashboard</h1>  
        '''
    st.write(dashboard_icon, unsafe_allow_html=True) 

    date_icon = '''                                                                                                                                                   
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />
        <button id="btn"; class="material-symbols-outlined"; style = "font-size:26px; margin-top: 0px;">calendar_month</button>
        <div class="babe"; style = "display:inline; font-family: Source Sans Pro, sans-serif; font-weight: 600; font-size: calc(1.275rem + .3vw);">&nbsp; Select a date (2017-2020) </div>  
        '''
    st.write(date_icon, unsafe_allow_html=True) 

    st.write('')
    
    # Built date button #
    start_date = st.date_input('Start date',
                 datetime.date(2017, 1, 1))    # Start time at 2017-01-01 (y-m-d)
    end_date = st.date_input('End date',
                 datetime.date(2020, 12, 31))  # End time at 2020-12-31 (y-m-d)
    
    start_date = pd.to_datetime(start_date)   # Convert 'start_date' to datetime
    end_date = pd.to_datetime(end_date)   # Convert 'end_date' to datetime
    
    ###### Sort order date by start_date and end_date ######
    df_2017_2020 = df[df['Order Date'].between(start_date, end_date)] # Date time in year 2017-2020
    df_2017_2020 = df_2017_2020.sort_values(by=['Order Date'], ascending=True)   ##### Sort value just 1 column! #####

    total_sale = df_2017_2020['Sales'].sum().round(-3)   # Calculate total sale according to start_date 'til end_date
    total_sale = '$' + (total_sale.astype(float)/1000000).astype(str) + 'M'   # Convert number to Kilo, Mege, ...

    total_profit = df_2017_2020['Profit'].sum().round(-3)   # Calculate total profit according to start_date 'til end_date
    total_profit = '$' + (total_profit.astype(float)/1000000).astype(str) + 'M'   # Convert number to Kilo, Mege, ...

    total_order = df_2017_2020['Row ID'].value_counts().sum()

    total_discount = df_2017_2020['Discount'].sum().round(0)   # Calculate total discount according to start_date 'til end_date
    total_discount = '$' + (total_discount.astype(float)/1000).astype(str) + 'K'   # Convert number to Kilo, Mege, ...

    ########### Row 1 ###########
    st.write("#### Sales Overview")

    r1_c1, r1_c2, r1_c3, r1_c4 = st.columns(4)
    r1_c1.metric("Total Sales", value=total_sale)
    r1_c2.metric("Total Profit", value=total_profit)
    r1_c3.metric("Discount", value=total_discount)
    r1_c4.metric("Order", value=total_order)

    st.write('<br><br>', unsafe_allow_html=True)
    

    ########### Row 2 ###########
    r2_c1, r2_c2, r2_c3 = st.columns(3)

    #### Sales bar graph ####
    with r2_c1:
        st.write('#### &nbsp;&nbsp;&nbsp; Total sales (2017-2020)')

        y2017 = df[df['Order Date'].between('2017-01-01', '2017-12-31')]
        ts_2017 = y2017['Sales'].sum().round(2)

        y2018 = df[df['Order Date'].between('2018-01-01', '2018-12-31')]
        ts_2018 = y2018['Sales'].sum().round(2)

        y2019 = df[df['Order Date'].between('2019-01-01', '2019-12-31')]
        ts_2019 = y2019['Sales'].sum().round(2)

        y2020 = df[df['Order Date'].between('2020-01-01', '2020-12-31')]
        ts_2020 = y2020['Sales'].sum().round(2)

        #d = {'2017': ts_2017, '2018': ts_2018, '2019': ts_2019, '2020': ts_2020}
        d = {'Year': [2017, 2018, 2019, 2020], 'Sales': [ts_2017,ts_2018,ts_2019,ts_2020]}
        df_new = pd.DataFrame(data=d, index = [0, 1, 2, 3])

        fig1 = px.bar(df_new, x='Year', y='Sales', text= 'Sales')
        fig1.update_traces(texttemplate='%{text:.2s}', textposition='inside')
        
        fig1.update_layout(
        xaxis = dict(
            tickmode = 'linear',
            tick0 = 1,
        ),margin=dict(l=10, r=10, t=10, b=10),
        )
        fig1.update_layout(width=550, height=350, font_family="sans-serif", font_size=16, plot_bgcolor="#F2F2F2")
        group_labels = ['Group 1', 'Group 2', 'Group 3']
        st.plotly_chart(fig1, use_container_width=True)
    
    #### Sales Forecast ####
    with r2_c2:
        st.write('#### &nbsp;&nbsp;&nbsp; Sales Forecast')
        sale_f = df_2017_2020.groupby(df_2017_2020['Order Date'].dt.strftime('%Y-%m'))['Sales'].sum().reset_index()
        sale_f.sort_values(by=['Order Date'], inplace=True)

        od = sale_f['Order Date']
        od = pd.to_numeric(od.index, downcast='integer')
        sl = sale_f['Sales']

        slope, intercept, r, p, std_err = stats.linregress(od,sl)    # To extract the variables from the library

        def myfunc(od):
            return slope * od + intercept   # y = mx + c

        mymodel = list(map(myfunc, od))    

        fig2 = px.bar(sale_f, y="Sales", x="Order Date")
        fig2.update_traces(textfont_size=16, hovertemplate="%{x|%Y/%m} value: %{y}",)
        fig2.update_xaxes(tickangle=0)
        fig2.update_layout(width=550, height=350, bargap=0.4, font_family = "sans-serif", font_size = 16,
                           plot_bgcolor = "#F2F2F2", barmode = 'stack',
                           margin=dict(l=10, r=10, t=10, b=10),
                           legend=dict(yanchor="top", xanchor="left", x=0.01))  
        fig2.add_trace(
            go.Scatter(
                x=sale_f['Order Date'],
                y=mymodel,
                mode="markers+lines",
                name="Linear Regression Forecast<br>with R-squared = 0.501",
                hovertemplate="%{x|%Y/%m} value: %{y}",
                marker=dict(
                color='Green',
                size=4,
                    line=dict(
                        color='Green',
                        width=2,
                    )
                ),         
            )
        )
        st.plotly_chart(fig2, use_container_width=True)

    #### Profit % ####
    with r2_c3:
        st.write('#### &nbsp;&nbsp;&nbsp; Profit %')
        slsl = df_2017_2020.groupby(df_2017_2020['Order Date'].dt.strftime('%Y-%m'))[['Sales', 'Profit']].sum().reset_index()

        slsl['Profit %'] = ((100/(slsl['Sales'])) * slsl['Profit']).round(2)   # Calculate profit for each months in percentage

        slsl["Color"] = np.where(slsl["Profit %"]<0, 'red', 'green')   # Find which one that profit % < 0% >>> then put 'red' in Color column, otherwise is green.

        fig3 = px.bar(slsl, y = "Profit %", x = "Order Date")
        fig3.update_traces(textfont_size = 16, hovertemplate = "%{x|%Y/%m} value: %{y}%", marker_color = slsl['Color'])
        fig3.update_xaxes(tickangle=0, range=['2016-10','2021-03'])  
        fig3.update_layout(width=550, height=350, bargap = 0.4, font_family = "sans-serif", font_size = 16,
                           plot_bgcolor = "#F2F2F2", barmode = 'stack',
                           margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(fig3, use_container_width=True)

    ########### Row 3 ###########
    r3_c1, r3_c2, r3_c3 = st.columns(3)

    #### Sales by Cat ####
    with r3_c1:
        
        st.write('#### &nbsp;&nbsp;&nbsp; Sales by Category')
        cat_sale = df_2017_2020.groupby('Category')['Sales'].sum().round(2).nlargest(5).sort_values(ascending=False).reset_index()
        
        ##### Top Selling Category #####
        fig4 = px.pie(cat_sale, labels='Category', values='Sales', names='Category')
        fig4.update_traces(hoverinfo='label+percent', textinfo='label+percent', textfont_size=16)
        fig4.update_layout(font_family="sans-serif", plot_bgcolor="#F2F2F2", legend = dict(font = dict(family = "sans-serif", size = 16)),
                  legend_title = dict(font = dict(family = "sans-serif", size = 16)))
        st.plotly_chart(fig4, use_container_width=True)
    
    #### Sales by Sub-Cat ####
    with r3_c2:
        ##### Top Selling Sub-Category #####
        st.write('#### &nbsp;&nbsp;&nbsp; Top 5 Sales by Sub-Category')
        subcat_sale = df_2017_2020.groupby('Sub-Category')['Sales'].sum().round(2).nlargest(5).sort_values(ascending=False).reset_index()
        fig5 = px.pie(subcat_sale, labels='Sub-Category', values='Sales', names='Sub-Category')
        fig5.update_traces(hoverinfo='label+percent', textinfo='label+percent', textposition='inside', textfont_size=16)
        fig5.update_layout(font_family="sans-serif", plot_bgcolor="#F2F2F2", legend = dict(font = dict(family = "sans-serif", size = 16)),
                  legend_title = dict(font = dict(family = "sans-serif", size = 16)))
        st.plotly_chart(fig5, use_container_width=True)

    #### Sales by Segment and Sub-Cat ####
    with r3_c3:
        st.write('#### &nbsp;&nbsp;&nbsp; Sales by Segment and Category')
        g1 = df.groupby(['Segment', 'Category'])['Sales'].sum().round(2).sort_values(ascending=False).reset_index()

        fig8 = px.bar(g1, x="Segment", y="Sales",
                    color='Category', barmode='group',
                    height=400, text = 'Sales')
        fig8.update_traces(texttemplate='%{text:.2s}', textposition='inside', textfont_color = "White")
        fig8.update_layout(margin=dict(l=10, r=10, t=10, b=10), legend=dict(yanchor="top", xanchor="right", x=20),
                           font_family="sans-serif", font_size=16, plot_bgcolor="#F2F2F2")     
        fig8.show()
        st.plotly_chart(fig8, use_container_width=True)

    ########### Row 4 ###########
    r4_c1, r4_c2 = st.columns(2)
    t10_state = df_2017_2020.groupby('State')['Sales'].sum().round(2).nlargest(10).sort_values(ascending=False).reset_index()
    
    #### Top 10 by Sales ####
    with r4_c1:
        st.write('#### &nbsp;&nbsp;&nbsp; Top 10 State by Sales')
        fig6 = px.bar(t10_state, x='Sales', y='State', text= 'Sales', orientation='h')
        fig6.update_traces(texttemplate='%{text:.2s}', textposition='inside', marker_color='#FB83E5') 
        fig6.update_layout(margin=dict(l=10, r=10, t=10, b=10), font_family="sans-serif", font_size=16, plot_bgcolor="#F2F2F2")     
        fig6.update_yaxes(categoryorder="total ascending")
        st.plotly_chart(fig6, use_container_width=True)

    s_state_map = df_2017_2020.groupby(['State', 'latitude', 'longitude'])['Sales'].sum().round(2).sort_values(ascending=False).reset_index()

    #### Sales by Location (State) ####
    with r4_c2:
        st.write('#### &nbsp;&nbsp;&nbsp; Sales by Location')
        fig7 = px.scatter_geo(s_state_map, scope='usa',
                lat = s_state_map['latitude'],
                lon = s_state_map['longitude'],
                color = "State", # which column to use to set the color of markers
                hover_name="State", # column added to hover information
                size_max=50,   # inscrease a scatter plot
                size = "Sales",   # mass of size depends on a sales
                projection = "natural earth")
        fig7.update_layout(
            geo = dict(
                scope='usa',
                projection_type='albers usa',
                showland = True,
                landcolor = "#EAE9E9",
                subunitcolor = "#B7B7B7",
                countrywidth = 2,
                subunitwidth = 2,
                ),
            margin = dict(l=10, r=10, t=10, b=10), font_family="sans-serif", font_size=16, plot_bgcolor="#F2F2F2"
            )
        
        st.plotly_chart(fig7, use_container_width=True)

    st.write('')
    st.write(""" ###### Note: This dataset is an information about a sales report of a stores in North America. In this dashboard, you can select a date\
        in order to observe the information at each period. Furthermore, you can download the data as .CSV file here.""")

    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    csv = convert_df(df)

    st.download_button(
        label="Click to download the data",
        data=csv,
        file_name='sample-store.csv',
        mime='text/csv',
    )

    st.write('')
    st.write('')
    st.write(""" ##### This small web app was developed by using Streamlit. You can set up the web page by clicking the triple bar button (≡)\
        at the upper right-hand side, then click at "setting" in order to set up the theme of the web app. Finally, I sincerely thank you for\
        visiting this small web app. Hope I will have a chance to work with you.""")

page_names_to_funcs = {
    "Introduction": page2,
    "Dashboard": page3,
}

selected_page = st.sidebar.selectbox("Choose an option", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
