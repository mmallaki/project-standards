# Architecture

<!-- Read only when the question is "why is it built this way". The README answers "what is it";
     HANDOFF answers "where are we". This file answers "why these pieces and not others". -->

## The problem this shape solves

`<the failure that existed before, with numbers if there are numbers: file size, load time,
  bug frequency. A structure without a problem behind it is decoration.>`

## Layers

| layer | responsibility | what must never leak into it |
|---|---|---|
| `<layer>` | `<one sentence>` | `<the thing that would blur it>` |

## Flow

```mermaid
flowchart LR
    a[request] --> b[handler] --> c[(store)]
    c --> d[response]
```

## State: files versus runtime

`<what lives in code, what lives in a database/config, who owns each, and how a change crosses
  the boundary. If both exist, name the source of truth explicitly.>`

## Gates

- `<command>` — `<what it proves, and what it cannot prove>`.

## What was tried and dropped

- `<approach>` — `<why it was dropped>`. Kept here so it is not re-invented.
