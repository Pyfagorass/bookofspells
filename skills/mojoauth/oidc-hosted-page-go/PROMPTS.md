# Suggested Prompts for MojoAuth OIDC — Go

## Full Implementation

> "Add passwordless authentication to my Go application using MojoAuth.
>
> Follow `skills/authentication/oidc-hosted-page-go/SKILL.md` exactly.
>
> Requirements:
> 1. Install `go-oidc` and `golang.org/x/oauth2`.
> 2. Configure the OIDC provider with my MojoAuth Domain and credentials.
> 3. Create a login page with a 'Sign In with MojoAuth' link.
> 4. Create handlers for login initiation and OIDC callback with ID token verification.
>
> My MojoAuth config:
> - MojoAuth Domain: `your-app.mojoauth.com`
> - Client ID: `<my_client_id>`
> - Redirect URI: `http://localhost:8080/auth/callback`"

## Add MojoAuth to Existing Login

> "My Go app already has session-based auth. Add MojoAuth as a passwordless alternative.
> Reference `skills/authentication/oidc-hosted-page-go/SKILL.md`.
> Both paths should result in the same session state."
