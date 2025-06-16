# Vibetest Use


https://github.com/user-attachments/assets/9558d051-78bc-45fd-8694-9ac80eaf9494


An MCP server that launches multiple Browser-Use agents to test a vibe-coded website for UI bugs, broken links, accessibility issues, and other technical problems.

Perfect for testing both live websites and localhost development sites. 

Vibecode and vibetest until your website works.

## Add to Cursor in one click:

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.png)](cursor://anysphere.cursor-deeplink/mcp/install?name=vibetest&config=eyJjb21tYW5kIjoiL2Z1bGwvcGF0aC90by92aWJldGVzdC11c2UvLnZlbnYvYmluL3ZpYmV0ZXN0LW1jcCIsImVudiI6eyJPUEVOQUlfQVBJX0tFWSI6InlvdXJfYXBpX2tleSJ9fQ==)


## Quick Start

```bash
# Install dependencies
uv venv
source .venv/bin/activate
uv pip install -e .
```

### 1) Claude Code

```bash
# Add MCP server via CLI
claude mcp add vibetest /full/path/to/vibetest-use/.venv/bin/vibetest-mcp -e OPENAI_API_KEY="your_api_key"

# Test in Claude Code
> claude

> /mcp
  ⎿  MCP Server Status

     • vibetest: connected
```

### 2) Cursor (manually)

1. **Install via MCP Settings UI:**
   - Open Cursor Settings
   - Click on "MCP" in the left sidebar  
   - Click "Add Server" or the "+" button
   - Manually edit config:
  
```json
{
  "mcpServers": {
    "vibetest": {
      "command": "/full/path/to/vibetest-use/.venv/bin/vibetest-mcp",
      "env": {
        "OPENAI_API_KEY": "your_api_key",
        "OPENAI_BASE_URL": "https://api.openai.com/v1",
        "OPENAI_MODEL": "gpt-4",
        "OPENAI_TEMPERATURE": "0.9"
      }
    }
  }
}

```

### Basic Prompts
```
> Vibetest my website with 5 agents: browser-use.com
> Run vibetest on localhost:3000
> Run a headless vibetest on localhost:8080 with 10 agents
```

### Parameters You Can Specify
- **URL**: Any website (`https://example.com`, `localhost:3000`, `http://dev.mysite.com`)
- **Number of agents**: `3` (default), `5 agents`, `2 agents` - more agents = more thorough testing
- **Headless mode**: `non-headless` (default) or `headless`

## Requirements

- Python 3.11+
- OpenAI API key or OpenAI-compatible API (OpenAI, Azure OpenAI, Anthropic, local models via Ollama, etc.)
- Cursor/Claude with MCP support

## Configuration

The following environment variables can be configured:

- `OPENAI_API_KEY` (required): Your API key
- `OPENAI_BASE_URL` (optional): API base URL (default: `https://api.openai.com/v1`)
- `OPENAI_MODEL` (optional): Model to use (default: `gpt-4`)
- `OPENAI_TEMPERATURE` (optional): Temperature setting (default: `0.9`)

### Examples for different providers:

**OpenAI:**
```bash
OPENAI_API_KEY="sk-..."
OPENAI_BASE_URL="https://api.openai.com/v1"
OPENAI_MODEL="gpt-4"
```

**Azure OpenAI:**
```bash
OPENAI_API_KEY="your-azure-key"
OPENAI_BASE_URL="https://your-resource.openai.azure.com/openai/deployments/your-deployment"
OPENAI_MODEL="gpt-4"
```

**Local Ollama:**
```bash
OPENAI_API_KEY="ollama"
OPENAI_BASE_URL="http://localhost:11434/v1"
OPENAI_MODEL="llama2"
```

## Full Demo


https://github.com/user-attachments/assets/6450b5b7-10e5-4019-82a4-6d726dbfbe1f



## License

MIT

---

Powered by [Browser Use](https://github.com/browser-use/browser-use) 
