from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from extractor import extract_text
from summarizer import summarize, combine_summaries

app = FastAPI()
templates = Jinja2Templates(directory="templates")

MAX_URLS = 5

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/summarize", response_class=HTMLResponse)
def summarize_urls(request: Request, urls: str = Form(...)):
    url_list = [
        u.strip() for u in urls.splitlines()
        if u.strip().startswith("http")
    ][:MAX_URLS]

    results = []
    summaries = []

    for url in url_list:
        text = extract_text(url)
        if not text:
            continue

        summary = summarize(text)
        results.append((url, summary))
        summaries.append(summary)

    combined = combine_summaries(summaries) if summaries else ""

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "results": results,
            "combined": combined,
        },
    )
