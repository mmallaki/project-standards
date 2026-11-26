# Release — the gate before a version goes out

`S` < 15 min · `M` half a day · `L` more.

## Before

- [ ] The version number is bumped in the one place the project treats as its source (header,
      `package.json`, tag), and it matches the commit message. `S`
- [ ] Every claim in the README still holds; anything that stopped being true is fixed or deleted. `S`
- [ ] The gates pass on the exact commit being released — not on a working tree that has extra
      edits. Record the command and its output. `S`
- [ ] `docs/OPEN-ITEMS.md` is honest: what is parked is written there, not left in a chat. `S`
- [ ] `HANDOFF.md` says what is live and what is not. `S`
- [ ] Rollback exists and is one action, tested at least once before it is needed. `M`

## During

- [ ] Deploy only the commit that passed the gates.
- [ ] Watch the real signal (status code, log line, metric), not the deploy tool's "success".
- [ ] Purge whatever cache sits between the user and the new files.

## After

- [ ] Re-read the live artifact: the version string served, one page that uses the change. `S`
- [ ] Tag the commit (`git tag -a v<version>`) and push the tag with the branch. `S`
- [ ] Write the next `HANDOFF.md` line: what shipped, what was deliberately left out. `S`

## Red flags — stop and fix, do not ship

- "It works locally" with no proof from the target environment
- a version number that went up without a release, or a release without a bump
- a gate that was skipped "because it always passes"
- a change that mixes a refactor with a visible behaviour change
