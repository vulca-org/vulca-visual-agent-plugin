# Vulca Agent Plugin Submission Packet

**Plugin name:** Vulca
**Version:** 0.23.1
**Repository:** https://github.com/vulca-org/vulca-visual-agent-plugin
**License:** Apache-2.0
**Logo:** assets/vulca-icon.svg
**Logo URL:** https://raw.githubusercontent.com/vulca-org/vulca-visual-agent-plugin/main/assets/vulca-icon.svg
**PNG Logo URL:** https://raw.githubusercontent.com/vulca-org/vulca-visual-agent-plugin/main/assets/vulca-icon.png

## One-Liner

Vulca is an agent-native visual control layer for discovery, structured prompts, semantic layers, and cultural evaluation.

## Short Description

Add visual discovery, decomposition, planning, and L1-L5 cultural evaluation workflows to Claude Code, Gemini CLI, and Codex.

## Long Description

Vulca helps agentic coding users work with images through reviewable creative artifacts instead of one-shot prompting. It can explore fuzzy visual intent, produce direction cards, compose provider-aware prompts, decompose images into semantic layers, and evaluate visual results against cultural and quality criteria.

Vulca works with local files and configured image providers. Provider-backed generation, editing, and evaluation are explicit opt-in workflows.

## First-Release Emphasis

- `/vulca:visual-discovery` for taste, culture, and direction exploration.
- `/vulca:visual-brainstorm`, `/vulca:visual-spec`, and `/vulca:visual-plan` for proposal/design/plan artifacts.
- `/vulca:decompose` for semantic layer extraction.
- `/vulca:evaluate` for structured L1-L5 review.

## Safety And Boundaries

- Vulca does not host a foundation image model.
- Provider output quality is not guaranteed.
- Cultural terminology does not guarantee better image generation.
- Redraw and inpaint are advanced SDK/MCP workflows, not polished first-release skills for every image.
- Real-provider generation, editing, and VLM-backed evaluation should remain explicit opt-in.

## Validation

Run from this repository:

```bash
claude plugin validate .
claude plugin validate .claude-plugin/plugin.json
gemini extensions validate .
codex plugin marketplace add .
codex plugin add vulca --marketplace vulca-visual-agent-plugin
python3 -m json.tool .claude-plugin/plugin.json
python3 -m json.tool .codex-plugin/plugin.json
python3 -m json.tool .agents/plugins/marketplace.json
python3 -m json.tool .claude-plugin/marketplace.json
python3 -m json.tool .mcp.json
python3 -m json.tool gemini-extension.json
python3 scripts/validate_plugin.py
```

Observed on 2026-05-13: JSON manifest validation passed; Gemini CLI extension validation passed; Codex marketplace add validation passed with a temporary `CODEX_HOME` for both the local checkout and the public GitHub repository. Claude validation commands are listed above, but `claude` was not installed on the validation machine.

Observed on 2026-07-15 with bundled `codex-cli 0.144.2`: local marketplace add and plugin install passed with an isolated `CODEX_HOME`. `claude 2.1.119` was installed, but both validation commands timed out after 20 seconds without output; the repository-level contract validator and Gemini validation passed.

## Gemini CLI Extension

This repository is also packaged as a Gemini CLI extension. Users can install the public repository directly:

```bash
pip install "vulca[mcp]==0.23.1"
gemini extensions install vulca-org/vulca-visual-agent-plugin
```

The Gemini extension loads `GEMINI.md` as persistent context and starts the `vulca-mcp` server from `PATH`.

## Codex Desktop / CLI Marketplace

This repository is also packaged as a Codex-compatible plugin marketplace. Users can install the public repository directly:

```bash
pip install "vulca[mcp]==0.23.1"
codex plugin marketplace add vulca-org/vulca-visual-agent-plugin
codex plugin add vulca --marketplace vulca-visual-agent-plugin
```

The Codex plugin manifest is `.codex-plugin/plugin.json`, and the marketplace entry is `.agents/plugins/marketplace.json`.

## OpenAI Plugin Review Packet

OpenAI submission URL: https://platform.openai.com/plugins

Use this packet when creating or updating the Vulca plugin draft. Do not submit the MCP-backed app portion for review until the MCP server is hosted on a stable public domain; OpenAI's review flow does not accept local or testing endpoints.

### App Metadata

- App name: `Vulca`
- Developer / company name: `Vulca`
- Category: `Productivity`
- Logo file: `assets/vulca-icon.png`
- Logo URL: https://raw.githubusercontent.com/vulca-org/vulca-visual-agent-plugin/main/assets/vulca-icon.png
- Repository URL: https://github.com/vulca-org/vulca-visual-agent-plugin
- SDK / MCP server URL: https://github.com/vulca-org/vulca-visual-control-sdk
- Website URL: https://vulcaart.art
- Privacy policy URL: https://vulcaart.art/chatgpt-app-privacy

### Short Description

Agent-native visual control for discovery, structured prompts, semantic layers, and L1-L5 cultural evaluation.

### Long Description

Vulca helps ChatGPT and Codex users turn fuzzy visual intent into auditable creative work: visual discovery, direction cards, structured prompts, semantic layer decomposition, and L1-L5 cultural or quality evaluation. It is local-first by default, and provider-backed generation, editing, and VLM evaluation remain explicit opt-in workflows.

### MCP Server

- Submitted MCP URL: `https://harryhurry-vulca-openai-mcp.hf.space/mcp`.
- Do not submit for review with a localhost, tunnel, or other testing endpoint.
- Authentication: the submitted remote profile is unauthenticated and limited to the review-safe, read-only tool allowlist below. Broader production workflows should use OAuth or a scoped auth layer before public review.

### Tool Summary

- `list_traditions`: list available cultural and design traditions.
- `get_tradition_guide`: return a concise guide for one tradition.
- `search_traditions`: search tradition names and terminology.
- `compose_prompt_from_design`: turn a resolved design brief into a provider-aware prompt.
- `evaluate_artwork`: evaluate an image or image brief against a tradition and L1-L5 criteria.

### Test Prompts

1. `Use Vulca to list available visual traditions.`
   - Expected: returns traditions such as `chinese_xieyi`, `japanese_traditional`, `western_academic`, `photography`, `brand_design`, and `ui_ux_design`.
2. `Use Vulca to explain what Chinese xieyi emphasizes for an ink landscape.`
   - Expected: summarizes expressive brushwork, negative space, qi/spirit resonance, and tradition-specific composition guidance.
3. `Use Vulca to compose a prompt for a Scottish-Chinese fusion festival poster with warm lantern light and Edinburgh street context.`
   - Expected: returns a structured, provider-aware prompt with visual intent, cultural constraints, and safety notes.
4. `Use Vulca to evaluate whether this concept fits Chinese xieyi: misty mountains, sparse pavilion, heavy neon gradients.`
   - Expected: identifies xieyi-aligned elements, flags the neon gradients as likely departure, and gives L1-L5 style guidance.

### Review Notes

- Vulca does not host a foundation image model.
- It coordinates local or user-configured providers and returns structured artifacts.
- Do not market redraw or inpaint as guaranteed polished one-click workflows; they are advanced explicit opt-in tools.
- Privacy policy must disclose local file access and optional provider upload behavior.

## Screenshot Checklist

- Plugin visible in the target client plugin UI.
- `/help` or skill list showing Vulca skills.
- A no-cost `/vulca:visual-discovery` run producing direction cards.
- A no-cost `/vulca:evaluate` or rubric-only evaluation artifact.
- Terminal capture of validation commands for the target client.

Do not include private user images, provider API keys, or hidden local paths in screenshots.
