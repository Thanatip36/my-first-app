import time
import streamlit as st
from PIL import Image


image_path = "Thumbs_up_Emoji.png"  

try:
    image = Image.open(image_path)
    st.image(image, caption="My App Logo", use_container_width=True)
) except FileNotFoundError:
    st.error("Image file not found. Make sure it is pushed to GitHub.")
    
st.title("⏱️ เกมเติมศัพท์จับเวลา")

answers = ["Imposter", "ก้มโดนตบ", "พระบิดา", "67", "คาเนกิ"]
prompts = [
    "ข้อ 1: When the ______ is sus😳",
    "ข้อ 2: กบโดนต้ม = ??",
    "ข้อ 3: ใครคือผู้สร้างโลกใบนี้ (ข่าวดังในไทย)",
    'ข้อ 4: Mango + Mustard = “_ _”   (HARD)',
    "ข้อ 5: เคยมั่นใจว่าเหนือกว่า”   ใครคือราชาของเพลงนี้",
]

for i in range(7):
    st.session_state.setdefault(f"ans{i}", "")


def reset_game():
    for i in range(7):
        st.session_state[f"ans{i}"] = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False

def print_match(value):
    sequence = ["Newgen😒", "Beginner😬", "Alpha🐺", "Mango Mustard🥭", "Yes king👑"]
    
    index = value - 1  
    
    if 0 <= index < len(sequence):
        st.success(sequence[index])
    else:
       st.error("💀 error!")
        
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog():
    st.balloons()
    score = 0
    for i, correct in enumerate(answers):
        user_ans = st.session_state[f"ans{i}"].strip().lower()
        if user_ans == correct:
            score += 1
            st.success(f"✅ ข้อ {i+1}: ถูกต้อง")
        else:
            st.error(f"❌ ข้อ {i+1}: ยังไม่ถูกต้อง (คุณตอบ '{user_ans}')")

    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")
    print_match(score)


st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(45 - (time.time() - st.session_state.start))
    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

for i, prompt in enumerate(prompts):
    st.session_state[f"ans{i}"] = st.text_input(
        prompt, value=st.session_state[f"ans{i}"]
    )

if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()
    time.sleep(1)
    st.rerun()

if st.session_state.get("is_ended", False):
    show_result_dialog()

st.divider()
