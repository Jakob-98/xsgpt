def main():
    import openai, os, pickle
    from pathlib import Path
    c, h = (lambda m: openai.ChatCompletion.create(model='gpt-4', messages=m)), (lambda r, c: {"role": r, "content": c})
    m = pickle.load(open(Path(os.getenv('APPDATA', os.path.expanduser('~')),'ai_chat.pkl'), 'rb')) \
        if Path(os.getenv('APPDATA', os.path.expanduser('~')),'ai_chat.pkl').exists() else [h('system', 'You are an AI assitant')]

    while (i := input('You: ').strip()) != 'exit':
        print(f'AI: {(r:=c((m:=[*m,h("user",i)]))["choices"][0]["message"]["content"])}')
        m = [*m, h("assistant", r)][-10:] # Truncate to 10 last messages
        pickle.dump(m, open(Path(os.getenv('APPDATA', os.path.expanduser('~')),'ai_chat.pkl'), 'wb'))