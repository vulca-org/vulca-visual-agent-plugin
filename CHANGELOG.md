# Changelog

## v0.23.1 - 2026-05-11

### Changed
- Synced plugin manifests and marketplace metadata with Vulca SDK/PyPI v0.23.1.
- Updated Claude Code, Gemini CLI, and Codex install commands to use `vulca[mcp]==0.23.1`.

## v0.19.0-gemini-extension — 2026-05-01

### Added
- Gemini CLI extension packaging with `gemini-extension.json` and `GEMINI.md`.
- Codex plugin packaging with `.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json`.
- Gemini CLI installation and validation notes in `README.md` and `SUBMISSION.md`.

### Changed
- Align `/vulca:evaluate` redraw next-action wording with the main SDK repository.

## v0.19.0 — 2026-05-01

Platform-distribution sync from Vulca main v0.19.0.

### Added
- **`skills/visual-discovery/SKILL.md`** — upstream fuzzy-intent workflow for taste profile, direction cards, prompt artifacts, and visual-brainstorm handoff.
- **`skills/evaluate/SKILL.md`** — user-facing evaluation workflow over existing Vulca cultural and visual scoring.
- Portable MCP configuration using `vulca-mcp` from `PATH`.

### Changed
- **`skills/decompose/SKILL.md`**, **`skills/visual-brainstorm/SKILL.md`**, **`skills/visual-spec/SKILL.md`**, **`skills/visual-plan/SKILL.md`**, and **`skills/using-vulca-skills/SKILL.md`** synced from Vulca main v0.19.0.
- Plugin manifest now positions Vulca as visual control for discovery, prompt structure, provider routing, semantic layers, redraw, and cultural evaluation.
- README and marketplace copy no longer hard-code stale MCP tool counts or present redraw as a polished top-level skill.

### Release posture
- Lead marketplace copy with `/visual-discovery`, `/visual-brainstorm`, `/visual-spec`, `/visual-plan`, `/decompose`, and `/evaluate`.
- Keep redraw and inpaint as advanced SDK/MCP workflows until real-image target-aware redraw evidence is reviewed.
- Real-provider generation, editing, and VLM-backed evaluation remain explicit opt-in.

## v0.17.11 — 2026-04-23

Honesty + quality-of-life patch. Plugin-side changes mirror only the skill updates from vulca main v0.17.11 (code-level provider error normalization + MCP `create_artwork.ref_type` removal + README/BP honesty are shipped in the Python package, not the plugin).

### Added
- **`skills/visual-brainstorm/SKILL.md`** — **Style-Treatment 7th question-bank dimension** (mandatory, no skip): `additive` (photo preserved, elements painted as distinct objects on top) / `unified` (whole image transformed) / `collage` (visible cut-outs) / `wash` (global style filter). Closes the UX gap exposed by the Scottish-Chinese fusion smoke test where gpt-image-1.5 produced whole-image painterly overlay when user wanted additive treatment.
- **`skills/visual-brainstorm/SKILL.md`** — `proposal.md` frontmatter now carries `style_treatment` (7 → 8 fields).

### Changed
- **`skills/visual-spec/SKILL.md`** — Phase 1 step 8 validates `proposal.frontmatter.style_treatment ∈ {"additive", "unified", "collage", "wash"}` (Err #4); Phase 3 C.prompt derivation reads `style_treatment` and writes corresponding `negative_prompt` constraints; S4 invariant extended to cover `C.style_treatment` immutability across session.

### Upstream context (not plugin-affecting)
- vulca main Python package v0.17.11 also ships: provider error message normalization (Gemini/OpenAI/ComfyUI user-readable), MCP `create_artwork.ref_type` BREAKING removal, layers_split/layers_edit docstring fixes, hardcoded-path cleanup, README "Quick start" honesty, BP §5.4 moat softening, `.gitignore` hygiene. See https://github.com/vulca-org/vulca/releases/tag/v0.17.11 for the full package notes.

### Known v0.17.12 gap
`/visual-plan` Phase 3 does NOT yet read `C.style_treatment` in its generate-loop. The field is written to design.md + informs `/visual-spec` C.prompt's `negative_prompt`, but downstream propagation to pixel execution is deferred. Both parallel reviewers (codex + superpowers) agreed this is survivable for v0.17.11 because the `style_treatment` directive already rides in the composed `base_prompt` via `/visual-spec` governance — just not formally enforced.

### Upstream ship state
- PyPI: https://pypi.org/project/vulca/0.17.11/
- GH release: https://github.com/vulca-org/vulca/releases/tag/v0.17.11
- Full repo tests: 1920 passed / 12 pre-existing baseline failures / zero regressions.

## v0.17.10 — 2026-04-23

Catch-up release bundling v0.17.8 + v0.17.10 skill updates (supersedes PR #6). Plugin main was at v0.17.7; this brings it to v0.17.10 in a single merge.

### Added (v0.17.10)
- **`skills/using-vulca-skills/SKILL.md`** — new meta-skill (~50 lines) that establishes auto-invoke discipline for the brainstorm → spec → plan triad. Modeled on `superpowers:using-superpowers`. Intent-routing table, normalized finalize vocabulary, red-flag checklist.
- **`hooks/hooks.json`** — SessionStart hook (matcher `startup|clear|compact`) that cat's `using-vulca-skills/SKILL.md` into session context at start via `${CLAUDE_PLUGIN_ROOT}/skills/using-vulca-skills/SKILL.md`. This is what makes auto-invoke actually work: the meta-skill is preloaded every session.
- **`.claude-plugin/plugin.json`** — plugin manifest for distribution at v0.17.10.

### Changed (v0.17.10)
- **3 skill descriptions rewritten** from descriptive `Triggers: /slash-command` to imperative `Use when X / You MUST use this before X` — matches Superpowers' auto-invoke-friendly pattern:
  - `skills/visual-brainstorm/SKILL.md`
  - `skills/visual-spec/SKILL.md`
  - `skills/visual-plan/SKILL.md`
- Each skill also gained a new `## Triggers` body section documenting slash command + Chinese aliases + intent auto-match phrases + skip conditions. CN triggers preserved as aliases, not dropped; just moved out of the description field.
- **Finalize vocabulary normalized** across the 3 skills:
  - Brainstorm/Spec: 5-word set `{finalize, done, ready, lock it, approve}` (brainstorm previously had only 4; `approve` added).
  - Plan: `accept all` exact-match stays (stricter because it triggers real cost-incurring pixel calls).
- **Plan cap-hit prompt** corrected — was asking `"Turn cap reached. finalize or deep review?"` but the actual gate requires `accept all`. Now: `"Turn cap reached. 'accept all' or 'deep review'?"` (2 occurrences fixed for internal consistency).

### Changed (v0.17.8 — catch-up from PR #6)
- `/visual-spec` 10 clarity-gap patches (Err #9 wording, Err #5/#6 classifier tightening, multiplier table sdxl row, recommended_providers phantom → pipeline_variant, tradition_tokens shape, D1 example annotation, Phase 2 Err #3 resume, Phase 4 accept all finalize-Write absorption, 3 section-count cases, schema_version "0.1" frontmatter field).
- `/visual-plan` SKILL.md includes both the clarity patches from v0.17.8 AND the v0.17.10 alignment updates.

### Context
Both v0.17.8 and v0.17.10 changes came from real dogfooding of the /visual-plan showcase on 2026-04-23:
- **v0.17.8 clarity**: ship-gate Layer C v2 live-run exposed wording drift and MCP metadata passthrough gaps.
- **v0.17.10 alignment**: user feedback ("这种类似的问题很严重 很卡手") when discovering Vulca skills required slash-command invocation while Superpowers auto-invoke on intent match. Parallel codex + superpowers:code-reviewer audit confirmed systemic root cause (description wording + absent meta-skill preload + no SessionStart hook).

### Upstream ship state
- PyPI: https://pypi.org/project/vulca/0.17.10/
- GH release: https://github.com/vulca-org/vulca/releases/tag/v0.17.10
- Full repo tests: 1920 passed / 12 pre-existing baseline failures / zero regressions.
- Clarity-gap backlog from v0.17.5+v0.17.7 ship-gates: **CLOSED** (all 13 items folded into v0.17.8).

### Superseded
This PR supersedes open PR #6 (`sync/v0.17.8`). Close #6 after merging this PR.

## v0.17.7 — 2026-04-23

### Added
- `/visual-plan` skill — **3rd and final meta-skill** in the
  `brainstorm → spec → plan → execute` architecture. Completes the triad:
  - `/visual-brainstorm` (v0.17.3/v0.17.4) produces `proposal.md`
  - `/visual-spec` (v0.17.5/v0.17.6) resolves into `design.md`
  - `/visual-plan` (this release) executes → `plan.md` + `iters/*.png` +
    `plan.md.results.jsonl` → terminal artifact `{completed, partial, aborted}`.
  See `skills/visual-plan/SKILL.md` (~413 lines). Mirrored byte-identical
  from vulca main repo `.claude/skills/visual-plan/SKILL.md` at v0.17.7.
- 4 phases (precondition+derivation → plan-review loop with 5-turn cap →
  execution loop → finalize + hygiene), 7 invariants S1-S7, 16-row error
  matrix with verbatim `Print exactly:` strings, 8-variant handoff set.

### Ship-gate status (upstream)
- Layer A pytest: 57/57 PASS <30s
- Layer B simulated (3 parallel subagents, 14 cases): **14/14 PASS**
- Layer C live v2 (2 parallel subagents, 6 gaps / 4 cases): **4/4 PASS**
- Combined: 18/18 for non-pixel-heavy surface.

### Dependencies
Requires v0.17.6 (also bundled into this PR) for `generate_image` MCP
extension (`seed/steps/cfg_scale/negative_prompt` kwargs) + `schema_version`
field in `design.md` frontmatter.

### Superseded (still active from v0.17.6 bundling)
This PR now supersedes open plugin PRs #3 (`sync/v0.17.4`
/visual-brainstorm) and #4 (`sync/v0.17.5` /visual-spec first ship).
Both remain superseded by this branch; close #3 and #4 after merging.

## v0.17.6 — 2026-04-23

### Added
- `/visual-spec` skill — meta-skill #2 of the `brainstorm → spec → plan`
  architecture. Turns a resolved `proposal.md` (from `/visual-brainstorm`) into
  a `design.md` with 7 technical dimensions (A: provider + params, B: composition
  strategy, C: prompt composition, D1: L1-L5 weights, D2: thresholds + batch,
  E: optional spike plan, F: cost budget). 6 phases (precondition gate → F
  calibration → dimension derivation → derive-then-review loop with 5-turn cap →
  optional spike → finalize), 9-error matrix, 6 skill bans (S1-S6), 5-word
  finalize vocabulary. See `skills/visual-spec/SKILL.md` (~440 lines).
  Mirrored byte-identical from vulca main repo `.claude/skills/visual-spec/SKILL.md`
  at v0.17.6.

### Changed
- `/visual-brainstorm` skill updated to vulca main v0.17.4.

## v0.17.3 — 2026-04-21

### Added
- `/visual-brainstorm` skill — mirrored from vulca main repo. Guide fuzzy
  visual intent into proposal.md.
  See `skills/visual-brainstorm/SKILL.md`.
