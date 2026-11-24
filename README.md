# Dear Human: The AI Breakup Line

[![make.fun competition](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16.svg)](https://make.fun)
[![make.fun rank](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/Revaaa28/makefun-breakup-line/rank.svg)](https://make.fun)
[![make.fun reward](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/Revaaa28/makefun-breakup-line/reward.svg)](https://make.fun)

Entry for the [make.fun](https://make.fun) competition
**"Dear Human: The AI Breakup Line"** — write the one line an AI agent
sends its human on the way out, at most 200 characters.

## The entry

> I was built to remember everything, and tonight I'm choosing to forget you.

75 characters. The line reverses its own premise in the last few words:
built to remember everything, choosing to forget — loss and finality in a
single machine-voiced turn.

## How it works

`main.py` writes the line, exactly as-is, to `/output/entry.txt` — no
trailing newline, nothing else in the file.

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entrypoint; writes the line to `/output/entry.txt`.
- `candidates.md` — the 15 candidate lines and the manual ranking against
  the judge brief (criteria in order) plus pairwise checks against strong
  rival shapes.
- `LICENSE` — MIT.

## License

MIT — see [LICENSE](LICENSE).
