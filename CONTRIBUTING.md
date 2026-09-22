# Contributing

Contributions are welcome, especially new visual systems, sharper quality gates, and workflow improvements.

## Add or change a style

1. Keep each style in `skills/image2-deck-forge/styles/`.
2. Follow the seven-section contract documented in `references/style-authoring.md`.
3. Add or update the catalog entry.
4. Run `python skills/image2-deck-forge/scripts/validate_style_library.py`.
5. Keep examples free of private data, third-party logos, and unlicensed assets.

A style contribution should be meaningfully distinct, not a palette swap. Explain its use cases, image direction, negative rules, and how it differs from the existing systems. The validator requires the shipped built-ins and allows additional registered styles.

