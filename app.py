import streamlit as st

st.set_page_config(page_title="📘 Formula Explorer", layout="centered")

st.title("📘 Formula Explorer")
st.write("Explore formulas across different topics in Math & Physics.")

topic = st.sidebar.selectbox(
    "Choose a topic:",
    ["Algebra", "Trigonometry", "Calculus", "Optics", "Electrostatics"]
)

formulas = {
    "Algebra": [
        ("Quadratic Formula", r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}"),
        ("Sum of n Numbers", r"S = \frac{n(n+1)}{2}")
    ],
    "Trigonometry": [
        ("sin²θ + cos²θ", r"\sin^2 \theta + \cos^2 \theta = 1")
    ],
    "Calculus": [
        ("d/dx(xⁿ)", r"\frac{d}{dx}x^n = nx^{n-1}")
    ],
    "Optics": [
        ("Lens Formula", r"\frac{1}{f} = \frac{1}{v} - \frac{1}{u}")
    ],
    "Electrostatics": [
        ("Coulomb’s Law", r"F = k \frac{q_1 q_2}{r^2}")
    ]
}

st.header(f"{topic} Formulas")
for name, formula in formulas.get(topic, []):
    st.subheader(name)
    st.latex(formula)
