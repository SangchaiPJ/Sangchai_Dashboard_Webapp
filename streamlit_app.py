from os import write
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
from plotly.subplots import make_subplots
from time import sleep
import base64

st.set_page_config(layout="wide")   # Set the layout of web app as wide mode

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style.css")  # Load file "style.css"


def page1():

    image = Image.open('asset/My face.png') 
    
    #st.title('Hello 😊')
    st.image(image)
    st.write('')
    st.write('')
    st.write("""I\'m Sangchai Paijit. My nickname is Babe. I\'m 26 years old.\
        I graduated with a bachelor's degree in electronic engineering from Suranaree University of Technology.\
        Also, I graduated with a master's degree in electrical engineering from Suranaree University of Technology.\
        I had a chance to work with Seagate Technology (Thailand) as an internship for 4 months during my bachelor's studies,\
        that the responsibilities are inspecting various pieces of machinery, analyzing issues, identifying the root cause of\
        malfunctions, and electronic circuit design. Furthermore, I have knowledge of programming languages and automation\
        testing tools such as MATLAB, Python, Robot Framework, Selenium library, etc. Currently, seeking a challenging position\
        where utilize my abilities, analysis, and lateral thinking to achieve organizational objectives.""")

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
    st.write("""● Bachelor of Engineering (Electronic Engineering),\
              Suranaree University of Technology, Nakhon Ratchasima, Thailand""") 
    
    ### TECHNICAL SKILLS ###
    st.title('TECHNICAL SKILLS')
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write("● MATLAB\
        \n● Python\
        \n● C\
        \n● Streamlit")
    
    with col2:
        st.write("● Microsoft Office\
        \n● HTML\
        \n● CSS\
        \n● JavaScript (basic)")

    with col3:
        st.write("● Robot Framework\
        \n● Selenium\
        \n● Postman\
        \n● SQL")

    ### SOFT SKILLS ###
    st.title('SOFT SKILLS')
    col11, col22, col33 = st.columns(3)

    with col11:
        st.write("● Self-motivation\
        \n● Team working")
    
    with col22:
        st.write("● Planning and problem-solving\
        \n● Accepting feedback")

    ### LANGUAGES ###
    st.title('LANGUAGES')
    st.write("● Native Thai\
        \n● Good command in English")

    ### HOBBIES ###
    st.title('HOBBIES')
    col111, col222, col333, col444, col555 = st.columns(5, gap = "small")
    
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
        <span class="material-symbols-outlined"; style = "font-size:50px; margin-left: 0px;">movie</span>        
        '''  
        st.write(movies_icon, unsafe_allow_html=True)       
        st.write("Movies")
        st.write('')   

        walk_icon = '''                                                                                                                                                   
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />                                                                                                                     
        <span class="material-symbols-outlined"; style = "font-size:50px; margin-left: 0px;">sports_martial_arts</span>        
        '''  
        st.write(walk_icon, unsafe_allow_html=True)       
        st.write("Exercise")
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

    # Linkedin
    linkedin_icon = '''                                                                                                                                                   
        <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
        <i class='bx bxl-linkedin'; style = "position: absolute; font-size:32px; margin-top: -5px; margin-left: 5px;"></i>  
        <a href="http://www.linkedin.com/in/sangchai-paijit"; style = "margin-left: 46px;">www.linkedin.com/in/sangchai-paijit</a>
        '''
    st.write(linkedin_icon, unsafe_allow_html=True)


def page2():

    ### Row 1: Experimental setup, digital hologram, and numerical reconstruction signal ###
    st.title('MY THESIS')
    st.write('#### INTERACTIVE 3-D DIGITAL DISPLAY OF LINE-SHAPED PARTICLE FROM INLINE HOLOGRAMS')
    st.write('')
    row_1_col_1, row_1_col_2, row_1_col_3 = st.columns(3, gap = "large")

    ### Insert the image into web browser ###
    exp_setup = open("asset/Experimental setup.jpg", "rb")
    contents1 = exp_setup.read()
    data_url1 = base64.b64encode(contents1).decode("utf-8")
    exp_setup.close()

    with row_1_col_1:
        st.markdown(
            f'<div class = "imgthesis"; style = "margin-top: 40px;">'
            f'<img src="data:image/gif;base64,{data_url1}";  style = "border-radius:15px">'
            f'</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class = "txtthesis">'
            f'<p>Experimental setup for recording the line-shaped particle holograms</p>',
            unsafe_allow_html=True,
        )
        
    
    ### Insert the image into web browser ###
    holo = open("asset/Hologram 40 cm 60 degree.png", "rb")
    contents2 = holo.read()
    data_url2 = base64.b64encode(contents2).decode("utf-8")
    holo.close()

    with row_1_col_2:
        st.markdown(
            f'<div class = "imgthesis">'
            f'<img src="data:image/gif;base64,{data_url2}";  style = "border-radius:15px">'
            f'</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class = "txtthesis">'
            f'<p>Digital hologram of the line-shaped particle</p>',
            unsafe_allow_html=True,
        )

    ### Insert the image into web browser ###
    num_recon = open("asset/Reconstruction from best focus images 40 cm 60 degree 11th row.png", "rb")
    contents3 = num_recon.read()
    data_url3 = base64.b64encode(contents3).decode("utf-8")
    num_recon.close()
    
    with row_1_col_3:
        st.markdown(
            f'<div class = "imgthesis">'
            f'<img src="data:image/gif;base64,{data_url3}";  style = "border-radius:15px">'
            f'</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class = "txtthesis">'
            f'<p>Numerical reconstruction based on Fresnel diffraction integral</p>',
            unsafe_allow_html=True,
        )
        
    st.write('')
    st.write('')
    st.write(""" Since my master's degree studies, I have had a chance to work with the digital holography (DH). Firstly, it is the experimental
            setup for hologram recording. The particle is a microfiber with 100 μm diameter, that attached on the object holder. The hologram signal of the
            particle was stored by using the CCD sensor with the resolution of 640×480 pixel. The second one is the digital hologram image.
            After get the digital hologram signal from the particle, the numerical reconstruction was done by using Fresnel diffraction intergral,
            which was expressed by using Fourier transform. Then, extracting the depth position and particle diameter from row-by-row (480 rows)
            using the digital image processing and digital signal processing technique, which the depth position is the distance between
            CCD sensor to the line-shaped particle. Although we know the specification in that the particle diameter is 100 μm, 
            but the exact information of the particle diameter from row-by-row cannot be directly known. Therefore,
            this thesis has improved the accuracy of morphological analysis of the small particle.""")
    st.write('')
    st.write('')

    row_2_col_1, row_2_col_2 = st.columns(2, gap = "large")
    
    ### Insert the image into web browser ###
    depth_po = open("asset/Depth position (40 cm with 60_75 degree).png", "rb")
    contents4 = depth_po.read()
    data_url4 = base64.b64encode(contents4).decode("utf-8")
    depth_po.close()
    
    with row_2_col_1:
        st.markdown(
            f'<div class = "imgthesis">'
            f'<img src="data:image/gif;base64,{data_url4}";  style = "border-radius:15px">'
            f'</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class = "txtthesis">'
            f'<p>Depth measurements of the line-shaped particle</p>',
            unsafe_allow_html=True,
        )

    ### Insert the image into web browser ###
    depth_po = open("asset/Diameter (40 cm with 60_75 degree).png", "rb")
    contents5 = depth_po.read()
    data_url5 = base64.b64encode(contents5).decode("utf-8")
    depth_po.close()
    
    with row_2_col_2:
        st.markdown(
            f'<div class = "imgthesis">'
            f'<img src="data:image/gif;base64,{data_url5}";  style = "border-radius:15px">'
            f'</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class = "txtthesis">'
            f'<p>Depth measurements of the line-shaped particle</p>',
            unsafe_allow_html=True,
        )
    
    st.write('')
    st.write('')
    st.write("""After extracting the depth position and diameter measurements, analyze the measurements 
            that why the plotting of these measurements is spread out like the images shown above. 
            For the reason of the error, it cause from the spatial frequency for the shorter recording 
            distance is higher, that cause more aliasing effect. To improve the measurement results,
            it can be done by using a higher resolution of image sensor for hologram recording.
            Finally, use this 3-D information to construct the 3-D microtube shape.""")
    st.write('')
    st.write('')

    row_3_col_1, row_3_col_2 = st.columns(2, gap = "large")
    
    ### Insert the image into web browser ###
    microtube_shape = open("asset/3-D microtube from 40 cm 60 degree.png", "rb")
    contents6 = microtube_shape.read()
    data_url6 = base64.b64encode(contents6).decode("utf-8")
    microtube_shape.close()
    
    with row_3_col_1:
        st.markdown(
            f'<div class = "imgthesis">'
            f'<img src="data:image/gif;base64,{data_url6}";  style = "border-radius:15px">'
            f'</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class = "txtthesis">'
            f'<p>3-D display of the microtube shape</p>',
            unsafe_allow_html=True,
        )

    video_file = open('asset/Movement along the x-axis (480p).mp4', 'rb')
    video_bytes = video_file.read()
   
    with row_3_col_2:
        st.write('')
        st.write('')
        st.write('')
        st.video(video_bytes)
        st.markdown(
            f'<div class = "txtthesis"; style = "margin-top: -6px;">'
            f'<p>Interactive of the 3-D display microtube shape</p>',
            unsafe_allow_html=True,
        )

    st.write('')
    st.write('')
    st.write("""According to the proposed thesis, a user can interact with the 3-D microtube shape
            by using a hand movement via an external webcam. In addition, the hand detection was developed
            based on the blob analysis algorithm. In conclusion, this thesis not only improved 
            the accuracy of the morphological analysis of particle, but also the visual perception and reality 
            sense of a user.""")
    st.write('')
    st.write('')


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
        <span id="btn"; class="material-symbols-outlined"; style = "font-size:22px; margin-top: 0px;">calendar_month</span>
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
        st.write('#### &nbsp;&nbsp;&nbsp; Total Sales (2017-2020)')

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
        st.write('#### &nbsp;&nbsp;&nbsp; Sales-Profit Forecast')
        sale_f = df_2017_2020.groupby(df_2017_2020['Order Date'].dt.strftime('%Y-%m'))['Sales'].sum().reset_index()
        sale_f.sort_values(by=['Order Date'], inplace=True)
        
        df_2017_2020["Color"] = np.where(df_2017_2020["Profit"]<0, 'red', 'green')   # Add color according to Profit (+/-)

        sale_scat = df_2017_2020['Sales'].round(2)
        #od = pd.to_numeric(od.index, downcast='integer')
        pro_scat = df_2017_2020['Profit'].round(2)

        slope, intercept, r, p, std_err = stats.linregress(sale_scat,pro_scat)    # To extract the variables from the library

        def myfunc(sale_scat):
            return slope * sale_scat + intercept   # y = mx + c

        mymodel = list(map(myfunc, sale_scat))    
        fig2 = make_subplots(rows=1, cols=1,
                      specs=[[{"secondary_y": False}]])
        # fig2 = px.scatter(df_2017_2020, y="Profit", x="Sales")
        fig2.add_trace(
            go.Scatter(
                x=df_2017_2020['Sales'], 
                y=df_2017_2020['Profit'], 
                mode='markers',
                name=None,
                showlegend=False))

        fig2.update_traces(textfont_size=16, hovertemplate="Sale: %{x}\n Profit: %{y}", marker_color = df_2017_2020['Color'])
        fig2.update_xaxes(tickangle=0)
        fig2.update_layout(width=550, height=350, bargap=0.4, font_family = "sans-serif", font_size = 16,
                           plot_bgcolor = "#F2F2F2", barmode = 'stack',
                           margin=dict(l=10, r=10, t=10, b=10),
                           legend=dict(yanchor="top", xanchor="left", x=0.01),
                           xaxis_title="Sales", yaxis_title="Profit",
                           yaxis = dict(
                                tickmode = 'linear',
                                tick0 = 0,
                                dtick = 2000,
                            )
        )

        fig2.add_trace(
            go.Scatter(
                x=df_2017_2020['Sales'],
                y=mymodel,
                mode="lines",
                name="Linear Regression Forecast<br>with R-squared = 0.501",
                hovertemplate="Profit forecast: %{y}",
                marker=dict(color='Black'),
                line=dict(color='#C459F3', 
                          width=4,
                          dash='dot'),
            ), secondary_y=False
        )        

        st.plotly_chart(fig2, use_container_width=True)

    #### Profit % ####
    with r2_c3:
        st.write('#### &nbsp;&nbsp;&nbsp; Profit %')
        profit_per = df_2017_2020.groupby(df_2017_2020['Order Date'].dt.strftime('%Y-%m'))[['Sales', 'Profit']].sum().reset_index()

        profit_per['Profit %'] = ((100/(profit_per['Sales'])) * profit_per['Profit']).round(2)   # Calculate profit for each months in percentage

        profit_per["Color"] = np.where(profit_per["Profit %"]<0, 'red', 'green')   # Find which one that profit % < 0% >>> then put 'red' in Color column, otherwise is green.

        fig3 = px.bar(profit_per, y = "Profit %", x = "Order Date")
        fig3.update_traces(textfont_size = 16, hovertemplate = "%{x|%Y/%m} value: %{y}%", marker_color = profit_per['Color'])
        fig3.update_xaxes(tickangle=0, range=['2016-10','2021-03'])  
        fig3.update_layout(width=550, height=350, bargap = 0.4, font_family = "sans-serif", font_size = 16,
                           plot_bgcolor = "#F2F2F2", barmode = 'stack',
                           margin=dict(l=10, r=10, t=10, b=10),)
        st.plotly_chart(fig3, use_container_width=True)

    ########### Row 3 ###########
    r3_c1, r3_c2, r3_c3 = st.columns(3)

    #### Sales by Cat ####
    with r3_c1:
        
        st.write('#### &nbsp;&nbsp;&nbsp; Sales by Category')
        cat_sale = df_2017_2020.groupby('Category')['Sales'].sum().round(2).nlargest(5).sort_values(ascending=False).reset_index()
        
        ##### Top Selling Category #####
        fig4 = px.pie(cat_sale, labels='Category', values='Sales', names='Category')
        fig4.update_traces(hoverinfo='label+percent', textinfo='label+percent', textposition='inside', textfont_size=16, textfont_color = "White")
        fig4.update_layout(font_family="sans-serif", plot_bgcolor="#F2F2F2", legend = dict(font = dict(family = "sans-serif", size = 16)),
                  legend_title = dict(font = dict(family = "sans-serif", size = 16)),
                  margin=dict(l=3, r=3, t=3, b=3))
        st.plotly_chart(fig4, use_container_width=True)
    
    #### Sales by Sub-Cat ####
    with r3_c2:
        ##### Top Selling Sub-Category #####
        st.write('#### &nbsp;&nbsp;&nbsp; Top 5 Sales by Sub-Category')
        subcat_sale = df_2017_2020.groupby('Sub-Category')['Sales'].sum().round(2).nlargest(5).sort_values(ascending=False).reset_index()
        fig5 = px.pie(subcat_sale, labels='Sub-Category', values='Sales', names='Sub-Category')
        fig5.update_traces(hoverinfo='label+percent', textinfo='label+percent', textposition='inside', textfont_size=16, textfont_color = "White")
        fig5.update_layout(font_family="sans-serif", plot_bgcolor="#F2F2F2", legend = dict(font = dict(family = "sans-serif", size = 16)),
                  legend_title = dict(font = dict(family = "sans-serif", size = 16)),
                  margin=dict(l=25, r=25, t=25, b=25))
        st.plotly_chart(fig5, use_container_width=True)

    #### Sales by Segment and Sub-Cat ####
    with r3_c3:
        st.write('#### &nbsp;&nbsp;&nbsp; Sales by Segment and Category')
        g1 = df_2017_2020.groupby(['Segment', 'Category'])['Sales'].sum().round(2).sort_values(ascending=False).reset_index()

        fig8 = px.bar(g1, x="Segment", y="Sales",
                    color='Category', barmode='group',
                    height=400, text = 'Sales')
        fig8.update_traces(texttemplate='%{text:.2s}', textposition='inside', textangle=0, textfont_size=16, textfont_color = "White")
        fig8.update_layout(margin=dict(l=10, r=10, t=10, b=10), bargap=0.15, 
                           legend=dict(
                                orientation="h",
                                yanchor="bottom",
                                y=1.02,
                                xanchor="right",
                                x=1),
                           font_family="sans-serif", font_size=16, plot_bgcolor="#F2F2F2")     
        fig8.show()
        st.plotly_chart(fig8, use_container_width=True)

    ########### Row 4 ###########
    r4_c1, r4_c2 = st.columns(2)
    t10_state = df_2017_2020.groupby('State')['Sales'].sum().round(2).nlargest(10).sort_values(ascending=False).reset_index()
    
    #### Top 10 by Sales ####
    with r4_c1:
        st.write('#### &nbsp;&nbsp;&nbsp; Top 10 Sales by State')
        fig6 = px.bar(t10_state, x='Sales', y='State', text= 'Sales', orientation='h', color='State')
        fig6.update_traces(texttemplate='%{text:.2s}', textposition='inside', textfont_color = "White") 
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
        visiting this small web app.""")

def page4():
    st.title('AUTOMATED TEST')
    st.write('#### XYZ bank (basic web app to practice an automation testing skill)')

    row_1_col_1, row_1_col_2 = st.columns(2, gap = "large")

    ### Import XYZ banking web page ###
    xyz_page = open("asset/XYZ banking web page.png", "rb")
    contents7 = xyz_page.read()
    data_url7 = base64.b64encode(contents7).decode("utf-8")
    xyz_page.close()

    ### Insert the image of XYZ banking web page ###
    with row_1_col_1:
        st.markdown(
            f'<div class = "imgautomated"; style = "margin-top: 50px;">'
            f'<img src="data:image/gif;base64,{data_url7}">'
            f'</div>',
            unsafe_allow_html=True,
        )
        
    with row_1_col_2:
        ### Insert the video of login functional ###    
        video_file2 = open('asset/Names to login.mp4', 'rb')
        video_bytes2 = video_file2.read()
        st.write('')
        st.write('')
        st.write('')
        st.video(video_bytes2)

    st.markdown(
        f'<div class = "txtautomated">'
        f'<p>XYZ bank web page</p>',
        f'<a href="https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account></a>',
        unsafe_allow_html=True,
    )

    st.write('')
    st.write(""" On this bank website, we can login by clicking "Customer Login" button then we will see various names inside a dropdown list\
        to login. Due to this website is no username and password required to login, when user select a name then\
        click login button, the login is successful. Inside this website, user can see their account number, current balance and currency of account.\
        Furthermore, user can deposit money, withdraw  money, and also view a history of transactions.""")
    st.write('')
    st.write('')


page_names_to_funcs = {
    "Resume": page1,
    "Thesis (master's studies)": page2,
    "Sales Dashboard (proj_1)": page3,
    "Automated test (proj_2)": page4,
}

selected_page = st.sidebar.selectbox("Choose an option", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
