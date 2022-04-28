# Jina Auth
Pypi package (jina-auth), provide a CLI to login Jina Eco.

## Install

```shell
pip install --pre jina-auth
```

## Core functionality

* Authentication and token management.

## Usage

### Login to Jina Cloud

Open browser automatically and login via 3rd party. Token will be saved locally.

```shell
jina auth login
```

### Logout

If there is a valid token locally, this will disable that token and remove it from local config.

```shell
jina auth logout
```

### Personal access token (PAT) management

#### Create a new PAT

```shell
jina auth token <name of PAT> -e <expiration days>
```

#### List PATs

```shell
jina auth token list
```

#### Delete PAT

```shell
jina auth token delete <name of PAT>
```

## Release cycle

Each time new commits come into `main` branch, the pre-release procedure will be started.
It will generate a pre-release in Pypi.

## Development guide

### Step 1: Install dependencies with extra requirements

`pip install -e ".[test]"`

<!-- start support-pitch -->
## Support

- Use [Discussions](https://github.com/jina-ai/auth/discussions) to talk about your use cases, questions, and
  support queries.
- Join our [Slack community](https://slack.jina.ai) and chat with other Jina community members about ideas.
- Join our [Engineering All Hands](https://youtube.com/playlist?list=PL3UBBWOUVhFYRUa_gpYYKBqEAkO4sxmne) meet-up to discuss your use case and learn Jina's new features.
    - **When?** The second Tuesday of every month
    - **Where?**
      Zoom ([see our public events calendar](https://calendar.google.com/calendar/embed?src=c_1t5ogfp2d45v8fit981j08mcm4%40group.calendar.google.com&ctz=Europe%2FBerlin)/[.ical](https://calendar.google.com/calendar/ical/c_1t5ogfp2d45v8fit981j08mcm4%40group.calendar.google.com/public/basic.ics))
      and [live stream on YouTube](https://youtube.com/c/jina-ai)
- Subscribe to the latest video tutorials on our [YouTube channel](https://youtube.com/c/jina-ai)

## Join Us

Hubble Python SDK is backed by [Jina AI](https://jina.ai) and licensed under [Apache-2.0](./LICENSE). [We are actively hiring](https://jobs.jina.ai) AI engineers, solution engineers to build the next neural search ecosystem in opensource.

<!-- end support-pitch -->