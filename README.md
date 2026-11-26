# Project standards

[فارسی](README.fa.md) · **English**

The documentation skeleton I put in every repository, so that a project explains itself to a
stranger, to a future me, and to an agent — without depending on chat history or on one machine.

It exists because of a concrete failure: the same codebase felt easy on one computer and painful
on another, not because the code changed, but because one machine had the project's facts written
down in the repo and the other only had them in a conversation. Chat history does not travel;
files and skills do.

## At a glance

| | |
|---|---|
| What | a documentation skeleton (README ×2, `AGENTS.md`, `HANDOFF.md`, `OPEN-ITEMS.md`, `DECISIONS.md`) |
| For | any repo of mine, on any machine, with or without an agent |
| Gate | `python3 scripts/check-docs.py .` — shape and secrets, not truth |

## What is in here

| path | what it is |
|---|---|
| `templates/README.en.md` | the English front page: what, why, how it fits, how to run, how to verify |
| `templates/README.fa.md` | the Persian twin — same sections, not a compression of the English one |
| `templates/AGENTS.md` | the entry point for an AI: file map, hard rules, how to add a thing (≈60 lines) |
| `templates/HANDOFF.md` | current state, last change, live decisions (≈40 lines, kept short on purpose) |
| `templates/OPEN-ITEMS.md` | the open checklist with `S`/`M`/`L` cost, cheap first, traps at the end |
| `templates/DECISIONS.md` | dated decisions with the reason and the rejected options |
| `templates/ARCHITECTURE.md` | why each piece exists — read only when the question needs it |
| `checklists/new-project.md` | eight steps from empty repo to documented repo |
| `checklists/release.md` | what must be true before a version goes out |
| `scripts/new-project.sh` | copies the templates into a repo and fills in the name |
| `scripts/check-docs.py` | the gate: both READMEs, the switch links, the required sections, no secrets |

## The rules behind the files

1. **Two languages, two files.** `README.md` is English — it is what a visitor sees by default.
   `README.fa.md` is the full Persian version, not a summary. One file with both halves is easier
   to keep in sync but slower to read and it doubles in length; two files cost a synchronisation
   check, which `check-docs.py` makes cheap.
2. **The README answers five questions, in this order:** what is this, why does it exist, how is it
   built, how do I run it, how do I know it still works. A diagram goes before prose when the answer
   is a shape.
3. **Every claim is checkable.** No "production-ready", no "scalable" — a version number, a command,
   a measured number instead. If a status is unknown, write that it is unknown.
4. **`AGENTS.md` is a map, not a manual.** It names files and rules and says "open only the file the
   task names". A 400-line agents file gets skimmed; a 60-line one gets followed.
5. **`HANDOFF.md` stays short.** Last change plus live decisions. When it passes ~100 lines, the
   older sections move to `docs/HISTORY.md`. A handoff that became a log is no longer a handoff.
6. **Decisions carry their reason and the options that were rejected.** "Chose X" is a fact that
   invites re-litigation; "chose X because Y, not Z because W" ends the argument.
7. **An open list is a checklist, not prose**, sorted cheap to expensive, with a one-line "what it
   means" for each item — decisions are made on meaning, not on file names.
8. **Screenshots and diagrams live in the repo.** `docs/images/` for screenshots (optimised, WebP),
   Mermaid for anything that is a flow. A diagram that renders on GitHub and lives next to the code
   gets updated; a picture on someone's desktop does not.

## Run it

```bash
git clone https://github.com/mmallaki/project-standards /tmp/standards
/tmp/standards/scripts/new-project.sh my-project ~/projects/my-project
cd ~/projects/my-project && python3 /tmp/standards/scripts/check-docs.py .
```

The script never overwrites an existing file; it copies what is missing and prints what it skipped.

## Verify it

`scripts/check-docs.py` fails when a repository claims to follow this standard but does not:

- `README.md` or `README.fa.md` missing, or the switch link missing from either
- a required section absent (what / run / verify)
- a Mermaid block that the file opens and never closes
- a `TODO` left in a heading, or an empty code fence
- a credential-looking string (`password = "…"`, `ghp_…`, `sk-…`) anywhere in tracked text

It is deliberately shallow: it checks presence and shape, not truth. Truth is the reviewer's job.
