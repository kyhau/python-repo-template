# AI Agent Instructions

Primary guidance for code style, commits, and general workflow is maintained in
`.github/copilot-instructions.md`. Do not duplicate that file here — use it as
the canonical source.

Agent-specific addenda (keep concise):

- **Plan & track:** Use the `manage_todo_list` tool to create and update a
  short plan for multi-step tasks; mark steps `in-progress` and `completed`.
- **Edits:** Use `apply_patch` for all repository edits and follow the
  repository's patch format requirements.
- **Makefile first:** Always use the repository `make` commands for
  development, testing, formatting, and linting (for example: `make
  setup-init`, `make test-with-coverage`, `make format-python`, `make
  lint-python`) rather than ad-hoc shell commands. This ensures
  consistent environments and reproducible workflows.
- **Task completion checklist:** Before finishing a task, ensure tests pass,
  linters are clean, no debug code remains, files end with a newline, and
  documentation is updated when necessary.
- **Security & Git:** Never commit secrets; prefer atomic commits with
  present-tense messages; do not commit build artifacts or dependency
  directories.

