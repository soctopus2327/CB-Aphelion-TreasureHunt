import streamlit as st
import random

st.set_page_config(page_title="Celestial Biscuit", page_icon="🌌", layout="centered")

hide_streamlit_style = """
    <style>
    /* Hide Streamlit's default header */
    header[data-testid="stHeader"] {
        background: none !important;
        height: 0px;
    }

    /* Hide the footer ("Made with Streamlit") */
    footer {visibility: hidden;}

    /* Optional: also hide the top hamburger menu */
    #MainMenu {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

CLUES = {
    "it": 
    ["Seek the digital nebula where our society's first navigator charted the course. In this constellation of computers, the founder’s legacy still processes through the cosmic web.", 
     '''There is a department of digital dreams,
      Where our founder built celestial schemes,
      With code as her brush,
      And innovation's rush,
      She painted the future in algorithmic streams. [A01]
      ''', 
     '''Decode this cosmic transmission to navigate your stellar journey:
    ... . . -.- / - .... . / -... .. -. .- .-. -.-- / .-. . .- .-.. -- / .-- .... . .-. . / --- ..- .-. / ..-. --- ..- -. -.. . .-. / ..-. .. .-. … - / -.-. --- -- .--. .. .-.. . -.. / -.. .-. . .- -- ... / .. -. - --- / .-. . .- .-.. .. - -.-- [A02]''',
    '''In cosmic webs where starlight flows,
    This realm of code forever grows.
    The department with the newest ship
    Where AKM leads with kindness and skill. [A03]'''
    ],
    "ece": 
    ["Enter the quantum dimension where subatomic particles obey the laws of probability, and engineers harness the power of distant pulsars through electromagnetic wizardry. [D01]", 
     '''In chambers smaller than a grain of sand,
      Billions of transistors take their stand,
      Each one a soldier in the binary war,
      Fighting chaos with logic's law.
      Seek the temple where chips are born,
      In this electronic cosmic dawn. [D02]''', 
     "Navigate to the stellar laboratory where circuit constellations are born, and resistors align like planets in perfect orbital harmony. [D03]",
     '''Decrypt this signal to locate your next station.
    - .... . / .--. .-.. .- -.-. . / .-- .... . .-. . / ...- --- .-.. - .- --. . / -.. .- -. -.-. . ... / .- -. -.. / . .-.. . -.-. - .-. --- -. ... / .--. .-.. .- -.-- [D04]''',
    '''Signals pulse like cosmic rays,
      Through this place in endless ways.
      Hardware, software, side by side,
      Here your treasure likes to hide. [D05]''',
      '''Constellations are stars combined,
      Here too, great circuits are designed.
      Explore the hub where sparks ignite,
      Your cosmic clue is kept in sight. [D06]''',
      '''Circuits whisper, logic sings,
      Where future minds build cosmic things.
      The giant of growth, wise and vast,
      Seek where codes and circuits last. [D07]
'''
     ],
    "canteen": 
    ["The galactic diner where space travelers dock to refuel their biological engines before venturing into the academic cosmos. [B01]", 
     "Seek the nebula where stellar chefs transform cosmic ingredients into earthly delights, fueling the next generation of space explorers. [B02]", 
     '''Astronauts dine in packets small,
      But here awaits a feast for all.
      Where hunger fades and chatter flows,
      Your cosmic trail in whispers grows. [B03]''',
     '''Gravity pulls both moon and sun,
      This place pulls everyone for fun.
      Fuel your voyage, take a stand,
      The next star waits where meals are planned. [B04]''',
     '''Like a nebula swirling, warm and sweet,
      This corner of CB is where all meet.
      Look where biscuits, samosas, fry
      Your clue lies where the hungry fly. [B05]''',
     '''Warmth and chatter, bites divine,
      Venus rules where hearts align.
      Sweet or spicy, taste your fate —
      The planet hides where friends debate. [B06]
      '''
    ],
    "badminton": 
      ["Houston, we have a game! Navigate to the launch pad where feathered projectiles orbit between opposing space stations. [C01]", 
       '''Up and down, up and down,
        Like satellites around Earth's crown,
        White birds that never truly fly,
        Yet dance between the floor and sky.
        Find the court where gravity's jest
        Makes earthbound souls feel truly blessed. [C02]
        ''', 
       "Where objects defy gravity in graceful arcs, much like comets dancing through the asteroid belt, the sport that mimics celestial mechanics awaits your discovery. [C03]",
       '''Where comets streak and races are fast,
        Here every shot is built to last.
        Shuttles soar like meteors bright,
        Find this court where stars take flight. [C04]''',
        '''Galaxies spin, quick and wide,
        Players here move side to side.
        With every smash the cosmos sings,
        Seek the place of feathered wings. [C05]
        ''',
        '''I’m a court where feathers fly,
        Red like Mars, I touch the sky.
        Smashes echo, spirits soar —
        Find the planet near the score. [C06]
        '''
       ],
    "architecture": 
    ["Seek the cosmic architects who draft the blueprints for tomorrow's space colonies, where every line drawn reaches toward the stars. [E01]", 
     '''There once was a department of design,
      Where cosmic blueprints intertwine,
      With rulers straight
      They calculate fate,
      And make the future plans align. [E02]
      ''', 
      '''Galaxies form with balance and grace,
      Here too, structures take their place.
      Designs are born of cosmic art,
      Seek the halls where visions start. [E03]''',
      '''Blueprints trace like starlight beams,
      Here they build their cosmic dreams.
      Bricks and domes in thought appear,
      Among their models, sharp and grand. [E04]''',
     "Find the department where universal blueprints take form, and designers shape the future homes of interplanetary civilizations. [E05]"],
}

def pick_clues():
    chosen = [random.choice(v) for v in CLUES.values()]  
    random.shuffle(chosen)                             
    return chosen

if "clues" not in st.session_state:
    st.session_state.clues = pick_clues()

css = """
<style>
/* Try to override Streamlit default with !important */
html, body, .stApp {
  background: radial-gradient(circle at 10% 10%, #03041a 0%, #071633 25%, #0b2540 60%, #071225 100%) !important;
  color: #eaf2ff;
}

/* Inner card that contains the content */
.app-container {
  max-width: 920px;
  margin: 10px auto;
  padding: 32px;
  border-radius: 16px;
  background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
  border: 1px solid rgba(140,160,255,0.05);
  box-shadow: 0 12px 40px rgba(10,20,60,0.6), inset 0 1px 0 rgba(255,255,255,0.02);
}

/* Title */
.title {
  font-size: 44px;
  font-weight: 800;
  font-family: 'Courier New', monospace;
  text-align: center;
  margin-bottom: 6px;
  color: #cfe3ff;
  text-shadow: 0 3px 22px rgba(120,70,255,0.25);
}

.midtitle {
  font-size: 28px;   /* between 44px title and 14px subtitle */
  font-weight: 600;
  text-align: center;
  margin-bottom: 12px;
  color: #d4e0ff;
  text-shadow: 0 2px 12px rgba(140,180,255,0.25);
}

.smalltitle {
  font-size: 16px;   /* between 44px title and 14px subtitle */
  font-weight: 600;
  text-align: center;
  margin-bottom: 12px;
  color: #d4e0ff;
  text-shadow: 0 2px 12px rgba(140,180,255,0.25);
}

/* Subtitle */
.subtitle {
  text-align:center;
  color: #b8d6ff;
  margin-bottom: 20px;
  font-size: 14px;
}

/* Clue cards */
.clue {
  background: linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01));
  border-radius: 12px;
  padding: 16px 22px;
  margin: 12px 0;
  font-size: 18px;
  text-align: center;
  color: #eaf3ff;
  border: 1px solid rgba(130,170,255,0.06);
  box-shadow: 0 10px 24px rgba(60,110,255,0.06), 0 0 36px rgba(80,130,255,0.03);
}

/* small responsive tweaks */
@media (max-width: 700px) {
  .title { font-size: 32px; }
  .clue { font-size: 16px; padding: 14px; }
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

html = '<div class="app-container">'
html += '<div class="smalltitle">🌠 Celestial Biscuit</div>'
html += '<div class="title">Aphelion</div>'
html += '<div class="midtitle">Treasure Hunt</div>'
html += '<div class="subtitle">Go to the locations given in these clues and look for planets 🌍</div>'

for c in st.session_state.clues:
    html += f'<div class="clue">{c}</div>'

html += '</div>'

st.markdown(html, unsafe_allow_html=True)
