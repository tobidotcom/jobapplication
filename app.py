import streamlit as st
import random
import string

# CSS for matrix effect
matrix_css = """
<style>
body {
    background-color: black;
    color: lime;
    font-family: 'Courier New', Courier, monospace;
    overflow: hidden;
}
#matrix {
    position: absolute;
    width: 100%;
    height: 100%;
    z-index: -1;
    color: lime;
    font-size: 20px;
    white-space: nowrap;
    line-height: 20px;
    opacity: 0.8;
}
</style>
<div id="matrix"></div>
<script>
const matrix = document.getElementById("matrix");
const cols = Math.floor(window.innerWidth / 20);
const ypos = Array(cols).fill(0);

const matrixEffect = () => {
    matrix.innerHTML = '';
    ypos.forEach((y, ind) => {
        const text = String.fromCharCode(Math.random() * 128);
        const x = ind * 20;
        matrix.innerHTML += `<span style="position:absolute;top:${y}px;left:${x}px">${text}</span>`;
        ypos[ind] = y > window.innerHeight && Math.random() > 0.975 ? 0 : y + 20;
    });
};
setInterval(matrixEffect, 50);
</script>
"""

# Message to display
message = """
# Justin should hire Tobi Dotcom because:

- **Tobi is highly skilled in software development.**
- **Tobi has a strong problem-solving ability.**
- **Tobi is a team player and communicates effectively.**
- **Tobi is dedicated and always strives for excellence.**
- **Tobi brings a fresh perspective and innovative ideas.**
"""

def main():
    st.markdown(matrix_css, unsafe_allow_html=True)
    st.markdown(message)

if __name__ == "__main__":
    main()
