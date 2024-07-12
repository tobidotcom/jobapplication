import streamlit as st
from pywebio.output import put_html

# HTML and CSS for the matrix effect
matrix_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            margin: 0;
            overflow: hidden;
            background: black;
            color: lime;
            font-family: 'Courier New', Courier, monospace;
        }
        .matrix {
            position: absolute;
            width: 100%;
            height: 100%;
        }
        .message {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            color: lime;
            font-size: 24px;
            z-index: 1;
        }
    </style>
</head>
<body>
    <canvas id="matrixCanvas" class="matrix"></canvas>
    <div class="message" id="message">
        <p>Justin should hire Tobi Dotcom because:</p>
        <ul>
            <li>Tobi is highly skilled in software development.</li>
            <li>Tobi has a strong problem-solving ability.</li>
            <li>Tobi is a team player and communicates effectively.</li>
            <li>Tobi is dedicated and always strives for excellence.</li>
            <li>Tobi brings a fresh perspective and innovative ideas.</li>
        </ul>
    </div>
    <script>
        const canvas = document.getElementById('matrixCanvas');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        const letters = Array(256).join(1).split('');
        const draw = () => {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = '#0F0';
            letters.map((y, index) => {
                const text = String.fromCharCode(3e4 + Math.random() * 33);
                const x = index * 10;
                ctx.fillText(text, x, y);
                letters[index] = y > 758 + Math.random() * 1e4 ? 0 : y + 10;
            });
        };
        setInterval(draw, 33);
    </script>
</body>
</html>
"""

def main():
    st.title("Justin Should Hire Tobi Dotcom")
    if st.button("Show Matrix Screen"):
        put_html(matrix_html)

if __name__ == "__main__":
    main()

    st.markdown(message)

if __name__ == "__main__":
    main()
