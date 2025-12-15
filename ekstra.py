import streamlit as st
import base64

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()
def ekstra():
    st.html(f"""
                <div class="container-judul">
                    <img  src="data:image/jpg;base64,{get_base64("images/newdarkstbg.jpg")}" class="gambar">
                    <div class="judul-utama bbh-sans-bogle-regular">🛠️EXTRA🎨</div>
                    <div class="keterangan-judul fredoka-e">Projek lain yang bisa dikunjungi</div>
                </div>

                <style>
                .container-judul {{
                    border-top: 8px solid #e66225;
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

    st.markdown(f"""
                <div class="extra-text-container">
                    <div class=" judultop jost-bold" style='font-weight:bold;font-size:1.2rem;text-align:center'>Kelompok Generator</div> 
                    <div style="text-align:center">
                        <span class="isi jost-normal" style='font-size:1rem;color:#dbdbdb;'>Jumlah cowo & cewe tiap kelompok yang dibuat langsung adil, pencet gambar di bawah untuk nyoba</span>
                    </div>
                </div>
                <style>
                .extra-text-container {{
                    background-color: #1f1f1f;
                    max-width: 80%;
                    margin: 0px auto;
                    padding: 10px;
                    border-radius: 10px;
                    border: 2px solid #505050;
                }}
                </style>
                """, unsafe_allow_html=True)
    st.markdown(f"""
    <div class="ultimate-img-wrapper">
        <div class="img-wrapper" style="text-align:center;margin:25px 0;">
          <a draggable="false" href="https://kelompok.streamlit.app" target="_blank">
            <img  src="data:image/jpg;base64,{get_base64("images/extra_img2.jpg")}"
                 alt="placeholder"
                 class="kelompok">
          </a>
          <div class="arrow" id="panah1"></div>
          <div class="arrow" id="panah2"></div> 
        </div>
    </div>
    <div class="extra-text-container">
        <div class="judul jost-bold" style='font-weight:bold;font-size:1.2rem;text-align:center'>Spelling Bee</div> 
        <div style="text-align:center">
            <span class="isi jost-normal" style='color:#dbdbdb;font-size:1rem'>Nih website tu tujuan sebenernya cuma untuk STS TIK/Informatika doang, pencet gambar di bawah untuk nyoba</span>
        </div>
    </div>
    <div class="ultimate-img-wrapper">    
        <div class="img-wrapper" style="text-align:center;margin:25px 0;">
          <a draggable="false" href="https://kelompok.streamlit.app" target="_blank">
            <img src="data:image/jpg;base64,{get_base64("images/spelling bee img.jpg")}"
                 alt="placeholder"
                 class="kelompok">
          </a>
          <div class="arrow" id="panah1"></div>
          <div class="arrow" id="panah2"></div>     
        </div>
    </div>
    
    <style>
    .judul {{}}
    
    .kelompok {{
      border-radius: 15px;
      cursor: pointer;
      width: 215px;
      border: 5px solid #e09151;
      transition: all 0.35s ease;
      margin: 0;
      position: relative;
      box-shadow: 0 0 15px 0 black; 
    }}

    .kelompok:hover {{
      border: 5px solid #d1d07d;
      transition: all 0.35s ease;
    }}

    .kelompok:active {{
        border: 5px solid #85ff8b;
        transition: all 0.2s ease;
    }}    
    
    a {{
        z-index: 1;
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
    }}
    
    .arrow {{
        height: 25%;
        width: 25%;
        position: absolute;
        transform: translate(0,0);
        background-color: #e3cc49;
        box-shadow: 0 0 15px 0 black inset;
    }}
    
    #panah1 {{
        pointer-events: none;
        clip-path: polygon(75% 0%, 100% 50%, 75% 100%, 40% 100%, 65% 50%, 40% 0);
        transition: all 0.2s ease;
        z-index: 0;    
    }}
    a:hover ~ #panah1 {{
        transform: translateX(-125%);
        transition: all 0.2s ease;
    }}
    
    #panah2 {{
        pointer-events: none;
        clip-path: polygon(25% 0, 0 50%, 25% 100%, 60% 100%, 35% 50%, 60% 0);
        transition: all 0.2s ease; 
    }}
    a:hover ~ #panah2 {{
        transform: translateX(125%);
        transition: all 0.2s ease;
    }}
    
    .img-wrapper {{
    display: flex;
    justify-content: center;
    align-items: center;
    }}
    
    .ultimate-img-wrapper {{
    box-sizing: content-box;
    margin-bottom: 100px;
    }}
    
    @media (max-width: 700px) {{
        .kelompok {{
        width: 175px;
        }}
        
        .arrow {{ 
        height: 15%;
        width: 18%;
        }}
        
        a:hover ~ #panah1 {{
        transform: translateX(-220%);
        }}
        a:hover ~ #panah2 {{
        transform: translateX(220%);
        }}
    }}
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