import base64
import marshal

with open('veerjan.py', 'r', encoding='utf-8') as f:
    code = f.read()

enc = base64.b64encode(marshal.dumps(compile(code, '<string>', 'exec')))

output_code = f"import base64, marshal\nexec(marshal.loads(base64.b64decode({enc!r})))\n"

with open('veer_locked.py', 'w', encoding='utf-8') as f:
    f.write(output_code)

print("[✓] File successfully lock ho gayi hai: veer_locked.py")
