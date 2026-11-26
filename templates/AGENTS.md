# {{PROJECT}} — entry point

<!-- ≤60 lines. A map, not a manual. If this file grows past that, it stops being read. -->

One line: what this project is, what it runs on, and where the source of truth lives.

- Local: `<url>` — `<how it is started>`
- Source of truth: **this repo** (production is read-only unless the owner says deploy)
- Read this file first. Open only the file the task names. Never dump the whole tree.

## File map

| path | role |
|---|---|
| `src/…` | … |
| `docs/…` | … |
| `scripts/…` | … |

## Hard rules

1. Never mix a behaviour change with a refactor; a refactor must prove it changed nothing.
2. One feature = one file (or one module). One logical change = one commit.
3. Any state change that must survive restarts lives in a script, never in a one-off command.
4. Secrets never enter the repo, a commit message, or a log line.
5. Verify with a command, not by looking. A screenshot is evidence only with a number next to it.

## Add a feature

1. Create `<path>` at the position its name implies, not at the end of a list.
2. Register it where the manifest/registry lives — that file is the only place order exists.
3. Verify: `<command>`.

## Verify (never eyeball a refactor)

```bash
<test command>          # what it proves
<check command>         # what it proves
```

## Traps

- `<trap>` — what happens, and the signal that you hit it.
