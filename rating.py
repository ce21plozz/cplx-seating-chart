import streamlit as st
import base64

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def rating():
    st.html(f"""
                <div class="container-judul">
                    <img  src="data:image/jpg;base64,{get_base64("images/newdarkstbg.jpg")}" class="gambar">
                    <div class="judul-utama bbh-sans-bogle-regular">🌟Kredit🌟</div>
                    <div class="keterangan-judul fredoka-e">Beserta rating untuk feedback</div>
                </div>

                <style>
                .container-judul {{
                    border-top: 8px solid #e60707;
                    border-right: 12px solid transparent;
                    border-left: 12px solid transparent;
                    position: relative;
                    overflow: hidden;
                    height: auto;
                    mask-image: linear-gradient(to bottom,red 65%, transparent 95%);
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

    st.html(f"""
            <div class="grid-container">
                <div class="me" style="grid-area: box1">
                    <div class="inner">
                        <div class="nama fredoka-e">ceplox21</div>
                        <img src="https://avatars.githubusercontent.com/u/230108871?v=4">
                        <div class="fredoka-e" id="text">Developer Utama</div>
                    </div>
                </div>
                <div class="him" style="grid-area: box2">
                    <div class="inner">
                        <div class="nama fredoka-e">molimen</div>
                        <img src="https://avatars.githubusercontent.com/u/95009791?v=4">
                        <div class="fredoka-e" id="text">Helper dan Tester</div>
                    </div>
                </div>
                <div class="her" style="grid-area: box3">
                    <div class="inner">
                        <div class="nama fredoka-e">Kelly</div>
                        <img src="data:image/png;base64,{get_base64("images/pfp anak populer upscaled.png")}">
                        <div class="fredoka-e" id="text">Promosi dan Pembuat Database X-5</div>
                    </div>
                </div>
                <div class="sign" style="grid-area: box4">
                    <div class="signtext momo-trust-display-regular">Kotak kotak di bagian kiri <br> dapat diinteraksi</div>
                </div>
            </div>

            <style>
            .nama {{
                position: absolute;
                color: #003fb5;
                bottom: 0%;
                left: 0%;
                padding: 5px;
                border-radius: 0 10px 0 0;
                background-color: #eb766c;
                font-size: 1.2rem;
                transition: background-color .75s ease;
                width: 100px;
                text-align: center;
            }}
            .her .nama {{
                color: #b500af;
            }}
            
            .grid-container > div:hover .nama {{
                position: absolute;
                bottom: 0%;
                left: 0%;
                padding: 5px;
                border-radius: 0 10px 0 0;
                background-color: var(--bg);
                font-size: 1.2rem;
                transition: background-color .75s ease;
            }}
            
            .sign .signtext{{
                display: flex;
                writing-mode: vertical-rl;
                text-orientation: sideways;
                font-size: 2rem;
                line-height: 2.65rem;
                height: 100%;
                width: 100%;
                justify-content: center;
                padding: .5em;
                align-items: center;
                color: black;
            }}
            
            .me #text {{
                font-size: 1.7rem;
                line-height: 2rem;
            }}
            .him #text {{
                font-size: 2rem;
                line-height: 2rem;
            }}
            .her #text {{
                font-size: 1.6rem;
                line-height: 1.6rem;
            }}
            
            .grid-container {{
                --bg: #f04643;
                --hover-effect: lime;
                display: grid;
                grid-template-columns: 75px 75px 75px 75px 75px;
                grid-template-rows: 75px 75px 75px 75px 75px 75px;
                gap: .5rem;
                grid-template-areas:
                "box1 box1 box1 box4 box4"
                "box1 box1 box1 box4 box4"
                "box2 box2 box2 box4 box4"
                "box2 box2 box2 box4 box4"
                "box3 box3 box3 box4 box4"
                "box3 box3 box3 box4 box4";
                justify-content: center;
                margin-bottom: 1.3rem;
            }}
            .grid-container > div {{ 
                transform-origin: left;
                transition: all .75s ease;
                border-radius: .75rem;
            }}
            
            #text {{
                display: flex;
                position: absolute;
                transform: translatex(190%);
                font-size: 1.2rem;
                transition: all .75s ease;
                letter-spacing: .05rem;
                color: black;
                z-index: -1;
                height: 148px;
                width: 130px;
                text-align: left;
                align-items: center;
                justify-content: center;
            }}
            
            .inner:hover #text {{
                transform: translatex(550%);
                transition: all .75s ease;
            }}
                    
            .sign {{
                background-image: linear-gradient(to right,#eb766c -15%, #b03e35 22%);
                border-radius: .75rem;
                border: 4px solid #7d1c14;
                box-shadow: 0 0 10px 2px black;
            }}
            
            .inner {{
                padding: 5px;
                border-radius: .75rem;
                background-color: #eb766c;
                pointer-events: none;
                height: 100%;
                transition: all .75s ease;
                overflow: hidden;
                box-shadow: 0 0 10px 2px black;
                position: relative;
                box-sizing: border-box;
                z-index: 0;
            }}
            .inner::before {{
            content: none;
            height: 10%;
            width: 10%;
            position: absolute;
            background-color: lime;
            z-index: 1;
            }}
            
            .me, .him, .her {{
            transform-style: preserve-3d;
            perspective: 1000px;
            z-index: 1;  
            }}
            
            .me:hover, .him:hover, .her:hover {{
                width: 160%;
                transition: all .75s ease;       
            }}
            .me .inner, .him .inner, .her .inner{{
                width: 241px;
                transition: all .75s ease;
                border: none;
            }} 
            .me:hover .inner, .him:hover .inner, .her:hover .inner{{
                width: 400px;
                transition: all .75s ease;
                transform: rotatey(-40deg);
                background-color: var(--bg);
            }}  
            
            .grid-container div img {{
                object-fit: cover;
                border-radius: .75rem;
                width: calc((75px * 3) + 1rem - 10px);
                height: 100%;
                pointer-events: none;
                float: left;
                z-index: 0;
            }}
            
            @media (max-width: 470px) {{
                .grid-container {{
                    transform: scale(.66);
                    margin: -60px auto;
                }}
            }}
            </style>
            """)

    st.markdown(f"""
                <form class="fblayout" action="https://formspree.io/f/mwprrgkn" method="POST">
                    <label for="rating" class="label galdeano-regular">Kasih Rating dalam bintang</label>
                    <br>
                    <div class="rating">
                      <input value="5" name="rate" id="star5" type="radio" required>
                      <label title="text" for="star5"></label>
                      <input value="4" name="rate" id="star4" type="radio">
                      <label title="text" for="star4"></label>
                      <input value="3" name="rate" id="star3" type="radio">
                      <label title="text" for="star3"></label>
                      <input value="2" name="rate" id="star2" type="radio">
                      <label title="text" for="star2"></label>
                      <input value="1" name="rate" id="star1" type="radio">
                      <label title="text" for="star1"></label>
                    </div>
                    <br>  
                    <label class="label galdeano-regular">
                        Kasih Feedback (saran atau kritik)
                        <br>
                        <textarea class='widget' name="feedback" rows="3" cols="20" placeholder="Tulis Feedback (maks 250 karakter)" maxlength="250" required></textarea>
                    </label>
                    <br>
                    <button class="widget" id="submit-btn" type="submit">Kirim Feedback</button>
                </form>
                """, unsafe_allow_html=True)
    # form's css stuff
    st.markdown("""
                <style>
                form {
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
                border: .15rem solid #505050;
                border-radius: 12px;
                background-color: #1f1f1f;
                margin: auto;
                width: clamp(18em,50%,85%);
                padding: .3em;
                box-shadow: 0px 5px 15px 1px black;
                }
                  
                .rating {
                display: inline-block;
                line-height: 2rem;
                margin-bottom: 1.45rem;
                }
                .labelradio:first-child {
                margin-left: 0;
                }
                
                .fblayout {
                flex-direction: rows;
                }

                .label {
                color:white;
                font-size:1.1rem;
                text-align:center;
                }
                .labelradio {
                color:yellow;
                font-size:.8rem;
                margin-left: 20px;
                }

                .widget {
                border-radius: 10px;
                border: 2px solid grey;
                transition: all 0.2s ease;
                width: auto;
                line-height: 1em;
                padding: .4em;
                }
                .widget:hover {
                border-radius: 10px;
                border: 2px solid #a6505e;
                transition: all 0.2s ease;
                background-color: #333;
                }
                .widget:focus {
                outline: none;
                }
                
                #submit-btn {
                margin: .3rem 0;
                }
                
                /* From Uiverse.io by andrew-demchenk0 */ 
                .rating:not(:checked) > input {
                  position: absolute;
                  appearance: none;
                }
                
                .rating:not(:checked) > label {
                  float: right;
                  cursor: pointer;
                  font-size: 40px;
                  color: #666;
                }
                
                .rating:not(:checked) > label:before {
                  content: '★';
                }
                
                .rating > input:checked + label:hover,
                .rating > input:checked + label:hover ~ label,
                .rating > input:checked ~ label:hover,
                .rating > input:checked ~ label:hover ~ label,
                .rating > label:hover ~ input:checked ~ label {
                  color: #e58e09;
                }
                
                .rating:not(:checked) > label:hover,
                .rating:not(:checked) > label:hover ~ label {
                  color: #ff9e0b;
                }
                
                .rating > input:checked ~ label {
                  color: gold;
                }
                </style>
                """, unsafe_allow_html=True)

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