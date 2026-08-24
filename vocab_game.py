import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# 1. กำหนดค่าเริ่มต้นใน session_state ถ้ายังไม่มี
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
if "ans5_val" not in st.session_state:
    st.session_state.ans5_val = ""
if "ans6_val" not in st.session_state:
    st.session_state.ans6_val = ""
if "ans7_val" not in st.session_state:
    st.session_state.ans7_val = ""
    
# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    st.session_state.ans1_val = ""  # เคลียร์ค่าช่องข้อ 1
    st.session_state.ans2_val = ""  # เคลียร์ค่าช่องข้อ 2
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.ans5_val = ""
    st.session_state.ans6_val = ""
    st.session_state.ans7_val = ""
    st.session_state.start = time.time()  # เริ่มเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog


# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog)
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")

def show_result_dialog(ans1, ans2, ans3, ans4, ans5, ans6, ans7):
    st.balloons()
    
    score = 0
    hasans = 0

    def Check(ans, correct, number, score, hasans):
        hasans += 1

        if ans == correct:
            score += 1
            st.success(f"✅ ข้อ {number}: ถูกต้อง")
        else:
            st.error(f"❌ ข้อ {number}: ยังไม่ถูกต้อง (คุณตอบ '{ans}')")

        return score, hasans

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    u_ans5 = ans5.strip().lower()
    u_ans6 = ans6.strip().lower()
    u_ans7 = ans7.strip().lower()

    score, hasans = Check(u_ans1, "apple", 1, score, hasans)
    score, hasans = Check(u_ans2, "fish", 2, score, hasans)
    score, hasans = Check(u_ans3, "sun", 3, score, hasans)
    score, hasans = Check(u_ans4, "book", 4, score, hasans)
    score, hasans = Check(u_ans5, "pizza", 5, score, hasans)
    score, hasans = Check(u_ans6, "coffee", 6, score, hasans)
    score, hasans = Check(u_ans7, "rocket", 7, score, hasans)

    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 7:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# 2. แถบแสดงเวลานับถอยหลัง
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(45 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 3. ช่องรับคำตอบ (ใช้ value ผูกกับตัวแปรตรงๆ เพื่อสั่งเคลียร์ได้)
ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val,
)

ans2 = st.text_input(
    "ข้อ 2: Cats love to eat `f _ s _ h`. 🐟",
    value=st.session_state.ans2_val,
)

ans3 = st.text_input(
    "ข้อ 3: The `s _ n` shines brightly in the sky. ☀️",
    value=st.session_state.ans3_val,
)

ans4 = st.text_input(
    "ข้อ 4: I like to read a `b _ _ k` before bed. 📖",
    value=st.session_state.ans4_val,
)

ans5 = st.text_input(
    "ข้อ 5: My favorite food is `p _ z _ a`. 🍕",
    value=st.session_state.ans5_val,
)

ans6 = st.text_input(
    "ข้อ 6: I drink a cup of `c _ _ f _ e` every morning. ☕",
    value=st.session_state.ans6_val,
)

ans7 = st.text_input(
    "ข้อ 7: A `r _ c _ _ t` flies into space. 🚀",
    value=st.session_state.ans7_val,
)

# อัปเดตค่าล่าสุดเข้าตัวแปร
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5
st.session_state.ans6_val = ans6
st.session_state.ans7_val = ans7
# ✏️ [พื้นที่สำหรับนักเรียน]: เพิ่มข้อ 3, 4 ตรงนี้


# 4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

# 5. แสดง Dialog ผลลัพธ์
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4, ans5, ans6, ans7)

st.divider()
st.write("นายธนาธิป พัชรวงค์ เลขที่ 43 ม.4/3")


