import time
import streamlit as st
import random
import base64
from ekstra import ekstra
from rating import rating
from streamlit_extras.stylable_container import stylable_container
import secrets
from streamlit_cookies_controller import CookieController
from datetime import datetime, timedelta, timezone

cookies = CookieController()
COOKIE_NAME = 'logged_in'
login_status = cookies.get(COOKIE_NAME)
expiry = datetime.now(timezone.utc) + timedelta(days=180)

st.markdown("""
<meta name="viewport" content="width=device-width, initial-scale=1">
""", unsafe_allow_html=True)

st.set_page_config(page_title="Tempat Duduk Generator", page_icon="icon.jpg")

st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Amaranth:ital,wght@0,400;0,700;1,400;1,700&family=Anta&family=Convergence&family=Fredoka:wght@550&family=Patrick+Hand&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Galdeano&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,100..900;1,100..900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Arima:wght@100..700&family=BBH+Sans+Bogle&family=Momo+Trust+Display&family=Rowdies:wght@300;400;700&display=swap');            

.jost-normal {
  font-family: "Jost", sans-serif;
  font-optical-sizing: auto;
  font-weight: 400;
  font-style: normal;
}
.jost-bold {
  font-family: "Jost", sans-serif;
  font-optical-sizing: auto;
  font-weight: 800;
  font-style: normal;
}
.momo-trust-display-regular {
font-family: "Momo Trust Display", sans-serif;
font-weight: 400;
font-style: normal;
}
.bbh-sans-bogle-regular {
font-family: "BBH Sans Bogle", sans-serif;
font-weight: 400;
font-style: normal;
}
</style>""", unsafe_allow_html=True)
st.markdown("""
<style>
.galdeano-regular {
  font-family: "Galdeano", sans-serif;
  font-weight: 400;
  font-style: normal;
}
.fredoka-e {
  font-family: "Fredoka", sans-serif;
  font-optical-sizing: auto;
  font-weight: 550;
  font-style: normal;
  font-size: 3rem;
  font-variation-settings:
    "wdth" 100;
}
.patrick-hand-regular {
  font-family: "Patrick Hand", cursive;
  font-weight: 400;
  font-style: normal;
}
.anta-regular {
  font-family: "Anta", sans-serif;
  font-weight: 400;
  font-style: normal;
}
.amaranth-regular {
  font-family: "Amaranth", sans-serif;
  font-weight: 400;
  font-style: normal;
}
.convergence-regular {
  font-family: "Convergence", sans-serif;
  font-weight: 400;
  font-style: normal;
}

</style>""", unsafe_allow_html=True)

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


if not "select" in st.session_state:
    st.session_state.select = "Utama"

st.markdown(
    f"""
    <style>
    .stApp {{
    background: transparent;
    }}
    .stApp::before {{
        --c1 : #19202e;
        --c2 : #101727;
        content: "";
        z-index: -1;
        inset: 0;
        width: 200%;
        height: 200%;
        position: fixed;
        background: linear-gradient(135deg, var(--c1) 25%, var(--c2)25%, var(--c2) 50%,var(--c1) 50%, var(--c1) 75%, var(--c2) 75%);
        background-size: 100px 100px;
        animation: BGmove 4500ms linear infinite;    
    }}
    
    @keyframes BGmove {{
        to {{transform: translate(-100px, -100px);}}
    }}
    </style>
    """, unsafe_allow_html=True)

if  st.session_state.select == 'Utama':
    st.html(f"""
            <div class="container-judul">
                <img  src="data:image/jpg;base64,{get_base64("images/newdarkstbg.jpg")}" class="gambar">
                <div class="judul-utama bbh-sans-bogle-regular">Tempat duduk generator</div>
                <div class="keterangan-judul fredoka-e">Untuk kelas 10 (TA 2025-2026)</div>
            </div>
            
            <style>
            .container-judul {{
                border-top: 8px solid #198de6;
                border-right: 12px solid transparent;
                border-left: 12px solid transparent;
                position: relative;
                overflow: hidden;
                height: auto;
                mask-image: linear-gradient(to bottom,red 65%, transparent 95%);
                transition: border .5s ease-in-out;
            }}
            
            .judul-utama, .keterangan-judul {{
                margin: auto;
                text-align: center;
                position: relative;
                user-select: transparent;
            }}
            
            .gambar {{
                height: 170px;
                width: 100%;
                object-fit: cover;
                position: absolute;
                padding: 0 5px;
                color: transparent;
            }}
            
            .judul-utama {{
                text-align: center;
                color:white;
                font-size:2.5rem;
                letter-spacing:.2rem;
                margin-top: .7rem;
                line-height: 2.35rem;
                animation: judul-slidedown 800ms ease;  
            }}
            .keterangan-judul {{
                text-align: center;
                color:#d1d1d1;
                font-size:1.05rem;
                letter-spacing:.025rem;
                margin: -5px auto 1.2rem;
                line-height: 2.5rem;
                animation: judul-slideup 1400ms ease;
            }}
            
            @keyframes judul-slidedown {{
                from {{
                    transform: translatey(-200%);
                }}
                to {{
                    transform: translatey(0%);
                }}
            }}
            @keyframes judul-slideup {{
                from {{
                    transform: translatey(200%);
                }}
                to {{
                    transform: translatey(0%);
                }}
            }}
            </style>
            """)

    def seatgen(subclass):
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                30, 31, 32]
        # 10.1
        if subclass == 'X-1':
            data = {1: 'L', 2: 'L', 3: 'L', 4: 'P', 5: 'P', 6: 'L', 7: 'P', 8: 'P', 9: 'L', 10: 'L', 11: 'L', 12: 'P',
                    13: 'L', 14: 'L', 15: 'P', 16: 'P', 17: 'P', 18: 'L', 19: 'P', 20: 'L', 21: 'L', 22: 'L', 23: 'P',
                    24: 'P', 25: 'L', 26: 'P', 27: 'L', 28: 'L', 29: 'P', 30: 'P', 31: 'P', 32: 'L'}
        # 10.2
        if subclass == 'X-2':
            data = {1: 'L', 2: 'P', 3: 'P', 4: 'L', 5: 'L', 6: 'P', 7: 'L', 8: 'P', 9: 'P', 10: 'P', 11: 'P', 12: 'P',
                    13: 'P', 14: 'P', 15: 'L', 16: 'P', 17: 'L', 18: 'L', 19: 'L', 20: 'L', 21: 'L', 22: 'P', 23: 'L',
                    24: 'P', 25: 'L', 26: 'L', 27: 'P', 28: 'L', 29: 'P', 30: 'L', 31: 'L', 32: 'L'}
        # 10.3
        if subclass == 'X-3':
            data = {1: 'L', 2: 'L', 3: 'L', 4: 'L', 5: 'L', 6: 'L', 7: 'L', 8: 'P', 9: 'P', 10: 'P', 11: 'P', 12: 'L',
                    13: 'L', 14: 'P', 15: 'L', 16: 'L', 17: 'P', 18: 'L', 19: 'L', 20: 'L', 21: 'P', 22: 'P', 23: 'L',
                    24: 'P', 25: 'P', 26: 'P', 27: 'L', 28: 'P', 29: 'P', 30: 'P', 31: 'L', 32: 'P'}
        # 10.4
        if subclass == 'X-4':
            data = {1: 'L', 2: 'P', 3: 'L', 4: 'P', 5: 'P', 6: 'L', 7: 'L', 8: 'L', 9: 'P', 10: 'L', 11: 'L', 12: 'P',
                    13: 'P', 14: 'P', 15: 'P', 16: 'P', 17: 'L', 18: 'P', 19: 'P', 20: 'L', 21: 'L', 22: 'L', 23: 'L',
                    24: 'P', 25: 'L', 26: 'L', 27: 'L', 28: 'L', 29: 'P', 30: 'P', 31: 'L', 32: 'P'}
        # 10.5
        if subclass == 'X-5':
            data = {1: 'P', 2: 'L', 3: 'L', 4: 'P', 5: 'P', 6: 'P', 7: 'L', 8: 'P', 9: 'L', 10: 'P', 11: 'L', 12: 'P',
                    13: 'L', 14: 'P', 15: 'P', 16: 'L', 17: 'L', 18: 'L', 19: 'P', 20: 'L', 21: 'L', 22: 'L', 23: 'L',
                    24: 'L', 25: 'P', 26: 'L', 27: 'L', 28: 'P', 29: 'P', 30: 'P', 31: 'L', 32: 'P'}
            names = st.secrets['x5']
            nama = [name.center(6, '-').title() for name in names]
        # 10.6
        if subclass == 'X-6':
            data = {1: 'P', 2: 'P', 3: 'L', 4: 'L', 5: 'L', 6: 'P', 7: 'L', 8: 'L', 9: 'L', 10: 'P', 11: 'P', 12: 'L',
                    13: 'L', 14: 'L', 15: 'P', 16: 'P', 17: 'L', 18: 'L', 19: 'P', 20: 'P', 21: 'P', 22: 'P', 23: 'L',
                    24: 'L', 25: 'L', 26: 'L', 27: 'P', 28: 'P', 29: 'P', 30: 'P', 31: 'L', 32: 'P'}
            names = st.secrets['x6']
            nama = [name.center(6,'-').title() for name in names]
        def luminance(r, g, b):
            return 0.2126 * r + 0.7152 * g + 0.0722 * b
        def darkener(r, g, b, faktor):
            r = int(r * faktor)
            g = int(g * faktor)
            b = int(b * faktor)
            return [r,g,b]

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = luminance(r, g, b)
        border = darkener(r, g, b, 0.5)
        shadow = darkener(r, g, b, 1.1)
        if color > 128:
            result_color = 'black'
        else:
            result_color = 'white'
        st.markdown(
            f"""<div style="font-size: 1.1rem;font-family: Times New Roman;text-align:center;font-weight:bold;background-color: rgb({r},{g},{b});border-radius:8px;padding:0.05px;color:{result_color};margin: 1.15em 1em;border: .2rem solid rgb({border[0]},{border[1]},{border[2]});box-shadow: 0 0 10px 3px rgb({shadow[0]},{shadow[1]},{shadow[2]});transition: all .25s ease;">Tata Letak Tempat Duduk Baru!</div>""",
            unsafe_allow_html=True)
        st.html(f"""
                <div style="display: flex;justify-content: center;">    
                    <div class="testbox"></div>
                </div>
                <style>
                .testbox {{
                    width: 103%;
                    height: 180px;
                    background-image: linear-gradient(90deg, #4f2f03,black 15%, black 85%,#4f2f03);
                    position: absolute;
                    margin: auto;
                    border-radius: 10px;
                    border: 2px solid #383838;
                    box-shadow: 0px 0px 5px 0 white;
                }}
                
                @media (max-width: 600px) and (min-width: 471px) {{
                    .testbox {{
                        height: 175px;
                    }}
                }}
                @media (max-width: 470px) {{
                    .testbox {{
                        height: {'155px' if subclass == "X-5" or subclass == "X-6" else "180px"};
                    }}
                }}
                
                </style>
                """)
        st.markdown(
            f"""
            <div id="whiteboard">
                PAPAN TULIS
            </div>
            <style>
            #whiteboard {{
                background-color: #9a9c9a;
                border: 2px solid #6b6e6b;
                color: black;
                padding: 0px;
                border-radius: 6px;
                text-align: center;
                font-weight: bold;
                width: {475 if subclass == "X-5" or subclass == "X-6" else 240}px;
                margin: auto;
                box-sizing: content-box;
            }}
            
            @media (max-width: 600px) and (min-width: 471px) {{
                #whiteboard {{
                    width: {420 if subclass == "X-5" or subclass == "X-6" else 240}px;
                }}
            }}
            @media (max-width: 470px) {{
                #whiteboard {{
                    width: {290 if subclass == "X-5" or subclass == "X-6" else 240}px;
                }}
            }}
            </style>
            """,
            unsafe_allow_html=True)
        match subclass:
            case 'X-1' | 'X-2' | 'X-3' | 'X-4':
                st.markdown(
                    """
                    <div style="
                        background-color: #ba6900;
                        border: 2px solid #8f5304;
                        color: black;
                        padding: 1px;
                        border-radius: 5px;
                        text-align: center;
                        font-weight: bold;
                        font-size: 0.7rem;
                        display: block;
                        width: 50px;
                        margin: 0 auto;
                        transform: translateX(95px);
                        box-sizing: content-box;
                    ">
                        MejaGuru
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            case 'X-5' | 'X-6':
                st.markdown(
                    """
                   <div id="mejaguru">
                       Meja Guru
                   </div>
                   <style>
                   #mejaguru {
                       background-color: #ba6900;
                       border: 2px solid #8f5304;
                       color: black;
                       padding: 1px;
                       border-radius: 5px;
                       text-align: center;
                       font-weight: bold;
                       font-size: 0.75rem;
                       display: block;
                       width: 110px;
                       margin: 0 auto;
                       transform: translateX(-182px);
                   }
                   
                   @media (max-width: 600px) and (min-width: 471px) {
                    #mejaguru {
                        transform: translateX(-161px);
                    }
                   }
                   @media (max-width: 470px) {
                    #mejaguru {
                        transform: translateX(-112px);
                        width: 68px;
                    }
                   }
                   </style>
                   """,
                    unsafe_allow_html=True
                )
        counter = 1
        for h in range(4):
            st.write()
            counter -= 1
            rcount = 0
            rows = ['', '', '', '']
            for i in range(4):
                for j in range(2):
                    #random.shuffle(list)
                    while True:
                        try:
                            idk = secrets.choice(list)
                        except IndexError:
                            rows[3] += "&nbsp;&nbsp&nbsp;[XX]"
                            break
                        if data[idk] == 'L' and (counter % 2 != 0 or counter % 2 == 0) and not 'P' in data.values():
                            output = f"[<span style = 'color : #006aff'>{nama[idk-1] if subclass == "X-6" or subclass == "X-5" else str(idk).rjust(2, "0") }</span>]"
                            rows[rcount] += output
                            del data[idk]
                            list.remove(idk)
                            break
                        if data[idk] == 'P' and (counter % 2 != 0 or counter % 2 == 0) and not 'L' in data.values():
                            output = f"[<span style = 'color : #e91ef7'>{nama[idk-1] if subclass == "X-6" or subclass == "X-5" else str(idk).rjust(2, "0") }</span>]"
                            rows[rcount] += output
                            del data[idk]
                            list.remove(idk)
                            break
                        if data[idk] == "P":
                            if counter % 2 != 0:
                                output = f"[<span style = 'color : #e91ef7'>{nama[idk-1] if subclass == "X-6" or subclass == "X-5" else str(idk).rjust(2, "0") }</span>]"
                                counter += 1
                                rows[rcount] += output
                                del data[idk]
                                list.remove(idk)
                                break
                            else:
                                continue
                        if data[idk] == "L":
                            if counter % 2 == 0:
                                output = f"[<span style = 'color : #006aff'>{nama[idk-1] if subclass == "X-6" or subclass == "X-5" else str(idk).rjust(2, "0") }</span>]"
                                counter += 1
                                rows[rcount] += output
                                del data[idk]
                                list.remove(idk)
                                break
                            else:
                                continue
                if j != 2 and i != 3:
                    rows[rcount] += '&nbsp;&nbsp;'
                rows[rcount] = rows[rcount].strip()
            st.markdown(f"""
            <div class="res-container" style="text-align:center;max-width: 100%; margin: 0;"> 
                <span class="result" style= "">{rows[rcount]}</span>
            </div>
            
            <style>
            .res-container{{
            margin: 0 auto;
            display: flex;
            justify-content: center;
            }}
            
            .result {{
                font-family: monospace;
                letter-spacing:-0.025em;
                border-radius: 3px;
                padding:1.5px;
                line-height: auto;
                font-size: {0.8 if subclass == "X-5" or subclass == "X-6" else 0.75}rem;
                }}
            
            @media (max-width: 600px) and (min-width: 471px){{
                .result {{
                letter-spacing:-0.05em;
                padding:1px;
                font-size: .75rem;
                }}
            }}
            @media (max-width: 470px){{
                .result {{
                letter-spacing:-0.07rem;
                padding:1px .1px;
                font-size: {0.6 if subclass == "X-5" or subclass == "X-6" else 0.85}rem;
                line-height: -1.9rem;
                display: flex;
                justify-content: center;
                margin: 0 auto;
                width: {'300px' if subclass == "X-5" or subclass == "X-6" else 'auto'};
                }}
            }}
            </style>
            
            """, unsafe_allow_html=True)
            rcount += 1
        st.markdown("""
                    <style>
                    .rainbow {
                    background: linear-gradient(90deg, red, orange, yellow, lime, cyan,violet, pink);  
            -webkit-background-clip: text;  
            -webkit-text-fill-color: transparent;
                    }
                    </style>
                    """,unsafe_allow_html=True)
        if subclass == "X-6":
            st.markdown("""  
    <br>
    <div style="text-align:center;max-width: 100%; margin: .5rem auto 2rem auto;line-height: 0.25;">
        <span class="x6-rainbow" style="text-align: center; background-color: black;border-radius:5px;border: 1px solid #636363;padding:.15rem;">
            <span>☝️</span>         
            <span class='rainbow'>Senin-Kamis sesuai ini</span>
            <span>☝️</span> 
            <span class='rainbow'>Jumat bebas!!</span>
            <span>✨</span> 
        </span>  
    </div>
    
    <style>
    .x6-rainbow span {
        font-size: 0.85rem;
    }
    .x6-rainbow span:nth-child(odd) {
        letter-spacing: -0.15em;
    }
    </style> 
    """, unsafe_allow_html=True)
        st.markdown("""
                <style>
                .stAlert {
                    background-color: #00d907 ;
                    opacity: 0.5 ;
                    border-radius: 30px ;
                }
                </style>
            """, unsafe_allow_html=True)
        st.html(f"""<div class="jost-bold sukses" style='background-color:rgba(0,175,0,0.8);border:2px solid #4bd14b;opacity:0.9;border-radius:20px 99px 99px 20px;text-align:left;padding:12px;
                        color: #000000; max-width:85%;'><i>Pengacakan Berhasil!! 🥳🥳🥳<br>(kamu dah rolling {st.session_state.count} kali)</i></div>
                    
                    <style>
                    @media (max-width: 470px) {{
                        .sukses {{
                            font-size: 0.85rem;
                        }}
                    }}
                    </style>
                    """)

    st.markdown(
        """
        <div class="jost-normal" style = "color:white;margin: 1.55rem .1rem .3rem .2rem;font-size:1.1rem">
        Rolling tempat duduk kelas berapa? 🔢
        </div>
        """,
        unsafe_allow_html=True
    )
    subclass = st.selectbox('', ['Kosong', 'X-1', 'X-2', 'X-3', 'X-4', 'X-5', 'X-6'], label_visibility="collapsed")
    if 'count' not in st.session_state:
        st.session_state.count = 1
    if st.button("Buat Seating-Chart baru! 🎲"):
        if subclass != 'Kosong':
            if (subclass == "X-5" or subclass == 'X-6') and login_status != "yes":
                @st.dialog("Keamanan Privasi")
                def login():
                    st.html("""<div class="jost-normal" style="margin-bottom: -10px;">Masukin passwordmu</div>""")
                    user_input = st.text_input("", label_visibility="collapsed")
                    if st.button("Submit Passwordmu"):
                        if user_input != st.secrets["user_pw"]:
                            st.html("""<div class="jost-normal" style="margin-bottom: -10px;color:red;">Password Salah</div>""")
                        else:
                            cookies.set(COOKIE_NAME,"yes",expires=expiry,secure=False,same_site="Lax")
                            time.sleep(0.2)
                            st.rerun()
                login()
            else:
                seatgen(subclass)
                st.session_state.count += 1
        elif subclass == 'Kosong':
            st.markdown("""<div class="jost-bold" style='background-color:rgba(255,0,0,0.8);opacity:0.9;border-radius:28px 89px 89px 28px;text-align:left;padding:13px;
                        color: #000000;max-width:78%;border: 2px solid #fc5858'><i>Pilih kelas dulu lah kocak... 😐</i></div>""",
                        unsafe_allow_html=True)
    else:
        st.markdown("""<div class="jost-bold" style='background-color:rgba(242,210,0,0.8);opacity:0.9;border-radius:25px 89px 89px 25px;text-align:left;padding:13px;
                        color: #000000;max-width:55%;border:2px solid #ffec70;'><i>Pilih Kelasmu! 📚</i></div>""", unsafe_allow_html=True)

    st.html(""" 
            <style>
            .sidebar-title {
                display: flex;
                justify-content: center;
                align-items: center;
                border: 3px solid black;
                flex-direction: column;
                background-image: linear-gradient(20deg, transparent 35%, #0a112b 55%, #0e1d52), repeating-linear-gradient(-10deg,transparent 45px, #1f1f1f 45px, #1f1f1f 48px,transparent 48px, transparent 80px), repeating-linear-gradient(80deg,black 45px, #1f1f1f 45px, #1f1f1f 48px,black 48px, black 80px);
                border-radius: 10px;
                box-shadow: 0 0 5px 0 #858585, 0 0 15px 0 #2e3d73 inset;
                padding: 5px;
                font-size: 1.25rem;
            }
            </style>
            """)
elif st.session_state.select == "Ekstra":
    ekstra()
elif st.session_state.select == 'Kredit':
    rating()

btn_css_property = """
                    button {
                    background-image: linear-gradient(90deg,#383838 -5%,#181818 20%);
                    margin: .4rem;
                    border-left: 3px solid #424242;
                    border-right: 2px solid #424242;
                    border-top: 2px solid #424242;
                    border-bottom: 2px solid #424242;
                    transition: all .25s ease;
                    color: white;
                    width: 100px;
                    border-radius: 14px 50px 50px 14px ;
                    transition: all 1s ease;
                    font-weight: bold;
                    }
                    """

with st.sidebar:
    st.html(f"""
            <div class="sidebar-title momo-trust-display-regular">{st.session_state.select}</div>
            """)
    with stylable_container(key="utama", css_styles=btn_css_property):
        if st.button("Utama", key="btn_utama"):
            st.session_state.select = "Utama"
            st.rerun()
    with stylable_container(key="ekstra", css_styles=btn_css_property):
        if st.button("Extra", key="btn_ekstra"):
            st.session_state.select = "Ekstra"
            st.rerun()
    with stylable_container(key="kredit", css_styles=btn_css_property):
        if st.button("Kredit", key="btn_kredit"):
            st.session_state.select = "Kredit"
            st.rerun()

