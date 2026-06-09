# Suggested Prompts for MojoAuth OIDC — Python / Flask

## Full Implementation

> "Add passwordless authentication to my Python Flask application using MojoAuth.
>
> Follow `skills/authentication/oidc-hosted-page-python/SKILL.md` exactly.
>
> Requirements:
> 1. Install `authlib` and `python-dotenv`.
> 2. Configure the OAuth client with my MojoAuth Domain and credentials.
> 3. Create a login page with a 'Sign In with MojoAuth' link.
> 4. Create routes for login initiation and OIDC callback.
>
> My MojoAuth config:
> - MojoAuth Domain: `your-app.mojoauth.com`
> - Client ID: `<my_client_id>`
> - Redirect URI: `http://localhost:5000/auth/callback`"

## Add MojoAuth to Existing Login

> "My Flask app already has Flask-Login with password auth. Add MojoAuth as a passwordless alternative.
> Reference `skills/authentication/oidc-hosted-page-python/SKILL.md`.
> Both paths should result in the same Flask-Login session."
