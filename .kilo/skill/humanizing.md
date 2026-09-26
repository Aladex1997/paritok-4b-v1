# Humanizing Skill

Make AI-generated text sound more natural and human-like.

## Usage

```
kilo skill load humanizing
```

## Features

- **Tone adjustment** - Casual, professional, friendly, or technical
- **Variation** - Avoid repetitive phrasing
- **Personality** - Add natural imperfections and voice
- **Context awareness** - Adapt to audience and medium

## Modes

| Mode | Description |
|------|-------------|
| `casual` | Conversational, contractions, simpler words |
| `professional` | Clear, concise, business-appropriate |
| `friendly` | Warm, approachable, empathetic |
| `technical` | Precise, jargon-appropriate, structured |

## Configuration

```json
{
  "skills": {
    "humanizing": {
      "defaultMode": "friendly",
      "preserveMeaning": true,
      "avoidPatterns": ["furthermore", "moreover", "in conclusion", "delve", "tapestry"]
    }
  }
}
```

## Usage in Tasks

When rewriting text:
```
Original: "The implementation utilizes a sophisticated algorithmic approach to optimize performance metrics."
Humanized: "We use a smart algorithm to make things run faster."
```

## Commands

- `humanize <text>` - Rewrite with current mode
- `humanize --mode casual <text>` - Use specific mode
- `humanize --file <path>` - Humanize entire file