# New project — eight steps

`S` < 15 min · `M` half a day · `L` more.

1. **Create the repo as `private` first** (`gh repo create <name> --private`). Public comes after the
   secret scan, never before. `S`
2. **Scaffold the docs** — `scripts/new-project.sh <name> <dest>`. It never overwrites. `S`
3. **Write the README with what is true today**, not what you plan to build: version, status, the
   command that currently works. A README that describes the future is a wish list. `M`
4. **Draw one diagram** of the real flow, four to eight boxes. If you cannot draw it, the design is
   not settled yet — that is the finding. `S`
5. **Run it from a fresh clone** in a clean directory. Every missing step you hit goes into
   "Run it", with the exact command. `S`
6. **Add the first gate** — one command that proves the thing works, wired into `## Verify it`. `M`
7. **Take the screenshots** — real UI, 1280 and 390 wide, WebP, into `docs/images/`. Name by role
   (`home-hero.webp`), put the subject in `alt`. `S`
8. **Flip to public** only after `check-docs.py` passes and `git log -p` shows no credential ever
   entered history. Then `gh repo edit --visibility public --accept-visibility-change-consequences`. `S`

## Done when

- `python3 scripts/check-docs.py .` exits 0
- a stranger can clone, run, and verify without asking a question
- `AGENTS.md` is ≤60 lines and names the file map
- `HANDOFF.md` says where the work stopped
