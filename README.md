# FAF DNA Validator (Archived)

> **Status: ARCHIVED** — Superseded by production tools in the FAF ecosystem.

This was an early prototype GitHub Action for validating `.faf` files and syncing to `GEMINI.md`. All functionality now lives in better homes:

| Capability | Now lives in |
|------------|-------------|
| FAF scoring | [faf-cli](https://npmjs.com/package/faf-cli) (`faf score`) |
| FAF validation | [WJTTC](https://npmjs.com/package/wjttc) Tier 8 |
| GEMINI.md sync | [gemini-faf-mcp](https://github.com/Wolfe-Jam/gemini-faf-mcp) (`sync_faf.py`) |
| GEMINI.md bi-sync | [faf-cli](https://npmjs.com/package/faf-cli) (`faf gemini sync`) |
| CI gating | [faf-cli](https://npmjs.com/package/faf-cli) + [WJTTC](https://npmjs.com/package/wjttc) |

## Use Instead

```bash
# Score your .faf
faf score

# Validate via WJTTC (MCP servers)
npx wjttc certify --mcp "npx your-server"

# Sync to GEMINI.md
faf gemini sync
```

## Links

- [FAF Specification](https://faf.one)
- [IANA Registration](https://www.iana.org/assignments/media-types/application/vnd.faf+yaml)

---

Built by [@wolfe_jam](https://x.com/wolfe_jam) | wolfejam.dev
