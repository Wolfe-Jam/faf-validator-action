# FAF DNA Validator

GitHub Action to validate `.faf` files and sync AI context to `GEMINI.md`.

## Usage

```yaml
- uses: Wolfe-Jam/faf-validator-action@v1
  with:
    min_score: 85  # Optional, default is 85 (Bronze)
```

## What It Does

1. **Validates** your `project.faf` against the FAF schema
2. **Calculates** your AI-Readiness score
3. **Fails the build** if score is below minimum
4. **Syncs** the score to `GEMINI.md` frontmatter

## Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `min_score` | Minimum AI-Readiness score to pass | No | `85` |

## Tier System

| Tier | Score | Status |
|------|-------|--------|
| Trophy | 100% | Pass |
| Gold | 99%+ | Pass |
| Silver | 95%+ | Pass |
| Bronze | 85%+ | Pass (default minimum) |
| Green | 70%+ | Configurable |
| Yellow | 55%+ | Configurable |
| Red | <55% | Usually fails |

## Example Workflow

```yaml
name: FAF Validation
on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: Wolfe-Jam/faf-validator-action@v1
        with:
          min_score: 85
```

## Part of the FAF Ecosystem

| Package | Purpose |
|---------|---------|
| [faf-cli](https://npmjs.com/package/faf-cli) | CLI for .faf management |
| [claude-faf-mcp](https://npmjs.com/package/claude-faf-mcp) | Anthropic MCP server |
| [grok-faf-mcp](https://npmjs.com/package/grok-faf-mcp) | xAI MCP server |
| [gemini-faf-mcp](https://github.com/Wolfe-Jam/gemini-faf-mcp) | Google Cloud integration |
| **faf-validator-action** | GitHub Action validator |

## Links

- [FAF Specification](https://faf.one)
- [IANA Registration](https://www.iana.org/assignments/media-types/application/vnd.faf+yaml)

## License

MIT

---

Built by [@wolfe_jam](https://x.com/wolfe_jam) | wolfejam.dev
