# scaffold-fastapi-backend

Production-ready FastAPI backend with PostgreSQL

**Built by [Augustus Rivers](https://offlabel.design)** - because building from scratch every time sucks.

## What's This?

A production-ready scaffold that actually works. Not some half-assed tutorial code,
but real shit you can deploy. Still needs customization for your specific use case,
but the hard parts are done.

## Quick Start

```bash
# Clone it
git clone https://github.com/offlabel-scaffolds/scaffold-fastapi-backend.git
cd scaffold-fastapi-backend

# Check the setup instructions in docs/
# (Each scaffold is different, so read those first)
```

## What's Included

- Production-ready configuration files
- Proper error handling (not just `console.log` everywhere)
- Documentation that doesn't assume you're psychic
- Tests setup (you should write more tests though)
- CI/CD pipeline ready to go
- Docker config for easy deployment

## Customization

This is a scaffold, not a straitjacket. Change whatever you need:

- Update configs for your stack
- Replace placeholder values
- Add your own features
- Remove stuff you don't need

The code has comments explaining the non-obvious bits. I spent time on this
so you don't have to spend time debugging weird edge cases at 2am.

## Common Issues

Most problems are environment-related:
- Check your .env file (copy from .env.example)
- Make sure dependencies are installed
- Read the error messages (I know, revolutionary concept)

If something's actually broken, open an issue or email me.

## Structure

```
.
├── src/          # Source code
├── docs/         # Documentation
├── tests/        # Tests (write more!)
├── .github/      # CI/CD workflows
└── config/       # Configuration files
```

## Deployment

See [docs/DEPLOYMENT.md](./docs/DEPLOYMENT.md) for deployment instructions.

TL;DR: It's containerized, so deploy anywhere that runs Docker.

## Contributing

Found a bug? Have a better way to do something? PRs welcome.

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## License

MIT - do whatever you want with it.

## Questions?

- Email: hello@offlabel.design
- Website: https://offlabel.design

Don't be shy. If this helped you ship faster, let me know. Makes my day.

---

Built with ❤️ (and lots of debugging) by Augustus Rivers at [Off Label Design](https://offlabel.design)
