import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Preetesh Shivam
##### *Resume* 
''')

image = Image.open('dp1.png')
st.image(image, width=150)

st.markdown('## Professional Summary', unsafe_allow_html=True)
st.markdown('''
- Data Science & Analytics leader with over 10 years of experience in transforming complex business needs into scalable data-driven solutions.
- Proven expertise in creating advanced Tableau visualizations, collaborating with stakeholders to refine requirements, and ensuring data quality through rigorous analysis and modeling.
- Skilled in deploying predictive models and AI tools to enhance operational efficiency and drive impactful business decisions.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-dark">
  <a class="navbar-brand" href="https://www.linkedin.com/in/preetesh-shivam/" target="_blank">Preetesh Shivam</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#Personal-Projects">Personal Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)


#####################
st.markdown('''
## Work Experience
''')

txt('**Customer Insights & Analytics Manager** | London Stock Exchange Group (LSEG) | New York, NY',
'Jan, 2023 - Jul, 2024')
st.markdown('''
- Designed competitor analysis dashboard in Tableau, integrating market data to provide real-time insights, enabling leadership team to identify competitive gaps and adjust pricing strategies, resulting in 15% increase in market share. 
- Developed and deployed an AI-driven chatbot in Python working cross-functionally with business analysts and Product teams to resolve customer issues efficiently, achieving a 23% reduction in average response time.
- Increased customer lifetime value by 5% by designing a Customer Insights dashboard in Tableau, which translated to a significant boost in revenue and improved customer retention and customer acquisition strategies.
- Crafted SQL queries in Snowflake and deployed it in Alteryx to set up ETL/ELT processes for daily sales pipeline data from Salesforce CRM, reducing data processing time by 30% and enhancing data availability for real-time analytics.
''')

txt('**Director of Sales Operations & Analytics** | London Stock Exchange Group (LSEG) | New York, NY',
'Jan, 2021 - Dec, 2022')
st.markdown('''
- Designed a contract-renewal dashboard in Tableau that predicted the probability of accounts renewing contracts based on inputs from business analysts and stakeholders leading to 3% increase in contract renewal rate YoY.
-	Developed sales pipeline dashboard in Power BI, visualizing key metrics such as pipeline velocity and deal stage progression, enabling sales teams to prioritize high-value opportunities and improve sales conversion rates by 20%. 
-	Spearheaded the integration of Snowflake and Azure data warehouses into single Snowflake instance, collaborating with the Backend team and Data Architect on data modelling design considerations.
-	Developed revenue forecasting model in Python, leveraging advanced statistical techniques and machine learning algorithms to predict future revenue trends with 95% accuracy, informing business planning and resource allocation.
''')

txt('**Senior Data Scientist** | Antuit AI | New York, NY',
'Feb, 2017 - Jan, 2021')
st.markdown('''
- Built Revenue dashboard for a SaaS B2B client in Power BI that tracked sales and pipeline velocity analyzing very large and complex data sets, resulting in a remarkable 4% reduction in average lead conversion time YoY.
-	Championed rigorous code review and quality assurance within the development team, enhancing machine learning model quality by resolving over 30% of potential issues pre-deployment, thereby accelerating project timelines.
-	Created the Microsoft SharePoint repository that stored analytics dashboards, advanced SQL queries, visualization best practices contributing to the enhancement and application of visualization design principles and standards.
''')

txt('**Data Scientist** | Antuit AI | Bangalore, India',
'Jun, 2014 - Jan, 2017')
st.markdown('''
- Designed Business Intelligence Tableau dashboards for a CPG client, which were adopted by 5 departments, driving a 15% increase in sales by optimizing product performance insights across various markets and consumer segments.
-	Designed scalable data pipelines using advanced SQL techniques for a software company, enhancing data extraction and analysis capabilities and enabling 50% larger dataset processing and 40% faster processing.
''')

#####################
st.markdown('''
## Education
''')

txt('**Bachelor of Engineering** (Computer Science), *Sir MVIT*, India',
'2010-2014')

#####################
st.markdown('''
## Personal Projects
''')
txt4('Live Stock Price Dashboard', 'Deployed a web-based live stock price dashboard app in Python using Streamlit framework.', 'https://livestockpricedb-ps-live-stock-price.streamlit.app/')
txt4('Ecommerce Product Sales Dashboard', 'Designed an Ecommerce product sales dashboard in tableau to analyze sales and product trends for an Ecommerce while showcasing my tableau skills. Used demo data.', 'https://public.tableau.com/views/EcommerceProductSalesDashboard2024/Summary?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link')
txt4('Profit & Loss Statement Dashboard', 'Designed a simple Profit & Loss FP&A dashboard to highlight my tableau skills. Used demo data.', 'https://public.tableau.com/views/Section1File_17238260404180/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `SAS`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`, `Alteryx`')
txt3('Data Warehouse', '`Snowflake`, `Azure`, `Google Cloud Platform`, `Oracle`')
txt3('Data visualization', '`Tableau`, `Power BI`, `Julius`, `matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`, `LightweightMMM`, `Prophet`')
txt3('Deep Learning', '`Pytorch`')
txt3('AI', '`ChatGPT`, `Perplexity`, `OpenAI`, `Anthropic`, `Retrieval Augmented Generation`')
#####txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `gradio`, `Heroku`, `AWS`')
txt3('Project Management', '`Agile Methodology`, `Scrum`, `Kanban`, `Notion`')

#####################
<h2>Social Media</h2>
<ul style="list-style: none; padding: 0;">
    <li style="margin: 10px 0;">
        <a href="https://www.linkedin.com/in/preetesh-shivam/" style="color: #0077b5; text-decoration: none;">LinkedIn</a>
    </li>
    <li style="margin: 10px 0;">
        <a href="https://x.com/curious_memer" style="color: #1DA1F2; text-decoration: none;">Twitter</a>
    </li>
    <li style="margin: 10px 0;">
        <a href="https://github.com/intellectual-memer" style="color: #333; text-decoration: none;">GitHub</a>
    </li>
</ul>
## st.markdown('''
## Social Media
## ''')
st.header("Social Media")

# Using markdown for the links
st.markdown("[LinkedIn](https://www.linkedin.com/in/preetesh-shivam/)")
st.markdown("[Twitter](https://x.com/curious_memer)")
st.markdown("[GitHub](https://github.com/intellectual-memer)")
               
## txt2('LinkedIn', 'https://www.linkedin.com/in/preetesh-shivam/')
## txt2('Twitter', 'https://x.com/curious_memer')
## txt2('GitHub', 'https://github.com/intellectual-memer')
##txt2('', 'https://github.com/chaninlab/')
##txt2('ORCID', 'http://orcid.org/0000-0003-1040-663X')
##txt2('', 'https://github.com/dataprofessor')
##txt2('Scopus', 'http://www.scopus.com/authid/detail.url?authorId=12039071300')
##txt2('ResearcherID', 'http://www.researcherid.com/rid/F-1021-2010')
##txt2('ResearchGate', 'https://www.researchgate.net/profile/Chanin_Nantasenamat')
##txt2('Publons', 'https://publons.com/a/303133/')
