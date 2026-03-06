import re

with open('index.html', 'r') as f:
    content = f.read()

# Improved details/summary styling
css_addition = """
        details {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 12px;
            margin-bottom: 15px;
            padding: 15px 20px;
            transition: all 0.3s ease;
        }
        details[open] {
            background: rgba(233, 69, 96, 0.05);
            border-color: rgba(233, 69, 96, 0.3);
        }
        details summary {
            font-weight: 700;
            cursor: pointer;
            color: #ff6b6b;
            font-size: 1.15rem;
            outline: none;
            list-style: none;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        details summary::-webkit-details-marker {
            display: none;
        }
        details summary::after {
            content: "+";
            color: #e94560;
            font-size: 1.5rem;
            line-height: 1;
            transition: transform 0.3s;
        }
        details[open] summary::after {
            content: "−";
            transform: rotate(180deg);
        }
        details p {
            margin-top: 15px !important;
            padding-top: 15px;
            border-top: 1px solid rgba(255,255,255,0.05);
        }
"""

content = content.replace("details summary { font-weight: bold; cursor: pointer; color: #ff6b6b; font-size: 1.1rem; margin: 10px 0 5px; outline: none; }", css_addition)

with open('index.html', 'w') as f:
    f.write(content)
