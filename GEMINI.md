# Vulca Gemini CLI Extension

Vulca is an agent-native visual control layer. Use the `vulca` MCP server when the user asks for visual discovery, prompt structure, semantic layer decomposition, or L1-L5 cultural/visual evaluation.

The extension expects the `vulca-mcp` command to be available on `PATH`, usually from:

```bash
pip install "vulca[mcp]==0.23.1"
```

Prefer no-cost or local workflows first:

- use visual discovery and direction cards to clarify fuzzy intent;
- produce proposal/design/plan artifacts before provider-backed generation;
- use semantic decomposition for local image layer work;
- use rubric-based evaluation before recommending another generation pass.

Provider-backed generation, editing, redraw, inpaint, VLM evaluation, or any workflow that uploads prompts/images/masks to an external provider must remain explicit user-approved work. Do not claim Vulca hosts a foundation image model or guarantees provider output quality.
