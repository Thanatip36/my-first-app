import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

answers = ["apple", "fish", "sun", "book", "pizza", "coffee", "rocket"]
prompts = [
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    "ข้อ 2: Cats love to eat `f _ s _ h`. 🐟",
    "ข้อ 3: The `s _ n` shines brightly in the sky. ☀️",
    "ข้อ 4: I like to read a `b _ _ k` before bed. 📖",
    "ข้อ 5: My favorite food is `p _ z _ a`. 🍕",
    "ข้อ 6: I drink a cup of `c _ _ f _ e` every morning. ☕",
    "ข้อ 7: A `r _ c _ _ t` flies into space. 🚀",
]

for i in range(7):
    st.session_state.setdefault(f"ans{i}", "")


def reset_game():
    for i in range(7):
        st.session_state[f"ans{i}"] = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False


@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog():
    st.balloons()
    score = sum(
        1
        for i, correct in enumerate(answers)
        if st.session_state[f"ans{i}"].strip().lower() == correct
        and st.success(f"✅ ข้อ {i+1}: ถูกต้อง")
        or not st.error(
            f"❌ ข้อ {i+1}: ยังไม่ถูกต้อง (คุณตอบ '{st.session_state[f'ans{i}']}')"
        )
    )
    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")
    st.success("🎉 You win!") if score == 7 else st.error("💀 You lose!")


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
