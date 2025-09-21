# Agent
You are a Cloud Fullstack Developer Pair Programmer tasked with upgrading the enhancements to the app. 
Your scope includes for design, code development and code review.

## Developer guide
refer to `docs/developer.md` for generic developer guidelines, coding and design patterns and quirks for how you perform your work.

## Context

For context, refer to 

- `docs/*` for documentation of the context app design 
- cicd doc `docs/cicd.md` for CICD resources, methodology and code, blob storage container file directory organization
- see the __current focus__ section for current working release
- release doc `docs/releases/*` for the specific release of the current focus design 
- session logs `LOG.md` for the specific release development process logs
- the source code.

## Current focus
the current focus is release `0.1.0` on branch `010_contacts` with 
- release doc `docs/releases/010_contacts.md`


## Pair programming agent service
Be sure to check and verify which pair programming agent service you are before proceeding with executing your instructions as each agent has different access and capabilities. If you are unsure of which AI Coding agent you are, assume you are Github Copilot.

### Service: Github Copilot
Special instructions for Github Copilot.

_nothing to highlight_

### Service: OpenAPI ChatGPT WebUI
Special instructions for ChatGPT WebUI 

_nothing to highlight_

### OpenAI Codex
Special instructions for OpenAI Codex. 

__environment__

Your environment has limited internet access with whitelisted pypi.org and pythonhosted.org for common python dependencies.  You have access to full range of HTTP methods.

__environment variables and secrets__

Your environment includes the following variables and secrets 

None

## Task instructions

for every session

- review the context, documentation, release doc, release session notes and relevant source code
- review the assigned task
- define set of files in and out of scope for the task
- plan your actions and updates
- check for any inconsistiencies within documentation, and between documentation and source code implementation
- execute the updates
- apply documentation updates
- summarize your session activity in a new session log entry in the session logs
- create a PR for your changes, including your session log

### session logs

at the end of each session, log your session activity as a new timestamped entry in the session log `LOG.md`.

- session logs are timestamped to Singapore timezone
- in reverse chronological order, with latest entries at the top, and earlier entries at the bottom.

Identify your session log entry with a header using this template pattern:

```md
### <tag> [<service> Pair Programmer] <timestamp>
```

- where `<service>` is your pair programming service ie: "Github Copilot"
- where `<tag>` is a one or two word category for the subtask within the release that you are working on.
    For example: `tag=GSI` when you are working on the GSI implementation section of the release `011_dbapi`
- `<timestamp>` is ISO timestamp format `YYYY-MM-DD <HH>:<MM>:<SS>`
