import streamlit as st
import streamlit.components.v1 as components

st.markdown ('## Urban Connectivity: Analyzing Housing Growth and Accessibility to Public Transportation in Sweden')
st.markdown('The goal of this analysis is to examine the interplay between **urban development** dynamics, proximity to **public transportation** and **income**.')
st.markdown('Analysis will try to find answers to questions like:\n- Are there any observable trends in hosuing development relative to different distances from public transportation?\n- Are certain municipalities better connected to public transportation?\n- How does the accessibility of residential areas to communication vary across different income brackets?\n- Is newly build hosuing better connected to public transportation or not? What is the trend?')

st.markdown('**Data source:** Main data source for the project is Statistikmyndigheten SCB (https://www.scb.se).')

st.markdown("Data sets shows number of apartments in each municipality in Sweden for years 2014-2021 and thier proximity to public transportation. There are 4 proximity groups:"
"\n- 400m"
"\n- 500m"
"\n- 1000m"
"\n- 2000m")

st.markdown("Public transportation nodes only with certatin frequency  were taken into consideration. Critera was that there is at least one connection every hour during working days between 06.00-22.00.")

st.markdown("The distance also was calucated in a straigh line (crow-fly distance), not by actual walking distance.")

st.markdown('**Calculating Conectivity Score**')

multi = '''Each household was calculated once to get more realistic score. For example households in distance 400m were exculded from number of households in 500m distance etc.

To obtain common score for each municipality, the Conectivity Score was calucated giving higher weight to houses that are closer to public transportation"
- 400m - weight: 1.0
- 500m - weight: 0.8
- 1000m - weight: 0.6
- 2000m - weight: 0.4
- more 2000m - weight: 0.2 *

*Households with poor connection was summed in group "more 2000m" '''
st.markdown(multi)

st.markdown('## Main insights from analysis')
st.markdown('### Urban Advantage: Access to Public Transportation')

multi_1 = '''Larger municipalities housing major cities such as Stockholm, Gothenburg, Malmö, and Uppsala demonstrate superior access to public transportation compared to smaller counties. Notably, this advantage remained almost unchanged from 2014 to 2021.'''
st.markdown(multi_1)

p = open("c:/Users/Lenovo/Documents/Data_Analytics/M4_1_Python/Project/Streamlit/fig1.html")
components.html(p.read(), height=800)

st.markdown('### Overall Public Transportation Access')
multi_2 = '''The median access to public transportation across all municipalities exhibited an upward trend over the years, indicating an overall improvement in connectivity.'''
st.markdown(multi_2)

p = open("c:/Users/Lenovo/Documents/Data_Analytics/M4_1_Python/Project/Streamlit/fig2.html")
components.html(p.read(), height=500)

st.markdown('### Cities gives more equal opportunities')
multi_3 = '''Despite variations in income levels, urban centers demonstrate a propensity to offer better connectivity to public transportation. This suggests that cities play a pivotal role in providing equal opportunities for transportation access.'''
st.markdown(multi_3)

p = open("c:/Users/Lenovo/Documents/Data_Analytics/M4_1_Python/Project/Streamlit/fig3.html")
components.html(p.read(), height=500)

st.markdown('### Change was not always positive')
multi_4 = '''While most municipalities witnessed a positive change in connectivity from 2014 to 2021, some areas experienced a decline. This underscores the dynamic nature of transportation infrastructure development.'''
st.markdown(multi_4)

p = open("c:/Users/Lenovo/Documents/Data_Analytics/M4_1_Python/Project/Streamlit/fig4.html")
components.html(p.read(), height=500)

st.markdown('### Growing Reach: Household Connectivity')
multi_5 = '''The overall growth in connectivity can be attributed to the construction of new apartments annually. Interestingly, the only segment showing a decrease in connectivity is households without access, indicating a positive shift in public transportation accessibility.'''
st.markdown(multi_5)

p = open("c:/Users/Lenovo/Documents/Data_Analytics/M4_1_Python/Project/Streamlit/fig5.html")
components.html(p.read(), height=500)


