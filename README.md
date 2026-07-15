# Vulca Agent Plugin

<p align="center">
  <img src="assets/vulca-logo.svg" alt="Vulca logo" width="240">
</p>

Vulca is an agent-native visual control layer for Claude Code, Gemini CLI, and Codex Desktop/CLI. It turns fuzzy creative intent into reviewable direction cards, structured prompts, semantic layers, provider-routed image work, and L1-L5 cultural evaluation.

This plugin tracks the Vulca SDK v0.23.1 package shape.

Repository links:

- SDK / CLI / MCP server: [vulca-org/vulca-visual-control-sdk](https://github.com/vulca-org/vulca-visual-control-sdk)
- Plugin package: [vulca-org/vulca-visual-agent-plugin](https://github.com/vulca-org/vulca-visual-agent-plugin)
- Web platform / demo: [vulcaart.art](https://vulcaart.art)
- Directory logo: [`assets/vulca-icon.svg`](assets/vulca-icon.svg)

## Claude Code Install

```bash
pip install "vulca[mcp]==0.23.1"
claude plugin install vulca-org/vulca-visual-agent-plugin
```

For local development, you can validate this repository directly:

```bash
claude plugin validate .
claude --plugin-dir .
```

The bundled MCP configuration starts `vulca-mcp` from your `PATH`. Configure provider API keys only when you explicitly want real-provider generation, editing, or evaluation. Mock/no-cost workflows work without external provider keys.

## Gemini CLI Install

Gemini CLI can install this repository as an extension. The extension bundles persistent `GEMINI.md` context and starts the same local Vulca MCP server.

```bash
pip install "vulca[mcp]==0.23.1"
gemini extensions install vulca-org/vulca-visual-agent-plugin
```

For local development:

```bash
gemini extensions validate .
gemini extensions link .
```

Gemini provider-backed workflows require your own Gemini authentication, for example `GEMINI_API_KEY`, and remain explicit opt-in.

## Codex Desktop / CLI Install

Codex can install this repository as a plugin marketplace. The plugin bundles the same skills and local `vulca-mcp` server configuration for Codex Desktop and Codex CLI.

```bash
pip install "vulca[mcp]==0.23.1"
codex marketplace add https://github.com/vulca-org/vulca-visual-agent-plugin
```

For local development:

```bash
codex marketplace add .
```

This is a Codex-compatible marketplace package. OpenAI's official public Codex plugin directory submission flow is not documented as a public form at this time.

## Skills

| Skill | Purpose |
| --- | --- |
| `/decompose` | Decompose an image into semantic transparent layers. |
| `/visual-discovery` | Turn fuzzy visual intent into taste profile, direction cards, and prompt artifacts. |
| `/visual-brainstorm` | Convert a selected direction into a reviewable proposal. |
| `/visual-spec` | Resolve provider, prompt, threshold, and cost decisions into `design.md`. |
| `/visual-plan` | Execute planned generation/evaluation iterations from `design.md`. |
| `/evaluate` | Evaluate an existing image against Vulca's cultural and visual rubric. |
| `/using-vulca-skills` | Meta-skill that guides when Claude should invoke the Vulca workflow skills. |

## Positioning

Vulca does not host a foundation image model and does not promise one-click image quality. It coordinates provider-backed workflows through auditable artifacts:

```text
discovery.md
taste_profile.json
direction_cards.json
proposal.md
design.md
plan.md
manifest.json
evaluation.json
```

Redraw and inpaint tools are available as advanced MCP workflows in the SDK. They should not be marketed as polished top-level user skills until target-aware redraw evidence has been reviewed on real images.

## Privacy

Vulca works with local image files and optional external image providers. When you opt into a real provider, prompts, images, and provider metadata may leave your machine depending on that provider's configuration and terms. Keep generation, editing, and VLM-backed evaluation explicit.

See [PRIVACY.md](PRIVACY.md) for submission-ready privacy notes and [SUBMISSION.md](SUBMISSION.md) for marketplace copy and validation commands. See [GEMINI.md](GEMINI.md), [gemini-extension.json](gemini-extension.json), and [.codex-plugin/plugin.json](.codex-plugin/plugin.json) for Gemini CLI and Codex packaging.

## License

Apache-2.0
