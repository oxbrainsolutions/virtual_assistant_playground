import streamlit as st
import openai
import pathlib
import base64
import imutils

openai.api_key = "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"

st.set_page_config(page_title="Virtual Assistant Playground", page_icon="images/oxbrain_favicon.png", layout="wide")

st.elements.utils._shown_default_value_warning=True

marker_spinner_css = """
<style>
    #spinner-container-marker {
        display: flex;
        align-items: center;
        justify-content: center;
        position: fixed;
        top: 0%;
        left: 0%;
        transform: translate(54%, 0%);
        width: 100%;
        height: 100%;
        z-index: 9999;
    }

    .marker0 {
        position: absolute;
        left: 0;
        width: 1.5em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 2s linear infinite;
        animation-delay: calc(2s * 0 / 12);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 0 / 12)) translate(calc(2em * (1 - cos(2 * 3.14159 * 0 / 12))), calc(2em * sin(2 * 3.14159 * 0 / 12)));        
    }
    
    .marker1 {
        position: absolute;
        left: 0;
        width: 1.5em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 2s linear infinite;
        animation-delay: calc(2s * 1 / 12);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 1 / 12)) translate(calc(2em * (1 - cos(2 * 3.14159 * 1 / 12))), calc(2em * sin(2 * 3.14159 * 1 / 12)));
    }
    
    .marker2 {
        position: absolute;
        left: 0;
        width: 1.5em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 2s linear infinite;
        animation-delay: calc(2s * 2 / 12);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 2 / 12)) translate(calc(2em * (1 - cos(2 * 3.14159 * 2 / 12))), calc(2em * sin(2 * 3.14159 * 2 / 12)));
    }
    
    .marker3 {
        position: absolute;
        left: 0;
        width: 1.5em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 2s linear infinite;
        animation-delay: calc(2s * 3 / 12);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 3 / 12)) translate(calc(2em * (1 - cos(2 * 3.14159 * 3 / 12))), calc(2em * sin(2 * 3.14159 * 3 / 12)));
    }
    
    .marker4 {
        position: absolute;
        left: 0;
        width: 1.5em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 2s linear infinite;
        animation-delay: calc(2s * 4 / 12);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 4 / 12)) translate(calc(2em * (1 - cos(2 * 3.14159 * 4 / 12))), calc(2em * sin(2 * 3.14159 * 4 / 12)));
    }
    
    .marker5 {
        position: absolute;
        left: 0;
        width: 1.5em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 2s linear infinite;
        animation-delay: calc(2s * 5 / 12);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 5 / 12)) translate(calc(2em * (1 - cos(2 * 3.14159 * 5 / 12))), calc(2em * sin(2 * 3.14159 * 5 / 12)));
    }
    
    .marker6 {
        position: absolute;
        left: 0;
        width: 1.5em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 2s linear infinite;
        animation-delay: calc(2s * 6 / 12);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 6 / 12)) translate(calc(2em * (1 - cos(2 * 3.14159 * 6 / 12))), calc(2em * sin(2 * 3.14159 * 6 / 12)));
    }
    
    .marker7 {
        position: absolute;
        left: 0;
        width: 1.5em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 2s linear infinite;
        animation-delay: calc(2s * 7 / 12);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 7 / 12)) translate(calc(2em * (1 - cos(2 * 3.14159 * 7 / 12))), calc(2em * sin(2 * 3.14159 * 7 / 12)));
    }
    
    .marker8 {
        position: absolute;
        left: 0;
        width: 1.5em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 2s linear infinite;
        animation-delay: calc(2s * 8 / 12);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 8 / 12)) translate(calc(2em * (1 - cos(2 * 3.14159 * 8 / 12))), calc(2em * sin(2 * 3.14159 * 8 / 12)));
    }
    
    .marker9 {
        position: absolute;
        left: 0;
        width: 1.5em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 2s linear infinite;
        animation-delay: calc(2s * 9 / 12);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 9 / 12)) translate(calc(2em * (1 - cos(2 * 3.14159 * 9 / 12))), calc(2em * sin(2 * 3.14159 * 9 / 12)));
    }
    
    .marker10 {
        position: absolute;
        left: 0;
        width: 1.5em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 2s linear infinite;
        animation-delay: calc(2s * 10 / 12);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 10 / 12)) translate(calc(2em * (1 - cos(2 * 3.14159 * 10 / 12))), calc(2em * sin(2 * 3.14159 * 10 / 12)));
    }
    
    .marker11 {
        position: absolute;
        left: 0;
        width: 1.5em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 2s linear infinite;
        animation-delay: calc(2s * 11 / 12);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 11 / 12)) translate(calc(2em * (1 - cos(2 * 3.14159 * 11 / 12))), calc(2em * sin(2 * 3.14159 * 11 / 12)));
    }
    
    @keyframes animateBlink {
    0% {
        background: #FCBC24;
    }
    75% {
        background: rgba(0, 0, 0, 0);
    }   
}
@media (max-width: 1024px) {
    #spinner-container-marker {
        transform: translate(57.4%, 0%);
    }
    .marker0 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 0 / 12)) translate(calc(7.5em * (1 - cos(2 * 3.14159 * 0 / 12))), calc(7.5em * sin(2 * 3.14159 * 0 / 12)));
    }
    .marker1 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 1 / 12)) translate(calc(7.5em * (1 - cos(2 * 3.14159 * 1 / 12))), calc(7.5em * sin(2 * 3.14159 * 1 / 12)));
    }
    .marker2 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 2 / 12)) translate(calc(7.5em * (1 - cos(2 * 3.14159 * 2 / 12))), calc(7.5em * sin(2 * 3.14159 * 2 / 12)));
    }
    .marker3 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 3 / 12)) translate(calc(7.5em * (1 - cos(2 * 3.14159 * 3 / 12))), calc(7.5em * sin(2 * 3.14159 * 3 / 12)));
    }
    .marker4 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 4 / 12)) translate(calc(7.5em * (1 - cos(2 * 3.14159 * 4 / 12))), calc(7.5em * sin(2 * 3.14159 * 4 / 12)));
    }
    .marker5 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 5 / 12)) translate(calc(7.5em * (1 - cos(2 * 3.14159 * 5 / 12))), calc(7.5em * sin(2 * 3.14159 * 5 / 12)));
    }
    .marker6 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 6 / 12)) translate(calc(7.5em * (1 - cos(2 * 3.14159 * 6 / 12))), calc(7.5em * sin(2 * 3.14159 * 6 / 12)));
    }
    .marker7 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 7 / 12)) translate(calc(7.5em * (1 - cos(2 * 3.14159 * 7 / 12))), calc(7.5em * sin(2 * 3.14159 * 7 / 12)));
    }
    .marker8 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 8 / 12)) translate(calc(7.5em * (1 - cos(2 * 3.14159 * 8 / 12))), calc(7.5em * sin(2 * 3.14159 * 8 / 12)));
    }
    .marker9 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 9 / 12)) translate(calc(7.5em * (1 - cos(2 * 3.14159 * 9 / 12))), calc(7.5em * sin(2 * 3.14159 * 9 / 12)));
    }
    .marker10 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 10 / 12)) translate(calc(7.5em * (1 - cos(2 * 3.14159 * 10 / 12))), calc(7.5em * sin(2 * 3.14159 * 10 / 12)));
    }
    .marker11 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 11 / 12)) translate(calc(7.5em * (1 - cos(2 * 3.14159 * 11 / 12))), calc(7.5em * sin(2 * 3.14159 * 11 / 12)));
    }
</style>

<div id="spinner-container-marker">
    <div class="marker0"></div>
    <div class="marker1"></div>
    <div class="marker2"></div>
    <div class="marker3"></div>
    <div class="marker4"></div>
    <div class="marker5"></div>
    <div class="marker6"></div>
    <div class="marker7"></div>
    <div class="marker8"></div>
    <div class="marker9"></div>
    <div class="marker10"></div>
    <div class="marker11"></div>
</div>
"""

subheader_media_query = '''
<style>
@media (max-width: 1024px) {
    p.subheader_text {
      font-size: 4em;
    }
}
</style>
'''

text_media_query1 = '''
<style>
@media (max-width: 1024px) {
    p.text {
        font-size: 1em;
    }
}
</style>
'''

information_media_query = '''
  <style>
  @media (max-width: 1024px) {
      p.information_text {
        font-size: 3.6em;
      }
  }
  </style>
'''

error_media_query1 = '''
<style>
@media (max-width: 1024px) {
    p.error_text1 {
      font-size: 4em;
    }
}
</style>
'''


styles2 = """
<style>
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .viewerBadge_link__1S137 {display: none !important;}
    .col2 {
        margin: 0em;
        display: flex;
        align-items: center;
        vertical-align: middle;
        padding-right: 0.875em;
        margin-top: -0.5em;
        margin-bottom: 0em;
    }
    .left2 {
        text-align: center;
        width: 80%;
        padding-top: 0em;
        padding-bottom: 0em;
    }
    .right2 {
        text-align: center;
        width: 20%;
        padding-top: 0em;
        padding-bottom: 0em;
    }

    /* Tooltip container */
    .tooltip2 {
        position: relative;
        margin-bottom: 0em;
        display: inline-block;
        margin-top: 0em;
    }

    /* Tooltip text */
    .tooltip2 .tooltiptext2 {
        visibility: hidden;
        width: 70em;
        background-color: #03A9F4;
        color: #FAFAFA;
        text-align: justify;
        font-family: sans-serif;
        display: block; 
        border-radius: 0.375em;
        white-space: normal;
        padding-left: 0.75em;
        padding-right: 0.75em;
        padding-top: 0.5em;
        padding-bottom: 0em;
        border: 0.1875em solid #FAFAFA;

        /* Position the tooltip text */
        position: absolute;
        z-index: 1;
        bottom: 125%;
        transform: translateX(-95%);

        /* Fade in tooltip */
        opacity: 0;
        transition: opacity 0.5s;
    }

    /* Tooltip arrow */
    .tooltip2 .tooltiptext2::after {
        content: "";
        position: absolute;
        top: 100%;
        left: 95.6%;
        border-width: 0.625em;
        border-style: solid;
        border-color: #FAFAFA transparent transparent transparent;
    }

    /* Show the tooltip text when you mouse over the tooltip container */
    .tooltip2:hover .tooltiptext2 {
        visibility: visible;
        opacity: 1;
    }
    /* Change icon color on hover */
    .tooltip2:hover i {
        color: #FAFAFA;
    }   
    /* Set initial icon color */
    .tooltip2 i {
        color: #03A9F4;
    }
    ul.responsive-ul2 {
        font-size: 0.8em;
    }
    ul.responsive-ul2 li {
        font-size: 1em;
    }

    /* Responsive styles */
    @media (max-width: 1024px) {
       .col2 {
            padding-right: 1em;
            margin-top: 0em;
        }
        p.subtext_manual2 {
            font-size: 3.6em;
        }
    .tooltip2 .tooltiptext2 {
        border-width: 0.6em;
        border-radius: 1.6em;
        width: 80em;
        left: 50%;
    }
    .tooltip2 .tooltiptext2::after {
        border-width: 2em;
        left: 93.5%;
    }
    .tooltip2 {
        
    }
    .tooltip2 i {
        font-size: 8em;
        margin-bottom: 0.2em;
    }
    ul.responsive-ul2 {
        font-size: 3.2em;
    }
    ul.responsive-ul2 li {
        font-size: 1em;
    }
    }
</style>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
"""

st.markdown(styles2, unsafe_allow_html=True)

st.markdown("""
  <style>
    div.block-container.css-ysnqb2.e1g8pov64 {
        margin-top: -3em;
    }
    div[data-modal-container='true'][key='Modal1'] > div:first-child > div:first-child {
        background-color: rgb(203, 175, 175) !important;
    }
    div[data-modal-container='true'][key='Modal1'] > div > div:nth-child(2) > div {
        max-width: 3em !important;
    }
    div[data-modal-container='true'][key='Modal2'] > div:first-child > div:first-child {
        background-color: rgb(203, 175, 175) !important;
    }
    div[data-modal-container='true'][key='Modal2'] > div > div:nth-child(2) > div {
        max-width: 3em !important;
    }
    .css-gesnqs {
        background-color: #FCBC24 !important;
    }
    .css-fpzaie {
        background-color: #FCBC24 !important;
    }
    .css-5qhjmn {
        z-index: 1000 !important;
    }
    .css-15d9ls5{
        z-index: 1000 !important;
    }
    .css-g6xpsg {
        z-index: 1000 !important;
    }
    .css-2542xv {
        z-index: 1000 !important;
    }
    .css-1h5vz9d {
        z-index: 1000 !important;
    }
    .css-1s3wgy2 {
        z-index: 1000 !important;
    }
    .css-1s3wgy2 {
        z-index: 1000 !important;
    }
    .css-1s3wgy2 {
        z-index: 1000 !important;
    }
    .css-1vb7lhv {
        z-index: 1000 !important;
    }
    .css-mx6j8v {
        z-index: 1000 !important;
    }
    .css-1s3wgy2 {
        z-index: 1000 !important;
    }
            div.css-1inwz65.ew7r33m0 {
            font-size: 0.8em !important;
            font-family: sans-serif !important;
        }
        div.StyledThumbValue.css-12gsf70.ew7r33m2{
            font-size: 0.8em !important;
            font-family: sans-serif !important;
            color: #FAFAFA !important;
        }
        @media (max-width: 1024px) {
          div.css-1inwz65.ew7r33m0 {
            font-size: 0.8em !important;
            font-family: sans-serif !important;
          }
          div.StyledThumbValue.css-12gsf70.ew7r33m2{
            font-size: 0.8em !important;
            font-family: sans-serif !important;
            color: #FAFAFA !important;
        }
      }
    @media (max-width: 1024px) {
        div.block-container.css-ysnqb2.e1g8pov64 {
            margin-top: -15em !important;;
        }
    }
    div.stButton {
        display: flex !important;
        justify-content: center !important;
    }
    
     div.stButton > button:first-child {
        background-color: #002147;
        color: #FAFAFA;
        border-color: #FAFAFA;
        border-width: 0.15em;
        width: 100%;
        height: 0.2em !important;
        margin-top: 0em;
        font-family: sans-serif;
    }
    div.stButton > button:hover {
        background-color: #76787A;
        color: #FAFAFA;
        border-color: #002147;
    }
    @media (max-width: 1024px) {
    div.stButton > button:first-child {
        width: 100% !important;
        height: 0.8em !important;
        margin-top: 0em;
        border-width: 0.15em; !important;
        }
    }
    /* The input itself */
  div[data-baseweb="select"] > div,
  input[type=number] {
  color: #FAFAFA;
  background-color: #4F5254;
  border: 0.25em solid #002147;
  font-size: 0.8em;
  font-family: sans-serif;
  height: 3em;
  }
  div[data-baseweb="textarea"] > div,
  input[type=text] {
  color: #FAFAFA;
  background-color: #4F5254;
  border: 0.25em solid #002147;
  font-family: sans-serif;
  height: 12em;
  }
  div[data-baseweb="textarea"] > div:hover,
  input[type=text]:hover {
  background-color: #76787A;
  }
 
  /* Hover effect */
  div[data-baseweb="select"] > div:hover,
  input[type=number]:hover {
  background-color: #76787A;
  }
  span.st-bj.st-cf.st-ce.st-f3.st-f4.st-af {
  font-size: 0.6em;
  }
  @media (max-width: 1024px) {
    span.st-bj.st-cf.st-ce.st-f3.st-f4.st-af {
    font-size: 0.8em;
    }
  }
  
  /* Media query for small screens */
  @media (max-width: 1024px) {
  div[data-baseweb="select"] > div,
  input[type=number] {
    font-size: 0.8em;
    height: 3em;
  }
  div[data-baseweb="textarea"] > div,
  input[type=text]{
    height: 12em;
  }
  .stMultiSelect [data-baseweb="select"] > div,
  .stMultiSelect [data-baseweb="tag"] {
    height: auto !important;
  }
  }
  button[title="View fullscreen"]{
    visibility: hidden;
    }
  </style>
""", unsafe_allow_html=True)

line1 = '<hr class="line1" style="height:0.1em; border:0em; background-color: #FCBC24; margin-top: 0em; margin-bottom: -2em;">'
line_media_query1 = '''
    <style>
    @media (max-width: 1024px) {
        .line1 {
            padding: 0.3em;
        }
    }
    </style>
'''

line2 = '<hr class="line2" style="height:0.1em; border:0em; background-color: #FAFAFA; margin-top: 0em; margin-bottom: -2em;">'
line_media_query2 = '''
    <style>
    @media (max-width: 1024px) {
        .line2 {
            padding: 0.05em;
        }
    }
    </style>
'''


def img_to_bytes(img_path):
    img_bytes = pathlib.Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

header = """
    <style>
        :root {{
            --base-font-size: 1vw;  /* Define your base font size here */
        }}

        .header {{
            font-family:sans-serif; 
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-image: url('data:image/png;base64,{}');
            background-repeat: no-repeat;
            background-size: cover;
            background-position: center;
            filter: brightness(0.9) saturate(0.8);
            opacity: 1;
            color: #FAFAFA;
            text-align: left;
            padding: 0.4em;  /* Convert 10px to em units */
            z-index: 1;
            display: flex;
            align-items: center;
        }}
        .middle-column {{
            display: flex;
            align-items: center;
            justify-content: center;
            float: center;            
            width: 100%;
            padding: 2em;  /* Convert 10px to em units */
        }}
        .middle-column img {{
            max-width: 200%;
            display: inline-block;
            vertical-align: middle;
        }}
        .clear {{
            clear: both;
        }}
        body {{
            margin-top: 1px;
            font-size: var(--base-font-size);  /* Set the base font size */
        }}
        @media screen and (max-width: 1024px) {{
        .header {{
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 3em;
       }}

        .middle-column {{
            width: 100%;  /* Set width to 100% for full width on smaller screens */
            justify-content: center;
            text-align: center;
            display: flex;
            align-items: center;
            float: center;
            margin-bottom: 0em;  /* Adjust margin for smaller screens */
            padding: 0em;
        }}
        .middle-column img {{
            width: 30%;
            display: flex;
            align-items: center;
            justify-content: center;
            float: center;
          }}
    }}
    </style>
    <div class="header">
        <div class="middle-column">
            <img src="data:image/png;base64,{}" class="img-fluid" alt="comrate_logo" width="8%">
        </div>
    </div>
"""

# Replace `image_file_path` with the actual path to your image file
image_file_path = "images/oxbrain_header_background.jpg"
with open(image_file_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

st.markdown(header.format(encoded_string, img_to_bytes("images/oxbrain_logo_trans.png")),
            unsafe_allow_html=True)

spinner = st.empty()


col1, col2, col3 = st.columns([1, 4, 1])
with col2:
  header_text = '''
    <p class="header_text" style="margin-top: 3.6em; margin-bottom: 0em; text-align: center;"><span style="color: #FAFAFA; font-family: sans-serif; font-size: 1.8em; ">Virtual Conversational Assistant</span></p>
  '''

  header_media_query = '''
      <style>
      @media (max-width: 1024px) {
          p.header_text {
            font-size: 3.2em;
          }
      }
      </style>
  '''
  st.markdown(header_media_query + header_text, unsafe_allow_html=True)
  information_text1 = '''
    <p class="information_text" style="margin-top: 2em; margin-bottom: 0em; text-align: justify;"><span style="color: #FAFAFA; font-family: sans-serif; font-size: 1em; ">In this interactive playground, you can explore the capabilities of conversational AI technology using advanced natural language processing algorithms. To begin, simply engage the virtual assistant by asking a question and the AI model will provide you with an insightful response. If you need inspiration, the playground can also provide example questions to kickstart your interactions. Please note that this playground is designed to process a maximum of 10 interactions.</span></p>
  '''
  subheader_text_field2 = st.empty()
  subheader_text_field2.markdown(information_media_query + information_text1, unsafe_allow_html=True)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

footer = """
<style>
    .footer {
        font-family:sans-serif;
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        color: #FAFAFA;
        background-color: #222222;
        text-align: left;
        padding: 0em;
        padding-left: 1.875em;
        padding-right: 1.875em;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        vertical-align: middle;
    }
    .left-column-footer {
        float: left;
        font-size: 0.65em;
        width: 17.5%;
        padding: 0.625em;
        text-align: left;
        vertical-align: middle;
    }
    .middle-column-footer {
        font-size: 0.65em;
        width: 65%;
        padding: 0.625em;
        text-align: justify;
    }
    .right-column-footer {
        font-size: 0.65em;
        width: 17.5%;
        padding: 0.625em;
    }
    .clear {
        clear: both;
    }

    .content-container {
        /*padding-bottom: 100px;*/
    }
     @media screen and (max-width: 1024px) {
        .footer {
            flex-direction: column;
            justify-content: left;
            align-items: flex-start;
            padding: 0.8em;  /* Adjust padding for smaller screens */
       }
        .left-column-footer {
            width: 30%;
            justify-content: justify;
            display: flex;
            font-size: 2.2em;
            padding: 0.625em;
            margin-bottom: 0em;
            text-align: left;
            display: flex;
        }

        .middle-column-footer {
            width: 100%;
            font-size: 2.2em;
            padding: 0.625em;
            margin-bottom: 0em;
            text-align: justify;
        }
        .right-column-footer {
            width: 0%;
        }
    }
    </style>

<div class="content-container">
    <div class="footer">
        <div class="left-column-footer">
            <b><span style="color: #FAFAFA;">Contents &copy; oxbr</span><span style="color: #FCBC24;">AI</span><span style="color: #FAFAFA;">n 2023</span></b>
        </div>
        <div class="middle-column-footer">
            <b>DISCLAIMER: The functionalities of the conversational technology provided in the playground are facilitated through advanced AI innovations developed by OpenAI. This playground may exhibit inherent limitations associated with the accuracy of its responses and is intended for educational purposes only.</b>
        </div>
        <div class="clear"></div>
    </div>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)



  
