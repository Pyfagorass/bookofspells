# Suggested Prompts for MojoAuth OIDC — Node.js

## Full Implementation

> "Add passwordless authentication to my Node.js Express application using MojoAuth.
>
> Follow `skills/authentication/oidc-hosted-page-node/SKILL.md` exactly.
>
> Requirements:
> 1. Install `openid-client` and `express-session`.
> 2. Configure the OIDC client with my MojoAuth Domain and credentials.
> 3. Create a login page with a 'Sign In with MojoAuth' link.
> 4. Create a `/auth/login` route that initiates the OIDC redirect to MojoAuth Hosted Login Page.
> 5. Create a `/auth/callback` route that exchanges the code for tokens and creates a session.
>
> My MojoAuth config:
> - MojoAuth Domain: `your-app.mojoauth.com`
> - Client ID: `<my_client_id>`
> - Redirect URI: `http://localhost:3000/auth/callback`"

## Add MojoAuth to Existing Login

> "My Express app already has passport.js local auth. Add MojoAuth as a passwordless alternative.
> Reference `skills/authentication/oidc-hosted-page-node/SKILL.md`.
> Both paths should result in the same session state."
