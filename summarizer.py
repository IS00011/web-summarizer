def summarize(text: str) -> str:
    sentences = text.split(". ")
    paragraph = ". ".join(sentences[:4]).strip()

    bullets = sentences[4:9]
    bullet_text = "\n".join(f"- {s.strip()}" for s in bullets if s.strip())

    return f"{paragraph}\n\nKey points:\n{bullet_text}"


def combine_summaries(summaries: list[str]) -> str:
    combined_text = " ".join(summaries)
    sentences = combined_text.split(". ")

    paragraph = ". ".join(sentences[:5]).strip()
    bullets = sentences[5:10]

    bullet_text = "\n".join(f"- {s.strip()}" for s in bullets if s.strip())

    return f"{paragraph}\n\nShared themes:\n{bullet_text}"
