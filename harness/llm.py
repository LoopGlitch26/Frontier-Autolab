"""Thin model clients: the real Anthropic API and an offline mock for dry runs."""

import json
import os
import random
import re
import time


class AnthropicClient:
    def __init__(self, max_tokens: int = 8000, temperature: float = 1.0):
        try:
            import anthropic  # noqa: F401
        except ImportError as e:  # pragma: no cover
            raise SystemExit("pip install anthropic  (or run with --dry-run)") from e
        import anthropic
        if not os.environ.get("ANTHROPIC_API_KEY"):
            raise SystemExit("Set ANTHROPIC_API_KEY (or run with --dry-run).")
        self._client = anthropic.Anthropic()
        self.max_tokens = max_tokens
        self.temperature = temperature

    def complete(self, model: str, prompt: str, web_search: bool = False, retries: int = 4) -> str:
        kwargs = dict(model=model, max_tokens=self.max_tokens, temperature=self.temperature,
                      messages=[{"role": "user", "content": prompt}])
        if web_search:
            kwargs["tools"] = [{"type": "web_search_20250305", "name": "web_search", "max_uses": 8}]
        for attempt in range(retries):
            try:
                resp = self._client.messages.create(**kwargs)
                return "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")
            except Exception as e:  # rate limits, overload
                if attempt == retries - 1:
                    raise
                wait = 2 ** attempt * 10
                print(f"  ! {type(e).__name__}: retrying in {wait}s")
                time.sleep(wait)
        return ""


class MockClient:
    """Returns well-formed placeholder output so the whole pipeline can be tested offline."""

    def __init__(self, seed: int = 0):
        self.rng = random.Random(seed)

    def complete(self, model: str, prompt: str, web_search: bool = False) -> str:
        tags = re.findall(r"<(\w+)>", prompt)
        wanted = [t for t in dict.fromkeys(tags) if t != "document" and f"</{t}>" in prompt
                  and not re.search(rf"<document name=\"{t}\">", prompt)]
        era = re.search(r"era (E\d)", prompt)
        era = era.group(1) if era else "E?"
        out = []
        for t in wanted:
            if t == "scores":
                keys = re.search(r"<scores>\{(.*)\}</scores>", prompt).group(1)
                names = re.findall(r'"(\w+)"', keys)
                d = {n: self.rng.randint(3, 9) for n in names}
                d["total"] = self.rng.randint(45, 70)
                out.append(f"<scores>{json.dumps(d)}</scores>")
            else:
                out.append(f"<{t}>[mock {t} for {era} from {model}]</{t}>")
        return "\n".join(out)


def extract(tag: str, text: str, default: str = "") -> str:
    m = re.search(rf"<{tag}>(.*?)</{tag}>", text, flags=re.S)
    if m:
        return m.group(1).strip()
    if re.search(rf"<{tag}\s*/>", text):
        return ""
    return default
