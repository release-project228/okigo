# okigo

Moscow events poster: concerts, exhibitions, theatre and cinema premieres.

**Website: [https://okigo.ru](https://okigo.ru)**

## What's inside

- `events_next.py` — filters a list of events to the next two weeks and
  prints them sorted by date. Events come on stdin, one per line:
  `YYYY-MM-DD|title|venue`.

```bash
cat events.txt | python events_next.py
```

## Why this repo

`events_next.py` is a small, dependency-free example of the listing logic
okigo runs as a web service. The full poster lives at
[https://okigo.ru](https://okigo.ru).

## License

MIT
