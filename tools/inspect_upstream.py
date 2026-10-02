import pathlib, re
s=(pathlib.Path(__file__).resolve().parents[1]/'upstream.decoded.js').read_text(encoding='utf-8')
for pattern in [r'import[^;]+;',r'async function Ro\(',r'async function Do\(',r'function Fo\(',r'function pe\(',r'async function [A-Za-z]+\([^)]*\)\{[^{}]{0,300}connect',r'\bconnect\(']:
    for m in list(re.finditer(pattern,s))[:6]: print(pattern, '\n', s[max(0,m.start()-50):m.start()+2200], '\n')
